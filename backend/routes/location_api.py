from fastapi import Depends, APIRouter
from sqlalchemy.sql.functions import now

from Requests.Location.CreateRequest import CreateLocationRequest
from Requests.Location.PatchRequest import PatchLocationRequest
from Requests.Location.SearchRequest import SearchLocationRequest
from auth.auth_bearer_users import JWTBearerUser
from controllers.LocationController import LocationController

from sqlalchemy.orm import Session

from database.database import SessionLocal, get_db
from models.Location import Location

router = APIRouter()

@router.get("/location/list", dependencies=[Depends(JWTBearerUser())])
def locationList(db: Session = Depends(get_db), controller=Depends(LocationController)):
    return controller.list(db)

@router.get("/location/countries", dependencies=[Depends(JWTBearerUser())])
def locationList(db: Session = Depends(get_db), controller=Depends(LocationController)):
    return controller.listCountries(db)

@router.get("/location/cities", dependencies=[Depends(JWTBearerUser())])
def locationList(db: Session = Depends(get_db), controller=Depends(LocationController)):
    return controller.listCities(db)

@router.get("/location/id/{id}", dependencies=[Depends(JWTBearerUser())])
def locationFindid(id: int, db: Session = Depends(get_db), controller=Depends(LocationController)):
    return controller.findByid(db, id)


@router.delete("/location/id/{id}", dependencies=[Depends(JWTBearerUser())])
def locationDelete(id: int, db: Session = Depends(get_db), controller=Depends(LocationController)):
    return controller.delete(db, id)

@router.post("/location/create", dependencies=[Depends(JWTBearerUser())])
def locationCreate(request: CreateLocationRequest, db: Session = Depends(get_db), controller=Depends(LocationController)):
    entity = Location(country=request.country,city=request.city,address=request.address, latitude=request.latitude, longitude=request.longitude)
    return controller.create(db, entity)


@router.post("/location/search", dependencies=[Depends(JWTBearerUser())])
def locationSearch(request: SearchLocationRequest, db: Session = Depends(get_db), controller=Depends(LocationController)):
    return controller.search(db, request)


@router.patch("/location/patch", dependencies=[Depends(JWTBearerUser())])
def locationPatch(request: PatchLocationRequest, db: Session = Depends(get_db), controller=Depends(LocationController)):
    entity = Location(id=request.id,country=request.country, city=request.city,address=request.address, latitude=request.latitude, longitude=request.longitude)
    return controller.patch(db, entity)
