from pydantic import BaseModel, Field
from typing import Optional

class SearchLocationRequest(BaseModel):
    id: Optional[int] = None
    country: Optional[str] = None
    city: Optional[str] = None 
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
