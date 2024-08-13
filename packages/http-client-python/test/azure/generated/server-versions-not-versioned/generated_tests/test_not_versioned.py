# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import NotVersionedClientTestBase, NotVersionedPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNotVersioned(NotVersionedClientTestBase):
    @NotVersionedPreparer()
    @recorded_by_proxy
    def test_without_api_version(self, notversioned_endpoint):
        client = self.create_client(endpoint=notversioned_endpoint)
        response = client.without_api_version()

        # please add some check logic here by yourself
        # ...

    @NotVersionedPreparer()
    @recorded_by_proxy
    def test_with_query_api_version(self, notversioned_endpoint):
        client = self.create_client(endpoint=notversioned_endpoint)
        response = client.with_query_api_version()

        # please add some check logic here by yourself
        # ...

    @NotVersionedPreparer()
    @recorded_by_proxy
    def test_with_path_api_version(self, notversioned_endpoint):
        client = self.create_client(endpoint=notversioned_endpoint)
        response = client.with_path_api_version()

        # please add some check logic here by yourself
        # ...
