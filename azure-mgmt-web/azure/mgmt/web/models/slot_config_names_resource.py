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

from .proxy_only_resource import ProxyOnlyResource


class SlotConfigNamesResource(ProxyOnlyResource):
    """Slot Config names azure resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param connection_string_names: List of connection string names.
    :type connection_string_names: list[str]
    :param app_setting_names: List of application settings names.
    :type app_setting_names: list[str]
    :param azure_storage_config_names: List of external Azure storage account
     identifiers.
    :type azure_storage_config_names: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'connection_string_names': {'key': 'properties.connectionStringNames', 'type': '[str]'},
        'app_setting_names': {'key': 'properties.appSettingNames', 'type': '[str]'},
        'azure_storage_config_names': {'key': 'properties.azureStorageConfigNames', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(SlotConfigNamesResource, self).__init__(**kwargs)
        self.connection_string_names = kwargs.get('connection_string_names', None)
        self.app_setting_names = kwargs.get('app_setting_names', None)
        self.azure_storage_config_names = kwargs.get('azure_storage_config_names', None)
