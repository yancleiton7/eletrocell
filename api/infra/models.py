from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.infra.database import Base, get_db
from api.schemas.negocio import Zona 


class Zona(Base):
    __tablename__ = "zona"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)

    def create(zona: Zona):
            get_db.add(zona.nome)
            get_db.commit()
            return zona

class TipoContrato(Base):
    __tablename__ = "tipo_contrato"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)



class TipoEquipamento(Base):
    __tablename__ = "tipo_equipamento"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)



class TipoManutencao(Base):
    __tablename__ = "tipo_manutencao"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)



class Cliente(Base):
    __tablename__ = "Cliente"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    contato = Column(String, nullable = True)
    
