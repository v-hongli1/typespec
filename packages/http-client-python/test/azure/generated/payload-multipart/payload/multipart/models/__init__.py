# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import Address
from ._models import BinaryArrayPartsRequest
from ._models import ComplexPartsRequest
from ._models import JsonArrayPartsRequest
from ._models import JsonPartRequest
from ._models import MultiBinaryPartsRequest
from ._models import MultiPartRequest
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Address",
    "BinaryArrayPartsRequest",
    "ComplexPartsRequest",
    "JsonArrayPartsRequest",
    "JsonPartRequest",
    "MultiBinaryPartsRequest",
    "MultiPartRequest",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
