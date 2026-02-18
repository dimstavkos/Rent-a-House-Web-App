from fastapi import Depends, APIRouter
from sqlalchemy.sql.functions import now

from Requests.UserMessage.CreateRequest import CreateUserMessageRequest
from Requests.UserMessage.PatchRequest import PatchUserMessageRequest
from Requests.UserMessage.SearchRequest import SearchUserMessageRequest
from auth.auth_bearer_users import JWTBearerUser
from controllers.UserMessageController import UserMessageController

from sqlalchemy.orm import Session

from database.database import SessionLocal, get_db
from models.UserMessage import UserMessage

router = APIRouter()

@router.get("/usermessage/list", dependencies=[Depends(JWTBearerUser())])
def userMessageList(db: Session = Depends(get_db), controller=Depends(UserMessageController)):
    return controller.list(db)


@router.get("/usermessage/id/{id}", dependencies=[Depends(JWTBearerUser())])
def userMessageFindid(id: int, db: Session = Depends(get_db), controller=Depends(UserMessageController)):
    return controller.findByid(db, id)

@router.get("/usermessage/outbox/{id}", dependencies=[Depends(JWTBearerUser())])
def userMessageFindUserid(id: int, db: Session = Depends(get_db), controller=Depends(UserMessageController)):
    return controller.findByUserid(db, id)

@router.get("/usermessage/inbox/{id}", dependencies=[Depends(JWTBearerUser())])
def userMessageFindSendid(id: int, db: Session = Depends(get_db), controller=Depends(UserMessageController)):
    return controller.findBySendid(db, id)


@router.delete("/usermessage/id/{id}", dependencies=[Depends(JWTBearerUser())])
def userMessageDelete(id: int, db: Session = Depends(get_db), controller=Depends(UserMessageController)):
    return controller.delete(db, id)

@router.post("/usermessage/create", dependencies=[Depends(JWTBearerUser())])
def userMessageCreate(request: CreateUserMessageRequest, db: Session = Depends(get_db), controller=Depends(UserMessageController)):
    entity = UserMessage(text=request.text,send_to_id=request.send_to_id,user_id=request.user_id,message_created=now())
    return controller.create(db, entity)


@router.post("/usermessage/search", dependencies=[Depends(JWTBearerUser())])
def userMessageSearch(request: SearchUserMessageRequest, db: Session = Depends(get_db), controller=Depends(UserMessageController)):
    return controller.search(db, request)


@router.patch("/usermessage/patch", dependencies=[Depends(JWTBearerUser())])
def userMessagePatch(request: PatchUserMessageRequest, db: Session = Depends(get_db), controller=Depends(UserMessageController)):
    entity = UserMessage(id=request.id,text=request.text,send_to_id=request.send_to_id,user_id=request.user_id,message_created=request.message_created)
    return controller.patch(db, entity)
