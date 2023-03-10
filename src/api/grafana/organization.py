from fastapi import APIRouter, Response

from errors.exceptions import GrafanaHTTPError
from modules.grafana import organization
from schemas import grafana_http as grafana_schemas

router = APIRouter()


@router.get("/")
async def get_current_organization(response: Response):
    try:
        resp = await organization.get_current_organization()
    except GrafanaHTTPError as err:
        response.status_code = err.status_code
        return grafana_schemas.ErrorResponse(message=err.message, response=err.data, status=err.status_code)
    else:
        return resp


@router.post("/")
async def create_organization(model: grafana_schemas.CreateOrg, response: Response):
    try:
        resp = await organization.create_organization(
            model.name,
            model.address.address1,
            model.address.address2,
            model.address.city,
            model.address.zipCode,
            model.address.country,
        )
    except GrafanaHTTPError as err:
        response.status_code = err.status_code
        return grafana_schemas.ErrorResponse(message=err.message, response=err.data, status=err.status_code)
    else:
        return resp


@router.get("/all/")
async def get_all_organizations(response: Response):
    try:
        resp = await organization.get_all_organization()
    except GrafanaHTTPError as err:
        response.status_code = err.status_code
        return grafana_schemas.ErrorResponse(message=err.message, response=err.data, status=err.status_code)
    else:
        return resp


@router.get("/{org_id}/users")
async def get_users_in_organization(org_id: int, response: Response):
    try:
        resp = await organization.get_users_in_organization(org_id)
    except GrafanaHTTPError as err:
        response.status_code = err.status_code
        return grafana_schemas.ErrorResponse(message=err.message, response=err.data, status=err.status_code)
    else:
        return resp


@router.patch("/{org_id}/user/{user_id}")
async def update_user_role(org_id: int, user_id: int, model: grafana_schemas.UserRole, response: Response):
    try:
        resp = await organization.update_user_role(org_id, user_id, model.role)
    except GrafanaHTTPError as err:
        response.status_code = err.status_code
        return grafana_schemas.ErrorResponse(message=err.message, response=err.data, status=err.status_code)
    else:
        return resp


@router.post("/{org_id}/user")
async def add_user_to_organization(org_id: int, model: grafana_schemas.AddUserToOrg, response: Response):
    try:
        resp = await organization.add_user_to_org(org_id, model.user_login, model.role)
    except GrafanaHTTPError as err:
        response.status_code = err.status_code
        return grafana_schemas.ErrorResponse(message=err.message, response=err.data, status=err.status_code)
    else:
        return resp


@router.delete("/{org_id}/user/{user_id}")
async def delete_user_from_organization(org_id: int, user_id: int, response: Response):
    try:
        resp = await organization.delete_user_from_organization(org_id, user_id)
    except GrafanaHTTPError as err:
        response.status_code = err.status_code
        return grafana_schemas.ErrorResponse(message=err.message, response=err.data, status=err.status_code)
    else:
        return resp


@router.get("/{org_id}")
async def get_organization_by_id(org_id: int, response: Response):
    try:
        resp = await organization.get_organization_by_id(org_id)
    except GrafanaHTTPError as err:
        response.status_code = err.status_code
        return grafana_schemas.ErrorResponse(message=err.message, response=err.data, status=err.status_code)
    else:
        return resp


@router.get("/name/{org_name}")
async def get_organization_by_name(org_name: str, response: Response):
    try:
        resp = await organization.get_organization_by_name(org_name)
    except GrafanaHTTPError as err:
        response.status_code = err.status_code
        return grafana_schemas.ErrorResponse(message=err.message, response=err.data, status=err.status_code)
    else:
        return resp


@router.delete("/{org_id}")
async def delete_organization_by_id(org_id: int, response: Response):
    try:
        resp = await organization.delete_organization_by_id(org_id)
    except GrafanaHTTPError as err:
        response.status_code = err.status_code
        return grafana_schemas.ErrorResponse(message=err.message, response=err.data, status=err.status_code)
    else:
        return resp


@router.put("/{org_name}")
async def update_current_organization(org_name: str, response: Response):
    try:
        resp = await organization.update_current_organization(org_name)
    except GrafanaHTTPError as err:
        response.status_code = err.status_code
        return grafana_schemas.ErrorResponse(message=err.message, response=err.data, status=err.status_code)
    else:
        return resp


@router.patch("/{org_id}")
async def update_organization_details(org_id: int, response: Response):
    try:
        resp = await organization.update_organization_details(org_id)
    except GrafanaHTTPError as err:
        response.status_code = err.status_code
        return grafana_schemas.ErrorResponse(message=err.message, response=err.data, status=err.status_code)
    else:
        return resp
