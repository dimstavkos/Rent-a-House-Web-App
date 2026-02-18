from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SearchAvailableDateRequest(BaseModel):

    id: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    property_id: Optional[int] = None