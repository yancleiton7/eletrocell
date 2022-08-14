from pydantic import BaseModel

class Usuario(BaseModel):
    matricula: int
    nome: str
    cpf: int
    email: str
    senha: str
    telefone: str
    zona_id: int 
    cidade: str
    cargo_id: str
    salario: float
    adm: bool
    

class Cargo(BaseModel):
    id: int
    nome: str
    