from sqlalchemy.orm import Session

from Requests.Booking.SearchRequest import SearchBookingRequest
from models.Booking import Booking
from sqlalchemy import desc


class BookingController:
    def list(self, db: Session):
        return db.query(Booking).all()

    def findByid(self, db: Session, id: int):
        return db.query(Booking).get(id)

    def findByUserid(self, db: Session, user_id: int):
        return db.query(Booking).filter_by(user_id=user_id).order_by(desc(Booking.booking_created)).all()

    def findByProperty(self, db:Session, property_id: int):
        return db.query(Booking).filter_by(property_id=property_id).order_by(desc(Booking.booking_created)).all()

    def delete(self, db: Session, id: int):
        db.query(Booking).filter_by(id=id).delete()
        db.commit()
        return "success"

    def create(self, db: Session, entity: Booking):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def search(self, db: Session, request: SearchBookingRequest):
        query = db.query(Booking)

        if request.id != None:
            query = query.filter_by(id = request.id)

        if request.start_date != None:
            query = query.filter_by(start_date=request.start_date)

        if request.end_date != None:
            query = query.filter_by(end_date=request.end_date)

        if request.total_night_num != None:
            query = query.filter_by(total_night_num=request.total_night_num)

        if request.total_price != None:
            query = query.filter_by(total_price=request.total_price)

        if request.user_id != None:
            query = query.filter_by(user_id=request.user_id)

        if request.property_id != None:
            query = query.filter_by(property_id=request.property_id)

        if request.review_id != None:
            query = query.filter_by(review_id=request.review_id)

        if request.booking_created != None:
            query = query.filter_by(booking_created=request.booking_created)

        if request.booking_updated != None:
            query = query.filter_by(booking_updated=request.booking_updated)

        if request.booking_completed != None:
            query = query.filter_by(booking_completed=request.booking_completed)

        if request.booking_verified != None:
            query = query.filter_by(booking_verified=request.booking_verified)

        return query.all()

    def patch(self, db: Session, newEntity: Booking):
        existingEntity = db.query(Booking).get(newEntity.id)

        existingEntity.start_date = newEntity.start_date
        existingEntity.end_date = newEntity.end_date
        existingEntity.total_night_num = newEntity.total_night_num
        existingEntity.total_price = newEntity.total_price
        existingEntity.user_id = newEntity.user_id
        existingEntity.property_id = newEntity.property_id
        existingEntity.review_id = newEntity.review_id
        existingEntity.booking_created = newEntity.booking_created
        existingEntity.booking_updated = newEntity.booking_updated
        existingEntity.booking_completed = newEntity.booking_completed
        existingEntity.booking_verified = newEntity.booking_verified


        db.commit()
        db.refresh(existingEntity)
        return existingEntity
