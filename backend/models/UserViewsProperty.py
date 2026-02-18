from typing import List

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from database.database import Base

class UserViewsProperty(Base):
    __tablename__ = "user_views_property"

    user_id = Column(Integer, index=True, primary_key=True)
    property_id = Column(Integer, index=True, primary_key=True)
    frequency = Column(Integer, index=False)
