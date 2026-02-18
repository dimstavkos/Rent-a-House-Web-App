from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from database.database import Base

class Location(Base):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=False)
    city = Column(String, index=False)
    address = Column(String, index=False)
    latitude = Column(Float, index=False)
    longitude = Column(Float, index=False)
