from datetime import datetime
from typing import Any, Dict, Optional
from uuid import UUID

from pydantic import BaseModel


class Endpoint(BaseModel):
    # id: UUID
    name: str
    url: str
    elapsed: float
    version: Optional[str] = None
    category: str
    status_code: int
    content_length: int
    # created_at: datetime


# class RequestBody(BaseModel):
#     id: UUID
#     endpoint_id: UUID
#     body: Dict[str, Any]
#     created_at: datetime
#     updated_at: datetime


# class ResponseSchema(BaseModel):
#     id: UUID
#     endpoint_id: UUID
#     body: Dict[str, Any]
#     created_at: datetime
#     updated_at: datetime
