"""
No being used
"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base import Base, CreateMixin, UpdateMixin


class API(Base, CreateMixin, UpdateMixin):
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    method = Column(String, nullable=False)
    version = Column(String, nullable=True)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)
    # Relationships
    responses = relationship("response")
