from pydantic import BaseModel
from datetime import datetime

class PatchReviewRequest(BaseModel):
    id: int
    rating: int
    comment: str