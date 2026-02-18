from typing import List

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, relationship

from database.database import Base
from models.AvailableDate import AvailableDate
from models.Booking import Booking
from models.IndoorSpace import IndoorSpace
from models.Location import Location
from models.Photo import Photo
from models.PropertyReviewView import PropertyRatingView
from models.PropertyRuleList import PropertyRuleList
from models.User import User


class Property(Base):
    __tablename__ = "property"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Numeric(precision=10, scale=2), index=False)
    has_wifi = Column(Boolean, index=False)
    has_airconditioning = Column(Boolean, index=False)
    has_heat = Column(Boolean, index=False)
    has_kitchen = Column(Boolean, index=False)
    has_tv = Column(Boolean, index=False)
    has_parking = Column(Boolean, index=False)
    has_elevator = Column(Boolean, index=False)
    description = Column(String, index=False)
    floor = Column(Integer, index=False)
    number_of_guests = Column(Integer, index=False)
    is_available = Column(Integer, index=False)
    user_id = Column(Integer, ForeignKey('user.id'), index=False)
    location_id = Column(Integer, ForeignKey('location.id'), index=False)
    indoor_space_id = Column(Integer, ForeignKey('indoor_space.id'), index=False)
    property_created = Column(DateTime, index=False)
    property_updated = Column(DateTime, index=False)
    # relations:
    location: Mapped[List[Location]] = relationship(Location)
    indoorspace: Mapped[List[IndoorSpace]] = relationship(IndoorSpace)

    owner: Mapped[User] = relationship("User")
    photos: Mapped[List[Photo]] = relationship("Photo", backref="property")
    rules: Mapped[List[PropertyRuleList]] = relationship("PropertyRuleList", backref="property")
    availableDates: Mapped[List[AvailableDate]] = relationship("AvailableDate", backref="property")
    review_score: Mapped[PropertyRatingView] = relationship(PropertyRatingView)
    booking: Mapped[List[Booking]] = relationship(Booking, backref="property")


# relationships

# user_id = Column(Integer, ForeignKey("user.id"))
# user = relationship("user", back_populates="properties")

# location_id = Column(Integer, ForeignKey("location.id"))
# location = relationship("location", back_populates="properties")

# indoor_space_id = Column(Integer, ForeignKey("indoor_space.id"))
# indoor_space = relationship("indoor_space", back_populates="properties")


