<!-- Create Dry Run Template -->
kubectl run httpd --image=httpd --dry-run=client -o yaml > httpd.yaml

<!-- Create the pod -->
kubectl create -f filename.yaml

<!-- Apply i.e create or update the pod -->
kubectl apply -f filename.yaml

<!-- Describe running pod info -->
kubectl describe pod nginx

<!-- Get the pods info -->
kubctl get pods

<!-- delete the pod -->
kubectl delete pod <name>

<!-- run some commands into the pod -->
kubectl exec -it nginx -- /bin/bash

<!-- get wide range of pod info like ip addr -->
kubectl get pods -o wide