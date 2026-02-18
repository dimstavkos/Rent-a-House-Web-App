from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from database.database import Base
from sqlalchemy.orm import Mapped, relationship

from models.UserHasReview import UserHasReview


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, ForeignKey('user_has_review.review_id'), primary_key=True, index=True, autoincrement=True)
    rating = Column(Integer, index=False)
    comment = Column(String, index=False)

    details = relationship("UserHasReview")

