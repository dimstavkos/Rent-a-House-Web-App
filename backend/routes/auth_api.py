from fastapi import Depends, APIRouter
from sqlalchemy.sql.functions import now

from Requests.auth.LoginRequest import LoginRequest
from Requests.auth.RegisterRequest import RegisterRequest
from controllers.AuthController import AuthController
from sqlalchemy.orm import Session

from database.database import SessionLocal, get_db
from models.User import User

router = APIRouter()

@router.post("/auth/register")
async def create_user(request: RegisterRequest, db: Session = Depends(get_db), controller=Depends(AuthController)):
    entity = User(username=request.username, password=request.password, name=request.name, lastname=request.lastname,
                  email=request.email, phone=request.phone, photo=request.photo, verified_status=False,
                  user_created=now())

    controller.register(db, entity, request.host, request.renter)

    return entity
    # return signJWT(user.email)


@router.post("/auth/login")
async def user_login(request: LoginRequest, db: Session = Depends(get_db), controller=Depends(AuthController)):
    username = request.username
    password = request.password

    return controller.login(db, username, password)



# def check_user(data: UserLoginSchema):
# @app.post("/auth/login")
# async def user_login(user: UserLoginSchema = Body(...)):
#
#     for user in users:
#         if user.email == data.email and user.password == data.password:
#             return True
#     return False
#
#     if check_user(user):
#         return signJWT(user.email)
#     return {
#         "error": "Wrong login details!"
#     }