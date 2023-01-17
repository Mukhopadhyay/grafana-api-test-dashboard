# Healthcheck router
import aiohttp
from fastapi import APIRouter

from database.utils import healthcheck_postgres

router = APIRouter()


@router.get("/db")
async def db_healthcheck():
    status = healthcheck_postgres()
    return {"Status": status}


@router.get("/grafana")
async def grafana_healthcheck():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://grafana-dashboard:3000") as resp:
            status = resp.status
    return {"Status": status == 200}
