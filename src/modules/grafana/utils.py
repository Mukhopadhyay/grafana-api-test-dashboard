import json
from typing import Any, Dict, Optional

from pydantic import ValidationError

from configs import database_config, grafana_config
from schemas.grafana_init import GrafanaInit


def get_base_url() -> str:
    base: str = f"http://{grafana_config.def_username}:{grafana_config.def_password}@{grafana_config.service_name}:{grafana_config.def_port}"
    return base


def get_data_source_url() -> str:
    endpoint = "/api/datasources"
    url: str = f"{get_base_url()}{endpoint}"
    return url


def get_create_users_url() -> str:
    endpoint = "/api/admin/users"
    url: str = f"{get_base_url()}{endpoint}"
    return url


def get_organization_url() -> str:
    endpoint = "/api/org"
    url: str = f"{get_base_url()}{endpoint}"
    return url


def get_dashboard_url() -> str:
    endpoint = "/api/dashboards"
    url: str = f"{get_base_url()}{endpoint}"
    return url


# TODO: Make one read json function
def get_grafana_init_json(path: Optional[str] = "configs/grafana.init.json") -> Dict[Any, Any]:
    with open(path, "r") as f:
        ginit = json.load(f)
    return ginit


def get_dashboard_json(path: str):
    with open(path, "r") as f:
        dash = json.load(f)
    return dash


def validate_init(data: Dict[str, Any]) -> GrafanaInit:
    return GrafanaInit(**data)
