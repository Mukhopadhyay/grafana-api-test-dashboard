from modules.grafana import dashboard
from fastapi import APIRouter, Response
from errors.exceptions import GrafanaHTTPError
from schemas import grafana_http as grafana_schemas

router = APIRouter()

@router.get('/')
def get_all_dashboards():
    return {'msg': "Returns all dashboards"}
