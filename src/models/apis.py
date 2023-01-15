from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy_utils import UUIDType

from src.models.base import Base, CreateMixin, UpdateMixin

# # TODO: Not used yet
# class Endpoint(Base, CreateMixin, UpdateMixin):
#     name = Column(String, nullable=False, unique=True)
#     url = Column(String, nullable=False)
#     version = Column(String, nullable=True)


# # TODO: Not used yet
# class RequestBody(Base, CreateMixin, UpdateMixin):
#     endpoint_id = Column(UUIDType, ForeignKey("endpoint.id", ondelete="CASCADE", onupdate="CASCADE"))
#     body = Column(JSON, nullable=False)


# # TODO: Not used yet
# class ResponseSchema(Base, CreateMixin, UpdateMixin):
#     endpoint_id = Column(UUIDType, ForeignKey("endpoint.id", ondelete="CASCADE", onupdate="CASCADE"))
#     body = Column(JSON, nullable=False)


class Endpoint(Base, CreateMixin):
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    url = Column(String, nullable=False)
    elapsed = Column(Numeric, nullable=False)
    category = Column(String, nullable=False)
    status_code = Column(Integer, nullable=False)
    content_length = Column(Integer, nullable=False)
