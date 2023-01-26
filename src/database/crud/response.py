from uuid import UUID

from sqlalchemy.orm import Session

from database.crud import base
from models import models


class ResponseCRUD(base.CRUDBase):
    def get_by_api_id(self, db: Session, api_id: UUID, skip: int = 0, limit: int = 100):
        return db.query(self.model).filter(self.model.api_id == api_id).offset(skip).limit(limit).all()

    def get_by_api_name(self, db: Session, api_name: str):
        return (
            db.query(self.model)
            .join(models.Api)
            .filter(self.model.api_id == models.Api.id)
            .filter(models.Api.name == api_name)
            .all()
        )
