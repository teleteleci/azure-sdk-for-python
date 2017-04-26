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

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.billing_periods_operations import BillingPeriodsOperations
from .operations.invoices_operations import InvoicesOperations
from .operations.operations import Operations
from . import models


class BillingManagementClientConfiguration(AzureConfiguration):
    """Configuration for BillingManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not isinstance(subscription_id, str):
            raise TypeError("Parameter 'subscription_id' must be str.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(BillingManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-billing/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class BillingManagementClient(object):
    """Billing client provides access to billing resources for Azure Web-Direct subscriptions. Other subscription types which were not purchased directly through the Azure web portal are not supported through this preview API.

    :ivar config: Configuration for client.
    :vartype config: BillingManagementClientConfiguration

    :ivar billing_periods: BillingPeriods operations
    :vartype billing_periods: .operations.BillingPeriodsOperations
    :ivar invoices: Invoices operations
    :vartype invoices: .operations.InvoicesOperations
    :ivar operations: Operations operations
    :vartype operations: .operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = BillingManagementClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2017-04-24-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.billing_periods = BillingPeriodsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.invoices = InvoicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)