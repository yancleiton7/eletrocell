from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    msg = "Bem vindo ao sistema da Eletrocell"
    return msg
