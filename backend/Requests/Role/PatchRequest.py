from pydantic import BaseModel


class PatchRoleRequest(BaseModel):
    id: int
    role_name: str