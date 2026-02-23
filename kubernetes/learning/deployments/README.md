- in kubernetes deployments are a way of defining the desired state.. the number of replicas needed 
 
- create deployments
```sh kubectl create deploy test --image=httpd --replicas=3 ```
- get the deployments
```sh kubectl get deployments ```
- delete the deployments
```sh kubectl delete deployments test ```
 
 - logical grouping of clusters is called namespaces

```sh
kubectl create namespace harshith
kubectl get namespaces
kubectl delete namespace harshith
```

```sh
kubectl create namespace harshith 
 kubectl run misha  --image=nginx
kubectl get pods --namespace=harshith
```

- to know the current namespace
```sh
kubectl config current-context
```
- to change namespace
```sh
kubectl config set-context --current --namespace=harshith
```