import datetime
import time

import uvicorn
from fastapi import FastAPI
from kubernetes import client, config
from kubernetes.client import api_client

NAMESPACE = "dev"
CM_NAME = "sync-cm"
RESOURCE_NAME = "resource"

app = FastAPI()

my_api_client = None


@app.get("/")
async def root(resources: int):
    log(f"Received a query for {resources} resources")
    set_argo_sem(resources)


def log(s: str, tag: str = "INFO"):
    print(f"{tag}: {s}")


def config_kube():
    config.load_kube_config()
    log("Successfully set kube config!")


def set_argo_sem(
    client: api_client.ApiClient,
    num_of_resources: int,
    resource_name: str = RESOURCE_NAME,
    cm_name: str = CM_NAME,
    namespace: str = NAMESPACE,
):
    log(f"Trying to set `{cm_name}.{resource_name}` to `{num_of_resources}` (in ns = `{namespace}`)...")

    patch_body = client.V1ConfigMap(
        api_version="v1", kind="ConfigMap", data={resource_name: num_of_resources}
    )

    try:
        api_response = global_instance.patch_namespaced_config_map(
            name=cm_name, namespace=namespace, body=patch_body, pretty=True
        )
        log(f"Response from k8s: {api_response}")
    except Exception as e:  # TODO: ApiException
        log(f"Could not patch configmap!\nGot error {e}", tag="ERROR")
        raise e


if __name__ == "__main__":
    config_kube()

    global_instance = client.CoreV1Api(client.ApiClient(client.Configuration()))

    uvicorn.run("app", host="localhost", port=8000, reload=False)
