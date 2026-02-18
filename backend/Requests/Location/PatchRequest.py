from pydantic import BaseModel


class PatchLocationRequest(BaseModel):
    id: int
    country: str
    city: str 
    address: str
    latitude: float
    longitude: float
