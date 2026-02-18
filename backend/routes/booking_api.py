from fastapi import Depends, APIRouter
from sqlalchemy.sql.functions import now

from Requests.Booking.CreateRequest import CreateBookingRequest
from Requests.Booking.PatchRequest import PatchBookingRequest
from Requests.Booking.SearchRequest import SearchBookingRequest
from auth.auth_bearer_users import JWTBearerUser
from controllers.BookingController import BookingController

from sqlalchemy.orm import Session

from database.database import SessionLocal, get_db
from models.Booking import Booking
from models.Property import Property

router = APIRouter()

@router.get("/booking/list", dependencies=[Depends(JWTBearerUser())])
def bookingList(db: Session = Depends(get_db), controller=Depends(BookingController)):
    return controller.list(db)


@router.get("/booking/id/{id}", dependencies=[Depends(JWTBearerUser())])
def bookingFindid(id: int, db: Session = Depends(get_db), controller=Depends(BookingController)):
    return controller.findByid(db, id)

@router.get("/booking/userid/{id}", dependencies=[Depends(JWTBearerUser())])
def bookingFindUserid(id: int, db: Session = Depends(get_db), controller=Depends(BookingController)):
    return controller.findByUserid(db, id)


@router.get("/booking/propertyid/{id}", dependencies=[Depends(JWTBearerUser())])
def bookingBypropertyid(id: int, db: Session = Depends(get_db), controller=Depends(BookingController)):
    return controller.findByProperty(db, id)


@router.delete("/booking/id/{id}", dependencies=[Depends(JWTBearerUser())])
def bookingDelete(id: int, db: Session = Depends(get_db), controller=Depends(BookingController)):
    return controller.delete(db, id)

@router.post("/booking/create", dependencies=[Depends(JWTBearerUser())])
def bookingCreate(request: CreateBookingRequest, db: Session = Depends(get_db), controller=Depends(BookingController)):
    d1 = request.start_date
    d2 = request.end_date

    print(d1)
    delta = d2 - d1
    days = delta.days + 1

    if days < 0:
        days = 1

    id = request.property_id

    p = db.query(Property).get(id)

    total_price = int(days)*p.price

    entity = Booking(start_date=request.start_date,end_date=request.end_date,total_night_num=days,total_price=total_price,user_id=request.user_id,property_id=request.property_id,booking_created=now(),booking_updated=now(),booking_completed=False, booking_verified=False)
    return controller.create(db, entity)


@router.post("/booking/search", dependencies=[Depends(JWTBearerUser())])
def bookingSearch(request: SearchBookingRequest, db: Session = Depends(get_db), controller=Depends(BookingController)):
    return controller.search(db, request)


@router.patch("/booking/patch", dependencies=[Depends(JWTBearerUser())])
def bookingPatch(request: PatchBookingRequest, db: Session = Depends(get_db), controller=Depends(BookingController)):
    entity = Booking(id=request.id,start_date=request.start_date,end_date=request.end_date,total_night_num=request.total_night_num,total_price=request.total_price,user_id=request.user_id,property_id=request.property_id,review_id=request.review_id,booking_created=request.booking_created,booking_updated=now(),booking_completed=request.booking_completed,booking_verified=request.booking_verified)
    return controller.patch(db, entity)