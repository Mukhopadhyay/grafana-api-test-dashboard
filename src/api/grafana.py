# Utility router
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def utils():
    return {"msg": "grafana"}

@router.get('/datasources')
def get_data_sources():
    return {}
