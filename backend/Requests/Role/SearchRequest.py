from typing import Optional

from pydantic import BaseModel


class SearchRoleRequest(BaseModel):
    id: Optional[int] = None
    role_name: Optional[str] = None