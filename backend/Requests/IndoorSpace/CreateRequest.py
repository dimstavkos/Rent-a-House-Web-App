from pydantic import BaseModel
from datetime import datetime


class CreateIndoorSpaceRequest(BaseModel):

    bed_num: int
    bath_num: int
    bedroom_num: int
    has_livingroom: bool
    total_space: int
    description: str
    property_type_id: int