from fastapi import Depends, APIRouter
from sqlalchemy.sql.functions import now

from Requests.AvailableDate.CreateRequest import CreateAvailableDateRequest
from Requests.AvailableDate.PatchRequest import PatchAvailableDateRequest
from Requests.AvailableDate.SearchRequest import SearchAvailableDateRequest
from auth.auth_bearer_users import JWTBearerUser
from controllers.AvailableDateController import AvailableDateController

from sqlalchemy.orm import Session

from database.database import SessionLocal, get_db
from models.AvailableDate import AvailableDate

router = APIRouter()

@router.get("/availabledate/list", dependencies=[Depends(JWTBearerUser())])
def availableDateList(db: Session = Depends(get_db), controller=Depends(AvailableDateController)):
    return controller.list(db)


@router.get("/availabledate/id/{id}", dependencies=[Depends(JWTBearerUser())])
def availableDateFindid(id: int, db: Session = Depends(get_db), controller=Depends(AvailableDateController)):
    return controller.findByid(db, id)

@router.get("/availabledate/userid/{id}", dependencies=[Depends(JWTBearerUser())])
def availableDateFindPropertyid(id: int, db: Session = Depends(get_db), controller=Depends(AvailableDateController)):
    return controller.findByUserid(db, id)


@router.delete("/availabledate/id/{id}", dependencies=[Depends(JWTBearerUser())])
def availableDateDelete(id: int, db: Session = Depends(get_db), controller=Depends(AvailableDateController)):
    return controller.delete(db, id)

@router.post("/availabledate/create", dependencies=[Depends(JWTBearerUser())])
def availableDateCreate(request: CreateAvailableDateRequest, db: Session = Depends(get_db), controller=Depends(AvailableDateController)):
    entity = AvailableDate(start_date=request.start_date,end_date=request.end_date,property_id=request.property_id)
    return controller.create(db, entity)


@router.post("/availabledate/search", dependencies=[Depends(JWTBearerUser())])
def availableDateSearch(request: SearchAvailableDateRequest, db: Session = Depends(get_db), controller=Depends(AvailableDateController)):
    return controller.search(db, request)


@router.patch("/availabledate/patch", dependencies=[Depends(JWTBearerUser())])
def availableDatePatch(request: PatchAvailableDateRequest, db: Session = Depends(get_db), controller=Depends(AvailableDateController)):
    entity = AvailableDate(id=request.id,start_date=request.start_date,end_date=request.end_date,property_id=request.property_id)
    return controller.patch(db, entity)