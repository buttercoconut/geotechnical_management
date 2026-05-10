# schemas/geotechnical_data.py
from pydantic import BaseModel

class GeotechnicalDataBase(BaseModel):
    site_id: int
    depth: float
    n_value: float
    location: str
    description: str | None = None

class GeotechnicalDataCreate(GeotechnicalDataBase):
    pass

class GeotechnicalData(GeotechnicalDataBase):
    id: int

    class Config:
        orm_mode = True
