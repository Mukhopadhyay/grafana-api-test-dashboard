from typing import Any, Dict, Optional

from errors.exceptions import GrafanaHTTPError
from modules.grafana import utils as grafana_utils
from schemas import grafana_http as grafana_http_schemas
from utils import http


async def update_user_role(org_id: int, user_id: int, role: Optional[str] = "Viewer") -> Dict[str, Any]:
    url = f"{grafana_utils.get_organization_url()}s/{org_id}/users/{user_id}"
    data = {"role": role}
    r, _, _, status = await http.patch_async(url, data=data)
    if status != 200:
        raise GrafanaHTTPError(f"Unable to update role for user: {user_id}", status_code=status, data=r)
    return r


async def update_organization_details(
    org_id: int, name: str, addr1: str, addr2: str, city: str, zip: str, state: str, country: str
) -> Dict[str, Any]:
    url = f"{grafana_utils.get_organization_url()}s/{org_id}"
    model = grafana_http_schemas.CreateOrg(
        name=name,
        address=grafana_http_schemas.OrgAddress(
            address1=addr1, address2=addr2, city=city, zipCode=zip, state=state, country=country
        ),
    )
    r, _, _, status = await http.put_async(url, data=model.dict())  # /api/orgs/:org_id/users
    if status != 200:
        raise GrafanaHTTPError(f"Unable to update organization: {org_id}", status_code=status, data=r)
    return r


async def get_users_in_organization(org_id: int) -> Dict[str, Any]:
    url = f"{grafana_utils.get_organization_url()}s/{org_id}/users"
    r, _, _, status = await http.get_async(url)  # /api/orgs/:org_id/users
    if status != 200:
        raise GrafanaHTTPError(f"Unable to get users in organization: {org_id}", status_code=status, data=r)
    return r


async def delete_user_from_organization(org_id: int, user_id: int) -> Dict[str, Any]:
    url = f"{grafana_utils.get_organization_url()}s/{org_id}/users/{user_id}"  # /api/orgs/:orgId/users/:userId
    r, _, _, status = await http.delete_async(url)
    if status != 200:
        raise GrafanaHTTPError(
            f"Unable to delete user: {user_id} from organization: {org_id}", status_code=status, data=r
        )
    return r


async def get_current_organization() -> Dict[str, Any]:
    url = grafana_utils.get_organization_url()  # /api/org
    r, _, _, status = await http.get_async(url)
    if status != 200:
        raise GrafanaHTTPError("Unable to fetch current organization", status_code=status, data=r)
    return r


async def update_current_organization(org_name: str) -> Dict[str, Any]:
    url = grafana_utils.get_organization_url()  # /api/org
    data = {"name": org_name}
    r, _, _, status = await http.put_async(url, data=data)
    if status != 200:
        raise GrafanaHTTPError(f"Unable to set default org: {org_name}", status_code=status, data=r)
    return r


async def delete_organization_by_id(org_id: int) -> Dict[str, Any]:
    url = f"{grafana_utils.get_organization_url()}s/{int(org_id)}"  # /api/orgs/:org_id
    r, _, _, status = await http.delete_async(url)
    if status != 200:
        raise GrafanaHTTPError(f"Unable to delete organization with id: {org_id}", status_code=status, data=r)
    return r


async def get_all_organization() -> Dict[str, Any]:
    url = f"{grafana_utils.get_organization_url()}s"  # /api/orgs
    r, _, _, status = await http.get_async(url)
    if status != 200:
        raise GrafanaHTTPError(f"Unable to fetch all organizations", status_code=status, data=r)
    return r

async def get_organization_by_id(org_id: int) -> Dict[str, Any]:
    url = f"{grafana_utils.get_organization_url()}s/{org_name}"
    r, _, _, status = await http.get_async(url)
    if status != 200:
        raise GrafanaHTTPError(f"Unable to fetch organization with id: {org_id}", status_code=status, data=r)
    return r

async def get_organization_by_name(org_name: str) -> Dict[str, Any]:
    url = f"{grafana_utils.get_organization_url()}s/name/{org_name}"
    r, _, _, status = await http.get_async(url)
    if status != 200:
        raise GrafanaHTTPError(f"Unable to fetch organization with name: {org_name}", status_code=status, data=r)
    return r


async def create_organization(
    name: str, addr1: str, addr2: str, city: str, zip: str, state: str, country: str
) -> Dict[str, Any]:
    url = f"{grafana_utils.get_organization_url()}s"  # /api/orgs
    model = grafana_http_schemas.CreateOrg(
        name=name,
        address=grafana_http_schemas.OrgAddress(
            address1=addr1, address2=addr2, city=city, zipCode=zip, state=state, country=country
        ),
    )
    r, _, _, status = await http.post_async(url, data=model.dict())
    if status != 200:
        raise GrafanaHTTPError(f"Unable to create organization : {name}", status_code=status, data=r)
    return r


async def add_user_to_org(org_id: int, user_login: str, user_role: Optional[str] = "Viewer"):
    url = f"{grafana_utils.get_organization_url()}s/{org_id}/users"
    data = {"loginOrEmail": user_login, "role": user_role}
    r, _, _, status = await http.post_async(url, data=data)
    if status != 200:
        raise GrafanaHTTPError(f"Unable to add user {user_role} to organization: {org_id}", status_code=status, data=r)
    return r
