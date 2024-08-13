# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import BasicClientTestBase, BasicPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBasic(BasicClientTestBase):
    @BasicPreparer()
    @recorded_by_proxy
    def test_create_or_update(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.create_or_update(
            id=0,
            resource={"etag": "str", "id": 0, "name": "str", "orders": [{"detail": "str", "id": 0, "userId": 0}]},
        )

        # please add some check logic here by yourself
        # ...

    @BasicPreparer()
    @recorded_by_proxy
    def test_create_or_replace(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.create_or_replace(
            id=0,
            resource={"etag": "str", "id": 0, "name": "str", "orders": [{"detail": "str", "id": 0, "userId": 0}]},
        )

        # please add some check logic here by yourself
        # ...

    @BasicPreparer()
    @recorded_by_proxy
    def test_get(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.get(
            id=0,
        )

        # please add some check logic here by yourself
        # ...

    @BasicPreparer()
    @recorded_by_proxy
    def test_list(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.list()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @BasicPreparer()
    @recorded_by_proxy
    def test_list_with_page(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.list_with_page()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @BasicPreparer()
    @recorded_by_proxy
    def test_list_with_parameters(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.list_with_parameters(
            body_input={"inputName": "str"},
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @BasicPreparer()
    @recorded_by_proxy
    def test_list_with_custom_page_model(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.list_with_custom_page_model()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @BasicPreparer()
    @recorded_by_proxy
    def test_delete(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.delete(
            id=0,
        )

        # please add some check logic here by yourself
        # ...

    @BasicPreparer()
    @recorded_by_proxy
    def test_export(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.export(
            id=0,
            format="str",
        )

        # please add some check logic here by yourself
        # ...
