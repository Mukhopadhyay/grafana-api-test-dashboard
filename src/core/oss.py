"""
This is where your test goes
"""
import asyncio
from uuid import UUID
from utils import http
from typing import Dict, Callable, Tuple, Any
from functools import wraps
from core.metadata import apis
from database.db import database
from database import utils as db_utils
from models.models import Response, Api
from database.crud.base import CRUDBase

response_crud = CRUDBase(Response)
api_crud = CRUDBase(Api)


# GET_URLS = (
#     "http://router.project-osrm.org/route/v1/driving/13.388860,52.517037;13.397634,52.529407;13.428555,52.523219?overview=false",
# )

# Dictionary with {Name: Id} mapping
API_ID: Dict[str, UUID] = {}

def save(name: str) -> Callable:
    def decorator(function):
        @wraps
        async def wrapper(*args, **kwargs) -> Tuple[Dict[Any, Any], float, int, int]:
            response, elapsed, length, status = await function(*args, **kwargs)
            db = database.get_db()

            # NOT DOING ANYTHING WITH THE RESPONSE
            api_id = API_ID.get(name)
            if api_id:
                response_crud.create(db, Response(
                    api_id=api_id,
                    elapsed=elapsed,
                    status_code=status,
                    content_length=length
                ))

            return response, elapsed, length, status
        return wrapper
    return decorator


# Insert the Apis into Apis table first
for api in apis:
    db = database.get_db()
    db_obj = api_crud.create(db, Api(**api.dict()))
    API_ID[db_obj.name] = db_obj.id

print("Apis inserted into Database!")

############################################################
#  Individual API calls
############################################################

@save(name='OSRM')
async def osrm():
    m = apis['OSRM']
    task = asyncio.create_task(http.get_async(m.url,))
    await task
    return task.result()


# def osrm_route():
#     print("OSRM ROUTE CALLED!")
#     name = "OSRM"
#     url = GET_URLS[0]
#     version = "v1"
#     category = "GEO"
#     (resp, elapsed, con_len, stat) = asyncio.run(http.get_async(url))
#     data = Response(
#         name=name, url=url, elapsed=elapsed, version=version, category="GEO", status_code=stat, content_length=con_len
#     )
#     r = db_utils.insert_into_endpoint(data)
#     print(r)
