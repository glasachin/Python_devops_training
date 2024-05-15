# Docker

* It is an oper platform, or engine where:
    * develop, ship and run

* It is written in `Go` programming language.
* It uses Linux Kernel's features to deliver functionality.
* Uses the `namespaces` technology to provide an isolated workspace called `container`.
* Creates a set of `namespaces` for every container and each aspect runs in a separeate namespace with access limited to that namespace.
* It supports `Agile` and `CI/CD` Devops practices.

* Docker is not good for the following applications:
    * Requiring high performance or security
    * Based on Monolith Architecture
    * Using rich GUI features
    * Performing standard desktop or limited functions


## Bulding and Running Container Image using Dockerfile

**Docker Container Creation Process**

steps are as follows:

1. Create a `dockerfile`.
2. Use the `dockerfile` to create a container image.
3. Use the `container image` to create a running container.


**Dockerfile Example**

```
FROM alpine
CMD ["echo", 
Hello World!"]
```

`FROM`: defines the base image
`CMD` : prints the words on terminal.

**Cocker build command**

format is as follows

`docker <command> <tag> <repository>:<version> <current_directory>`

`docker build -t my-app:v1 .`

**Docker Image Verification**

`$docker images`

**Docker Run Command**

`$ docker run my-app:v1`

`$ docker ps -a`

### different command purpose and example

| command | Purpose | Example|
|----|----|----|
|build|creates container images from a docker file| `docker build -t my-app:v1`|
|images|Lists all images, repo, tags and sizes|`docker images`|
run| creates a container from an image | `docker run -p 8080:80 nginx`|
push|Stores images in a configured registry|`docker push my-app:v1`|
pull|retrieves images from a configured registry|`docker pull nginx`|


## Docker Objects

1. `dockerfile`: It is a text file containing instructions needed to create an image.
    * It should only have `one command instruction`. If it has multiple command instructions then only the last `command instruction` will take effect.
    * `FROM`, `RUN`, `CMD`
2. `Docker Image`: It is a read-only template with instructions for creating docker container.
    * it is built using instructions in a `dockerfile`.
    * Each instruction creates a new `read-only` image layer docker image.
    * Layers can be shared between images, which saves disk space. 
    * **container image** naming, `hostname/repository:tag`. e.g. `docker.io/ubuntu:18.04`

3. `Docker Container`: It is a runnable instance of an image.
    * Can be created, stopped, started or deleted using the docker API or CLI.

4. `Docker Networks`: Networks are used for the isolated container communication

5. `Storage`: Docker uses volumes and bind mounts to persist data even after a container stops.

6. `Plugins`: Storage pugins provide the ability to connect to external sorage platforms.


## Docker Architecture
It is based on client-server architecture. 

**Docker Process Overview**

1. Docker CLI (command line interface) or `REST APIs`, docker client sends instructions or commands to the `Docker Host Server`.
2. The `host` (docker host server), includes the `Docker Daemon` known as `dockerd`.
3. The `daemon` listens for Docker API requests or commands such as `docker run` and processes those commands.
4. The `daemon` builds, runs and distributes containers to the registry.
5. The `registry` stores the images.

**Docker Host**
The docker hosts also includes and manages: `Images, Containers, Namespaces, Networks, Storage, Plugins and add-ons`.

**Docker Communications**
1. The docker client can communicate with both local and remote hosts.
2. Docker client and host daemon can run on same system or on different systems.
3. Docker daemons can also communicate with other daemons to manage docker services.

**Registry**

1. It stores and distributes images.
2. Access is public or private.
    * `Public` such as Docker Hub --> Everyone can access.
    * `Private` implemented for security
3. Registry locations are either hosted or self-hosted.

**Registry Access**
 
* Developers build and push images using automation or a build pipeline to a registry where docker stores these images.
* Then local systems or cloud etc, can pull the images.

![](./1_Q-9FEZawpzE63afTdtEZ4w.gif)



