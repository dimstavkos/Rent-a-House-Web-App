from typing import Optional

from pydantic import BaseModel
from datetime import datetime


class PatchBookingRequest(BaseModel):
    id: int
    start_date: datetime
    end_date: datetime
    total_night_num: int
    total_price: float
    user_id: int
    property_id: int
    review_id: Optional[int]
    booking_created: datetime
    booking_updated: datetime
    booking_completed: bool
    booking_verified: bool