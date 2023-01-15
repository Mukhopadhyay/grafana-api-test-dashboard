# Tests for utils.http

import pytest
import asyncio
from src.utils import http

@pytest.mark.utils
def test_post_async():
    data = { "name": "morpheus", "job": "leader" }
    resp, elapsed, length, status = asyncio.run(
        http.post_async(
            "https://reqres.in/api/users",
            data=data
        )
    )
    assert isinstance(resp, dict)
    assert isinstance(elapsed, float)
    assert str(length).isnumeric()
    assert isinstance(status, int)

@pytest.mark.utils
def test_get_async():
    resp, elapsed, length, status = asyncio.run(
        http.get_async(
            "https://reqres.in/api/users?page=2"
        )
    )
    assert isinstance(resp, dict)
    assert isinstance(elapsed, float)
    assert str(length).isnumeric()
    assert isinstance(status, int)
