from typing import Any, Dict, Literal, Optional

from pydantic import BaseModel


class SecureJsonData(BaseModel):
    password: str


class JsonData(BaseModel):
    sslmode: Optional[str] = "disable"
    postgresVersion: Optional[str] = None


class DataSourceRequest(BaseModel):
    name: str
    type: str
    access: Optional[str] = "proxy"
    url: str
    database: str
    user: str
    basicAuth: Optional[bool] = True
    basicAuthUser: Optional[str] = "admin"
    secureJsonData: SecureJsonData
    jsonData: Optional[JsonData] = JsonData()
    isDefault: Optional[bool] = True


class CreateUser(BaseModel):
    name: str
    email: str
    login: str
    password: str


class OrgAddress(BaseModel):
    address1: Optional[str] = ""
    address2: Optional[str] = ""
    city: Optional[str] = ""
    zipCode: Optional[str] = ""
    state: Optional[str] = ""
    country: Optional[str] = ""


class CreateOrg(BaseModel):
    name: str
    address: Optional[OrgAddress] = OrgAddress()


class ErrorResponse(BaseModel):
    response: Dict[Any, Any]
    status: int
    message: str


class UserRole(BaseModel):
    role: Optional[Literal["Admin", "Editor", "Viewer"]] = "Viewer"


class AddUserToOrg(BaseModel):
    user_login: str
    role: Optional[Literal["Admin", "Editor", "Viewer"]] = "Viewer"
