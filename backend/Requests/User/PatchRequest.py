from pydantic import BaseModel
from typing import Optional

class PatchUserRequest(BaseModel):
    id: int
    username: Optional[str] = None
    password: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    photo: Optional[str] = None
    verified_status: Optional[bool] = None