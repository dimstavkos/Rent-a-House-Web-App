from sqlalchemy.orm import Session

from Requests.IndoorSpace.SearchRequest import SearchIndoorSpaceRequest
from models.IndoorSpace import IndoorSpace


class IndoorSpaceController:
    def list(self, db: Session):
        return db.query(IndoorSpace).all()

    def findByid(self, db: Session, id: int):
        return db.query(IndoorSpace).get(id)

    def delete(self, db: Session, id: int):
        db.query(IndoorSpace).filter_by(id=id).delete()
        db.commit()
        return "success"

    def create(self, db: Session, entity: IndoorSpace):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def search(self, db: Session, request: SearchIndoorSpaceRequest):
        query = db.query(IndoorSpace)

        if request.id != None:
            query = query.filter_by(id = request.id)

        if request.bed_num != None:
            query = query.filter_by(bed_num=request.bed_num)

        if request.bedroom_num != None:
            query = query.filter_by(bedroom_num=request.bed_num)

        if request.has_livingroom != None:
            query = query.filter_by(has_livingroom=request.has_livingroom)

        if request.total_space != None:
            query = query.filter_by(total_space=request.total_space)

        if request.description != None:
            query = query.filter(IndoorSpace.description.like('%' + request.description + '%'))

        if request.property_type_id != None:
            query = query.filter_by(property_type_id=request.property_type_id)

        return query.all()

    def patch(self, db: Session, newEntity: IndoorSpace):
        existingEntity = db.query(IndoorSpace).get(newEntity.id)

        existingEntity.bed_num = newEntity.bed_num
        existingEntity.bath_num = newEntity.bath_num
        existingEntity.bedroom_num = newEntity.bedroom_num
        existingEntity.has_livingroom = newEntity.has_livingroom
        existingEntity.total_space = newEntity.total_space
        existingEntity.description = newEntity.description
        existingEntity.property_type_id = newEntity.property_type_id

        db.commit()
        db.refresh(existingEntity)
        return existingEntity
