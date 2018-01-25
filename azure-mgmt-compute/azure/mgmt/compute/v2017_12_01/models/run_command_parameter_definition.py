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

from msrest.serialization import Model


class RunCommandParameterDefinition(Model):
    """Describes the properties of a run command parameter.

    :param name: The run command parameter name.
    :type name: str
    :param type: The run command parameter type.
    :type type: str
    :param default_value: The run command parameter default value.
    :type default_value: str
    :param required: The run command parameter required. Default value: False
     .
    :type required: bool
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'required': {'key': 'required', 'type': 'bool'},
    }

    def __init__(self, name, type, default_value=None, required=False):
        super(RunCommandParameterDefinition, self).__init__()
        self.name = name
        self.type = type
        self.default_value = default_value
        self.required = required