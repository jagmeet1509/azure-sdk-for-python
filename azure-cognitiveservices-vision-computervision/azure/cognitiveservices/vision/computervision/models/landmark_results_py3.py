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


class LandmarkResults(Model):
    """List of landmarks recognized in the image.

    :param landmarks:
    :type landmarks:
     list[~azure.cognitiveservices.vision.computervision.models.LandmarksModel]
    :param request_id: Id of the REST API request.
    :type request_id: str
    :param metadata:
    :type metadata:
     ~azure.cognitiveservices.vision.computervision.models.ImageMetadata
    """

    _attribute_map = {
        'landmarks': {'key': 'landmarks', 'type': '[LandmarksModel]'},
        'request_id': {'key': 'requestId', 'type': 'str'},
        'metadata': {'key': 'metadata', 'type': 'ImageMetadata'},
    }

    def __init__(self, *, landmarks=None, request_id: str=None, metadata=None, **kwargs) -> None:
        super(LandmarkResults, self).__init__(**kwargs)
        self.landmarks = landmarks
        self.request_id = request_id
        self.metadata = metadata
