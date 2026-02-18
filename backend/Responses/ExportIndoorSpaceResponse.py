from pydantic import BaseModel
from Responses.ExportPropertyTypeResponse import ExportPropertyTypeResponse
from typing import List
class ExportIndoorSpaceResponse(BaseModel):
    id: int
    bed_num: int
    bath_num: int
    bedroom_num: int
    has_livingroom: bool
    total_space: int
    description: str
    property_type_id: List[ExportPropertyTypeResponse]
