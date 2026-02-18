from fastapi import Depends, APIRouter

from Requests.Role.CreateRequest import CreateRoleRequest
from Requests.Role.PatchRequest import PatchRoleRequest
from Requests.Role.SearchRequest import SearchRoleRequest
from controllers.RoleController import RoleController
from sqlalchemy.orm import Session

from database.database import SessionLocal
from models.Role import Role

router = APIRouter()



