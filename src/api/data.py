# Database router
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.deps import get_db
from database.crud.api import ApiCRUD
from database.crud.response import ResponseCRUD
from models import models
from schemas import db as db_schemas

router = APIRouter()


@router.get("/apis")
async def get_all_apis(session: Session = Depends(get_db)):
    try:
        crud = ApiCRUD(models.Api)
        data = crud.get_multi(session)
    except Exception as err:
        return {"msg": str(err)}
    else:
        return data


@router.get("/response/{api_id}")
async def get_response_by_api_id(api_id: str, session: Session = Depends(get_db)):
    crud = ResponseCRUD(models.Response)
    try:
        api_id = UUID(api_id)
        data = crud.get_by_api_id(session, api_id)
    except Exception as err:
        return {"err": str(err)}
    else:
        return data


@router.get("/response/{api_name}")
async def get_response_by_api_name(api_name: str, session: Session = Depends(get_db)):
    crud = ResponseCRUD(models.Response)
    try:
        data = crud.get_by_api_name(session, api_name)
    except Exception as err:
        return {"err": str(err)}
    else:
        return data


@router.post("/response")
async def post_response_schema(body: db_schemas.Response, session: Session = Depends(get_db)):
    crud = ResponseCRUD(models.Response)
    try:
        data = crud.create(session, obj_in=models.Response(**body.dict()))
    except Exception as err:
        return {"err": str(err)}
    else:
        return data


# @router.get("/")
# async def index():
#     return {"msg": "data endpoint"}


# @router.post("/endpoint")
# async def insert_endpoint_result(endpoint: db_schemas.Response):
#     data = models.Response(**endpoint.dict())
#     return {}
#     # return utils.insert_into_endpoint(data)


# @router.delete("/endpoint")
# async def truncate_endpoint_results_table():
#     return {}
#     # return utils.truncate_endpoint_tbl()


# @router.get("/all")
# def temp():
#     base = CRUDBase(models.Response)
#     eps = base.get_multi(database.get_db())
#     return eps


# @router.delete("/{id}")
# def delete(id: str):
#     base = CRUDBase(models.Response)
#     obj = base.remove(database.get_db(), id=UUID(id))
#     return obj


# @router.put("/{id}")
# def update(id: str, model: db_schemas.Response):
#     base = CRUDBase(models.Response)
#     db_obj = base.get(database.get_db(), id=UUID(id))
#     if not db_obj:
#         raise HTTPException(status_code=404, detail="Endpoint not found")
#     obj = base.update(database.get_db(), db_obj=db_obj, obj_in=model)
#     return obj
