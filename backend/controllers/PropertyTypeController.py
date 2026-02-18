from sqlalchemy.orm import Session

from Requests.PropertyType.SearchRequest import SearchPropertyTypeRequest
from models.PropertyType import PropertyType


class PropertyTypeController:
    def list(self, db: Session):
        return db.query(PropertyType).all()

    def findByid(self, db: Session, id: int):
        return db.query(PropertyType).get(id)


    def delete(self, db: Session, id: int):
        db.query(PropertyType).filter_by(id=id).delete()
        db.commit()
        return "success"

    def create(self, db: Session, entity: PropertyType):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def search(self, db: Session, request: SearchPropertyTypeRequest):
        query = db.query(PropertyType)

        if request.id != None:
            query = query.filter_by(id = request.id)

        if request.property_type_name != None:
            query = query.filter(PropertyType.property_type_name.like('%' + request.property_type_name + '%'))


        return query.all()

    def patch(self, db: Session, newEntity: PropertyType):
        existingEntity = db.query(PropertyType).get(newEntity.id)

        existingEntity.property_type_name = newEntity.property_type_name


        db.commit()
        db.refresh(existingEntity)
        return existingEntity
