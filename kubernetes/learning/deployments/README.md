- in kubernetes deployments are a way of defining the desired state.. the number of replicas needed 
 
- create deployments
```sh kubectl create deploy test --image=httpd --replicas=3 ```
- get the deployments
```sh kubectl get deployments ```
- delete the deployments
```sh kubectl delete deployments test ```
 