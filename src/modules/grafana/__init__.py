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
        # self.dashboard_data = utils.get_dashboard_json(self.dash_path)

        self.org_id: int = 1
        self.datasource_uid: str = None  # This will be populated after setting the datasource

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
            r = asyncio.run(datasource.set_postgres_source())
        except GrafanaHTTPError as graf_err:
            print(f"{str(graf_err.message)}\nstatus: {graf_err.status_code}\n{graf_err.data}")
        else:
            self.datasource_uid = r["datasource"]["uid"]
            print(f"Datasource installed!")

    def create_folders(self) -> None:
        # Folder creation code goes here
        pass

    def create_dashboard(self) -> None:
        # Fetch the dashboard json dynamically
        utils.get_dashboard_json(self.dash_path)

        # Setting uid and version to empty string
        self.dashboard_data["dashboard"]["id"] = None
        self.dashboard_data["dashboard"]["uid"] = None
        self.dashboard_data["dashboard"]["version"] = 1

        # Setting the new datasource's uid
        for panel in self.dashboard_data["dashboard"].get("panels", []):
            if panel.get("datasource", {}).get("type") == "postgres":
                panel["datasource"]["uid"] = self.datasource_uid

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
