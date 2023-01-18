from typing import Any, Dict, Optional

from errors.exceptions import GrafanaHTTPError
from modules.grafana import utils as grafana_utils
from schemas import grafana_http as grafana_http_schemas
from utils import http


async def create_dashboard(data: Dict[str, Any]) -> Dict[str, Any]:
    url = f"{grafana_utils.get_dashboard_url()}/db"
    r, _, _, status = await http.post_async(url, data=data)
    if status != 200:
        raise GrafanaHTTPError(f"Unable to create the dashboard", status_code=status, data=r)
    return r
