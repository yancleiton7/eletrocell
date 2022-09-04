from pydantic import BaseModel
from typing import List, Optional

class Schema_Usuario(BaseModel):
    matricula: Optional[int] = None
    nome: str
    cpf: int
    email: str
    senha: str
    telefone: str
    zona_id: int 
    cidade: str
    cargo_id: str
    salario: float
    adm: Optional[bool] = False
    

class Schema_Cargo(BaseModel):
    id: int
    cargo: str