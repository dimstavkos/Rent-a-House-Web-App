from fastapi import Depends, APIRouter
from sqlalchemy.sql.functions import now

from Requests.User.CreateRequest import CreateUserRequest
from Requests.User.PatchRequest import PatchUserRequest
from Requests.User.SearchRequest import SearchUserRequest
from auth.auth_bearer_users import JWTBearerUser
from controllers.UserController import UserController
from sqlalchemy.orm import Session

from database.database import SessionLocal, get_db
from models.User import User

router = APIRouter()

@router.get("/user/list", dependencies=[Depends(JWTBearerUser())])
def userList(db: Session = Depends(get_db), controller=Depends(UserController)):
    return controller.list(db)


@router.get("/user/id/{id}", dependencies=[Depends(JWTBearerUser())])
def userFind(id: int, db: Session = Depends(get_db), controller=Depends(UserController)):
    return controller.find(db, id)


@router.delete("/user/id/{id}", dependencies=[Depends(JWTBearerUser())])
def userDelete(id: int, db: Session = Depends(get_db), controller=Depends(UserController)):
    return controller.delete(db, id)



 # username: str
 #    password: str
 #    name: str
 #    lastname: str
 #    email: str
 #    phone: str
 #    photo: str

@router.post("/user/create", dependencies=[Depends(JWTBearerUser())])
def userCreate(request: CreateUserRequest, db: Session = Depends(get_db), controller=Depends(UserController)):
    entity = User(username=request.username, password=request.password, name=request.name, lastname=request.lastname, email=request.email, phone=request.phone, photo=request.photo, verified_status=False, user_created = now())
    return controller.create(db, entity)


@router.post("/user/search", dependencies=[Depends(JWTBearerUser())])
def userSearch(request: SearchUserRequest, db: Session = Depends(get_db), controller=Depends(UserController)):
    return controller.search(db, request)


@router.patch("/user/patch", dependencies=[Depends(JWTBearerUser())])
def userPatch(request: PatchUserRequest, db: Session = Depends(get_db), controller=Depends(UserController)):
    entity = User(id=request.id, username=request.username, password=request.password, name=request.name, lastname=request.lastname, email=request.email, phone=request.phone, photo=request.photo, verified_status=request.verified_status)
    return controller.patch(db, entity)
