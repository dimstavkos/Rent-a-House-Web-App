from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class SearchPropertyRequest(BaseModel):
    id: Optional[int] = None
    price: Optional[float] = None  # min_price, max_price
    has_wifi: Optional[bool] = None
    has_airconditioning: Optional[bool] = None
    has_heat: Optional[bool] = None
    has_kitchen: Optional[bool] = None
    has_tv: Optional[bool] = None
    has_parking: Optional[bool] = None
    has_elevator: Optional[bool] = None
    description: Optional[str] = None
    floor: Optional[int] = None
    number_of_guests: Optional[int] = None
    is_available: bool = True
    user_id: Optional[int] = None
    country: Optional[str] = None
    city: Optional[str] = None
    location: Optional[str] = None
    indoor_space_id: Optional[int] = None
    property_created: Optional[datetime] = None
    property_updated: Optional[datetime] = None
    is_flat: Optional[bool] = None
    is_house: Optional[bool] = None
    is_villa: Optional[bool] = None
    is_cabin: Optional[bool] = None
    is_cottage: Optional[bool] = None
    is_manson: Optional[bool] = None
    date_from: Optional[str] = None
    date_to: Optional[str] = None

    # relationship properties:
    property_type_id: Optional[int] = None