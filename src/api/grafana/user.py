from fastapi import APIRouter, Response

from errors.exceptions import GrafanaHTTPError
from modules.grafana import users
from schemas import grafana_http as grafana_schemas

router = APIRouter()


@router.post("/")
async def create_new_user(model: grafana_schemas.CreateUser, response: Response):
    try:
        resp = await users.create_user(model.name, model.email, model.login, model.password)
    except GrafanaHTTPError as err:
        response.status_code = err.status_code
        return grafana_schemas.ErrorResponse(message=err.message, response=err.data, status=err.status_code)
    else:
        return resp
