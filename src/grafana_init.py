# Script for initializing grafana
# import json
# from typing import Any, Dict

# import requests

from utils import grafana
# from schemas import grafana_http

# def get_data_sources() -> Dict[str, Any]:
#     r = requests.get(grafana.get_data_source_url())
#     return json.loads(r.text)

# def set_postgres_sources() -> Dict[str, Any]:
#     model = grafana_http.DataSourceRequest(
#         name="PostgreSQL",
#         type="postgres",
#         url="postgres:5432",
#         database="grafana",
#         user="grafana",
#         basicAuthUser="admin",
#         secureJsonData=grafana_http.SecureJsonData(password="grafana"),
#     )
#     r = requests.post(f"{base}/api/datasources", json=model.dict())
#     return json.loads(r.text)


if __name__ == "__main__":
    # set_postgres_sources()
    _ = grafana.set_postgres_source()
    print("Datasource installed!")
