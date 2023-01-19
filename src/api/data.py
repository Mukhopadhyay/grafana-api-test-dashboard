# Database router
from uuid import UUID

from fastapi import APIRouter, HTTPException

from database import utils
from database.crud.base import CRUDBase
from database.db import database
from models import apis
from schemas.db import apis as api_schemas

router = APIRouter()


@router.get("/")
async def index():
    return {"msg": "data endpoint"}


@router.post("/endpoint")
async def insert_endpoint_result(endpoint: api_schemas.Endpoint):
    data = apis.Endpoint(**endpoint.dict())
    return utils.insert_into_endpoint(data)


@router.delete("/endpoint")
async def truncate_endpoint_results_table():
    return utils.truncate_endpoint_tbl()


@router.get("/all")
def temp():
    base = CRUDBase(apis.Endpoint)
    eps = base.get_multi(database.get_db())
    return eps


@router.delete("/{id}")
def delete(id: str):
    base = CRUDBase(apis.Endpoint)
    obj = base.remove(database.get_db(), id=UUID(id))
    return obj


@router.put("/{id}")
def update(id: str, model: api_schemas.Endpoint):
    base = CRUDBase(apis.Endpoint)
    db_obj = base.get(database.get_db(), id=UUID(id))
    if not db_obj:
        raise HTTPException(status_code=404, detail="Endpoint not found")
    obj = base.update(database.get_db(), db_obj=db_obj, obj_in=model)
    return obj
