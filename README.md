## About

Azure API does not currently have a way to obtain AKS container information.

https://learn.microsoft.com/en-us/answers/questions/779912/azure-aks-api-to-get-details-on-docker-containers

## Configuration

You must obtain k8s cluster config using AZ cli. For example

`az aks get-credentials --resource-group rg-aks-dev --name aks-dev`

This will import the k8s cluster context into your `~/.kube/config`. This is where the python kubernetes client finds authentication information.

## Helpful Resources

https://learn.microsoft.com/en-us/rest/api/aks/agent-pools/list?tabs=Python#list-agent-pools-by-managed-cluster
