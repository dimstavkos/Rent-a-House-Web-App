from pydantic import BaseModel
from datetime import datetime

class PatchUserMessageRequest(BaseModel):
    id: int
    text: str
    send_to_id: int
    user_id: int
    message_created: datetime