from typing import List

from pydantic import BaseModel
from datetime import datetime

from Responses.ExportReviewResponse import ExportReviewResponse


class ExportBookingResponse(BaseModel):
    id: int
    start_date: datetime
    end_date: datetime
    total_night_num: int
    total_price: float
    user_id: int
    property_id: int
    user_id: int
    review_id: ExportReviewResponse
    booking_created: datetime
    booking_updated: datetime
    booking_completed: bool
