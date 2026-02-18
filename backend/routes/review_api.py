from fastapi import Depends, APIRouter
from sqlalchemy.sql.functions import now

from Requests.Review.CreateRequest import CreateReviewRequest
from Requests.Review.PatchRequest import PatchReviewRequest
from Requests.Review.SearchRequest import SearchReviewRequest
from auth.auth_bearer_users import JWTBearerUser
from controllers.ReviewController import ReviewController

from sqlalchemy.orm import Session

from database.database import SessionLocal, get_db
from models.Review import Review

router = APIRouter()

@router.get("/review/list", dependencies=[Depends(JWTBearerUser())])
def reviewList(db: Session = Depends(get_db), controller=Depends(ReviewController)):
    return controller.list(db)


@router.get("/review/id/{id}", dependencies=[Depends(JWTBearerUser())])
def reviewFindid(id: int, db: Session = Depends(get_db), controller=Depends(ReviewController)):
    return controller.findByid(db, id)


@router.delete("/review/id/{id}", dependencies=[Depends(JWTBearerUser())])
def reviewDelete(id: int, db: Session = Depends(get_db), controller=Depends(ReviewController)):
    return controller.delete(db, id)

@router.post("/review/create", dependencies=[Depends(JWTBearerUser())])
def reviewCreate(request: CreateReviewRequest, db: Session = Depends(get_db), controller=Depends(ReviewController)):
    entity = Review(rating=request.rating, comment=request.comment)
    return controller.create(db, entity)


@router.post("/review/search", dependencies=[Depends(JWTBearerUser())])
def reviewSearch(request: SearchReviewRequest, db: Session = Depends(get_db), controller=Depends(ReviewController)):
    return controller.search(db, request)


@router.patch("/review/patch", dependencies=[Depends(JWTBearerUser())])
def reviewPatch(request: PatchReviewRequest, db: Session = Depends(get_db), controller=Depends(ReviewController)):
    entity = Review(id=request.id, rating=request.rating, comment=request.comment)
    return controller.patch(db, entity)
