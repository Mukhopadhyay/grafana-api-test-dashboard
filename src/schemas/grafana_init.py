"""
Pydantic class for grafana.init.json
"""

from pydantic import BaseModel
from typing import List, Optional
from schemas.grafana_http import OrgAddress

class GrafanaInitUsers(BaseModel):
    name: str
    email: str
    login: str
    password: str

class GrafanaOrgUsers(BaseModel):
    login: str
    role: str

class GrafanaInitOrg(BaseModel):
    name: str
    address: OrgAddress
    is_default: bool
    users: Optional[List[GrafanaOrgUsers]] = []

class GrafanaInit(BaseModel):
    users: List[GrafanaInitUsers]
    organization: GrafanaInitOrg
