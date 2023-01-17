import sys
import time
import aiohttp
from typing import Optional, Dict, Any, Tuple


def get_content_length(response: aiohttp.ClientResponse):
    header_keys = [x.casefold() for x in list(response.headers.keys())]
    if 'content-length' in header_keys:
        idx = header_keys.index('content-length')
        len_key = list(response.headers.keys())[idx]
        return response.headers[len_key]
    else:
        return None


async def post_async(
    url,
    data: Dict[Any, Any],
    headers: Optional[Dict[str, Any]] = None
) -> Tuple[Dict[Any, Any], float, int, int]:
    async with aiohttp.ClientSession(headers=headers) as session:
        start = time.time()

        async with session.post(url, json=data) as response:
            json_data = await response.json()
            elapsed = time.time() - start

            content_length = get_content_length(response)
            if not content_length:
                content_length = sys.getsizeof(json_data)

            return (
                json_data, elapsed, content_length, response.status
            )


async def get_async(
    url,
    headers: Optional[Dict[str, Any]] = None
) -> Tuple[Dict[Any, Any], float, int, int]:
    async with aiohttp.ClientSession(headers=headers) as session:
        start = time.time()

        async with session.get(url) as response:
            json_data = await response.json()
            elapsed = time.time() - start

            content_length = get_content_length(response)
            if not content_length:
                content_length = sys.getsizeof(json_data)

            return (
                json_data, elapsed, content_length, response.status
            )

# from utils.utils import detailed_http

# @detailed_http
# async def get(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as client:
#             return client
