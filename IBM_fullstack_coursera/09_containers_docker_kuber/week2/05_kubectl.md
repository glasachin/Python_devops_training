# Using Kubectl
It is `Kubernetes` command line interface. 

## Command Structure

`kubectl [command] [type] [name] [flags]`

* `command`: any operation to be performed
* `type`: resource type
* `name`: resource name
* `flags` : special options or modifiers that override default values.

## Imperative Commands
create, update and delete live objects directly:

* Operations specified as arguments or flags. ```kubectl run nginx --image nginx```
* No audit trail

## Imperative object configuration
The kubectl command specifies required operations, operational flags and at least one file name:

* The configuration file specified must contain a full definition of the objects in YAML or JSON format.
```kubectl create -f nginx.yaml```

* Configuration templates help replicate identical results.

### Declarative object configuration
It stores configuration data in files:
* Operations are identified by `Kubectl`, not the user
* works on directories or individual files

`kubectl apply -f nginx/`

* they define desired state


## Cheat Sheet: Understanding Kubernetes Architecture

Command	|Description
---|---
for …do|	Runs a for command multiple times as specified.
kubectl apply|	Applies a configuration to a resource.
kubectl config get-clusters	|Displays clusters defined in the kubeconfig.
kubectl config get-contexts|	Displays the current context.
kubectl create	|Creates a resource.
kubectl delete|	Deletes resources.
kubectl describe	|Shows details of a resource or group of resources.
kubectl expose	|Exposes a resource to the internet as a Kubernetes service.
kubectl get	|Displays resources.
kubectl get pods	|Lists all the Pods.
kubectl get pods -o wide	|Lists all the Pods with details.
kubectl get deployments	|Lists the deployments created.
kubectl get services	|Lists the services created.
kubectl proxy	|Creates a proxy server between a localhost and the Kubernetes API server.
kubectl run	|Creates and runs a particular image in a pod.
kubectl version	|Prints the client and server version information.
