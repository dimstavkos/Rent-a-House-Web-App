from pydantic import BaseModel
class ExportReviewResponse(BaseModel):
    id: int
    rating: int
    comment: str
    reviewer_id: int
    reviewee_id: int