from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import datetime
from typing import Optional
from app.core.validators import clean_and_validate_string

class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, description='O nome deve ter pelo menos, 3 caracteres!')
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v: str) -> str:
        cleaned = clean_and_validate_string(v)
        return cleaned.upper()
    
    email: EmailStr
    
    password: str = Field(..., min_length=6, description='A senha deve ter no minimo, 6 caracteres!')
    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        return clean_and_validate_string(v)
        
    abre_rnc: Optional[bool] = False
    responsavel_setor: Optional[bool] = False

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    abre_rnc: bool
    responsavel_setor: bool
    created_at: datetime

    class Config:
        from_attributes = True
        
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    abre_rnc: Optional[bool] = None
    responsavel_setor: Optional[bool] = None
    
    @field_validator('name')
    @classmethod
    def updated_name(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return None
        
        cleaned = clean_and_validate_string(v)
        if len(cleaned) < 3:
            raise ValueError('O nome deve ter pelo menos, 3 caracteres!')
        return cleaned.upper()
    
    @field_validator('password')
    @classmethod
    def update_password(cls, v:Optional[str]) -> Optional[str]:
        if v is None:
            return None
        
        cleaned = clean_and_validate_string(v)
        if len(cleaned) < 6:
            raise ValueError('A senha deve ter no minimo, 6 caracteres!')
        return cleaned