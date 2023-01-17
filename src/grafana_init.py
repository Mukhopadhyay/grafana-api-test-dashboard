# Script for initializing grafana
import asyncio
import json

from errors import exceptions
from utils import grafana

"""
Ordering in which to do things:

* Create an organization
* Select the organization as default
* Create the users
* Add users to the organization
* Create the datasources

"""


if __name__ == "__main__":
    try:
        r = asyncio.run(grafana.set_postgres_source())
    except exceptions.GrafanaHTTPError as graf_err:
        print(graf_err)
    else:
        print("Datasource has been setup!")
