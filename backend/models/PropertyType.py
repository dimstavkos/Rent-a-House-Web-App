from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database.database import Base

class PropertyType(Base):
    __tablename__ = "property_type"

    id = Column(Integer, primary_key=True, index=True)
    property_type_name = Column(String, index=False)