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


class RegexEntityExtractor(Model):
    """Regex Entity Extractor.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The ID of the Entity Model.
    :type id: str
    :param name: Name of the Entity Model.
    :type name: str
    :param type_id: The type ID of the Entity Model.
    :type type_id: int
    :param readable_type: Required. Possible values include: 'Entity
     Extractor', 'Hierarchical Entity Extractor', 'Hierarchical Child Entity
     Extractor', 'Composite Entity Extractor', 'Closed List Entity Extractor',
     'Prebuilt Entity Extractor', 'Intent Classifier', 'Pattern.Any Entity
     Extractor', 'Regex Entity Extractor'
    :type readable_type: str or
     ~azure.cognitiveservices.language.luis.authoring.models.enum
    :param roles:
    :type roles:
     list[~azure.cognitiveservices.language.luis.authoring.models.EntityRole]
    :param regex_pattern: The Regex entity pattern.
    :type regex_pattern: str
    """

    _validation = {
        'id': {'required': True},
        'readable_type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type_id': {'key': 'typeId', 'type': 'int'},
        'readable_type': {'key': 'readableType', 'type': 'str'},
        'roles': {'key': 'roles', 'type': '[EntityRole]'},
        'regex_pattern': {'key': 'regexPattern', 'type': 'str'},
    }

    def __init__(self, *, id: str, readable_type, name: str=None, type_id: int=None, roles=None, regex_pattern: str=None, **kwargs) -> None:
        super(RegexEntityExtractor, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.type_id = type_id
        self.readable_type = readable_type
        self.roles = roles
        self.regex_pattern = regex_pattern
