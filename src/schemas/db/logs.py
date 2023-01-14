from datetime import datetime
from typing import Any, Dict
from uuid import UUID

from pydantic import BaseModel


class Request(BaseModel):
    id: UUID
    endpoint_id: UUID
    elapsed: float
    status_code: int
    response: Dict[str, Any]
    created_at: datetime
