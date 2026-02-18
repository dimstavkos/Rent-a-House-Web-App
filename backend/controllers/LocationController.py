from sqlalchemy.orm import Session, load_only

from Requests.Location.SearchRequest import SearchLocationRequest
from models.Location import Location
class LocationController:
    def list(self, db: Session):
        return db.query(Location).all()

    def listCountries(self, db: Session):
        countryEntities = db.query(Location).all()
        results = set()

        for x in countryEntities:
            results.add(x.country)
        return sorted(results)

    def listCities(self, db: Session):
        cityEntities = db.query(Location).all()
        results = set()

        for x in cityEntities:
            results.add(x.city)
        return sorted(results)


    def findByid(self, db: Session, id : int):
        return db.query(Location).get(id)

    def delete(self, db: Session, id : int):
        db.query(Location).filter_by(id=id).delete()
        db.commit()
        return "success"

    def create(self, db: Session, entity : Location):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def search(self, db: Session, request : SearchLocationRequest):
        query = db.query(Location)

        if request.id != None:
            query = query.filter_by(id = request.id)

        if request.country != None:
            query = query.filter(Location.country.like('%' + request.country + '%'))

        if request.city != None:
            query = query.filter(Location.city.like('%' + request.city + '%'))

        if request.address != None:
            query = query.filter(Location.address.like('%' + request.address + '%'))

        if request.latitude != None:
            query = query.filter_by(latitude = request.latitude)

        if request.longitude != None:
            query = query.filter_by(latitude = request.longitude)

        return query.all()

    def patch(self, db: Session, newEntity : Location):
        existingEntity = db.query(Location).get(newEntity.id)
        
        #existingEntity.country = newEntity.country 
        #existingEntity.city = newEntity.city
        existingEntity.address = newEntity.address
        
        db.commit()
        db.refresh(existingEntity)
        return existingEntity
