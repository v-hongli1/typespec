# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import SpecialWordsPreparer
from testpreparer_async import SpecialWordsClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSpecialWordsModelsOperationsAsync(SpecialWordsClientTestBaseAsync):
    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_and(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_and(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_as(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_as(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_assert(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_assert(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_async(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_async(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_await(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_await(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_break(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_break(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_class(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_class(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_constructor(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_constructor(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_continue(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_continue(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_def(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_def(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_del(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_del(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_elif(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_elif(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_else(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_else(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_except(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_except(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_exec(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_exec(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_finally(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_finally(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_for(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_for(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_from(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_from(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_global(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_global(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_if(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_if(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_import(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_import(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_in(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_in(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_is(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_is(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_lambda(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_lambda(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_not(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_not(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_or(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_or(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_pass(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_pass(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_raise(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_raise(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_return(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_return(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_try(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_try(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_while(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_while(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_with(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_with(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_with_yield(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.models.with_yield(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...
