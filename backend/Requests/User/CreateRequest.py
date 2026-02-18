from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    username: str
    password: str
    name: str
    lastname: str
    email: str
    phone: str
    photo: str