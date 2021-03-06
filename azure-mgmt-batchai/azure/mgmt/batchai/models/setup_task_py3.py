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


class SetupTask(Model):
    """Specifies a setup task which can be used to customize the compute nodes of
    the cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param command_line: Required. Command line to be executed on each
     cluster's node after it being allocated or rebooted. Command line to be
     executed on each cluster's node after it being allocated or rebooted. The
     command is executed in a bash subshell as a root.
    :type command_line: str
    :param environment_variables: Collection of environment variables to be
     set for setup task.
    :type environment_variables:
     list[~azure.mgmt.batchai.models.EnvironmentVariable]
    :param secrets: Collection of environment variables with secret values to
     be set for setup task. Server will never report values of these variables
     back.
    :type secrets:
     list[~azure.mgmt.batchai.models.EnvironmentVariableWithSecretValue]
    :param std_out_err_path_prefix: Required. The prefix of a path where the
     Batch AI service will upload the stdout and stderr of the setup task.
    :type std_out_err_path_prefix: str
    :ivar std_out_err_path_suffix: A path segment appended by Batch AI to
     stdOutErrPathPrefix to form a path where stdout and stderr of the setup
     task will be uploaded. Batch AI creates the setup task output directories
     under an unique path to avoid conflicts between different clusters. You
     can concatinate stdOutErrPathPrefix and stdOutErrPathSuffix to get the
     full path to the output directory.
    :vartype std_out_err_path_suffix: str
    """

    _validation = {
        'command_line': {'required': True},
        'std_out_err_path_prefix': {'required': True},
        'std_out_err_path_suffix': {'readonly': True},
    }

    _attribute_map = {
        'command_line': {'key': 'commandLine', 'type': 'str'},
        'environment_variables': {'key': 'environmentVariables', 'type': '[EnvironmentVariable]'},
        'secrets': {'key': 'secrets', 'type': '[EnvironmentVariableWithSecretValue]'},
        'std_out_err_path_prefix': {'key': 'stdOutErrPathPrefix', 'type': 'str'},
        'std_out_err_path_suffix': {'key': 'stdOutErrPathSuffix', 'type': 'str'},
    }

    def __init__(self, *, command_line: str, std_out_err_path_prefix: str, environment_variables=None, secrets=None, **kwargs) -> None:
        super(SetupTask, self).__init__(**kwargs)
        self.command_line = command_line
        self.environment_variables = environment_variables
        self.secrets = secrets
        self.std_out_err_path_prefix = std_out_err_path_prefix
        self.std_out_err_path_suffix = None
