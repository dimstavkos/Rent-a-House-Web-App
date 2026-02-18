from sqlalchemy.orm import Session

from Requests.PropertyRuleList.SearchRequest import SearchPropertyRuleListRequest
from models.PropertyRuleList import PropertyRuleList




class PropertyRuleListController:
    def list(self, db: Session):
        return db.query(PropertyRuleList).all()

    def findByid(self, db: Session, property_id: int):
        return db.query(PropertyRuleList).get(property_id)

    def delete(self, db: Session, list_id: int):
        db.query(PropertyRuleList).filter_by(id=list_id).delete()
        db.commit()
        return "success"

    def create(self, db: Session, entity: PropertyRuleList):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def search(self, db: Session, request: SearchPropertyRuleListRequest):
        query = db.query(PropertyRuleList)

        if request.id != None:
            query = query.filter_by(id = request.id)

        if request.property_id != None:
            query = query.filter_by(id=request.property_id)

        if request.smoking_allowed != None:
            query = query.filter_by(smoking_allowed=request.smoking_allowed)

        if request.pet_allowed != None:
            query = query.filter_by(pet_allowed=request.pet_allowed)

        if request.party_allowed != None:
            query = query.filter_by(party_allowed=request.party_allowed)

        if request.min_night_number != None:
            query = query.filter_by(min_night_number=request.min_night_number)

        return query.all()

    def patch(self, db: Session, newEntity: PropertyRuleList):
        existingEntity = db.query(PropertyRuleList).get(newEntity.id)

        existingEntity.property_id = newEntity.property_id
        existingEntity.smoking_allowed = newEntity.smoking_allowed
        existingEntity.pet_allowed = newEntity.pet_allowed
        existingEntity.party_allowed = newEntity.party_allowed
        existingEntity.min_night_number = newEntity.min_night_number

        db.commit()
        db.refresh(existingEntity)
        return existingEntity
