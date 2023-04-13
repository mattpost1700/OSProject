## Scripts
0. Installs prerequisites locally and on the cluster
1. Installs Rancher on the cluster
2. Port forwards Rancher

## How to get Rancher secret token
`kubectl get secret --namespace cattle-system bootstrap-secret -o go-template='{{.data.bootstrapPassword|base64decode}}{{"\n"}}'`