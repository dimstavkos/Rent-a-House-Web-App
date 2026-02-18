from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from database.database import Base
from sqlalchemy.orm import Mapped, relationship

from models.UserHasReview import UserHasReview


class ReviewView(Base):
    __tablename__ = "review_view"

    review_id = Column(Integer, primary_key=True)
    reviewer_id = Column(Integer, index=False)
    reviewee_id = Column(String, index=False)
    property_id = Column(Integer, ForeignKey('property.id'), index=False)
    rating = Column(Integer, index=False)

