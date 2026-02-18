from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric, DateTime
from database.database import Base


class PropertyRuleList(Base):
    __tablename__ = "property_rule_list"

    id = Column(Integer, primary_key=True, index=True)
    smoking_allowed = Column(Boolean, index=False)
    pet_allowed = Column(Boolean, index=False)
    party_allowed = Column(Boolean, index=False)
    min_night_number = Column(Integer, index=False)
    property_id = Column(Integer, ForeignKey('property.id'), index=False)
