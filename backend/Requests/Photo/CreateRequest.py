from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database.database import Base
from sqlalchemy.orm import Mapped
from pydantic import BaseModel
class CreatePhotoRequest(BaseModel):

    photo: str
    property_id: int
