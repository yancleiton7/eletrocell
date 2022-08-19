from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.infra.database import Base, get_db
from api.schemas.negocio import Zona as zn


class Zona(Base):
    __tablename__ = "zona"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)

    def create(zona: zn):
        db = get_db()
        nova_zona = Zona(nome = zona.nome)
        db.add(nova_zona)
        db.commit()
        return nova_zona

    def get_all():
        db = get_db()
        zonas = db.query(Zona).all()
        return zonas

    def remove(id: int):
        db = get_db()
        zona = db.query(Zona).filter_by(id=id).first()
        db.delete(zona)
        db.commit()
        return "deletado"
        
    def update(zona: zn):
        db = get_db()
        name_zona =  zona.nome
        zona_editada = db.query(Zona).filter_by(nome=name_zona).first()
        zona_editada.id = zona.id 
        db.commit()
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
    
