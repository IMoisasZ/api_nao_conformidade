from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Lembre-se de substituir 'root' e 'sua_senha', e de criar o banco 'db_qualidade' no MySQL
DATABASE_URL = "mysql+pymysql://root:""@localhost:3306/db_qualidade"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()