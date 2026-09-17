from contextlib import asynccontextmanager
from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.core.database import engine, Base
from app.users.models import User  # Importante para o SQLAlchemy registrar a tabela
from app.sector.models import Sector
from app.users.router import router as users_router
from app.sector.router import router as sector_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    print("Banco de dados verificado/tabelas criadas com sucesso!")
    yield
    
app = FastAPI(
    title="API de Gestão de Não Conformidades",
    version="1.0.0",
    lifespan=lifespan
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    # Extrai a mensagem personalizada do ValueError que você configurou no schema
    errors = exc.errors()
    error_message = errors[0].get("msg", "Erro de validação nos campos.")
    
    # Remove o prefixo técnico "Value error, " se o Pydantic o adicionar
    if error_message.startswith("Value error, "):
        error_message = error_message.replace("Value error, ", "", 1)

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail":error_message}
    )


app.include_router(users_router, prefix="/api/v1")
app.include_router(sector_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "API rodando com sucesso!"}