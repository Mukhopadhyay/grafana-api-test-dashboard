from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from models.base import Base, CreateMixin, UpdateMixin


class Api(Base, CreateMixin, UpdateMixin):
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    method = Column(String, nullable=False)
    version = Column(String, nullable=True)
    category = Column(String, nullable=True)
    description = Column(String, nullable=True)
    status = Column(Boolean, nullable=False, default=True)
    # Relationships
    responses = relationship("Response")


class Response(Base, CreateMixin):
    api_id = Column(UUIDType, ForeignKey("api.id", onupdate="CASCADE"))
    elapsed = Column(Numeric, nullable=False)
    status_code = Column(Integer, nullable=False)
    content_length = Column(Integer, nullable=False)
    # Relationships
    api = relationship("Api", back_populates="responses")

