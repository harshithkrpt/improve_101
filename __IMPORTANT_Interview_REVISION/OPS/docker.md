# Docker Commands

- running a docker image

```sh
docker run nginx
```

- list containers 

```sh
docker ps
```

- list all running and exited use -a option

```sh
docker ps -a
```

- stop a container

```sh
docker stop <container-name>
```

> find out container-name using docker ps

- remove a container

```sh
docker rm <container-name>
```

- list images 

```sh
docker images
```

- remove a image

> to remove an image , all the dependant containers should be stopped and removed

```sh
docker rmi <image-name>
```

- download an image but not run it 

```sh
docker pull <image-name>
```

- to run a command inside a container

```sh
docker exec <container-name> cat /etc/hosts
```

- run a image and detach

```sh
docker run -d kodukloud/simple-webapp 
```

- to attach the container

```sh
docker attach <container-id> # first 5 chars are enough
```

