from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import datetime
from typing import Optional, ClassVar
from app.core.validators import clean_and_validate_string

class UserCreate(BaseModel):
    min_length_name: ClassVar[int] = 3
    min_length_password: ClassVar[int] = 6

    name: str = Field(..., min_length=min_length_name, description=f'O nome deve ter pelo menos, {min_length_name} caracteres!')
    email: EmailStr
    password: str = Field(..., min_length=min_length_password, description=f'A senha deve ter no minimo, {min_length_password} caracteres!')
    abre_rnc: Optional[bool] = False
    responsavel_setor: Optional[bool] = False
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v: str) -> str:
        cleaned = clean_and_validate_string(v, cls.min_length_name)
        return cleaned.upper()
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        return clean_and_validate_string(v, cls.min_length_password)

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    abre_rnc: bool
    responsavel_setor: bool
    created_at: datetime

    model_config = {'from_attributes': True}
        
class UserUpdate(BaseModel):
    min_length_name: ClassVar[int] = 3
    min_length_password: ClassVar[int] = 6

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
        cleaned = clean_and_validate_string(v, cls.min_length_name)
        return cleaned.upper()
    
    @field_validator('password')
    @classmethod
    def update_password(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return None
        return clean_and_validate_string(v, cls.min_length_password)