from .configs import DatabaseConfig, GrafanaConfig

grafana_config = GrafanaConfig()
database_config = DatabaseConfig(_env_file=".env", _env_file_encoding="utf-8")
