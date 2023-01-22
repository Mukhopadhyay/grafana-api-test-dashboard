"""
This is where your test goes
"""
import asyncio
from functools import wraps
from typing import Any, Callable, Dict, Optional, Tuple
from uuid import UUID

from core.metadata import apis
from database.crud.base import CRUDBase
from database.db import database

# from database import utils as db_utils
from models.models import Api, Response
from utils import http

response_crud = CRUDBase(Response)
api_crud = CRUDBase(Api)


# GET_URLS = (
#     "http://router.project-osrm.org/route/v1/driving/13.388860,52.517037;13.397634,52.529407;13.428555,52.523219?overview=false",
# )

# Dictionary with {Name: Id} mapping
API_ID: Dict[str, UUID] = {}

# def save(name: str) -> Callable:
#     def decorator(function):
#         @wraps
#         async def wrapper(*args, **kwargs) -> Tuple[Dict[Any, Any], float, int, int]:
#             response, elapsed, length, status = await function(*args, **kwargs)
#             db = database.get_db()

#             # NOT DOING ANYTHING WITH THE RESPONSE
#             api_id = API_ID.get(name)
#             if api_id:
#                 response_crud.create(db, Response(
#                     api_id=api_id,
#                     elapsed=elapsed,
#                     status_code=status,
#                     content_length=length
#                 ))

#             return response, elapsed, length, status
#         return wrapper
#     return decorator


def save(
    api_name,
    response: Dict[Any, Any],
    elapsed: float,
    length: int,
    status: int,
    headers: Optional[str] = None,
    request: Optional[str] = None,
    cookies: Optional[str] = None,
) -> None:
    db = database.get_db()

    api_id = API_ID.get(api_name)
    if api_id:
        response_crud.create(
            db,
            obj_in=Response(
                api_id=api_id,
                elapsed=elapsed,
                status_code=status,
                content_length=length,
            ),
        )
    else:
        print("ApiID not found!")


# Insert the Apis into Apis table first
for api in apis.values():
    db = database.get_db()
    db_obj = api_crud.create(db, obj_in=Api(**api.dict()))
    API_ID[db_obj.name] = db_obj.id

print("Apis inserted into Database!")

############################################################
#  Individual API calls
############################################################


def osrm():
    print("OSRM")
    m = apis["OSRM"]
    response, elapsed, length, status = asyncio.run(
        http.get_async(
            m.url,
        )
    )
    print(response)
    # response, elapsed, length, status = task.result()
    save("OSRM", response, elapsed, length, status)
