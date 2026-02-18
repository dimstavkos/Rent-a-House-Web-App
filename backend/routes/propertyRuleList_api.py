from fastapi import Depends, APIRouter
from sqlalchemy.sql.functions import now

from Requests.PropertyRuleList.CreateRequest import CreatePropertyRuleListRequest
from Requests.PropertyRuleList.PatchRequest import PatchPropertyRuleListRequest
from Requests.PropertyRuleList.SearchRequest import SearchPropertyRuleListRequest
from auth.auth_bearer_users import JWTBearerUser
from controllers.PropertyRuleListController import PropertyRuleListController

from sqlalchemy.orm import Session

from database.database import SessionLocal, get_db
from models.PropertyRuleList import PropertyRuleList

router = APIRouter()

@router.get("/propertyrulelist/list", dependencies=[Depends(JWTBearerUser())])
def propertyRuleListList(db: Session = Depends(get_db), controller=Depends(PropertyRuleListController)):
    return controller.list(db)
@router.get("/propertyrulelist/id/{id}", dependencies=[Depends(JWTBearerUser())])
def propertyRuleListFindid(id: int, db: Session = Depends(get_db), controller=Depends(PropertyRuleListController)):
    return controller.findByid(db, id)


@router.delete("/propertyrulelist/id/{id}", dependencies=[Depends(JWTBearerUser())])
def propertyrulelistDelete(id: int, db: Session = Depends(get_db), controller=Depends(PropertyRuleListController)):
    return controller.delete(db, id)

@router.post("/propertyrulelist/create", dependencies=[Depends(JWTBearerUser())])
def propertyrulelistCreate(request: CreatePropertyRuleListRequest, db: Session = Depends(get_db), controller=Depends(PropertyRuleListController)):
    entity = PropertyRuleList(smoking_allowed=request.smoking_allowed,pet_allowed=request.pet_allowed,party_allowed=request.party_allowed,min_night_number=request.min_night_number,property_id=request.property_id)
    return controller.create(db, entity)


@router.post("/propertyrulelist/search", dependencies=[Depends(JWTBearerUser())])
def propertySearch(request: SearchPropertyRuleListRequest, db: Session = Depends(get_db), controller=Depends(PropertyRuleListController)):
    return controller.search(db, request)


@router.patch("/propertyrulelist/patch", dependencies=[Depends(JWTBearerUser())])
def propertyrulelistPatch(request: PatchPropertyRuleListRequest, db: Session = Depends(get_db), controller=Depends(PropertyRuleListController)):
    entity = PropertyRuleList(id = request.id,property_id=request.property_id,smoking_allowed=request.smoking_allowed,pet_allowed=request.pet_allowed,party_allowed=request.party_allowed,min_night_number=request.min_night_number)
    return controller.patch(db, entity)
