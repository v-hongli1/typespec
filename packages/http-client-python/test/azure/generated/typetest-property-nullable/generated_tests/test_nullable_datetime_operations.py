# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import NullableClientTestBase, NullablePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNullableDatetimeOperations(NullableClientTestBase):
    @NullablePreparer()
    @recorded_by_proxy
    def test_get_non_null(self, nullable_endpoint):
        client = self.create_client(endpoint=nullable_endpoint)
        response = client.datetime.get_non_null()

        # please add some check logic here by yourself
        # ...

    @NullablePreparer()
    @recorded_by_proxy
    def test_get_null(self, nullable_endpoint):
        client = self.create_client(endpoint=nullable_endpoint)
        response = client.datetime.get_null()

        # please add some check logic here by yourself
        # ...

    @NullablePreparer()
    @recorded_by_proxy
    def test_patch_non_null(self, nullable_endpoint):
        client = self.create_client(endpoint=nullable_endpoint)
        response = client.datetime.patch_non_null(
            body={"nullableProperty": "2020-02-20 00:00:00", "requiredProperty": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @NullablePreparer()
    @recorded_by_proxy
    def test_patch_null(self, nullable_endpoint):
        client = self.create_client(endpoint=nullable_endpoint)
        response = client.datetime.patch_null(
            body={"nullableProperty": "2020-02-20 00:00:00", "requiredProperty": "str"},
        )

        # please add some check logic here by yourself
        # ...
