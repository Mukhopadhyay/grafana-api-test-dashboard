from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy_utils import UUIDType

from models.base import Base, CreateMixin, ForeignKey

# https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html


class Response(Base, CreateMixin):
    api_id = Column(UUIDType, ForeignKey("api.id", onupdate="CASCADE"))
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    elapsed = Column(Numeric, nullable=False)
    version = Column(String, nullable=True)
    category = Column(String, nullable=False)
    status_code = Column(Integer, nullable=False)
    content_length = Column(Integer, nullable=False)
