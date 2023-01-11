from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy_utils import UUIDType

from src.models.base import Base, CreateMixin


# TODO: Not used yet
class Request(Base, CreateMixin):
    endpoint_id = Column(UUIDType, ForeignKey("endpoint.id", ondelete="CASCADE", onupdate="CASCADE"))
    elapsed = Column(Numeric, nullable=False)
    status_code = Column(Integer, nullable=False)
    response = Column(JSON, nullable=True)
