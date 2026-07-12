from sqlalchemy.orm import Session


class BaseService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self, db: Session):
        return self.repository.get_all(db)

    def get_by_id(self, db: Session, obj_id: int):
        return self.repository.get_by_id(db, obj_id)

    def create(self, db: Session, data):
        return self.repository.create(
            db,
            data.model_dump(),
        )

    def update(
        self,
        db: Session,
        obj_id: int,
        data,
    ):
        return self.repository.update(
            db,
            obj_id,
            data.model_dump(exclude_unset=True),
        )

    def delete(
        self,
        db: Session,
        obj_id: int,
    ):
        return self.repository.delete(
            db,
            obj_id,
        )
