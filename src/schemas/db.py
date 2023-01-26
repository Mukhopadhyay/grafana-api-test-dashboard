from typing import Literal, Optional
from uuid import UUID

from pydantic import BaseModel


class Api(BaseModel):
    name: str
    url: str
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH"]
    version: Optional[str]
    category: Optional[str]
    description: Optional[str]
    status: bool = True


class Response(BaseModel):
    api_id: UUID
    elapsed: float
    status_code: int
    content_length: int
    headers: Optional[str] = None
    request: Optional[str] = None
    response: Optional[str] = None
    cookies: Optional[str] = None


class Errors(BaseModel):
    message: str
    api_id: UUID
