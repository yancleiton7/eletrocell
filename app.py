from fastapi import FastAPI
from api.infra.models import Zona

app = FastAPI()

@app.get("/")
async def root():
    msg = "Bem vindo ao sistema da Eletrocell"
    return msg

@app.post("/nova_zona")
async def new_zona():
    Zona.create()
    return 0
