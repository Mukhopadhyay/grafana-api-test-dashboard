from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy_utils import UUIDType

from models.base import Base, CreateMixin, UpdateMixin


class Endpoint(Base, CreateMixin):
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    elapsed = Column(Numeric, nullable=False)
    version = Column(String, nullable=True)
    category = Column(String, nullable=False)
    status_code = Column(Integer, nullable=False)
    content_length = Column(Integer, nullable=False)
