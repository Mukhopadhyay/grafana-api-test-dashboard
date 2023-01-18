# Utility router
from fastapi import APIRouter

from errors import exceptions
from schemas import grafana_http as grafana_schemas
from utils import grafana

router = APIRouter()


@router.get("/")
def grafana_index():
    return {"msg": "grafana"}


@router.post("/user")
async def create_new_user(model: grafana_schemas.CreateUser):
    pass
    # try:
    #     r = await grafana.create_user(model.name, model.email, model.login, model.password)
    # except exceptions.GrafanaHTTPError as graf_err:
    #     return {"msg": str(err.message), "status": err.status_code, "response": err.data}
    # except Exception as err:
    #     return {"msg": str(err)}
    # else:
    #     return r


@router.get("/datasources")
def get_data_sources():
    return {}
