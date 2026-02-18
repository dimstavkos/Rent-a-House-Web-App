from sqlalchemy.orm import Session

from Requests.Role.SearchRequest import SearchRoleRequest
from models.Role import Role


class RoleController:
    def list(self, db: Session):
        return db.query(Role).all()

    def find(self, db: Session, id : int):
        return db.query(Role).get(id)

    def delete(self, db: Session, id : int):
        db.query(Role).filter_by(id=id).delete()
        db.commit()
        return "success"

    def create(self, db: Session, entity : Role):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def search(self, db: Session, request : SearchRoleRequest):
        query = db.query(Role)

        if request.id != None:
            query = query.filter_by(id=request.id)

        if request.role_name != None:
            query = query.filter(Role.role_name.like('%' + request.role_name + '%'))

        return query.all()

    def patch(self, db: Session, newEntity : Role):
        existingEntity = db.query(Role).get(newEntity.id)
        existingEntity.role_name = newEntity.role_name
        db.commit()
        db.refresh(existingEntity)
        return existingEntity