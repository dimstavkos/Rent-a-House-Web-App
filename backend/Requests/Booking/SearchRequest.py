from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class SearchBookingRequest(BaseModel):
    id: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    total_night_num: Optional[int] = None
    total_price: Optional[float] = None
    user_id: Optional[int] = None
    property_id: Optional[int] = None
    review_id: Optional[int] = None
    booking_created: Optional[datetime] = None
    booking_updated: Optional[datetime] = None
    booking_completed: Optional[bool] = None
    booking_verified: Optional[bool] = None