from utils import http
from typing import Dict, Any
from errors.exceptions import GrafanaHTTPError
from modules.grafana import utils as grafana_utils
from schemas import grafana_http as grafana_http_schemas


async def create_user(name: str, email: str, login: str, password: str) -> Dict[str, Any]:
    model = grafana_http_schemas.CreateUser(name=name, email=email, login=login, password=password)
    r, _, _, status = await http.post_async(grafana_utils.get_create_users_url(), data=model.dict())
    if status != 200:
        raise GrafanaHTTPError(f"Unable to create user : {name}", status_code=status, data=r)
    return r
