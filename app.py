from fastapi import FastAPI
from api.infra.models import Zona

from api.schemas.negocio import Zona  as Zn

app = FastAPI()

@app.get("/")
async def root():
    msg = "Bem vindo ao sistema da Eletrocell"
    return msg


@app.get("/zonas")
async def zonas():
    zonas = Zona.get_all()
    return zonas

@app.post("/nova_zona")
async def new_zona(zona: Zn):
    zona_criada = Zona.create(zona)
    return zona_criada
