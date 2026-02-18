from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SearchUserMessageRequest(BaseModel):
    id: Optional[int] = None
    text: Optional[str] = None
    send_to_id: Optional[int] = None
    user_id: Optional[int] = None
    message_created: Optional[datetime] = None