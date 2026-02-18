from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from database.database import Base
class UserMessage(Base):
    __tablename__ = "user_message"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=False)
    send_to_id = Column(Integer, index=False)
    user_id = Column(Integer, index=False)
    message_created = Column(DateTime, index=False)
