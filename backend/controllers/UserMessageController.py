from sqlalchemy.orm import Session

from Requests.UserMessage.SearchRequest import SearchUserMessageRequest
from models.UserMessage import UserMessage
from sqlalchemy import desc


class UserMessageController:
    def list(self, db: Session):
        return db.query(UserMessage).all()

    def findByid(self, db: Session, id: int):
        return db.query(UserMessage).get(id)

    def findByUserid(self,db:Session, userid):
      return  db.query(UserMessage).filter_by(user_id=userid).order_by(desc(UserMessage.message_created)).all()

    def findBySendid(self,db:Session, userid):
      return  db.query(UserMessage).filter_by(send_to_id=userid).order_by(desc(UserMessage.message_created)).all()



    def delete(self, db: Session, id: int):
        db.query(UserMessage).filter_by(id=id).delete()
        db.commit()
        return "success"

    def create(self, db: Session, entity: UserMessage):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def search(self, db: Session, request: SearchUserMessageRequest):
        query = db.query(UserMessage)

        if request.id != None:
            query = query.filter_by(id=request.id)

        if request.text != None:
            query = query.filter(UserMessage.text.like('%' + request.text + '%'))

        if request.send_to_id != None:
            query = query.filter_by(send_to_id=request.send_to_id)

        if request.user_id != None:
            query = query.filter_by(user_id=request.user_id)

        if request.message_created != None:
            query = query.filter_by(message_created=request.message_created)

        return query.all()

    def patch(self, db: Session, newEntity: UserMessage):
        existingEntity = db.query(UserMessage).get(newEntity.id)

        existingEntity.text = newEntity.text
        existingEntity.send_to_id = newEntity.send_to_id
        existingEntity.user_id = newEntity.user_id
        existingEntity.message_created = newEntity.message_created

        db.commit()
        db.refresh(existingEntity)
        return existingEntity
