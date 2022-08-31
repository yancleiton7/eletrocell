from fastapi import FastAPI
from api.infra.models import Usuario, Zona

from api.schemas.negocio import Schema_Zona
from api.schemas.pessoal import Schema_Usuario 

app = FastAPI()

@app.get("/")
async def root():
    msg = "Bem vindo ao sistema da Eletrocell"
    return msg

#rotas de zonas

@app.get("/zona")
async def zonas():
    zonas = Zona.get_all()
    return zonas

@app.post("/nova_zona")
async def new_zona(zona: Schema_Zona):
    zona_criada = Zona.create(zona)
    return zona_criada

@app.delete("/zona/{id}")
async def delete_zona(id: int):
    delete = Zona.remove(id)
    return delete


@app.get("/zona/{id}")
async def get_zona(id: int):
    selected = Zona.get(id)
    return selected

@app.put("/zona")
async def update_zona(zona: Schema_Zona):
    zona_editada = Zona.update(zona)
    return zona_editada

#Rotas para usuario

@app.post("/user")
async def update_zona(user: Schema_Usuario):
    new_user = Usuario.create(user)
    return new_user

@app.put("/user")
async def update_zona(user: Schema_Usuario):
    updated_user = Usuario.update(user)
    return updated_user

@app.get("/user")
async def get_users():
    users = Usuario.get_all()
    return users

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    user = Usuario.get(user_id)
    return user

@app.delete("/user/{user_id}")
async def delete_user(user_id:int):
    removed_user = Usuario.remove(user_id)
    return removed_user