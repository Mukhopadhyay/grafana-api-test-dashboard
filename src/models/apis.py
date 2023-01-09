from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy_utils import UUIDType

from src.models.base import Base, CreateMixin, UpdateMixin


class Endpoint(Base, CreateMixin, UpdateMixin):
    name = Column(String, nullable=False, unique=True)
    url = Column(String, nullable=False)
    version = Column(String, nullable=True)


class RequestBody(Base, CreateMixin, UpdateMixin):
    endpoint_id = Column(UUIDType, ForeignKey("endpoint.id", ondelete="CASCADE", onupdate="CASCADE"))
    body = Column(JSON, nullable=False)


class ResponseSchema(Base, CreateMixin, UpdateMixin):
    endpoint_id = Column(UUIDType, ForeignKey("endpoint.id", ondelete="CASCADE", onupdate="CASCADE"))
    body = Column(JSON, nullable=False)
