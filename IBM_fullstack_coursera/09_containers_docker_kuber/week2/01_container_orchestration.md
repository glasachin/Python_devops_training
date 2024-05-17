# Container Orchestration
One container (which starts with single deployment) becomes multiple containers as deployment need increases. To manage large number of containers `container orchestration` is needed.

## Container Orchestration
It is a process that automates the container lifecycle of containerized applications. Lifecycle of container includes the following:
* Deployment
* Management
* Scaling
* Networking
* Availability

## Container orchestration features
1. Defines container images and registry.
2. Improves provisioning and deployment
3. Secures network connectivity
4. Ensures availability and performance.
5. Manages scalability and load balancing.
6. Resource allocation and scheduling.
7. Rolling updates and roll backs.
8. Health checks and automated error handling.

## Working of Orchestration
* It used configuration files `YAML or JSON` to find resources, establish a network and store logs.
* Deployment scheduling
    * Automatically schedules new container deployment
    * Finds the right host based on predefined settings or restrictions.

* Manages container lifecycle
    * configuration file specs inform container decisions
        * system parameters
        * File parameters.

* Scaling and productivity

## container Orchestration tools

* Marathon
* Nomad
* Docker Swarm
* Kubernetes ==> standard for open source container orchestration platforms.