from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Dict, Any

class Endpoint(BaseModel):
    id: UUID
    name: str
    url: str
    version: Optional[str] = None
    created_at: datetime
    updated_at: datetime

class RequestBody(BaseModel):
    id: UUID
    endpoint_id: UUID
    body: Dict[str, Any]
    created_at: datetime
    updated_at: datetime

class ResponseSchema(BaseModel):
    id: UUID
    endpoint_id: UUID
    body: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
