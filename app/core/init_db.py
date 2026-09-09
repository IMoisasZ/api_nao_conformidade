from app.core.database import engine, Base
# Importamos o model User para que o SQLAlchemy saiba que ele existe e deve ser criado
from app.users.models import User

def init_db():
    print("Conectando ao MySQL e criando as tabelas...")
    # Este comando lê todas as classes que herdam de Base e cria as tabelas se não existirem
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    init_db()