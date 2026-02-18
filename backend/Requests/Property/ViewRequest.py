from pydantic import BaseModel


class ViewPropertyRequest(BaseModel):
    user_id: int
    property_id: int