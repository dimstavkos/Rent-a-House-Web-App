from fastapi import Depends, APIRouter
from sqlalchemy.sql.functions import now

from Requests.PropertyType.CreateRequest import CreatePropertyTypeRequest
from Requests.PropertyType.PatchRequest import PatchPropertyTypeRequest
from Requests.PropertyType.SearchRequest import SearchPropertyTypeRequest
from auth.auth_bearer_users import JWTBearerUser
from controllers.PropertyTypeController import PropertyTypeController

from sqlalchemy.orm import Session

from database.database import SessionLocal, get_db
from models.PropertyType import PropertyType

router = APIRouter()

@router.get("/propertytype/list", dependencies=[Depends(JWTBearerUser())])
def propertyTypeList(db: Session = Depends(get_db), controller=Depends(PropertyTypeController)):
    return controller.list(db)


@router.get("/propertytype/id/{id}", dependencies=[Depends(JWTBearerUser())])
def propertyTypeFindid(id: int, db: Session = Depends(get_db), controller=Depends(PropertyTypeController)):
    return controller.findByid(db, id)


@router.delete("/propertytype/id/{id}", dependencies=[Depends(JWTBearerUser())])
def propertyTypeDelete(id: int, db: Session = Depends(get_db), controller=Depends(PropertyTypeController)):
    return controller.delete(db, id)

@router.post("/propertytype/create", dependencies=[Depends(JWTBearerUser())])
def propertyTypeCreate(request: CreatePropertyTypeRequest, db: Session = Depends(get_db), controller=Depends(PropertyTypeController)):
    entity = PropertyType(property_type_name = request.property_type_name)
    return controller.create(db, entity)


@router.post("/propertytype/search", dependencies=[Depends(JWTBearerUser())])
def propertyTypeSearch(request: SearchPropertyTypeRequest, db: Session = Depends(get_db), controller=Depends(PropertyTypeController)):
    return controller.search(db, request)


@router.patch("/propertytype/patch", dependencies=[Depends(JWTBearerUser())])
def propertyTypePatch(request: PatchPropertyTypeRequest, db: Session = Depends(get_db), controller=Depends(PropertyTypeController)):
    entity = PropertyType(id=request.id, property_type_name = request.property_type_name)
    return controller.patch(db, entity)
