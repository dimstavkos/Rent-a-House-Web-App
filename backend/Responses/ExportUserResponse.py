from typing import List

from pydantic import BaseModel

from Responses.ExportRoleResponse import ExportRoleResponse


class ExportUserResponse(BaseModel):
    id : int
    username: str
    name: str
    lastname: str
    email: str
    phone: str
    photo: str
    roles: List[ExportRoleResponse]

