"""
Pydantic class for grafana.init.json
"""

from pydantic import BaseModel
from schemas.grafana_http import OrgAddress
from typing import List, Optional, Dict, Any

class GrafanaInitUsers(BaseModel):
    name: str
    email: str
    login: str
    password: str

class GrafanaInitOrg(BaseModel):
    name: str
    address: OrgAddress
    is_default: bool
    users: Optional[List[Dict[str, Any]]] = []

class GrafanaInit(BaseModel):
    users: List[GrafanaInitUsers]
    organization: GrafanaInitOrg
