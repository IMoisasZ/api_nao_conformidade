from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.users.models import User

class UserRepository:
    @staticmethod
    def create_user(db: Session, user_data: dict) -> User:
        try:      
            db_user = User(**user_data)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except SQLAlchemyError as e:
            db.rollback()
            raise e
    
    @staticmethod
    def update_user(db: Session, db_user: User, update_data: dict) -> User:
        try:
            for key, value in update_data.items():
                setattr(db_user, key, value)
            
            db.commit()
            db.refresh(db_user)
            return db_user      
        except SQLAlchemyError as e:
            db.rollback()
            raise e
    
    @staticmethod
    def get_all_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
        try:
            return db.query(User).offset(skip).limit(limit).all()
        except SQLAlchemyError as e:
            raise e
    
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> User | None:
        try:
            return db.query(User).filter(User.email == email).first()
        except SQLAlchemyError as e:
            raise e
    
    @staticmethod
    def get_user_by_id(db: Session, id: int) -> User | None:
        try:
            return db.query(User).filter(User.id == id).first()
        except SQLAlchemyError as e:
            raise e
    