# Replica Set
If application is deployed as single pod then it will be unable to perform certain actions if requests increase manifold or outages occur.

It can't 
* accomodate growing demands
* Handle outages
* Minimize downtime
* Auto restart on interruptions

A `replicaset` ensures the right number of pods are always up and running. I adds or deletes pods for scaling and redundancy. 

Kubernetes keeps object types independent. A `replicaset` does not own pods. It uses pod labels. 

A `replicaset` is automatically created for you when we create a deployment. It we describe the pod, we will see the pod's details and that it controlled. 

## Create Replicaset from scratch
to create, we need to apply YAML file with the kind attribute set to `Replicaset`. STeps are as follows:

* create: `kubectl create -f replicaset.yaml`
* check: `kubectl get pods`
* get: `kubectl get rs`

## Replicaset: Create Deployment
Before we scale a deployment, we must ensure to have a deployment and pod. 
* create deployment: `kubectl create -f deployment.yaml`
* `kubectl get pods`
* `kubectl get deploy`

## ReplicaSet: Scale Deployment
Once the deployment and pod are in place, we can scale our deployment. 

* `kubectl scale deploy hello-kubernetes --replicas=3`
* `kubectl get pods`

