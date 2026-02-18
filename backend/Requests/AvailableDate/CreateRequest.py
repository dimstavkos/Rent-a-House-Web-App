from pydantic import BaseModel
from datetime import datetime


class CreateAvailableDateRequest(BaseModel):

    start_date: datetime
    end_date: datetime
    property_id: int
