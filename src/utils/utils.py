# # import sys
# # from functools import wraps
# # from time import time
# # from typing import Any, Callable, Dict, Tuple
# # from database.db import database
# # from database.crud.base import CRUDBase
# # from models.models import Response, Api

# import aiohttp


# def get_content_length(response: aiohttp.ClientResponse):
#     header_keys = [x.casefold() for x in list(response.headers.keys())]
#     if "content-length" in header_keys:
#         idx = header_keys.index("content-length")
#         len_key = list(response.headers.keys())[idx]
#         return response.headers[len_key]
#     else:
#         return None
