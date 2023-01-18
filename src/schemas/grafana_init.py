"""
Pydantic class for grafana.init.json
"""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from schemas.grafana_http import OrgAddress


class GrafanaInitUsers(BaseModel):
    name: str
    email: str
    login: str
    password: str


class GrafanaInitOrg(BaseModel):
    name: str
    address: OrgAddress
    is_default: bool
    users: Optional[Dict[str, Any]] = {}


class GrafanaInit(BaseModel):
    users: List[GrafanaInitUsers]
    organization: GrafanaInitOrg
