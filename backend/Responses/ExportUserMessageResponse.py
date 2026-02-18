from pydantic import BaseModel
from datetime import datetime
from ExportUserResponse import ExportUserResponse
from typing import List
class ExportUserMessageResponse(BaseModel):
    id: int
    text: str
    send_to_id: List[ExportUserResponse]
    user_id: List[ExportUserResponse]
    message_created: datetime
