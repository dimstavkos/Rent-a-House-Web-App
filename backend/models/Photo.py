from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database.database import Base

class Photo(Base):
    __tablename__ = "photo"

    id = Column(Integer, primary_key=True, index=True)
    photo = Column(String, index=False)
    property_id = Column(Integer, ForeignKey('property.id'), index=False)
