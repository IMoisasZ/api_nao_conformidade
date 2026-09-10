from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.core.database import get_db
from app.sector.schemas import SectorCreate, SectorResponse, SectorUpdate
from app.sector.service import SectorService

router = APIRouter(prefix="/sectors", tags=['Sectors'])

@router.post("/", response_model=SectorResponse, status_code=status.HTTP_201_CREATED)
def create_sector(sector_data: SectorCreate, db: Session = Depends(get_db)):
    try:
        return SectorService.create_sector(db=db, sector_data=sector_data)
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Não foi possivel incluir o setor {sector_data.description}'
        )

@router.put("/{sector_id}", response_model=SectorResponse, status_code=status.HTTP_200_OK)
def update_sector(sector_id: int, sector_update: SectorUpdate, db: Session = Depends(get_db)):
    try:
        return SectorService.update_sector(db=db, sector_id=sector_id, sector_update=sector_update)
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Não foi possivel alterar o setor com o ID {sector_id}'
        )
        
@router.get("/", response_model=list[SectorResponse], status_code=status.HTTP_200_OK)
def get_all_sectors(db: Session=Depends(get_db), skip:int=0, limit:int=100):
    try:
        return SectorService.get_all_sectors(db=db, skip=skip, limit=limit)
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Erro interno. Tente novamente mais tarde!'
        )
        
@router.get("/{sector_id}", response_model=SectorResponse, status_code=status.HTTP_200_OK)
def get_sector_by_id(sector_id: int, db:Session=Depends(get_db)):
    try:
        return SectorService.get_sector_by_id(db=db, sector_id=sector_id)
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Erro interno. Tente novamente mais tarde!'
        )