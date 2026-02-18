from pydantic import BaseModel, Field
from typing import Optional


class SearchPropertyRuleListRequest(BaseModel):
    id: Optional[int] = None
    smoking_allowed: Optional[bool] = None
    pet_allowed: Optional[bool] = None
    party_allowed: Optional[bool] = None
    min_night_number: Optional[int] = None
    property_id: Optional[int] = None