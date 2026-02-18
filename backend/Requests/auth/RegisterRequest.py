from pydantic import BaseModel, constr


class RegisterRequest(BaseModel):
    username: constr(min_length=3)
    password: constr(min_length=3)
    name: constr(min_length=3)
    lastname: constr(min_length=3)
    email: constr(min_length=3)
    phone: constr(min_length=3)
    photo: constr(min_length=3)

    host: bool
    renter: bool

