from fastapi import APIRouter
from api.healthcheck import router as healthcheck_router
from api.utils import router as utility_router

router = APIRouter()
router.include_router(healthcheck_router, prefix='/healthcheck', tags="healthchecks")
router.include_router(utility_router, prefix='/utils', tags="utility")

