from typing import Optional

from pydantic import BaseModel, SecretStr


class SecureJsonData(BaseModel):
    password: SecretStr


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
    password: SecretStr
