from pydantic import BaseModel
from typing import List, Optional



class Schema_TipoContrato(BaseModel):
    id: int
    nome: str
    
class Schema_TipoOrg(BaseModel):
    #privada /publica
    tipo: str
    
class Schema_TipoEquipamento(BaseModel):
    id: int
    nome: str
    
class Schema_TipoManutencao(BaseModel):
    id: int
    nome: str

class Schema_Zona(BaseModel):
    id: Optional[int] = None
    nome: str

    class Config():
        orm_mode = True


class Schema_Cliente(BaseModel):
    id: int
    nome: str
    contato: Optional[str]


class Schema_Equipamento(BaseModel):
    id: int
    tipo_id: int
    marca: str
    modelo: str
    num_serie: str
    contrato_id: int
    local: str
    capacidade: Optional[str]
    velocidade: Optional[str]
    
       
class Schema_Contrato(BaseModel):
    id: int
    nome_empresa: str
    natureza_id: Schema_TipoOrg
    vencimento: str
    objetos: List[Schema_Equipamento]
    valor_contrato: str
    contato: str
    responsavel_nome: str
    zona_id: int

class Schema_Chamado(BaseModel):
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
