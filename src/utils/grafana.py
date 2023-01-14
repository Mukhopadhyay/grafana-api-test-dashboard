import json
import requests
from typing import Dict, Any
from configs import grafana_config, database_config
from schemas import grafana_http as grafana_http_schemas

def get_base_url() -> str:
    base: str = f'http://{grafana_config.def_username}:{grafana_config.def_password}@{grafana_config.service_name}:{grafana_config.def_port}'
    return base

def get_data_source_url() -> str:
    url: str = f'{get_base_url()}{grafana_config.datasource.endpoint}'
    return url

def set_postgres_source() -> Dict[str, Any]:
    grafana_ds = grafana_config.datasource
    model = grafana_http_schemas.DataSourceRequest(
        name=grafana_ds.name,
        type=grafana_ds.type,
        url=f'{database_config.postgres_service}:{database_config.postgres_port}',
        database=database_config.postgres_db,
        user=database_config.postgres_user,
        basicAuthUser=grafana_config.def_username,
        secureJsonData=grafana_http_schemas.SecureJsonData(password=grafana_config.def_password),
    )
    r = requests.post(get_data_source_url(), json=model.dict())
    return json.loads(r.text)
