# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.container_host_mappings_operations import ContainerHostMappingsOperations
from .operations.operations import Operations
from .operations.controllers_operations import ControllersOperations
from . import models


class DevSpacesManagementClientConfiguration(AzureConfiguration):
    """Configuration for DevSpacesManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(DevSpacesManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-devspaces/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class DevSpacesManagementClient(SDKClient):
    """Dev Spaces Client

    :ivar config: Configuration for client.
    :vartype config: DevSpacesManagementClientConfiguration

    :ivar container_host_mappings: ContainerHostMappings operations
    :vartype container_host_mappings: azure.mgmt.devspaces.operations.ContainerHostMappingsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.devspaces.operations.Operations
    :ivar controllers: Controllers operations
    :vartype controllers: azure.mgmt.devspaces.operations.ControllersOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = DevSpacesManagementClientConfiguration(credentials, subscription_id, base_url)
        super(DevSpacesManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-01-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.container_host_mappings = ContainerHostMappingsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.controllers = ControllersOperations(
            self._client, self.config, self._serialize, self._deserialize)
