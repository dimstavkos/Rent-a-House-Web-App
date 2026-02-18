from pydantic import BaseModel


class ExportPropertyTypeResponse(BaseModel):
    id: int
    property_type_name: str
