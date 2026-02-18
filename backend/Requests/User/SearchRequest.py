from typing import Optional

from pydantic import BaseModel


class SearchUserRequest(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None



