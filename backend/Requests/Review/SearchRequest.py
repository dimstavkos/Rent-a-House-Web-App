from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SearchReviewRequest(BaseModel):
    id: Optional[int] = None
    rating: Optional[int] = None
    comment: Optional[str] = None