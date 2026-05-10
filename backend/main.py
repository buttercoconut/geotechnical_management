# main.py
from fastapi import FastAPI
from .api.routers import geotechnical_data
from .database.database import Base, engine

app = FastAPI(title="Geotechnical Management API")

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(geotechnical_data.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Geotechnical Management API"}
