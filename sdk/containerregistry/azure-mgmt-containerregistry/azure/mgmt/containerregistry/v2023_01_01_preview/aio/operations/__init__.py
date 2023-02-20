# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._cache_rules_operations import CacheRulesOperations
from ._connected_registries_operations import ConnectedRegistriesOperations
from ._credential_sets_operations import CredentialSetsOperations
from ._export_pipelines_operations import ExportPipelinesOperations
from ._registries_operations import RegistriesOperations
from ._import_pipelines_operations import ImportPipelinesOperations
from ._operations import Operations
from ._pipeline_runs_operations import PipelineRunsOperations
from ._private_endpoint_connections_operations import PrivateEndpointConnectionsOperations
from ._replications_operations import ReplicationsOperations
from ._scope_maps_operations import ScopeMapsOperations
from ._tokens_operations import TokensOperations
from ._webhooks_operations import WebhooksOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CacheRulesOperations",
    "ConnectedRegistriesOperations",
    "CredentialSetsOperations",
    "ExportPipelinesOperations",
    "RegistriesOperations",
    "ImportPipelinesOperations",
    "Operations",
    "PipelineRunsOperations",
    "PrivateEndpointConnectionsOperations",
    "ReplicationsOperations",
    "ScopeMapsOperations",
    "TokensOperations",
    "WebhooksOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()