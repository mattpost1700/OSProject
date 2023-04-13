"""
Author: Matthew Post
File: main.py
Description: This module is a RESTful server that adjusts the number of resources on a k8s cluster
"""

import os
import uuid

import uvicorn
from fastapi import FastAPI
from kubernetes import client, config, dynamic

NAMESPACE = "dev"
CM_NAME = "sync"
RESOURCE_NAME = "resource"

app = FastAPI()

_global_cm_api = None
_global_client = None


#################################### Endpoints ####################################


@app.get("/")
async def root(resources: int, resource_name: str = None, cm_name: str = None, ns: str = None) -> dict[str, str]:
    """
    A root endpoint to the server. The main endpoint that changes the number of instances in the cluster

    Args:
        resources (int): The number to set the resources to.
        resource_name (str, optional): The name of the resource to set. Defaults to None.
        cm_name (str, optional): The name of config map in the k8s cluster. Defaults to None.
        ns (str, optional): The namespace where the config map is located. Defaults to None.

    Returns:
        dict[str, str]: The response from both requests to the cluster
    """
    config_kube()

    # Set defaults
    if not resource_name:
        resource_name = RESOURCE_NAME
    if not cm_name:
        cm_name = CM_NAME
    if not ns:
        ns = NAMESPACE
    _log(f"Received a query for `{resources}` `{resource_name}` resources")

    sem_http_resp = set_argo_sem(resources, resource_name=resource_name, cm_name=cm_name, namespace=ns)
    sf_http_resp = ping_workflow(resource_name=resource_name, cm_name=cm_name, namespace=ns)

    return {"msg", f"{sem_http_resp}\n{sf_http_resp}"}


@app.get("/set_config")
async def manual_set_config() -> dict[str, str]:
    """
    A manual endpoint that allows the user to config the service to have access to the cluster.

    Returns:
        dict[str, str]: A success message if the configuration has no exceptions
    """
    config_kube()

    return {"msg": "Success!"}


#################################### Helper functions ####################################


def _log(s: str, tag: str = "INFO"):
    """
    Logs a message.
    NOTE: Uses `print` over the logging lib

    Args:
        s (str): The string to log
        tag (str, optional): The tag to prepend to the string. Defaults to "INFO".
    """
    print(f"{tag}: {s}")


#################################### Core functions ####################################


def config_kube():
    """
    Configures the service to connect to a k8s cluster
    """
    if os.environ.get("RUNNING_IN_CLUSTER"):  # NOTE: This is true if any string is passed through
        my_configuration = config.load_incluster_config()
    else:
        my_configuration = config.load_kube_config()
    _log("Successfully set kube config!")

    # Configure global client
    global _global_client
    _global_client = dynamic.DynamicClient(client.api_client.ApiClient(configuration=my_configuration))

    # Configure config map api to k8s cluster
    global _global_cm_api
    _global_cm_api = _global_client.resources.get(api_version="v1", kind="ConfigMap")


def set_argo_sem(
    num_of_resources: int, resource_name: str = RESOURCE_NAME, cm_name: str = CM_NAME, namespace: str = NAMESPACE,
) -> str:
    """
    Sets a config map in k8s

    Args:
        resources (int): The number to set the resources to.
        resource_name (str, optional): The name of the resource to set. Defaults to RESOURCE_NAME.
        cm_name (str, optional): The name of config map in the k8s cluster. Defaults to CM_NAME.
        ns (str, optional): The namespace where the config map is located. Defaults to NAMESPACE.

    Raises:
        Exception: Config map api was not initialized!
        k8s_exception: There was was error with the config map api / k8s api

    Returns:
        str: A message showing the patched data
    """
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
        return f"Data patched to: {configmap_patched['data']}"

    except client.exceptions.ApiException as k8s_exception:
        _log(f"Could not patch configmap!\nGot error {k8s_exception}", tag="ERROR")
        raise k8s_exception


def ping_workflow(
    resource_name: str = RESOURCE_NAME, cm_name: str = CM_NAME, namespace: str = NAMESPACE
) -> dict[str, str]:
    """
    Pings all workflows waiting for a resource

    Args:
        resource_name (str, optional): The resource that has changed. Defaults to RESOURCE_NAME.
        cm_name (str, optional): The name of config map in the k8s cluster. Defaults to CM_NAME.
        ns (str, optional): The namespace where the config map is located. Defaults to NAMESPACE.

    Raises:
        k8s_exception: There was was error with the config map api or workflow api / k8s api

    Returns:
        dict[str, str]: The workflows that were pinged
    """
    workflows_waiting_for_semas = []
    semaphore_str = f"{namespace}/ConfigMap/{cm_name}/{resource_name}"

    # Get Workflow api
    _global_wf_api = _global_client.resources.get(api_version="argoproj.io/v1alpha1", kind="Workflow")

    # Get all workflows
    try:
        workflows_api_resp = _global_wf_api.get()
        # _log(f"Response from k8s: {workflows_resp}")

        all_workflows = workflows_api_resp.to_dict()["items"]
        _log(f"{len(all_workflows)} workflows found")

        for item in all_workflows:
            item_name = item["metadata"]["name"]
            try:
                # Get waiting resources from response
                waiting_semaphores = item["status"]["synchronization"]["semaphore"]["waiting"]

                for semaphore in waiting_semaphores:
                    if semaphore["semaphore"] == semaphore_str:  # is waiting for semaphore
                        _log(f"{item_name} is waiting for semaphore `{resource_name}` (added to list)")
                        workflows_waiting_for_semas.append(item_name)

            except:  # Dictionary look up error
                _log(f"{item_name} is not waiting for semaphore `{resource_name}`")

    except client.exceptions.ApiException as k8s_exception:
        _log(f"Could not get workflow!\nGot error {k8s_exception}", tag="ERROR")
        raise k8s_exception

    # Patch (Ping) all waiting workflows
    try:
        patch_manifest = {"metadata": {"labels": {"usesSync": str(uuid.uuid4())}}}
        # _log(f"\n\nBody to submit: {patch_manifest}", tag="DEBUG")

        for waiting_workflow_name in workflows_waiting_for_semas:
            # _log(f"Data: {waiting_workflow_name}, {namespace}\n\n", tag="DEBUG")

            workflows_ping_resp = _global_wf_api.patch(
                name=waiting_workflow_name,
                namespace=namespace,
                body=patch_manifest,
                content_type="application/merge-patch+json",
            )
            _log(f"Patched: {waiting_workflow_name}")
            # _log(f"Response from k8s from ping: {workflows_ping_resp}")

    except client.exceptions.ApiException as k8s_exception:
        _log(f"Could not patch workflow!\nGot error {k8s_exception}", tag="ERROR")
        raise k8s_exception

    return {"Pinged workflows": workflows_waiting_for_semas}


if __name__ == "__main__":
    # Configure server to connect to the cluster
    config_kube()

    # Start the server
    uvicorn.run("main:app", port=8000, reload=False)
