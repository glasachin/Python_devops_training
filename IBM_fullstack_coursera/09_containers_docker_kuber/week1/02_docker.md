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

