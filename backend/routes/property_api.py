from fastapi import Depends, APIRouter
from sqlalchemy.sql.functions import now

from Requests.Property.CreateRequest import CreatePropertyRequest
from Requests.Property.PatchRequest import PatchPropertyRequest
from Requests.Property.SearchRequest import SearchPropertyRequest
from Requests.Property.ViewRequest import ViewPropertyRequest
from auth.auth_bearer_users import JWTBearerUser
from controllers.PropertyController import PropertyController

from sqlalchemy.orm import Session

from database.database import SessionLocal, get_db
from models.Property import Property

router = APIRouter()


@router.get("/property/list", dependencies=[Depends(JWTBearerUser())])
def propertyList(db: Session = Depends(get_db), controller=Depends(PropertyController)):
    return controller.list(db)


@router.get("/property/id/{id}", dependencies=[Depends(JWTBearerUser())])
def propertyFindid(id: int, db: Session = Depends(get_db), controller=Depends(PropertyController)):
    return controller.findByid(db, id)


@router.get("/property/userid/{id}", dependencies=[Depends(JWTBearerUser())])
def propertyFindUserid(id: int, db: Session = Depends(get_db), controller=Depends(PropertyController)):
    return controller.findByUserid(db, id)


@router.delete("/property/id/{id}", dependencies=[Depends(JWTBearerUser())])
def propertyDelete(id: int, db: Session = Depends(get_db), controller=Depends(PropertyController)):
    return controller.delete(db, id)


@router.post("/property/create", dependencies=[Depends(JWTBearerUser())])
def propertyCreate(request: CreatePropertyRequest, db: Session = Depends(get_db),
                   controller=Depends(PropertyController)):
    entity = Property(price=request.price, has_wifi=request.has_wifi, has_airconditioning=request.has_airconditioning,
                      has_heat=request.has_heat, has_kitchen=request.has_kitchen, has_tv=request.has_tv,
                      has_parking=request.has_parking, has_elevator=request.has_elevator,
                      description=request.description, floor=request.floor, number_of_guests=request.number_of_guests,
                      is_available=request.is_available, user_id=request.user_id, location_id=request.location_id,
                      indoor_space_id=request.indoor_space_id, property_created=now(),
                      property_updated=now())
    return controller.create(db, entity)


@router.post("/property/search", dependencies=[Depends(JWTBearerUser())])
def propertySearch(request: SearchPropertyRequest, db: Session = Depends(get_db),
                   controller=Depends(PropertyController)):
    return controller.search(db, request)


@router.get("/property/recommend/{user_id}", dependencies=[Depends(JWTBearerUser())])
def propertySearch(user_id: int, db: Session = Depends(get_db), controller=Depends(PropertyController)):
    return controller.recommend(db, user_id)


@router.patch("/property/patch", dependencies=[Depends(JWTBearerUser())])
def propertyPatch(request: PatchPropertyRequest, db: Session = Depends(get_db), controller=Depends(PropertyController)):
    entity = Property(id=request.id, price=request.price, has_wifi=request.has_wifi,
                      has_airconditioning=request.has_airconditioning, has_heat=request.has_heat,
                      has_kitchen=request.has_kitchen, has_tv=request.has_tv, has_parking=request.has_parking,
                      has_elevator=request.has_elevator, description=request.description, floor=request.floor,
                      number_of_guests=request.number_of_guests, is_available=request.is_available,
                      user_id=request.user_id, location_id=request.location_id, indoor_space_id=request.indoor_space_id,
                      property_created=request.property_created, property_updated=now())

    return controller.patch(db, entity)


@router.post("/property/view", dependencies=[Depends(JWTBearerUser())])
def propertyCreate(request: ViewPropertyRequest, db: Session = Depends(get_db), controller=Depends(PropertyController)):
    user_id = request.user_id
    property_id = request.property_id
    return controller.commitView(db, user_id, property_id)
