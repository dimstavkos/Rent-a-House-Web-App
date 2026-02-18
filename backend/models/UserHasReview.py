from typing import List

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from database.database import Base

class UserHasReview(Base):
    __tablename__ = "user_has_review"

    review_id = Column(Integer, index=False)
    reviewer_id = Column(Integer, index=True, primary_key=True)
    reviewee_id = Column(Integer, index=True, primary_key=True)
