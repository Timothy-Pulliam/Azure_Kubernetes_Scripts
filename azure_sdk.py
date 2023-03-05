#!/usr/bin/env python

from azure.identity import DefaultAzureCredential
from azure.mgmt.containerservice import ContainerServiceClient
from pprint import pprint

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-containerservice
# USAGE
    python agent_pools_list.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""

subscription_id=""
resource_group_name=""
resource_name=""

client = ContainerServiceClient(
    credential=DefaultAzureCredential(),
    subscription_id=subscription_id,
)

def get_managed_clusters():
    response = client.managed_clusters.list()
    print(help(client.managed_clusters.list))
    exit(1)
    for item in response:
        pprint(item.as_dict())

def get_agent_pools():
    response = client.agent_pools.list(
        resource_group_name=resource_group_name,
        resource_name=resource_name,
    )
    for item in response:
        pprint(item.as_dict())


# x-ms-original-file: specification/containerservice/resource-manager/Microsoft.ContainerService/aks/stable/2023-01-01/examples/AgentPoolsList.json
if __name__ == "__main__":
    get_managed_clusters()
    get_agent_pools()
