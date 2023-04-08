import uuid

import uvicorn
from fastapi import FastAPI
from kubernetes import client, config, dynamic

NAMESPACE = "dev"
CM_NAME = "sync-cm"
RESOURCE_NAME = "resource"

app = FastAPI()

_global_cm_api = None
_global_client = None


@app.get("/")
async def root(resources: int, resource_name: str = None, cm_name: str = None, ns: str = None):
    config_kube()
    _log(f"Received a query for `{resources}` `{resource_name}` resources")
    
    sem_http_resp = set_argo_sem(resources, resource_name=resource_name, cm_name=cm_name, namespace=ns)
    sf_http_resp = ping_workflow(resource_name=resource_name, cm_name=cm_name, namespace=ns)

    return f"{sem_http_resp}\n{sf_http_resp}"


@app.get("/set_config")
async def manual_set_config():
    config_kube()
    return {"msg": "Success!"}


def _log(s: str, tag: str = "INFO"):
    print(f"{tag}: {s}")


def config_kube():
    my_configuration = config.load_kube_config()
    _log("Successfully set kube config!")

    global _global_client
    _global_client = dynamic.DynamicClient(client.api_client.ApiClient(configuration=my_configuration))

    global _global_cm_api
    _global_cm_api = _global_client.resources.get(api_version="v1", kind="ConfigMap")


def set_argo_sem(
    num_of_resources: int, resource_name: str = RESOURCE_NAME, cm_name: str = CM_NAME, namespace: str = NAMESPACE,
):
    if not resource_name:
        resource_name = RESOURCE_NAME
    if not cm_name:
        cm_name = CM_NAME
    if not namespace:
        namespace = NAMESPACE

    _log(f"Trying to set `{cm_name}.{resource_name}` to `{num_of_resources}` (in ns = `{namespace}`)...")

    # Create data patch
    patch_manifest = {"data": {resource_name: str(num_of_resources)}}

    # Check api was created
    global _global_cm_api
    if not _global_cm_api:
        err_msg = "api not defined!"
        _log(err_msg, tag="ERROR")
        raise Exception(err_msg)

    try:
        # Perform patch
        configmap_patched = _global_cm_api.patch(name=cm_name, namespace=namespace, body=patch_manifest)
        _log(f"Response from k8s: {configmap_patched}")

        return f"Data patched to: {configmap_patched['data']}"

    except client.exceptions.ApiException as e:
        _log(f"Could not patch configmap!\nGot error {e}", tag="ERROR")
        raise e


def ping_workflow(resource_name: str = RESOURCE_NAME, cm_name: str = CM_NAME, namespace: str = NAMESPACE):
    if not resource_name:
        resource_name = RESOURCE_NAME
    if not cm_name:
        cm_name = CM_NAME
    if not namespace:
        namespace = NAMESPACE

    semaphore_str = f"{namespace}/ConfigMap/{cm_name}/{resource_name}"

    _global_wf_api = _global_client.resources.get(api_version="argoproj.io/v1alpha1", kind="Workflow")

    workflows_waiting_for_semas = []

    # Get all workflows
    try:
        workflows_resp = _global_wf_api.get()
        _log(f"Response from k8s: {workflows_resp}")

        all_workflows = workflows_resp.to_dict()["items"]
        for item in all_workflows:
            item_name = item["metadata"]["name"]
            try:
                waiting_semaphores = item["status"]["synchronization"]["semaphore"]["waiting"]
                for sema in waiting_semaphores:
                    if sema["semaphore"] == semaphore_str:  # is waiting for semaphore
                        _log(f"{item_name} is waiting for semaphore `{resource_name}` (added to list)")
                        workflows_waiting_for_semas.append(item_name)
            except:
                _log(f"{item_name} is not waiting for semaphore `{resource_name}`")

    except client.exceptions.ApiException as e:
        _log(f"Could not get workflow!\nGot error {e}", tag="ERROR")
        raise e

    # Patch (Ping) all waiting workflows
    try:
        patch_manifest = {"metadata": {"labels": {"usesSync": str(uuid.uuid4())}}}
        _log(f"\n\nBody to submit: {patch_manifest}", tag="DEBUG")

        for waiting_workflow_name in workflows_waiting_for_semas:
            _log(f"Data: {waiting_workflow_name}, {namespace}\n\n", tag="DEBUG")
            
            workflows_ping_resp = _global_wf_api.patch(
                name=waiting_workflow_name, namespace=namespace, body=patch_manifest, content_type="application/merge-patch+json"
            )
            _log(f"Patched: {waiting_workflow_name}")
            _log(f"Response from k8s from ping: {workflows_ping_resp}")

    except client.exceptions.ApiException as e:
        _log(f"Could not patch workflow!\nGot error {e}", tag="ERROR")
        raise e

    return {"Pinged workflows": workflows_waiting_for_semas}


if __name__ == "__main__":
    config_kube()

    uvicorn.run("app", host="localhost", port=8000, reload=False)
