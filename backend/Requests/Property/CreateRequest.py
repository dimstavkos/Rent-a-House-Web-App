from pydantic import BaseModel
from datetime import datetime


class CreatePropertyRequest(BaseModel):
    price: float
    has_wifi: bool
    has_airconditioning: bool
    has_heat: bool
    has_kitchen: bool
    has_tv: bool
    has_parking: bool
    has_elevator: bool
    description: str
    floor: int
    number_of_guests: int
    is_available: bool
    user_id: int
    location_id: int
    indoor_space_id: int