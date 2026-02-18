from pydantic import BaseModel
from datetime import datetime

class CreateReviewRequest(BaseModel):

    rating: int
    comment: str
