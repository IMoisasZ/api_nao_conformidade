from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.sector.models import Sector

class SectorRepository:
    @staticmethod
    def create_sector(db: Session, sector_data: dict) -> Sector:
        try:
            db_sector = Sector(**sector_data)
            db.add(db_sector)
            db.commit()
            db.refresh(db_sector)
            return db_sector
        except SQLAlchemyError as e:
            db.rollback()
            raise e
        
    @staticmethod
    def update_sector(db: Session, db_sector: Sector, update_data: dict) -> Sector:
        try:
            for key, value in update_data.items():
                setattr(db_sector, key, value)
                
            db.commit()
            db.refresh(db_sector)
            return db_sector
        except SQLAlchemyError as e:
            db.rollback()
            raise e
        
    @staticmethod
    def get_all_sectors(db: Session, skip: int=0, limit: int=100) -> list[Sector]:
        try:
            return db.query(Sector).offset(skip).limit(limit).all()
        except SQLAlchemyError as e:
            raise e
        
    @staticmethod
    def get_sector_by_id(db: Session, sector_id: int) -> Sector | None:
        try:
            return db.query(Sector).filter(Sector.id == sector_id).first()
        except SQLAlchemyError as e:
            raise e
    