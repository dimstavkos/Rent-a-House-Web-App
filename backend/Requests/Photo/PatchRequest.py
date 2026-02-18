from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel
class PatchPhotoRequest(BaseModel):

    id: int
    photo: str
    property_id: int