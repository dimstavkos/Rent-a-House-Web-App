from pydantic import BaseModel
from datetime import datetime

class PatchPropertyTypeRequest(BaseModel):
    id: int
    property_type_name: str
