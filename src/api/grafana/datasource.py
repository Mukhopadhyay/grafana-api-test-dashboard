from modules.grafana import datasource
from fastapi import APIRouter, Response
from errors.exceptions import GrafanaHTTPError
from schemas import grafana_http as grafana_schemas

router = APIRouter()

@router.get('/')
def get_datasources():
    return {'msg': 'Returns all data sources in this organization'}
