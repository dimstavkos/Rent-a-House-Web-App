from pydantic import BaseModel
from datetime import datetime

class CreateUserMessageRequest(BaseModel):
    text: str
    send_to_id: int
    user_id: int