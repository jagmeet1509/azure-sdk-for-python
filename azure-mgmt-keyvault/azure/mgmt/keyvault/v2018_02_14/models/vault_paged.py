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

from msrest.paging import Paged


class VaultPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Vault <azure.mgmt.keyvault.v2018_02_14.models.Vault>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Vault]'}
    }

    def __init__(self, *args, **kwargs):

        super(VaultPaged, self).__init__(*args, **kwargs)