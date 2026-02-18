from sqlalchemy.orm import Session, joinedload

from Requests.Role.SearchRequest import SearchRoleRequest
from models.User import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserController:
    def list(self, db: Session):
        return db.query(User).options(joinedload(User.roles, innerjoin=True)).all()

    def find(self, db: Session, id : int):
        return db.query(User).options(joinedload(User.roles, innerjoin=True)).get(id)

    def findByUsername(self, db: Session, username : str):
        query = db.query(User).options(joinedload(User.roles, innerjoin=True))
        query = query.filter(User.username.like(username))
        return query.all()

    def delete(self, db: Session, id : int):
        db.query(User).filter_by(id=id).delete()
        db.commit()
        return "success"

    def create(self, db: Session, entity : User):
        entity.password  =pwd_context.hash(entity.password)
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def search(self, db: Session, request : SearchRoleRequest):
        query = db.query(User)

        if request.id != None:
            query = query.filter_by(id=request.id)

        if request.name != None:
            query = query.filter(User.name.like('%' + request.name + '%'))

        if request.lastname != None:
            query = query.filter(User.lastname.like('%' + request.lastname + '%'))

        if request.email != None:
            query = query.filter(User.email.like('%' + request.email + '%'))

        if request.phone != None:
            query = query.filter(User.phone.like('%' + request.phone + '%'))

        return query.options(joinedload(User.roles, innerjoin=True)).all()

    def patch(self, db: Session, newEntity : User):
        existingEntity = db.query(User).get(newEntity.id)

        if newEntity.username != None:
            existingEntity.username = newEntity.username

        if newEntity.password != None:
            existingEntity.password = pwd_context.hash(newEntity.password)

        if newEntity.name != None:
            existingEntity.name = newEntity.name

        if newEntity.lastname != None:
            existingEntity.lastname = newEntity.lastname

        if newEntity.email != None:
            existingEntity.email = newEntity.email

        if newEntity.phone != None:
            existingEntity.phone = newEntity.phone

        if newEntity.photo != None:
            existingEntity.photo = newEntity.photo

        if newEntity.verified_status != None:
            existingEntity.verified_status = newEntity.verified_status

        db.commit()
        db.refresh(existingEntity)
        return existingEntity
