# Script for initializing grafana
import json
import requests
from typing import Dict, Any, Optional
from schemas import grafana_http

base = 'http://admin:admin@localhost:3000'


def get_data_sources() -> Dict[str, Any]:
    r = requests.get(f'{base}/api/datasources')
    return json.loads(r.text)


def set_postgres_sources() -> Dict[str, Any]:
    model = grafana_http.DataSourceRequest(
        name="PostgreSQL", type="postgres",
        url="postgres:5432", database="grafana", user="grafana",
        basicAuthUser="admin",
        secureJsonData=grafana_http.SecureJsonData(
            password="grafana"
        )
    )
    r = requests.post(f'{base}/api/datasources', json=model.dict())
    return json.loads(r.text)


if __name__ == '__main__':
    set_postgres_sources()
    print("Datasource installed!")
