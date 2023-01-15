# Database router
from fastapi import APIRouter
from models import apis
from database import utils
from schemas.db import apis as api_schemas

router = APIRouter()

@router.get("/")
def index():
    return {"msg": "data endpoint"}

@router.post("/endpoint")
def insert_endpoint_result(endpoint: api_schemas.Endpoint):
    data = apis.Endpoint( **endpoint.dict() )
    return utils.insert_into_endpoint(data)
    # with database.get_session() as session:
    #     with session.begin():
    #         try:
    #             session.add(endpoint)
    #         except Exception as err:
    #             print(err)
    #             session.rollback()
    #             return {"msg": "Couldn't insert into database"}
    #         else:
    #             session.commit()
    #             return {"msg": "Data inserted"}

@router.delete("/endpoint")
def truncate_endpoint_results_table():
    return utils.truncate_endpoint_tbl()
    # with database.get_session() as session:
    #     with session.begin():
    #         try:
    #             session.execute('TRUNCATE TABLE endpoint;')
    #         except Exception as err:
    #             session.rollback()
    #             return {"msg": "Couldn't truncate table"}
    #         else:
    #             session.commit()
    #             return {"msg": "Table truncated"}
