# Database router
from uuid import UUID

from fastapi import APIRouter, Depends
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
        crud = ApiCRUD()
        data = crud.get_multi(session)
    except Exception as err:
        return {"msg": str(err)}
    else:
        return data


@router.get("/response/{api_id}")
async def get_response_by_api_id(api_id: str, session: Session = Depends(get_db)):
    crud = ResponseCRUD()
    try:
        api_id = UUID(api_id)
        data = crud.get_by_api_id(session, api_id)
    except Exception as err:
        return {"err": str(err)}
    else:
        return data


@router.get("/response/{api_name}")
async def get_response_by_api_name(api_name: str, session: Session = Depends(get_db)):
    crud = ResponseCRUD()
    try:
        data = crud.get_by_api_name(session, api_name)
    except Exception as err:
        return {"err": str(err)}
    else:
        return data


@router.post("/response")
async def post_response_schema(body: db_schemas.Response, session: Session = Depends(get_db)):
    crud = ResponseCRUD()
    try:
        data = crud.create(session, obj_in=models.Response(**body.dict()))
    except Exception as err:
        return {"err": str(err)}
    else:
        return data
