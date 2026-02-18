from pydantic import BaseModel
from datetime import date


class CreateBookingRequest(BaseModel):
    start_date: date
    end_date: date
    user_id: int
    property_id: int