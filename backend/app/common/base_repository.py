from typing import Generic, TypeVar, Type

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def get_by_id(self, db: Session, obj_id: int):
        return db.query(self.model).filter(self.model.id == obj_id).first()

    def create(self, db: Session, data: dict):
        obj = self.model(**data)

        db.add(obj)
        db.commit()
        db.refresh(obj)

        return obj

    def update(
        self,
        db: Session,
        obj_id: int,
        data: dict,
    ):
        obj = self.get_by_id(db, obj_id)

        if not obj:
            return None

        for key, value in data.items():
            setattr(obj, key, value)

        db.commit()
        db.refresh(obj)

        return obj

    def delete(
        self,
        db: Session,
        obj_id: int,
    ):
        obj = self.get_by_id(db, obj_id)

        if not obj:
            return None

        db.delete(obj)
        db.commit()

        return obj
