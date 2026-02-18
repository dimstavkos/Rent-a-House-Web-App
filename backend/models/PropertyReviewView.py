from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, Float
from database.database import Base
from sqlalchemy.orm import Mapped, relationship

from models.UserHasReview import UserHasReview


class PropertyRatingView(Base):
    __tablename__ = "property_rating_view"

    id = Column(Integer, ForeignKey('property.id'), primary_key=True, index=True, autoincrement=True)
    rating = Column(Float, index=False)
    total_ratings = Column(Integer, index=False)
    stars = Column(Integer, index=False)

