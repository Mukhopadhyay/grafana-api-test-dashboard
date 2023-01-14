"""
Project level ocnfigurations
"""
from pydantic import BaseSettings, Field


class DatabaseConfig(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_server: str
    postgres_port: int


class Settings(BaseSettings):
    pass


class GrafanaDataSource(BaseSettings):
    endpoint: str = "/api/datasources"
    name: str
    type: str
    db_host: str
    # name: str = Field(..., env="NAME")
    # type: str = Field(..., env="TYPE")
    # db_host: str = Field(..., env="DB_HOST")


class GrafanaConfig(BaseSettings):
    api_base: str = "http://admin:admin@localhost:3000"
    datasource: GrafanaDataSource = GrafanaDataSource(_env_file=".env.grafana", _env_file_encoding="utf-8")
