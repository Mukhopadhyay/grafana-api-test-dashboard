import asyncio
from errors.exceptions import GrafanaHTTPError
from schemas.grafana_init import GrafanaInit as GrafanaInitSchema
from modules.grafana import utils, users, organization, datasource

GRAFANA_INIT_JSON = "configs/grafana.init.json"


class GrafanaInit:
    def __init__(self) -> None:
        self.path = GRAFANA_INIT_JSON
        self.init_data = utils.get_grafana_init_json(self.path)

        self.org_id: int = None

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

    def create_organization(self) -> None:
        org = self.model.organization
        print("Organization:", org)

        if org:
            try:
                org_resp = asyncio.run(
                    organization.create_organization(
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
                self.org_id = 1  # This is the Main Org.
            else:
                self.org_id = org_resp["orgId"]
                self.create_org_response = org_resp
                print(f"Created organization: {org.name}")

            # Select the default organization
            try:
                # Fetch the current organization first
                current_org = asyncio.run(organization.get_current_organization())
                current_org_name = current_org.get('name')

                if current_org_name == org.name:
                    print(f"Current organization is already set to {org.name}")
                else:
                    _ = asyncio.run(organization.update_current_organization(org.name))

            except GrafanaHTTPError as graf_err:
                print(f"{str(graf_err.message)}\nstatus: {graf_err.status_code}\n{graf_err.data}")

            else:
                print("Set organization: {org.name} as default")

            # The users will default to the current organization
            if self.org_id:
                if self.org_id == 1:
                    print("No organization created, adding users in 'Main Org.'")
                if org.users:
                    for user in org.users:
                        try:
                            _ = asyncio.run(organization.add_user_to_org(self.org_id, user.login, user.role))
                        except GrafanaHTTPError as graf_err:
                            print(f"{str(graf_err.message)}\nstatus: {graf_err.status_code}\n{graf_err.data}")
                        else:
                            print(f"User {user.login} is now a part of {self.org_id}")
            else:
                print("No OrganizationID found, unable to add users")
        else:
            print("Please provide an organization detail")
            # TODO: Raise appropriate exception here

    def set_datasource(self) -> None:
        try:
            asyncio.run(datasource.set_postgres_source())
        except GrafanaHTTPError as graf_err:
            print(f"{str(graf_err.message)}\nstatus: {graf_err.status_code}\n{graf_err.data}")
        else:
            print(f"Datasource installed!")

    def initialize(self) -> None:
        self.create_users()
        self.create_organization()
        self.set_datasource()
