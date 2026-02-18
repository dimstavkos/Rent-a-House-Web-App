from sqlalchemy.orm import Session

from Requests.AvailableDate.SearchRequest import SearchAvailableDateRequest
from models.AvailableDate import AvailableDate


class AvailableDateController:
    def list(self, db: Session):
        return db.query(AvailableDate).all()

    def findByid(self, db: Session, id: int):
        return db.query(AvailableDate).get(id)

    def findByPropertyid(self, db: Session, property_id: int):
        return db.query(AvailableDate).get(property_id)

    def delete(self, db: Session, id: int):
        db.query(AvailableDate).filter_by(id=id).delete()
        db.commit()
        return "success"

    def create(self, db: Session, entity: AvailableDate):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def search(self, db: Session, request: SearchAvailableDateRequest):
        query = db.query(AvailableDate)

        if request.id != None:
            query = query.filter_by(id = request.id)

        if request.start_date != None:
            query = query.filter_by(start_date=request.start_date)

        if request.end_date != None:
            query = query.filter_by(end_date=request.end_date)


        if request.property_id != None:
            query = query.filter_by(property_id=request.property_id)


        return query.all()

    def patch(self, db: Session, newEntity: AvailableDate):
        existingEntity = db.query(AvailableDate).get(newEntity.id)

        existingEntity.start_date = newEntity.start_date
        existingEntity.end_date = newEntity.end_date
        existingEntity.property_id = newEntity.property_id

        db.commit()
        db.refresh(existingEntity)
        return existingEntity
