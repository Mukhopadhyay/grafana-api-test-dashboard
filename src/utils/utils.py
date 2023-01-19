import sys
from functools import wraps
from time import time
from typing import Any, Callable, Dict, Tuple

import aiohttp


def get_content_length(response: aiohttp.ClientResponse):
    header_keys = [x.casefold() for x in list(response.headers.keys())]
    if "content-length" in header_keys:
        idx = header_keys.index("content-length")
        len_key = list(response.headers.keys())[idx]
        return response.headers[len_key]
    else:
        return None


# TODO: The clientresponse will have lost connection by the time it reaches here
def detailed_http(function: Callable[[str, Dict[Any, Any], None], aiohttp.ClientResponse]) -> Callable:
    """Decorator for detail based on aiohttp.ClientResponse object"""

    @wraps(function)
    async def wrapper(*args, **kwargs) -> Tuple[Dict[Any, Any], float, int, int]:
        print(function)
        t1 = time()
        client: aiohttp.ClientResponse = await function(*args, **kwargs)
        data = await client.json()
        tt = time() - t1

        # Content length
        content_length = get_content_length(client)
        if not content_length:
            content_length = sys.getsizeof(data)

        return (data, tt, content_length, client.status)
