"""
This is where your test goes
"""
import asyncio
from typing import Any, Dict, Optional
from uuid import UUID

from core.metadata import apis
from database.crud.base import CRUDBase
from database.db import database
from models.models import Api, Response
from utils import http

response_crud = CRUDBase(Response)
api_crud = CRUDBase(Api)


# Dictionary with {Name: Id} mapping
API_ID: Dict[str, UUID] = {}


def save_response(
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

############################################################
#  Individual API calls
############################################################


def osrm():
    name = "OSRM"
    try:
        m = apis[name]
        response, elapsed, length, status = asyncio.run(
            http.get_async(
                m.url,
            )
        )
    except Exception as err:
        # Handle exception here
        pass
    else:
        save_response(name, response, elapsed, length, status)
