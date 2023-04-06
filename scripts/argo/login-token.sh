token="Bearer $(kubectl get secret -n $1 argo-user.service-account-token -o=jsonpath='{.data.token}' | base64 --decode)"

echo $token

# Copy to clipboard
echo $token | clip.exe