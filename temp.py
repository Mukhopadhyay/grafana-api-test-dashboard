import warnings

warnings.filterwarnings("ignore")

import random
import re
from datetime import datetime
from typing import Generator, Optional
from uuid import UUID

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, PostgresDsn
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String, create_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Session, relationship, sessionmaker
from sqlalchemy.sql import text
from sqlalchemy_utils import UUIDType, get_columns


@as_declarative()
class Base:
    __name__: str

    id = Column(UUIDType, primary_key=True, server_default=text("uuid_generate_v4()"))

    @declared_attr
    def __tablename__(cls) -> str:
        """This makes table names from `TableName` to `table_name`"""
        name: str = re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__)
        return name.lower()


class CreateMixin:
    created_at = Column(DateTime, nullable=False, default=datetime.now)


class UpdateMixin:
    updated_at = Column(DateTime, nullable=False, default=datetime.now)


class Api(Base, CreateMixin, UpdateMixin):
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    method = Column(String, nullable=False)
    version = Column(String, nullable=True)
    category = Column(String, nullable=True)
    description = Column(String, nullable=True)
    # Relationships
    responses = relationship("Response")


class Response(Base, CreateMixin):
    api_id = Column(UUIDType, ForeignKey("api.id", onupdate="CASCADE"))
    elapsed = Column(Numeric, nullable=False)
    status_code = Column(Integer, nullable=False)
    content_length = Column(Integer, nullable=False)
    # Relationships
    api = relationship("Api", back_populates="responses")


# Equivalent schema (Pydantic)
class ApiSchema(BaseModel):
    name: str
    url: str
    method: str
    version: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None


class ResponseSchema(BaseModel):
    api_id: UUID
    elapsed: float
    status_code: int
    content_length: int


pg_config = {
    "scheme": "postgresql",
    "user": "grafana",
    "password": "grafana",
    "host": "localhost",
    "port": "6432",
    "path": "/grafana",
}

DB_URI = PostgresDsn.build(**pg_config)

engine = create_engine(DB_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(engine, autocommit=False, autoflush=False)


def get_db() -> Session:
    db = SessionLocal()
    return db


db = get_db()
db.execute(text("truncate table api cascade;"))
db.execute(text("truncate table response cascade;"))
db.commit()
db.close()


# Inserting into Api
apis = [
    ApiSchema(name="Google", url="https://www.google.com", method="GET", version="v5", category="WEB"),
    ApiSchema(name="Google", url="https://www.bing.com", method="GET", version="v1", category="WEB"),
    ApiSchema(name="Google", url="https://www.gitlab.com", method="GET", version="v2", category="CODE"),
    ApiSchema(name="Github", url="https://github.com/", method="GET", version="v1", category="CODE"),
    ApiSchema(name="Google", url="https://azure.devops.com", method="GET", version="v2", category="CODE"),
    ApiSchema(name="Google", url="https://www.amazon.com", method="GET", version="v2", category="ECOMMERCE"),
]

ids = []

for api in apis:
    db = get_db()
    db_obj = Api(**api.dict())
    db.add(db_obj)
    db.commit()
    ids.append(db_obj.id)
    db.close()


for i in range(1, 101):
    rs = ResponseSchema(
        api_id=random.choice(ids),
        elapsed=random.random(),
        status_code=random.choice([200, 400, 404, 500, 502]),
        content_length=random.randint(1, 4096),
    )
    db = get_db()
    db.add(Response(**rs.dict()))
    db.commit()
    print(f"{i}/100", end="\r", flush=True)
