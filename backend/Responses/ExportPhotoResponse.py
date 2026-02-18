from pydantic import BaseModel
from ExportPropertyResponse import ExportPropertyResponse
from typing import List
class ExportPhotoResponse(BaseModel):
    id: int
    photo: str
    property_id: List[ExportPropertyResponse]
