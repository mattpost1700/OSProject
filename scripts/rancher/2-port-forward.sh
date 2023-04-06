kubectl -n cattle-system port-forward svc/rancher 80:80 443:443

# NOTE
# $ kubectl get secret --namespace cattle-system bootstrap-secret -o go-template='{{.data.bootstrapPassword|base64decode}}{{"\n"}}'
# 4rz84r9ptmbsk6cslknz9l4whrgq5sq4qssq9gvs2j94xcjg9ghtdb
# PASS: JNVj0IslQbYdFt9D