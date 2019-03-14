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


class PatternOperations(object):
    """PatternOperations operations.

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

    def add_pattern(
            self, app_id, version_id, azure_region="westus", azure_cloud="com", pattern=None, intent=None, custom_headers=None, raw=False, **operation_config):
        """Adds one pattern to the specified application.

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
        :param pattern: The pattern text.
        :type pattern: str
        :param intent: The intent's name which the pattern belongs to.
        :type intent: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PatternRuleInfo or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.language.luis.authoring.models.PatternRuleInfo
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.luis.authoring.models.ErrorResponseException>`
        """
        pattern1 = models.PatternRuleCreateObject(pattern=pattern, intent=intent)

        # Construct URL
        url = self.add_pattern.metadata['url']
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
        body_content = self._serialize.body(pattern1, 'PatternRuleCreateObject')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('PatternRuleInfo', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_pattern.metadata = {'url': '/apps/{appId}/versions/{versionId}/patternrule'}

    def list_patterns(
            self, app_id, version_id, azure_region="westus", azure_cloud="com", skip=0, take=100, custom_headers=None, raw=False, **operation_config):
        """Returns an application version's patterns.

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
         list[~azure.cognitiveservices.language.luis.authoring.models.PatternRuleInfo]
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.luis.authoring.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_patterns.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("azure_region", azure_region, 'AzureRegions', skip_quote=True),
            'AzureCloud': self._serialize.url("azure_cloud", azure_cloud, 'AzureClouds', skip_quote=True),
            'appId': self._serialize.url("app_id", app_id, 'str'),
            'versionId': self._serialize.url("version_id", version_id, 'str')
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
            deserialized = self._deserialize('[PatternRuleInfo]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_patterns.metadata = {'url': '/apps/{appId}/versions/{versionId}/patternrules'}

    def update_patterns(
            self, app_id, version_id, patterns, azure_region="westus", azure_cloud="com", custom_headers=None, raw=False, **operation_config):
        """Updates patterns.

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
        :param patterns: An array represents the patterns.
        :type patterns:
         list[~azure.cognitiveservices.language.luis.authoring.models.PatternRuleUpdateObject]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype:
         list[~azure.cognitiveservices.language.luis.authoring.models.PatternRuleInfo]
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.luis.authoring.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.update_patterns.metadata['url']
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
        body_content = self._serialize.body(patterns, '[PatternRuleUpdateObject]')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[PatternRuleInfo]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_patterns.metadata = {'url': '/apps/{appId}/versions/{versionId}/patternrules'}

    def batch_add_patterns(
            self, app_id, version_id, patterns, azure_region="westus", azure_cloud="com", custom_headers=None, raw=False, **operation_config):
        """Adds a batch of patterns to the specified application.

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
        :param patterns: A JSON array containing patterns.
        :type patterns:
         list[~azure.cognitiveservices.language.luis.authoring.models.PatternRuleCreateObject]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype:
         list[~azure.cognitiveservices.language.luis.authoring.models.PatternRuleInfo]
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.luis.authoring.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.batch_add_patterns.metadata['url']
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
        body_content = self._serialize.body(patterns, '[PatternRuleCreateObject]')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('[PatternRuleInfo]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    batch_add_patterns.metadata = {'url': '/apps/{appId}/versions/{versionId}/patternrules'}

    def delete_patterns(
            self, app_id, version_id, pattern_ids, azure_region="westus", azure_cloud="com", custom_headers=None, raw=False, **operation_config):
        """Deletes the patterns with the specified IDs.

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
        :param pattern_ids: The patterns IDs.
        :type pattern_ids: list[str]
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
        url = self.delete_patterns.metadata['url']
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
        body_content = self._serialize.body(pattern_ids, '[str]')

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
    delete_patterns.metadata = {'url': '/apps/{appId}/versions/{versionId}/patternrules'}

    def update_pattern(
            self, app_id, version_id, pattern_id, pattern, azure_region="westus", azure_cloud="com", custom_headers=None, raw=False, **operation_config):
        """Updates a pattern.

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
        :param pattern_id: The pattern ID.
        :type pattern_id: str
        :param pattern: An object representing a pattern.
        :type pattern:
         ~azure.cognitiveservices.language.luis.authoring.models.PatternRuleUpdateObject
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PatternRuleInfo or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.language.luis.authoring.models.PatternRuleInfo
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.luis.authoring.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.update_pattern.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("azure_region", azure_region, 'AzureRegions', skip_quote=True),
            'AzureCloud': self._serialize.url("azure_cloud", azure_cloud, 'AzureClouds', skip_quote=True),
            'appId': self._serialize.url("app_id", app_id, 'str'),
            'versionId': self._serialize.url("version_id", version_id, 'str'),
            'patternId': self._serialize.url("pattern_id", pattern_id, 'str')
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
        body_content = self._serialize.body(pattern, 'PatternRuleUpdateObject')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PatternRuleInfo', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_pattern.metadata = {'url': '/apps/{appId}/versions/{versionId}/patternrules/{patternId}'}

    def delete_pattern(
            self, app_id, version_id, pattern_id, azure_region="westus", azure_cloud="com", custom_headers=None, raw=False, **operation_config):
        """Deletes the pattern with the specified ID.

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
        :param pattern_id: The pattern ID.
        :type pattern_id: str
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
        url = self.delete_pattern.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("azure_region", azure_region, 'AzureRegions', skip_quote=True),
            'AzureCloud': self._serialize.url("azure_cloud", azure_cloud, 'AzureClouds', skip_quote=True),
            'appId': self._serialize.url("app_id", app_id, 'str'),
            'versionId': self._serialize.url("version_id", version_id, 'str'),
            'patternId': self._serialize.url("pattern_id", pattern_id, 'str')
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
    delete_pattern.metadata = {'url': '/apps/{appId}/versions/{versionId}/patternrules/{patternId}'}

    def list_intent_patterns(
            self, app_id, version_id, intent_id, azure_region="westus", azure_cloud="com", skip=0, take=100, custom_headers=None, raw=False, **operation_config):
        """Returns patterns to be retrieved for the specific intent.

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
        :param intent_id: The intent classifier ID.
        :type intent_id: str
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
         list[~azure.cognitiveservices.language.luis.authoring.models.PatternRuleInfo]
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.luis.authoring.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_intent_patterns.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("azure_region", azure_region, 'AzureRegions', skip_quote=True),
            'AzureCloud': self._serialize.url("azure_cloud", azure_cloud, 'AzureClouds', skip_quote=True),
            'appId': self._serialize.url("app_id", app_id, 'str'),
            'versionId': self._serialize.url("version_id", version_id, 'str'),
            'intentId': self._serialize.url("intent_id", intent_id, 'str')
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
            deserialized = self._deserialize('[PatternRuleInfo]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_intent_patterns.metadata = {'url': '/apps/{appId}/versions/{versionId}/intents/{intentId}/patternrules'}
