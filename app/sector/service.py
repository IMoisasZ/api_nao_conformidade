from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.sector.schemas import SectorCreate, SectorResponse, SectorUpdate
from app.sector.repository import SectorRepository

class SectorService:
    # ----------------------------------------- Helpers functions -------------------------------------------------
    @staticmethod
    def exist_sector_by_id(db: Session, sector_id: int):
        sector = SectorRepository.get_sector_by_id(db, sector_id)
        
        if not sector:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Setor não encontrado com o ID {sector_id}'
            )
        return sector
            
    # ----------------------------------------- Functions of System -------------------------------------------------
    @staticmethod
    def create_sector(db: Session, sector_data: SectorCreate):
        sector_dict = sector_data.model_dump()
        return SectorRepository.create_sector(db=db, sector_data=sector_dict)
    
    @staticmethod
    def update_sector(db: Session, sector_id: int, sector_update: SectorUpdate):
        sector = SectorService.exist_sector_by_id(db, sector_id)
        
        sector_dict = sector_update.model_dump(exclude_unset=True)
        return SectorRepository.update_sector(db=db, db_sector=sector, update_data=sector_dict)
    
    @staticmethod
    def get_all_sectors(db: Session, skip: int=0, limit: int=100):
        return SectorRepository.get_all_sectors(db=db, skip=skip, limit=limit)
    
    @staticmethod
    def get_sector_by_id(db: Session, sector_id: int):
        sector = SectorService.exist_sector_by_id(db=db, sector_id=sector_id)
        return sector
    