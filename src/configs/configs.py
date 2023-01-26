"""
Project level configurations
"""
from typing import Optional

from pydantic import BaseSettings


class DatabaseConfig(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_server: str
    postgres_port: int
    postgres_service: str


class Settings(BaseSettings):
    pass


# class GrafanaHTTPEndpoints(BaseSettings):
#     datasource: str = "/api/datasources"
#     create_user: str = "/api/admin/users"
#     organization: str = "/api/org"
#     dashboard: str = "/api/dashboards"
#     folder: str = "/api/folders"


class GrafanaDataSource(BaseSettings):
    name: str
    type: Optional[str] = "postgres"
    db_host: str


class GrafanaConfig(BaseSettings):
    def_port: Optional[int] = 3000
    def_username: Optional[str] = "admin"
    def_password: Optional[str] = "admin"
    service_name: str = "grafana-dashboard"
    datasource: GrafanaDataSource = GrafanaDataSource(_env_file=".env.grafana", _env_file_encoding="utf-8")
    # endpoints: GrafanaHTTPEndpoints = GrafanaHTTPEndpoints()
