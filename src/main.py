from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.controllers import user_controller

app = FastAPI(
    title="Desafio API Valcann",
    description="API de leitura de usuários",
    version="1.0.0"
)

# configuração do CORS
origins = [
    "http://localhost:8000",
    "*"  # Para desenvolvimento...
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_controller.router, prefix="/users", tags=["Users"])
