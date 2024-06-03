# Autoscaling
It enables scaling as needed. It occurs at two level
* Cluster/Node level
* Pod level

Autoscaler Types:
* Horizontal Pod Autoscaler (HPA)
* Vertical Pod Autoscaler (VPA)
* Cluster Autoscaler (CA)

## Create Autoscaling with Kubectl
There is a `autoscale` command with attributes

`kubectl autoscale deploy hello-kubernetes --min=2 --max=5 --cpu-percent=50`


The deployment uses the `Replicaset` to scale up and down.

## Autoscaling Types
There are `three` autoscaling types:

1. `Horizontal Pod Autoscaler (HPA):` Adjusts the number of replicas of an application by increasing or decreasing the number of pods.
    * `kubectl get hpa`
    * We can create autoscale manually in a YAML file.

2. `Vertical Pod Autoscaler (VPA):` Adjusts the resource requests and limits of a container by increasing or decreasing the resource size or speed of the pods.
    * It adds resources to an existing machine. A VPA lets us to scale a service vertically within a cluster.

3. `Cluster Autoscaler (CA):` Adjusts the number of nodes in the cluster when pods fail to schedule or when demand increases or decreases in relation to the capacity of existing nodes.
    * It autoscales the cluster itself.


