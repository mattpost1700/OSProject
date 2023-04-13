How to use minikube

Start UI: minikube dashboard

Start K8s: minikube start

`kubectl port-forward --namespace kube-system service/registry 5000:80`

Test connection with: `curl http://localhost:5000/v2/_catalog`

`docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:host.docker.internal:5000"`

`docker tag my/image localhost:5000/myimage`


# Argo
```
kubectl apply -n argo -f https://github.com/argoproj/argo-workflows/releases/download/v3.4.5/install.yaml
kubectl -n argo port-forward deployment/argo-server 2746:2746
```
```
kubectl create namespace argo-events

kubectl apply -f https://raw.githubusercontent.com/argoproj/argo-events/stable/manifests/install.yaml
# Install with a validating admission controller
kubectl apply -f https://raw.githubusercontent.com/argoproj/argo-events/stable/manifests/install-validating-webhook.yaml

kubectl apply -n argo-events -f https://raw.githubusercontent.com/argoproj/argo-events/stable/examples/eventbus/native.yaml
```

# Helm Argo
Installing Argo Workflows
```
helm repo add argo https://argoproj.github.io/argo-helm

helm install argo argo/argo-workflows
```

Installing Argo Events
```
helm repo add argo https://argoproj.github.io/argo-helm

helm install argo argo/argo-events
```

## Log into Argo
How to: https://argoproj.github.io/argo-workflows/access-token/#token-creation
```
kubectl apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: infra.service-account-token
  annotations:
    kubernetes.io/service-account.name: infra
type: kubernetes.io/service-account-token
EOF

ARGO_TOKEN="Bearer $(kubectl get secret infra.service-account-token -o=jsonpath='{.data.token}' | base64 --decode)"

echo $ARGO_TOKEN
```

# Log into GitHub registry
`echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin`

# Log into GCP registry
```
kubectl create secret docker-registry gcr-json-key \
 --docker-server=gcr.io \
 --docker-username=_json_key \
 --docker-password="$(cat ./g-reg-key.json)"

kubectl patch serviceaccount default -p '{"imagePullSecrets": [{"name": "gcr-json-key"}]}'
```

# Secret from GH reg
```
kubectl create secret docker-registry <k8s-docker-registry-secret-name> --docker-server=ghcr.io --docker-username=<github-username> --docker-password=<github-personal-access-token>  --docker-email=<email-address>
```

```
kubectl create secret docker-registry gh-reg-cred --docker-server=ghcr.io --docker-username=mattpost1700 --docker-password=<github-personal-access-token>
```

# curl Pod (helpful for debugging IPC)
```
kubectl run mycurlpod -n dev --image=curlimages/curl -i --tty -- sh
```

# Installing an app
This is handled by out scripts but it is worth noting how this is done. Below is an example `print-time`
```
helm install --namespace dev print-time apps/print-time/helm/
```
