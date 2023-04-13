namespace=$1

kubectl create role -n $namespace argo-user --verb=list,update --resource=workflows.argoproj.io && \
kubectl create sa -n $namespace argo-user && \
kubectl create rolebinding argo-user -n $namespace --role=argo-user --serviceaccount=argo:argo-user && \

kubectl apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: argo-user.service-account-token
  namespace: $namespace
  annotations:
    kubernetes.io/service-account.name: argo-user
type: kubernetes.io/service-account-token
EOF
