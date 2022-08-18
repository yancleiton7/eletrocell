from pydantic import BaseModel
from typing import List, Optional



class TipoContrato(BaseModel):
    id: int
    nome: str
    
class TipoOrg(BaseModel):
    #privada /publica
    tipo: str
    
class TipoEquipamento(BaseModel):
    id: int
    nome: str
    
class TipoManutencao(BaseModel):
    id: int
    nome: str

class Zona(BaseModel):
    id: Optional[int] = None
    nome: str

    class Config():
        orm_mode = True


class Cliente(BaseModel):
    id: int
    nome: str
    contato: Optional[str]


class Equipamento(BaseModel):
    id: int
    tipo_id: int
    marca: str
    modelo: str
    num_serie: str
    contrato_id: int
    local: str
    capacidade: Optional[str]
    velocidade: Optional[str]
    
       
class Contrato(BaseModel):
    id: int
    nome_empresa: str
    natureza_id: TipoOrg
    vencimento: str
    objetos: List[Equipamento]
    valor_contrato: str
    contato: str
    responsavel_nome: str
    zona_id: int

class Chamado(BaseModel):
    id: int
    data_hora_abertura: str
    cliente_id: int
    equipamento_id: int
    tipo_manutencao_id: int
    acao: str
    data_hora_inicio: str
    data_hora_fim: str
    tecnico_matricula: int 
    observacao: str
