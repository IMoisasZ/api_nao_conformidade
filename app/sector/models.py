from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime, timezone
from app.core.database import Base

class Sector(Base):
    __tablename__ = "sector"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda:datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda:datetime.now(timezone.utc), onupdate=lambda:datetime.now(timezone.utc))