from pydantic import BaseModel, Field
from typing import Optional


class SearchIndoorSpaceRequest(BaseModel):
    id: Optional[int] = None
    bed_num: Optional[int] = None
    bedroom_num: Optional[int] = None
    has_livingroom: Optional[bool] = None
    total_space: Optional[int] = None
    description: Optional[str] = None
    property_type_id: Optional[int] = None