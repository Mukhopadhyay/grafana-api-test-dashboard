from fastapi import APIRouter

from api.grafana.dashboard import router as dashboard_router
from api.grafana.datasource import router as datasource_router
from api.grafana.organization import router as org_router
from api.grafana.user import router as user_router

router = APIRouter()

router.include_router(dashboard_router, prefix="/dashboard", tags=["Grafana-Dashboard"])
router.include_router(user_router, prefix="/user", tags=["Grafana-User"])
router.include_router(org_router, prefix="/organization", tags=["Grafana-Organization"])
router.include_router(datasource_router, prefix="/datasource", tags=["Grafana-Datasource"])
