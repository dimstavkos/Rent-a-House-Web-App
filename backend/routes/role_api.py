from fastapi import Depends, APIRouter

from Requests.Role.CreateRequest import CreateRoleRequest
from Requests.Role.PatchRequest import PatchRoleRequest
from Requests.Role.SearchRequest import SearchRoleRequest
from auth.auth_bearer_users import JWTBearerUser
from controllers.RoleController import RoleController
from sqlalchemy.orm import Session

from database.database import SessionLocal, get_db
from models.Role import Role

router = APIRouter()

@router.get("/role/list", dependencies=[Depends(JWTBearerUser())])
def roleList(db: Session = Depends(get_db), controller=Depends(RoleController)):
    return controller.list(db)


@router.get("/role/id/{id}", dependencies=[Depends(JWTBearerUser())])
def roleFind(id: int, db: Session = Depends(get_db), controller=Depends(RoleController)):
    return controller.find(db, id)


@router.delete("/role/id/{id}", dependencies=[Depends(JWTBearerUser())])
def roleDelete(id: int, db: Session = Depends(get_db), controller=Depends(RoleController)):
    return controller.delete(db, id)


@router.post("/role/create", dependencies=[Depends(JWTBearerUser())])
def roleCreate(request: CreateRoleRequest, db: Session = Depends(get_db), controller=Depends(RoleController)):
    role = Role(role_name=request.role_name)
    return controller.create(db, role)


@router.post("/role/search", dependencies=[Depends(JWTBearerUser())])
def roleSearch(request: SearchRoleRequest, db: Session = Depends(get_db), controller=Depends(RoleController)):
    return controller.search(db, request)


@router.patch("/role/patch", dependencies=[Depends(JWTBearerUser())])
def rolePatch(request: PatchRoleRequest, db: Session = Depends(get_db), controller=Depends(RoleController)):
    role = Role(id=request.id, role_name=request.role_name)
    return controller.patch(db, role)
