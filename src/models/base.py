import re
from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.sql import text
from sqlalchemy_utils import UUIDType


@as_declarative()
class Base:
    __name__: str

    id = Column(UUIDType, primary_key=True, server_default=text("get_random_uuid()"))

    @declared_attr
    def __tablename__(cls) -> str:
        name: str = re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__)
        return name.lower()


class CreateMixin:
    created_at = Column(DateTime, nullable=False, default=datetime.now)


class UpdateMixin:
    updated_at = Column(DateTime, nullable=False, default=datetime.now)
