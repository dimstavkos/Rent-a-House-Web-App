from pydantic import BaseModel


class PatchIndoorSpaceRequest(BaseModel):
    id: int
    bed_num: int
    bath_num: int
    bedroom_num: int
    has_livingroom: bool
    total_space: int
    description: str
    property_type_id: int