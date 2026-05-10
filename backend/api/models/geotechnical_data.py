# models/geotechnical_data.py
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database.database import Base

class GeotechnicalData(Base):
    __tablename__ = "geotechnical_data"

    id = Column(Integer, primary_key=True, index=True)
    site_id = Column(Integer, index=True)
    depth = Column(Float)
    n_value = Column(Float)
    location = Column(String)  # WKT or GeoJSON
    description = Column(String)

    # relationships
    # e.g., site = relationship("Site", back_populates="geotechnical_data")
