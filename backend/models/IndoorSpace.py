from typing import List

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric, DateTime
from sqlalchemy.orm import relationship, Mapped

from database.database import Base
from models.PropertyType import PropertyType


class IndoorSpace(Base):
    __tablename__ = "indoor_space"

    id = Column(Integer, primary_key=True, index=True)
    bed_num = Column(Integer, index=False)
    bath_num = Column(Integer, index=False)
    bedroom_num = Column(Integer, index=False)
    has_livingroom = Column(Boolean, index=False)
    total_space = Column(Integer, index=False)
    description = Column(String, index=False)
    property_type_id = Column(Integer, ForeignKey("property_type.id"))
    property_type : Mapped[List[PropertyType]] = relationship(PropertyType)

