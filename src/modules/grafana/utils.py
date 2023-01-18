import json
from pydantic import ValidationError
from typing import Optional, Any, Dict
from schemas.grafana_init import GrafanaInit
from configs import database_config, grafana_config


def get_base_url() -> str:
    base: str = f"http://{grafana_config.def_username}:{grafana_config.def_password}@{grafana_config.service_name}:{grafana_config.def_port}"
    return base


def get_data_source_url() -> str:
    endpoint = "/api/datasources"
    # url: str = f"{get_base_url()}{grafana_config.endpoints.datasource}"
    url: str = f"{get_base_url()}{endpoint}"
    return url


def get_create_users_url() -> str:
    endpoint = "/api/admin/users"
    # url: str = f"{get_base_url()}{grafana_config.endpoints.create_user}"
    url: str = f"{get_base_url()}{endpoint}"
    return url


def get_organization_url() -> str:
    endpoint = "/api/org"
    # url: str = f"{get_base_url()}{grafana_config.endpoints.organization}"
    url: str = f"{get_base_url()}{endpoint}"
    return url


def get_grafana_init_json(path: Optional[str] = "configs/grafana.init.json") -> Dict[Any, Any]:
    with open(path, "r") as f:
        ginit = json.load(f)
    return ginit


def validate_init(data: Dict[str, Any]) -> GrafanaInit:
    return GrafanaInit(**data)
    # try:
    #     _ = GrafanaInit(**data)
    # except ValidationError:
    #     return False
    # else:
    #     return True
