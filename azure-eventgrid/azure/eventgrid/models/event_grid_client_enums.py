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

from enum import Enum


class JobState(str, Enum):

    canceled = "Canceled"  #: The job was canceled. This is a final state for the job.
    canceling = "Canceling"  #: The job is in the process of being canceled. This is a transient state for the job.
    error = "Error"  #: The job has encountered an error. This is a final state for the job.
    finished = "Finished"  #: The job is finished. This is a final state for the job.
    processing = "Processing"  #: The job is processing. This is a transient state for the job.
    queued = "Queued"  #: The job is in a queued state, waiting for resources to become available. This is a transient state.
    scheduled = "Scheduled"  #: The job is being scheduled to run on an available resource. This is a transient state, between queued and processing states.