# Script for initializing grafana
import asyncio
from utils import grafana


if __name__ == "__main__":
    try:
        r = asyncio.run(grafana.set_postgres_source())
    except RuntimeError as run_err:
        print(run_err)
    else:
        print("Datasource has been setup!")
