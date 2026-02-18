from pydantic import BaseModel
from datetime import datetime


class CreateLocationRequest(BaseModel):
    country: str
    city: str 
    address: str
    latitude: float
    longitude: float

    