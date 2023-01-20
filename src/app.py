from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from api import router

app = FastAPI()
app.include_router(router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Grafana API Test Dashboard",
        version="0.0.1",
        description="Grafana dashboard for testing, checking availability of API endpoints",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://images.ctfassets.net/o7xu9whrs0u9/7Erq6IEoCaJkBtHMhblLzS/9310518537dffc123d3d9059edace8ed/Grafana-logo-2.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
