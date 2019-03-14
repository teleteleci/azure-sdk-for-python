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

from msrest.pipeline import ClientRawResponse

from .. import models


class VersionsOperations(object):
    """VersionsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def clone(
            self, app_id, version_id, azure_region="westus", azure_cloud="com", version=None, custom_headers=None, raw=False, **operation_config):
        """Creates a new version using the current snapshot of the selected
        application version.

        :param azure_region: Supported Azure regions for Cognitive Services
         endpoints. Possible values include: 'westus', 'westeurope',
         'southeastasia', 'eastus2', 'westcentralus', 'westus2', 'eastus',
         'southcentralus', 'northeurope', 'eastasia', 'australiaeast',
         'brazilsouth', 'virginia'
        :type azure_region: str or
         ~azure.cognitiveservices.language.luis.authoring.models.AzureRegions
        :param azure_cloud: Supported Azure Clouds for Cognitive Services
         endpoints. Possible values include: 'com', 'us'
        :type azure_cloud: str or
         ~azure.cognitiveservices.language.luis.authoring.models.AzureClouds
        :param app_id: The application ID.
        :type app_id: str
        :param version_id: The version ID.
        :type version_id: str
        :param version: The new version for the cloned model.
        :type version: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: str or ClientRawResponse if raw=true
        :rtype: str or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.luis.authoring.models.ErrorResponseException>`
        """
        version_clone_object = models.TaskUpdateObject(version=version)

        # Construct URL
        url = self.clone.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("azure_region", azure_region, 'AzureRegions', skip_quote=True),
            'AzureCloud': self._serialize.url("azure_cloud", azure_cloud, 'AzureClouds', skip_quote=True),
            'appId': self._serialize.url("app_id", app_id, 'str'),
            'versionId': self._serialize.url("version_id", version_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(version_clone_object, 'TaskUpdateObject')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('str', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    clone.metadata = {'url': '/apps/{appId}/versions/{versionId}/clone'}

    def list(
            self, app_id, azure_region="westus", azure_cloud="com", skip=0, take=100, custom_headers=None, raw=False, **operation_config):
        """Gets the application versions info.

        :param azure_region: Supported Azure regions for Cognitive Services
         endpoints. Possible values include: 'westus', 'westeurope',
         'southeastasia', 'eastus2', 'westcentralus', 'westus2', 'eastus',
         'southcentralus', 'northeurope', 'eastasia', 'australiaeast',
         'brazilsouth', 'virginia'
        :type azure_region: str or
         ~azure.cognitiveservices.language.luis.authoring.models.AzureRegions
        :param azure_cloud: Supported Azure Clouds for Cognitive Services
         endpoints. Possible values include: 'com', 'us'
        :type azure_cloud: str or
         ~azure.cognitiveservices.language.luis.authoring.models.AzureClouds
        :param app_id: The application ID.
        :type app_id: str
        :param skip: The number of entries to skip. Default value is 0.
        :type skip: int
        :param take: The number of entries to return. Maximum page size is
         500. Default is 100.
        :type take: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype:
         list[~azure.cognitiveservices.language.luis.authoring.models.VersionInfo]
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.luis.authoring.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("azure_region", azure_region, 'AzureRegions', skip_quote=True),
            'AzureCloud': self._serialize.url("azure_cloud", azure_cloud, 'AzureClouds', skip_quote=True),
            'appId': self._serialize.url("app_id", app_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if skip is not None:
            query_parameters['skip'] = self._serialize.query("skip", skip, 'int', minimum=0)
        if take is not None:
            query_parameters['take'] = self._serialize.query("take", take, 'int', maximum=500, minimum=0)

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[VersionInfo]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/apps/{appId}/versions'}

    def get(
            self, app_id, version_id, azure_region="westus", azure_cloud="com", custom_headers=None, raw=False, **operation_config):
        """Gets the version info.

        :param azure_region: Supported Azure regions for Cognitive Services
         endpoints. Possible values include: 'westus', 'westeurope',
         'southeastasia', 'eastus2', 'westcentralus', 'westus2', 'eastus',
         'southcentralus', 'northeurope', 'eastasia', 'australiaeast',
         'brazilsouth', 'virginia'
        :type azure_region: str or
         ~azure.cognitiveservices.language.luis.authoring.models.AzureRegions
        :param azure_cloud: Supported Azure Clouds for Cognitive Services
         endpoints. Possible values include: 'com', 'us'
        :type azure_cloud: str or
         ~azure.cognitiveservices.language.luis.authoring.models.AzureClouds
        :param app_id: The application ID.
        :type app_id: str
        :param version_id: The version ID.
        :type version_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VersionInfo or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.language.luis.authoring.models.VersionInfo or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.luis.authoring.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("azure_region", azure_region, 'AzureRegions', skip_quote=True),
            'AzureCloud': self._serialize.url("azure_cloud", azure_cloud, 'AzureClouds', skip_quote=True),
            'appId': self._serialize.url("app_id", app_id, 'str'),
            'versionId': self._serialize.url("version_id", version_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VersionInfo', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/apps/{appId}/versions/{versionId}/'}

    def update(
            self, app_id, version_id, azure_region="westus", azure_cloud="com", version=None, custom_headers=None, raw=False, **operation_config):
        """Updates the name or description of the application version.

        :param azure_region: Supported Azure regions for Cognitive Services
         endpoints. Possible values include: 'westus', 'westeurope',
         'southeastasia', 'eastus2', 'westcentralus', 'westus2', 'eastus',
         'southcentralus', 'northeurope', 'eastasia', 'australiaeast',
         'brazilsouth', 'virginia'
        :type azure_region: str or
         ~azure.cognitiveservices.language.luis.authoring.models.AzureRegions
        :param azure_cloud: Supported Azure Clouds for Cognitive Services
         endpoints. Possible values include: 'com', 'us'
        :type azure_cloud: str or
         ~azure.cognitiveservices.language.luis.authoring.models.AzureClouds
        :param app_id: The application ID.
        :type app_id: str
        :param version_id: The version ID.
        :type version_id: str
        :param version: The new version for the cloned model.
        :type version: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: OperationStatus or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.language.luis.authoring.models.OperationStatus
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.luis.authoring.models.ErrorResponseException>`
        """
        version_update_object = models.TaskUpdateObject(version=version)

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("azure_region", azure_region, 'AzureRegions', skip_quote=True),
            'AzureCloud': self._serialize.url("azure_cloud", azure_cloud, 'AzureClouds', skip_quote=True),
            'appId': self._serialize.url("app_id", app_id, 'str'),
            'versionId': self._serialize.url("version_id", version_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(version_update_object, 'TaskUpdateObject')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('OperationStatus', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update.metadata = {'url': '/apps/{appId}/versions/{versionId}/'}

    def delete(
            self, app_id, version_id, azure_region="westus", azure_cloud="com", custom_headers=None, raw=False, **operation_config):
        """Deletes an application version.

        :param azure_region: Supported Azure regions for Cognitive Services
         endpoints. Possible values include: 'westus', 'westeurope',
         'southeastasia', 'eastus2', 'westcentralus', 'westus2', 'eastus',
         'southcentralus', 'northeurope', 'eastasia', 'australiaeast',
         'brazilsouth', 'virginia'
        :type azure_region: str or
         ~azure.cognitiveservices.language.luis.authoring.models.AzureRegions
        :param azure_cloud: Supported Azure Clouds for Cognitive Services
         endpoints. Possible values include: 'com', 'us'
        :type azure_cloud: str or
         ~azure.cognitiveservices.language.luis.authoring.models.AzureClouds
        :param app_id: The application ID.
        :type app_id: str
        :param version_id: The version ID.
        :type version_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: OperationStatus or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.language.luis.authoring.models.OperationStatus
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.luis.authoring.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("azure_region", azure_region, 'AzureRegions', skip_quote=True),
            'AzureCloud': self._serialize.url("azure_cloud", azure_cloud, 'AzureClouds', skip_quote=True),
            'appId': self._serialize.url("app_id", app_id, 'str'),
            'versionId': self._serialize.url("version_id", version_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('OperationStatus', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete.metadata = {'url': '/apps/{appId}/versions/{versionId}/'}

    def export(
            self, app_id, version_id, azure_region="westus", azure_cloud="com", custom_headers=None, raw=False, **operation_config):
        """Exports a LUIS application to JSON format.

        :param azure_region: Supported Azure regions for Cognitive Services
         endpoints. Possible values include: 'westus', 'westeurope',
         'southeastasia', 'eastus2', 'westcentralus', 'westus2', 'eastus',
         'southcentralus', 'northeurope', 'eastasia', 'australiaeast',
         'brazilsouth', 'virginia'
        :type azure_region: str or
         ~azure.cognitiveservices.language.luis.authoring.models.AzureRegions
        :param azure_cloud: Supported Azure Clouds for Cognitive Services
         endpoints. Possible values include: 'com', 'us'
        :type azure_cloud: str or
         ~azure.cognitiveservices.language.luis.authoring.models.AzureClouds
        :param app_id: The application ID.
        :type app_id: str
        :param version_id: The version ID.
        :type version_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LuisApp or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.language.luis.authoring.models.LuisApp or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.luis.authoring.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.export.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("azure_region", azure_region, 'AzureRegions', skip_quote=True),
            'AzureCloud': self._serialize.url("azure_cloud", azure_cloud, 'AzureClouds', skip_quote=True),
            'appId': self._serialize.url("app_id", app_id, 'str'),
            'versionId': self._serialize.url("version_id", version_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LuisApp', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    export.metadata = {'url': '/apps/{appId}/versions/{versionId}/export'}

    def import_method(
            self, app_id, luis_app, azure_region="westus", azure_cloud="com", version_id=None, custom_headers=None, raw=False, **operation_config):
        """Imports a new version into a LUIS application.

        :param azure_region: Supported Azure regions for Cognitive Services
         endpoints. Possible values include: 'westus', 'westeurope',
         'southeastasia', 'eastus2', 'westcentralus', 'westus2', 'eastus',
         'southcentralus', 'northeurope', 'eastasia', 'australiaeast',
         'brazilsouth', 'virginia'
        :type azure_region: str or
         ~azure.cognitiveservices.language.luis.authoring.models.AzureRegions
        :param azure_cloud: Supported Azure Clouds for Cognitive Services
         endpoints. Possible values include: 'com', 'us'
        :type azure_cloud: str or
         ~azure.cognitiveservices.language.luis.authoring.models.AzureClouds
        :param app_id: The application ID.
        :type app_id: str
        :param luis_app: A LUIS application structure.
        :type luis_app:
         ~azure.cognitiveservices.language.luis.authoring.models.LuisApp
        :param version_id: The new versionId to import. If not specified, the
         versionId will be read from the imported object.
        :type version_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: str or ClientRawResponse if raw=true
        :rtype: str or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.luis.authoring.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.import_method.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("azure_region", azure_region, 'AzureRegions', skip_quote=True),
            'AzureCloud': self._serialize.url("azure_cloud", azure_cloud, 'AzureClouds', skip_quote=True),
            'appId': self._serialize.url("app_id", app_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if version_id is not None:
            query_parameters['versionId'] = self._serialize.query("version_id", version_id, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(luis_app, 'LuisApp')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('str', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    import_method.metadata = {'url': '/apps/{appId}/versions/import'}

    def delete_unlabelled_utterance(
            self, app_id, version_id, utterance, azure_region="westus", azure_cloud="com", custom_headers=None, raw=False, **operation_config):
        """Deleted an unlabelled utterance.

        :param azure_region: Supported Azure regions for Cognitive Services
         endpoints. Possible values include: 'westus', 'westeurope',
         'southeastasia', 'eastus2', 'westcentralus', 'westus2', 'eastus',
         'southcentralus', 'northeurope', 'eastasia', 'australiaeast',
         'brazilsouth', 'virginia'
        :type azure_region: str or
         ~azure.cognitiveservices.language.luis.authoring.models.AzureRegions
        :param azure_cloud: Supported Azure Clouds for Cognitive Services
         endpoints. Possible values include: 'com', 'us'
        :type azure_cloud: str or
         ~azure.cognitiveservices.language.luis.authoring.models.AzureClouds
        :param app_id: The application ID.
        :type app_id: str
        :param version_id: The version ID.
        :type version_id: str
        :param utterance: The utterance text to delete.
        :type utterance: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: OperationStatus or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.language.luis.authoring.models.OperationStatus
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.luis.authoring.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_unlabelled_utterance.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("azure_region", azure_region, 'AzureRegions', skip_quote=True),
            'AzureCloud': self._serialize.url("azure_cloud", azure_cloud, 'AzureClouds', skip_quote=True),
            'appId': self._serialize.url("app_id", app_id, 'str'),
            'versionId': self._serialize.url("version_id", version_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(utterance, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('OperationStatus', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_unlabelled_utterance.metadata = {'url': '/apps/{appId}/versions/{versionId}/suggest'}
