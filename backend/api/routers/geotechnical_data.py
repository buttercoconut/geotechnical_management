# routers/geotechnical_data.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..services.geotechnical_data_service import GeotechnicalDataService
from ..schemas.geotechnical_data import GeotechnicalDataCreate, GeotechnicalData

router = APIRouter(prefix="/geotechnical", tags=["geotechnical"])

@router.post("/data", response_model=GeotechnicalData)
def create_data(data: GeotechnicalDataCreate, db: Session = Depends(get_db)):
    service = GeotechnicalDataService(db)
    return service.create(data)

@router.get("/data/{id}", response_model=GeotechnicalData)
def read_data(id: int, db: Session = Depends(get_db)):
    service = GeotechnicalDataService(db)
    db_obj = service.get(id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj

@router.get("/data", response_model=list[GeotechnicalData])
def list_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = GeotechnicalDataService(db)
    return service.list(skip=skip, limit=limit)
