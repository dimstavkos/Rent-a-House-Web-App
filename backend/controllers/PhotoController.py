from sqlalchemy.orm import Session

from Requests.Photo.CreateRequest import CreatePhotoRequest
from Requests.Photo.PatchRequest import PatchPhotoRequest
from Requests.Photo.SearchRequest import SearchPhotoRequest
from models.Photo import Photo


class PhotoController:
    def list(self, db: Session):
        return db.query(Photo).all()

    def findByid(self, db: Session, id: int):
        return db.query(Photo).get(id)

    def delete(self, db: Session, id: int):
        db.query(Photo).filter_by(id=id).delete()
        db.commit()
        return "success"

    def create(self, db: Session, entity: Photo):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def search(self, db: Session, request: SearchPhotoRequest):
        query = db.query(Photo)

        if request.id != None:
            query = query.filter_by(id=request.id)

        if request.photo != None:
            query = query.filter(Photo.photo.like('%' + request.photo + '%'))

        if request.property_id != None:
            query = query.filter_by(property_id=request.property_id)

        return query.all()

    def patch(self, db: Session, newEntity: Photo):
        existingEntity = db.query(Photo).get(newEntity.id)

        existingEntity.photo = newEntity.photo
        existingEntity.property_id = newEntity.property_id

        db.commit()
        db.refresh(existingEntity)
        return existingEntity
