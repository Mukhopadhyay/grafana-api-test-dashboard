from datetime import datetime
from typing import Any, Dict, Optional
from uuid import UUID

from pydantic import BaseModel

class BaseIdModel(BaseModel):
    Id: UUID


class Api(BaseModel):
    name: str
    url: str
    method: str
    version: Optional[str]
    category: Optional[str]
    description: Optional[str]
    status: bool = True

class Response(BaseModel):
    api_id: UUID
    elapsed: float
    status_code: int
    content_length: int

# class Endpoint(BaseModel):
#     # id: UUID
#     name: str
#     url: str
#     elapsed: float
#     version: Optional[str] = None
#     category: str
#     status_code: int
#     content_length: int
    # created_at: datetime
