from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric, DateTime
from sqlalchemy.orm import relationship

from database.database import Base


class Booking(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(DateTime, index=False)
    end_date = Column(DateTime, index=False)
    total_night_num = Column(Integer, index=False)
    total_price = Column(Numeric(precision=10, scale=2), index=False)
    user_id = Column(Integer, index=False)
    property_id = Column(Integer, ForeignKey('property.id'), index=False)
    review_id = Column(Integer, ForeignKey('review.id'), index=False, nullable=True)
    booking_created = Column(DateTime, index=False)
    booking_updated = Column(DateTime, index=False)
    booking_completed = Column(Boolean, index=False)
    booking_verified= Column(Boolean, index=False)


    review = relationship("Review")

# relationships

# user_id = Column(Integer, ForeignKey("user.id"))
# user = relationship("user", back_populates="bookings")

# booking_id = Column(Integer, ForeignKey("booking.id"))
# booking = relationship("booking", back_populates="bookings")

# review_id = Column(Integer, ForeignKey("review.id"))
# review = relationship("review", back_populates="bookings")

