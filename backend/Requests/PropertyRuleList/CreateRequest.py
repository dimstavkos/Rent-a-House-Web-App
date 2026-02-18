from pydantic import BaseModel
from datetime import datetime


class CreatePropertyRuleListRequest(BaseModel):
    smoking_allowed: bool
    pet_allowed: bool
    party_allowed: bool
    min_night_number: int
    property_id: int
