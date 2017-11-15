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


class ARMErrorResponseBody(Model):
    """ARM error response body.

    :param message: Gets or sets the string that describes the error in detail
     and provides debugging information.
    :type message: str
    :param code: Gets or sets the string that can be used to programmatically
     identify the error.
    :type code: str
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
    }

    def __init__(self, message=None, code=None):
        self.message = message
        self.code = code