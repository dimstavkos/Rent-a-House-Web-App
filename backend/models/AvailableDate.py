from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric, DateTime
from database.database import Base


class AvailableDate(Base):
    __tablename__ = "available_date"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(DateTime, index=False)
    end_date = Column(DateTime, index=False)
    property_id = Column(DateTime, ForeignKey('property.id'), index=False)
