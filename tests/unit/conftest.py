import json

from pytest import fixture

from src.models import response as orm_response
from src.schemas.db import apis as pydantic_apis


@fixture
def endpoint_keys():
    ep_orm = orm_response.Response()
    ep_pyd = pydantic_apis.Endpoint

    pyd_attrs = list(json.loads(ep_pyd.schema_json())["properties"].keys())
    orm_attrs = [str(x).split(".")[-1] for x in ep_orm.__table__.columns]

    return (pyd_attrs, orm_attrs)
