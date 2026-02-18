import xmltodict
from dict2xml import dict2xml
from fastapi import Depends, APIRouter, Response, Request

from simplexml import dumps

from Requests.Role.CreateRequest import CreateRoleRequest
from Requests.Role.PatchRequest import PatchRoleRequest
from Requests.Role.SearchRequest import SearchRoleRequest
from controllers import ExportController
from controllers.RoleController import RoleController
from sqlalchemy.orm import Session

from database.database import SessionLocal
from models.Role import Role

router = APIRouter()

from controllers.ExportController import ExportController
from sqlalchemy.orm import Session

from auth.auth_bearer_admin import JWTBearerAdmin
from database.database import SessionLocal, get_db

@router.get("/export/users", dependencies=[Depends(JWTBearerAdmin())])
def exportUsers(request: Request, db: Session = Depends(get_db), controller=Depends(ExportController)):
    content_type = request.headers['Accept']

    if content_type == 'application/xml':
        data = controller.exportUsers(db, True)
        xml_string = dict2xml(data, wrap ='dataset')
        return Response(content=xml_string, media_type="application/xml")
    else:
        return controller.exportUsers(db, False)


@router.get("/export/properties", dependencies=[Depends(JWTBearerAdmin())])
def exportProperties(request: Request, db: Session = Depends(get_db), controller=Depends(ExportController)):
    content_type = request.headers['Accept']

    if content_type == 'application/xml':
        data = controller.exportProperties(db, True)
        xml_string = dict2xml(data, wrap ='dataset')
        return Response(content=xml_string, media_type="application/xml")
    else:
        return controller.exportProperties(db, False)



@router.get("/export/locations", dependencies=[Depends(JWTBearerAdmin())])
def exportLocaions(request: Request, db: Session = Depends(get_db), controller=Depends(ExportController)):
    content_type = request.headers['Accept']

    if content_type == 'application/xml':
        data = controller.exportLocations(db, True)
        xml_string = dict2xml(data, wrap ='dataset')
        return Response(content=xml_string, media_type="application/xml")
    else:
        return controller.exportLocations(db, False)



@router.get("/export/bookings", dependencies=[Depends(JWTBearerAdmin())])
def exportUsers(request: Request, db: Session = Depends(get_db), controller=Depends(ExportController)):
    content_type = request.headers['Accept']

    if content_type == 'application/xml':
        data = controller.exportUsers(db, True)
        xml_string = dict2xml(data, wrap ='dataset')
        return Response(content=xml_string, media_type="application/xml")
    else:
        return controller.exportBookings(db, False)


