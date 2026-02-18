from sqlalchemy.orm import Session

from Requests.Review.SearchRequest import SearchReviewRequest
from models.Review import Review


class ReviewController:
    def list(self, db: Session):
        return db.query(Review).all()

    def findByid(self, db: Session, id: int):
        return db.query(Review).get(id)


    def delete(self, db: Session, id: int):
        db.query(Review).filter_by(id=id).delete()
        db.commit()
        return "success"

    def create(self, db: Session, entity: Review):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def search(self, db: Session, request: SearchReviewRequest):
        query = db.query(Review)

        if request.id != None:
            query = query.filter_by(id=request.id)

        if request.rating != None:
            query = query.filter_by(rating=request.rating)

        if request.comment != None:
            query = query.filter(Review.comment.like('%' + request.comment + '%'))


        return query.all()

    def patch(self, db: Session, newEntity: Review):
        existingEntity = db.query(Review).get(newEntity.id)

        existingEntity.rating= newEntity.rating
        existingEntity.comment = newEntity.comment

        db.commit()
        db.refresh(existingEntity)
        return existingEntity
