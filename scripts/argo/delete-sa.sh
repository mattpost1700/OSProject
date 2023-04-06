namespace=$1

kubectl delete role -n $namespace argo-user && \
kubectl delete sa -n $namespace argo-user && \
kubectl delete rolebinding argo-user -n $namespace && \

# kubectl delete secret -n $namespace argo-user.service-account-token

echo "Deleted!"
