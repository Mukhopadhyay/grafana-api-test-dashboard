# Database router
from fastapi import APIRouter
from models import apis
from database import utils
from schemas.db import apis as api_schemas

router = APIRouter()

@router.get("/")
async def index():
    return {"msg": "data endpoint"}

@router.post("/endpoint")
async def insert_endpoint_result(endpoint: api_schemas.Endpoint):
    data = apis.Endpoint( **endpoint.dict() )
    return utils.insert_into_endpoint(data)


@router.delete("/endpoint")
async def truncate_endpoint_results_table():
    return utils.truncate_endpoint_tbl()

