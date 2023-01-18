# Script for initializing grafana
from modules.grafana import GrafanaInit

"""
Ordering in which to do things:

* Create an organization
* Select the organization as default
* Create the users
* Add users to the organization
* Delete users from Main Org. if any
* Create the datasources

"""

if __name__ == "__main__":

    grafana = GrafanaInit()
    grafana.validate()
    grafana.initialize()

