from fastapi import Depends, APIRouter
from sqlalchemy.sql.functions import now

from Requests.Photo.CreateRequest import CreatePhotoRequest
from Requests.Photo.PatchRequest import PatchPhotoRequest
from Requests.Photo.SearchRequest import SearchPhotoRequest
from auth.auth_bearer_users import JWTBearerUser
from controllers.PhotoController import PhotoController

from sqlalchemy.orm import Session

from database.database import SessionLocal, get_db
from models.Photo import Photo

router = APIRouter()

@router.get("/photo/list", dependencies=[Depends(JWTBearerUser())])
def photoList(db: Session = Depends(get_db), controller=Depends(PhotoController)):
    return controller.list(db)


@router.get("/photo/id/{id}", dependencies=[Depends(JWTBearerUser())])
def photoFindid(id: int, db: Session = Depends(get_db), controller=Depends(PhotoController)):
    return controller.findByid(db, id)


@router.delete("/photo/id/{id}", dependencies=[Depends(JWTBearerUser())])
def photoDelete(id: int, db: Session = Depends(get_db), controller=Depends(PhotoController)):
    return controller.delete(db, id)

@router.post("/photo/create", dependencies=[Depends(JWTBearerUser())])
def photoCreate(request: CreatePhotoRequest, db: Session = Depends(get_db), controller=Depends(PhotoController)):
    entity = Photo(photo=request.photo, property_id=request.property_id)
    return controller.create(db, entity)


@router.post("/photo/search", dependencies=[Depends(JWTBearerUser())])
def photoSearch(request: SearchPhotoRequest, db: Session = Depends(get_db), controller=Depends(PhotoController)):
    return controller.search(db, request)


@router.patch("/photo/patch", dependencies=[Depends(JWTBearerUser())])
def photoPatch(request: PatchPhotoRequest, db: Session = Depends(get_db), controller=Depends(PhotoController)):
    entity = Photo(id=request.id,photo=request.photo, property_id=request.property_id)
    return controller.patch(db, entity)
