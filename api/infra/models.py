from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.infra.database import get_db, Base
from api.schemas import negocio

class Zona(Base):
    __tablename__ = "zona"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)

    def create(db, zona:negocio.Zona):
        db = get_db()
        pass

class TipoContrato(Base):
    __tablename__ = 'tipo_contrato'

    id = Column(Integer, primary_key=True)
    nome = Column(String)

class TipoOrg(Base):
    __tablename__ = 'tipo_org'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    
class TipoEquipamento(Base):
    __tablename__ = 'tipo_equipamento'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    
class TipoManutencao(Base):
    __tablename__ = 'tipo_manutencao'
    id = Column(Integer, primary_key=True)
    nome = Column(String)

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    contato = Column(String)