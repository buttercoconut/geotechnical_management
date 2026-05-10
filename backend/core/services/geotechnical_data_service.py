# services/geotechnical_data_service.py
from sqlalchemy.orm import Session
from ..api.models.geotechnical_data import GeotechnicalData
from ..api.schemas.geotechnical_data import GeotechnicalDataCreate

class GeotechnicalDataService:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: GeotechnicalDataCreate) -> GeotechnicalData:
        db_obj = GeotechnicalData(**data.dict())
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def get(self, id: int) -> GeotechnicalData | None:
        return self.db.query(GeotechnicalData).filter(GeotechnicalData.id == id).first()

    def list(self, skip: int = 0, limit: int = 100):
        return self.db.query(GeotechnicalData).offset(skip).limit(limit).all()
