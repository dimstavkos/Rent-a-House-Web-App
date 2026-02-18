from pydantic import BaseModel
from datetime import datetime
from Responses.ExportUserResponse import ExportUserResponse
from Responses.ExportLocationResponse import ExportLocationResponse
from Responses.ExportIndoorSpaceResponse import ExportIndoorSpaceResponse
from typing import List
class ExportPropertyResponse(BaseModel):
    id: int
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
    user_id: List[ExportUserResponse]
    location_id:List[ExportLocationResponse]
    indoor_space_id:List[ExportIndoorSpaceResponse]
