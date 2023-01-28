from sqlalchemy_utils import UUIDType
from sqlalchemy.orm import relationship

from models.base import Base, CreateMixin, UpdateMixin
from sqlalchemy import Boolean, Column, ForeignKey, Integer, Numeric, String


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
    errors = relationship("Errors")


class Response(Base, CreateMixin):
    api_id = Column(UUIDType, ForeignKey("api.id", onupdate="CASCADE"))
    elapsed = Column(Numeric, nullable=False)
    status_code = Column(Integer, nullable=False)
    content_length = Column(Integer, nullable=False)
    headers = Column(String, nullable=True)
    request = Column(String, nullable=True)
    response = Column(String, nullable=True)
    cookies = Column(String, nullable=True)
    # Relationships
    api = relationship("Api", back_populates="responses")


class Errors(Base, CreateMixin):
    api_id = Column(UUIDType, ForeignKey("api.id", onupdate="CASCADE"))
    message = Column(String, nullable=False)
    # Relationships
    api = relationship("Api", back_populates="errors")
