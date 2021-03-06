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


class BatchAIError(Model):
    """An error response from the Batch AI service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: An identifier for the error. Codes are invariant and are
     intended to be consumed programmatically.
    :vartype code: str
    :ivar message: A message describing the error, intended to be suitable for
     display in a user interface.
    :vartype message: str
    :ivar details: A list of additional details about the error.
    :vartype details: list[~azure.mgmt.batchai.models.NameValuePair]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[NameValuePair]'},
    }

    def __init__(self, **kwargs):
        super(BatchAIError, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.details = None
