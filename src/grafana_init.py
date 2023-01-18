# Script for initializing grafana
# import json
# import asyncio

# from utils import grafana
# from typing import Optional
# from errors.exceptions import GrafanaHTTPError

# from modules.grafana import utils, organization, users

from modules.grafana import GrafanaInit

"""
Ordering in which to do things:

* Create an organization
* Select the organization as default
* Create the users
* Add users to the organization
* Create the datasources

"""

# def main():
    data = utils.get_grafana_init_json()

    model = utils.validate_init(data)

    # Create users
    for user in model.users:
        try:
            users.create_user(
                user.name, user.email, user.login, user.password
            )
        except GrafanaHTTPError as graf_err:
            print(f'{str(graf_err.message)}\nstatus: {graf_err.status_code}\n{graf_err.data}')
        else:
            print(f"User created: {user.name} <{user.email}>")

    # Create organizations
    org = model.organization

    org_id: int = None

    if not org:
        try:
            org_resp = organization.create_organization(
                org.name,
                org.address.address1,
                org.address.address1,
                org.address.city,
                org.address.zipCode,
                org.address.state,
                org.address.country
            )
        except GrafanaHTTPError as graf_err:
            print(f'{str(graf_err.message)}\nstatus: {graf_err.status_code}\n{graf_err.data}')
        else:
            org_id = org_resp['orgId']
            print("Created organization: {org.name}")

        # Select the default organization
        try:
            organization.update_current_organization(org.name)
        except GrafanaHTTPError as graf_err:
            print(f'{str(graf_err.message)}\nstatus: {graf_err.status_code}\n{graf_err.data}')
        else:
            print("Set organization: {org.name} as default")

        # Add the users to the organization
        if org_id:
            if org.users
            try:
                organization.add_user_to_org(org_id, )
        else:
            print("No OrganizationID found, unable to add users")


    else:
        print("Using Main Org.")


if __name__ == "__main__":

    grafana = GrafanaInit()
    grafana.validate()
    grafana.initialize()

    # try:
    #     r = asyncio.run(grafana.set_postgres_source())
    # except GrafanaHTTPError as graf_err:
    #     print(graf_err)
    # else:
    #     print("Datasource has been setup!")
