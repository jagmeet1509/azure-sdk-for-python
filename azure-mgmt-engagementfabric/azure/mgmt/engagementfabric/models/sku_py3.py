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


class SKU(Model):
    """The EngagementFabric SKU.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the SKU
    :type name: str
    :param tier: The price tier of the SKU
    :type tier: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(self, *, name: str, tier: str=None, **kwargs) -> None:
        super(SKU, self).__init__(**kwargs)
        self.name = name
        self.tier = tier
