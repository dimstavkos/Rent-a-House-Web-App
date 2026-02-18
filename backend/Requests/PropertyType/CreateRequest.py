from pydantic import BaseModel
from datetime import datetime

class CreatePropertyTypeRequest(BaseModel):
    property_type_name: str
