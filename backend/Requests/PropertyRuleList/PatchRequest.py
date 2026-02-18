from pydantic import BaseModel


class PatchPropertyRuleListRequest(BaseModel):
    id: int
    smoking_allowed: bool
    pet_allowed: bool
    party_allowed: bool
    min_night_number: int
    property_id: int