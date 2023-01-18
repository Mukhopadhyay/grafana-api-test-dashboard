from typing import Any, Dict

from configs import database_config, grafana_config
from errors.exceptions import GrafanaHTTPError
from schemas import grafana_http as grafana_http_schemas
from utils import http


# def get_base_url() -> str:
#     base: str = f"http://{grafana_config.def_username}:{grafana_config.def_password}@{grafana_config.service_name}:{grafana_config.def_port}"
#     return base


# def get_data_source_url() -> str:
#     url: str = f"{get_base_url()}{grafana_config.endpoints.datasource}"
#     return url


# def get_create_users_url() -> str:
#     url: str = f"{get_base_url()}{grafana_config.endpoints.create_user}"
#     return url


# def get_organization_url() -> str:
#     url: str = f"{get_base_url()}{grafana_config.endpoints.organization}"
#     return url


# async def create_organization(name, addr1, addr2, city, zip, state, country) -> Dict[str, Any]:
#     model = grafana_http_schemas.CreateOrg(
#         name,
#         address=grafana_http_schemas.OrgAddress(
#             address1=addr1, address2=addr2, city=city, zipCode=zip, state=state, country=country
#         ),
#     )
#     r, _, _, status = await http.post_async(get_organization_url(), data=model.dict())
#     if status != 200:
#         raise GrafanaHTTPError(f"Unable to create organization : {name}", status_code=status, data=r)
#     return r


# async def create_user(name: str, email: str, login: str, password: str) -> Dict[str, Any]:
#     model = grafana_http_schemas.CreateUser(name=name, email=email, login=login, password=password)
#     r, _, _, status = await http.post_async(get_create_users_url(), data=model.dict())
#     if status != 200:
#         raise GrafanaHTTPError(f"Unable to create user : {name}", status_code=status, data=r)
#     return r


# async def set_postgres_source() -> Dict[str, Any]:
#     grafana_ds = grafana_config.datasource
#     model = grafana_http_schemas.DataSourceRequest(
#         name=grafana_ds.name,
#         type=grafana_ds.type,
#         url=f"{database_config.postgres_service}:{database_config.postgres_port}",
#         database=database_config.postgres_db,
#         user=database_config.postgres_user,
#         basicAuthUser=grafana_config.def_username,
#         secureJsonData=grafana_http_schemas.SecureJsonData(password=grafana_config.def_password),
#     )
#     r, _, _, status = await http.post_async(get_data_source_url(), data=model.dict())
#     if status != 200:
#         raise GrafanaHTTPError("Could not create a datasource", status_code=status, data=r)
#     return r
