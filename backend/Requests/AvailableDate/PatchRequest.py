from pydantic import BaseModel
from datetime import datetime


class PatchAvailableDateRequest(BaseModel):

    id: int
    start_date: datetime
    end_date: datetime
    property_id: int