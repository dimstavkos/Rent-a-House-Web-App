from pydantic import BaseModel


class ExportRoleResponse(BaseModel):
    id : int
    role_name: str

