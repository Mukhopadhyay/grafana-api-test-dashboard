# Script for initializing grafana
from modules.grafana import GrafanaInit

"""
Ordering in which to do things:

* Creates the users
* Updates the default organization
* Connects to the datasource
* Creates the folder and adds dashboards to them

"""

if __name__ == "__main__":

    grafana = GrafanaInit()
    grafana.validate()
    grafana.initialize()
