from uuid import UUID
from models import models
from database.crud import base
from sqlalchemy.orm import Session


class ResponseCRUD(base.CRUDBase):
    def __init__(self):
        super().__init__(models.Response)

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
