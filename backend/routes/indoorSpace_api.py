from fastapi import Depends, APIRouter
from sqlalchemy.sql.functions import now

from Requests.IndoorSpace.CreateRequest import CreateIndoorSpaceRequest
from Requests.IndoorSpace.PatchRequest import PatchIndoorSpaceRequest
from Requests.IndoorSpace.SearchRequest import SearchIndoorSpaceRequest
from auth.auth_bearer_users import JWTBearerUser
from controllers.IndoorSpaceController import IndoorSpaceController

from sqlalchemy.orm import Session

from database.database import SessionLocal, get_db
from models.IndoorSpace import IndoorSpace

router = APIRouter()

@router.get("/indoorspace/list", dependencies=[Depends(JWTBearerUser())])
def indoorSpaceList(db: Session = Depends(get_db), controller=Depends(IndoorSpaceController)):
    return controller.list(db)


@router.get("/indoorspace/id/{id}", dependencies=[Depends(JWTBearerUser())])
def indoorSpaceFindid(id: int, db: Session = Depends(get_db), controller=Depends(IndoorSpaceController)):
    return controller.findByid(db, id)


@router.delete("/indoorspace/id/{id}", dependencies=[Depends(JWTBearerUser())])
def indoorSpaceDelete(id: int, db: Session = Depends(get_db), controller=Depends(IndoorSpaceController)):
    return controller.delete(db, id)

@router.post("/indoorspace/create", dependencies=[Depends(JWTBearerUser())])
def indoorSpaceCreate(request: CreateIndoorSpaceRequest, db: Session = Depends(get_db), controller=Depends(IndoorSpaceController)):
    entity = IndoorSpace(bed_num=request.bed_num,bath_num=request.bath_num,bedroom_num=request.bedroom_num,has_livingroom=request.has_livingroom,total_space=request.total_space,description=request.description,property_type_id=request.property_type_id)
    return controller.create(db, entity)


@router.post("/indoorspace/search", dependencies=[Depends(JWTBearerUser())])
def indoorSpaceSearch(request: SearchIndoorSpaceRequest, db: Session = Depends(get_db), controller=Depends(IndoorSpaceController)):
    return controller.search(db, request)


@router.patch("/indoorspace/patch", dependencies=[Depends(JWTBearerUser())])
def indoorSpacePatch(request: PatchIndoorSpaceRequest, db: Session = Depends(get_db), controller=Depends(IndoorSpaceController)):
    entity = IndoorSpace(id=request.id,bed_num=request.bed_num,bath_num=request.bath_num,bedroom_num=request.bedroom_num,has_livingroom=request.has_livingroom,total_space=request.total_space,description=request.description,property_type_id=request.property_type_id)
    return controller.patch(db, entity)
