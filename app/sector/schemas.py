from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional, ClassVar
from app.core.validators import clean_and_validate_string

class SectorCreate(BaseModel):
    min_length_description: ClassVar[int] = 3
    
    description: str = Field(..., min_length=min_length_description, description=f'O nome do setor deve ter no minimo {min_length_description} caracteres!')
    active: bool = True
    
    @field_validator('description')
    @classmethod
    def validate_description(cls, v: str):
        cleaned = clean_and_validate_string(v, cls.min_length_description)
        return cleaned.upper()
    
class SectorResponse(BaseModel):
    id: int
    description: str
    active: bool
    created_at: datetime
    
    model_config = {'from_attributes': True}
    
class SectorUpdate(BaseModel):
    min_length_description: ClassVar[int] = 3
    
    description: Optional[str] = None
    active: Optional[bool] = None
    
    @field_validator('description')
    @classmethod
    def updated_description(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return None
        
        cleaned = clean_and_validate_string(v, cls.min_length_description)
        return cleaned.upper()
    
