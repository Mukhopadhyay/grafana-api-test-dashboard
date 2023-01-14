"""
Project level ocnfigurations
"""
from pydantic import BaseSettings, Field, Optional


class DatabaseConfig(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_server: str
    postgres_port: int
    postgres_service: str


class Settings(BaseSettings):
    pass


class GrafanaDataSource(BaseSettings):
    endpoint: str = "/api/datasources"
    name: str
    type: Optional[str] = "postgres"
    db_host: str


class GrafanaConfig(BaseSettings):
    def_port: Optional[int] = 3000
    def_username: Optional[str] = 'admin'
    def_password: Optional[str] = 'admin'
    service_name: str = 'grafana-dashboard'
    datasource: GrafanaDataSource = GrafanaDataSource(_env_file=".env.grafana", _env_file_encoding="utf-8")
