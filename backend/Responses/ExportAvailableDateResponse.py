from pydantic import BaseModel
from datetime import datetime
from typing import List
class ExportAvailableDateResponse(BaseModel):
    id: int
    start_date: datetime
    end_date: datetime
    property_id: int