helm install rancher rancher-latest/rancher \
  --namespace cattle-system \
  --set hostname=r7.mpost.rancher.dev.com \
  --set replicas=2

kubectl -n cattle-system rollout status deploy/rancher