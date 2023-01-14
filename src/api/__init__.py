from fastapi import APIRouter

from api.healthcheck import router as healthcheck_router
from api.grafana import router as grafana_router

router = APIRouter()
router.include_router(healthcheck_router, prefix="/healthcheck", tags=["Healthcheck"])
router.include_router(grafana_router, prefix="/grafana", tags=["Grafana"])
