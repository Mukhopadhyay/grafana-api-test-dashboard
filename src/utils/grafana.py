from utils import http
from typing import Dict, Any
from configs import grafana_config, database_config
from schemas import grafana_http as grafana_http_schemas

def get_base_url() -> str:
    base: str = f'http://{grafana_config.def_username}:{grafana_config.def_password}@{grafana_config.service_name}:{grafana_config.def_port}'
    return base

def get_data_source_url() -> str:
    url: str = f'{get_base_url()}{grafana_config.endpoints.datasource}'
    return url

def get_users_url() -> str:
    url: str = f'{get_base_url()}{grafana_config.endpoints.users}'
    return url

async def crete_user(name: str, email: str, login: str, password: str) -> Dict[str, Any]:
    model = grafana_http_schemas.CreateUser(
        name=name,
        email=email,
        login=login,
        password=password
    )
    r, _, _, status = await http.post_async(get_users_url(), data=model.dict())
    if status != 200:
        raise RuntimeError("Unable to create user!")
    return r

async def set_postgres_source() -> Dict[str, Any]:
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
    r, _, _, status = await http.post_async(get_data_source_url(), data=model.dict())
    if status != 200:
        raise RuntimeError('Datasource could not be setup!')
    return r
