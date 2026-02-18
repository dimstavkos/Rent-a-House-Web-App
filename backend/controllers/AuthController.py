from fastapi import HTTPException
from sqlalchemy.orm import Session

from Requests.Role.SearchRequest import SearchRoleRequest
from auth.auth_handler import generateJWT
from controllers.UserController import UserController
from models.Role import Role
from models.User import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthController:

    def register(self, db: Session, entity : User, isHost: bool, isRenter: bool):
        # Check username
        n = db.query(User).filter(User.username.like(entity.username)).count()
        if n > 0:
            raise HTTPException(status_code=401, detail="Username already exists")

        n = db.query(User).filter(User.email.like(entity.email)).count()
        if n > 0:
            raise HTTPException(status_code=401, detail="email already exists")

        if isRenter:
            entity.verified_status = False
        else:
            entity.verified_status = True

        userController = UserController()

        host = db.get(Role, 2)
        renter = db.get(Role, 3)

        if isHost:
            entity.roles.append(host)

        if isRenter:
            entity.roles.append(renter)
            entity.verified_status = 0

        userController.create(db, entity)

        return entity

    def login(self, db: Session, username : str, password : str):
        userController = UserController()
        users =  userController.findByUsername(db, username)

        if (len(users) == 0):
            raise HTTPException(status_code=401, detail="User not found")

        user = users[0]

        if not pwd_context.verify(password, user.password):
            raise HTTPException(status_code=401, detail="Password does not match")

        id = user.id
        roles = []

        for r in user.roles:
            roles.append(r.role_name)

        string_roles = ','.join(roles)

        token = generateJWT(id, string_roles)

        return {
            "id" : id,
            "username" : username,
            "roles": user.roles,
            "tolen": token
        }

        return user

