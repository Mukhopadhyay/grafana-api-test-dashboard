from utils import http
from typing import Dict, Any
from errors.exceptions import GrafanaHTTPError
from modules.grafana import utils as grafana_utils
from configs import database_config, grafana_config
from schemas import grafana_http as grafana_http_schemas


async def set_postgres_source() -> Dict[str, Any]:
    grafana_ds = grafana_config.datasource
    model = grafana_http_schemas.DataSourceRequest(
        name=grafana_ds.name,
        type=grafana_ds.type,
        url=f"{database_config.postgres_service}:{database_config.postgres_port}",
        database=database_config.postgres_db,
        user=database_config.postgres_user,
        basicAuthUser=grafana_config.def_username,
        secureJsonData=grafana_http_schemas.SecureJsonData(password=grafana_config.def_password),
    )
    r, _, _, status = await http.post_async(grafana_utils.get_data_source_url(), data=model.dict())
    if status != 200:
        raise GrafanaHTTPError("Could not create a datasource", status_code=status, data=r)
    return r