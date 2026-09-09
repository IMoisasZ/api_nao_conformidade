import bcrypt
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.users.schemas import UserCreate, UserUpdate
from app.users.repository import UserRepository

class UserService:
    # ----------------------------------------- Helpers functions -------------------------------------------------
    @staticmethod
    def exist_user_by_email(db: Session, email: str):
        user = UserRepository.get_user_by_email(db, email)
        
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail= f'O email {email} já está cadastrado no sistema!'
            )
        return user
    
    @staticmethod
    def exist_user_by_id(db: Session, user_id: int):
        user = UserRepository.get_user_by_id(db, user_id)
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Não há usuário com o ID {user_id}!'
            )
        return user
    # ----------------------------------------- Functions of System -------------------------------------------------
    @staticmethod
    def create_user(db: Session, user_data: UserCreate):
        UserService.exist_user_by_email(db, user_data.email)
        
        password_bytes = user_data.password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt).decode('utf-8')

        user_dict = {
            "name":user_data.name,
            "email":user_data.email,
            "hashed_password":hashed_password,
            "abre_rnc":user_data.abre_rnc,
            "responsavel_setor":user_data.responsavel_setor
        }

        return UserRepository.create_user(db, user_dict)
    
    @staticmethod
    def update_user(db: Session, user_data: UserUpdate, user_id: int):
        user = UserService.exist_user_by_id(db, user_id)
        
        update_data = user_data.model_dump(exclude_unset=True)
        
        if "password" in update_data and update_data["password"]:
            password_bytes = update_data["password"].encode('utf-8')
            salt = bcrypt.gensalt()
            update_data["hashed_password"] = bcrypt.hashpw(password_bytes, salt).decode('utf-8')
            del update_data["password"]
            
        return UserRepository.update_user(db, user, update_data)

    @staticmethod
    def get_all_users(db: Session, skip: int = 0, limit: int = 100):
        return UserRepository.get_all_users(db, skip=skip, limit=limit)
    
    @staticmethod
    def get_user_by_email(db: Session, email: str):
        user = UserRepository.get_user_by_email(db, email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Não existe usuário com o email {email}, cadastrado no sistema!'
            )
        return user
    
    @staticmethod
    def get_user_by_id(db: Session, id: int):
        user = UserService.exist_user_by_id(db, id)
        return user