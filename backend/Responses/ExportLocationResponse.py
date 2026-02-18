from pydantic import BaseModel
from typing import List
class ExportLocationResponse(BaseModel):
    id: int
    country: str
    city: str
    address: str
