from fastapi import APIRouter

from api.data import router as db_router
from api.grafana import router as grafana_router
from api.healthcheck import router as health_router

router = APIRouter()

router.include_router(db_router, prefix="/data", tags=["Data"])
router.include_router(grafana_router, prefix="/grafana")
router.include_router(health_router, prefix="/health")
