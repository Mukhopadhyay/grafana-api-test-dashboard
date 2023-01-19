from uuid import UUID

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CRUDBase:
    def __init__(self, model):
        # This is the ORM model class
        self.model = model

    def get(self, db: Session, id: UUID):
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100):
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        try:
            db.add(db_obj)
        except Exception:
            db.rollback()
            return None
        else:
            db.commit()
            db.refresh(db_obj)
            return db_obj

    def update(self, db: Session, *, db_obj, obj_in):
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        try:
            db.add(db_obj)
        except Exception:
            db.rollback()
            return None
        else:
            db.commit()
            db.refresh(db_obj)
            return db_obj

    def remove(self, db: Session, *, id: UUID):
        obj = db.query(self.model).get(id)
        try:
            db.delete(obj)
        except Exception:
            db.rollback()
            return None
        else:
            db.commit()
            return obj
