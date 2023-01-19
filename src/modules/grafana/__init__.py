import asyncio
from typing import List

from errors.exceptions import GrafanaHTTPError
from modules.grafana import dashboard, datasource, organization, users, utils
from schemas.grafana_init import GrafanaInit as GrafanaInitSchema

GRAFANA_INIT_JSON = "configs/grafana.init.json"
DASHBOARD_JSON = "configs/dashboard.json"


class GrafanaInit:
    def __init__(self) -> None:
        self.init_path = GRAFANA_INIT_JSON
        self.dash_path = DASHBOARD_JSON

        self.init_data = utils.get_grafana_init_json(self.init_path)
        self.dashboard_data = utils.get_dashboard_json(self.dash_path)

        self.org_id: int = 1

        self.model: GrafanaInitSchema = None

        self.create_user_responses = []
        self.create_org_response = None

    def validate(self) -> None:
        self.model = utils.validate_init(self.init_data)

    def create_users(self) -> None:
        for user in self.model.users:
            try:
                response = asyncio.run(users.create_user(user.name, user.email, user.login, user.password))
            except GrafanaHTTPError as graf_err:
                print(f"{str(graf_err.message)}\nstatus: {graf_err.status_code}\n{graf_err.data}")
            else:
                print(f"User created: {user.name} <{user.email}>")
                self.create_user_responses.append(response)

    def update_organization(self) -> None:
        org = self.model.organization

        if org:
            try:
                # org_resp = asyncio.run(
                #     organization.create_organization(
                #         org.name,
                #         org.address.address1,
                #         org.address.address1,
                #         org.address.city,
                #         org.address.zipCode,
                #         org.address.state,
                #         org.address.country,
                #     )
                # )
                org_resp = asyncio.run(
                    organization.update_organization_details(
                        self.org_id,
                        org.name,
                        org.address.address1,
                        org.address.address1,
                        org.address.city,
                        org.address.zipCode,
                        org.address.state,
                        org.address.country,
                    )
                )
            except GrafanaHTTPError as graf_err:
                print(f"{str(graf_err.message)}\nstatus: {graf_err.status_code}\n{graf_err.data}")
                # self.org_id = 1  # This is the Main Org.
            else:
                # self.org_id = org_resp["orgId"]
                self.create_org_response = org_resp
                print(f"Updated organization: {org.name}")

            # Select the default organization
            # try:
            #     # Fetch the current organization first
            #     current_org = asyncio.run(organization.get_current_organization())
            #     current_org_name = current_org.get('name')

            #     if current_org_name == org.name:
            #         print(f"Current organization is already set to {org.name}")
            #     else:
            #         _ = asyncio.run(organization.update_current_organization(org.name))

            # except GrafanaHTTPError as graf_err:
            #     print(f"{str(graf_err.message)}\nstatus: {graf_err.status_code}\n{graf_err.data}")

            # else:
            #     print("Set organization: {org.name} as default")

            # The users will default to the current organization
            # if self.org_id:
            # if self.org_id == 1:
            #     print("No organization created, adding users in 'Main Org.'")

            # organization.get_users_in_organization(self.org_id)
            # if org.users:
            #     for user in org.users:
            #         try:
            #             _ = asyncio.run(organization.add_user_to_org(self.org_id, user.login, user.role))
            #         except GrafanaHTTPError as graf_err:
            #             print(f"{str(graf_err.message)}\nstatus: {graf_err.status_code}\n{graf_err.data}")
            #         else:
            #             print(f"User {user.login} is now a part of {self.org_id}")
            # else:
            #     print("No OrganizationID found, unable to add users")
        else:
            print("No organization detail found in grafana.init.json, Using 'Main Org.'")

        # Setting proper user roles
        org_users = asyncio.run(organization.get_users_in_organization(self.org_id))
        for u in org_users:
            if u["userId"] == 1:
                continue
            u_role = org.users.get(u["login"])
            if not u_role:
                u_role = "Viewer"
            if u["role"] != u_role:
                try:
                    asyncio.run(organization.update_user_role(self.org_id, u["userId"], u_role))
                except GrafanaHTTPError as graf_err:
                    print(f"{str(graf_err.message)}\nstatus: {graf_err.status_code}\n{graf_err.data}")
                else:
                    print(f"Role altered to {u_role} for user: {u['userId']}")
            else:
                print(f"User: {u['login']} already has {u_role} in organization: {u['orgId']}")

        # Checking if `organization.users `contains something that `users` doesnt
        org_user_logins: List[str] = [u["login"] for u in org_users]
        for org_uname in list(org.users.keys()):
            try:
                assert org_uname in org_user_logins
            except AssertionError:
                print(
                    f"User {org_uname} does not exist in this organization. Make sure the user detail is in 'users' object in grafana.init.json"
                )

    def set_datasource(self) -> None:
        try:
            asyncio.run(datasource.set_postgres_source())
        except GrafanaHTTPError as graf_err:
            print(f"{str(graf_err.message)}\nstatus: {graf_err.status_code}\n{graf_err.data}")
        else:
            print(f"Datasource installed!")

    def create_dashboard(self) -> None:
        # Setting uid and version to empty string
        self.dashboard_data["dashboard"]["id"] = None
        self.dashboard_data["dashboard"]["uid"] = None
        self.dashboard_data["dashboard"]["version"] = 1
        try:
            asyncio.run(dashboard.create_dashboard(self.dashboard_data))
        except GrafanaHTTPError as graf_err:
            print(f"{str(graf_err.message)}\nstatus: {graf_err.status_code}\n{graf_err.data}")
        else:
            print(f"Dashboard installed!")

    def initialize(self) -> None:
        self.create_users()
        self.update_organization()
        self.set_datasource()
        self.create_dashboard()
