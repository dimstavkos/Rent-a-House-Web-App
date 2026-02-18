from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SearchPropertyTypeRequest(BaseModel):
    id: Optional[int] = None
    property_type_name: Optional[str] = None
