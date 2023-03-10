import sys
import time
from typing import Any, Dict, Optional, Tuple

import aiohttp


def get_content_length(response: aiohttp.ClientResponse):
    header_keys = [x.casefold() for x in list(response.headers.keys())]
    if "content-length" in header_keys:
        idx = header_keys.index("content-length")
        len_key = list(response.headers.keys())[idx]
        return response.headers[len_key]
    else:
        return None


async def put_async(
    url, data: Optional[Dict[Any, Any]] = None, headers: Optional[Dict[str, Any]] = None
) -> Tuple[Dict[Any, Any], float, int, int]:
    async with aiohttp.ClientSession(headers=headers) as session:
        start = time.time()

        async with session.put(url, json=data) as response:
            json_data = await response.json()
            elapsed = time.time() - start

            content_length = get_content_length(response)
            if not content_length:
                content_length = sys.getsizeof(json_data)

            return (json_data, elapsed, content_length, response.status)


async def delete_async(
    url, data: Optional[Dict[Any, Any]] = None, headers: Optional[Dict[str, Any]] = None
) -> Tuple[Dict[Any, Any], float, int, int]:
    async with aiohttp.ClientSession(headers=headers) as session:
        start = time.time()

        async with session.delete(url, json=data) as response:
            json_data = await response.json()
            elapsed = time.time() - start

            content_length = get_content_length(response)
            if not content_length:
                content_length = sys.getsizeof(json_data)

            return (json_data, elapsed, content_length, response.status)


async def post_async(
    url: str, data: Dict[Any, Any] = None, headers: Optional[Dict[str, Any]] = None
) -> Tuple[Dict[Any, Any], float, int, int]:
    async with aiohttp.ClientSession(headers=headers) as session:
        start = time.time()

        async with session.post(url, json=data) as response:
            json_data = await response.json()
            elapsed = time.time() - start

            content_length = get_content_length(response)
            if not content_length:
                content_length = sys.getsizeof(json_data)

            return (json_data, elapsed, content_length, response.status)


async def get_async(url, headers: Optional[Dict[str, Any]] = None) -> Tuple[Dict[Any, Any], float, int, int]:
    async with aiohttp.ClientSession(headers=headers) as session:
        start = time.time()

        async with session.get(url) as response:
            json_data = await response.json()
            elapsed = time.time() - start

            content_length = get_content_length(response)
            if not content_length:
                content_length = sys.getsizeof(json_data)

            return (json_data, elapsed, content_length, response.status)


async def patch_async(
    url, data: Dict[Any, Any], headers: Optional[Dict[str, Any]] = None
) -> Tuple[Dict[Any, Any], float, int, int]:
    async with aiohttp.ClientSession(headers=headers) as session:
        start = time.time()

        async with session.patch(url, json=data) as response:
            json_data = await response.json()
            elapsed = time.time() - start

            content_length = get_content_length(response)
            if not content_length:
                content_length = sys.getsizeof(json_data)

            return (json_data, elapsed, content_length, response.status)
