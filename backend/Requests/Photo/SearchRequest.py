from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel
from typing import Optional

class SearchPhotoRequest(BaseModel):

    id: Optional[int] = None
    photo: Optional[str] = None
    property_id: Optional[int] = None