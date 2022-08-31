from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.infra.database import Base, get_db
from api.schemas import negocio, pessoal


class Zona(Base):
    __tablename__ = "zona"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    
    def create(zona: negocio.Schema_Zona):
        db = get_db()
        nova_zona = Zona(nome = zona.nome)
        db.add(nova_zona)
        db.commit()
        return nova_zona

    def get_all():
        db = get_db()
        zonas = db.query(Zona).all()
        return zonas

    def get(id:int):
        db = get_db()
        selected_zona = db.query(Zona).filter_by(id=id).first()
        if selected_zona is None:
            selected_zona = "Não conseguimos encontrar a zona solicitada."
        return selected_zona

    def remove(id: int):
        db = get_db()
        zona = db.query(Zona).filter_by(id=id).first()
        db.delete(zona)
        db.commit()
        return "deletado"
        
    def update(zona: negocio.Schema_Zona):
        '''
        Essa edição está fazendo a alteração do id da zona. Era o parametro que eu precisava mudar quando fiz os testes
        '''
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
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    contato = Column(String, nullable = True)
    


class Cargo(Base):
    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True, index=True)
    cargo = Column(String, index=True)
    usuario = relationship('Usuario', back_populates = "cargo")
        

class Usuario(Base):

    __tablename__ = "usuario"

    matricula = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cpf = Column(String, index=True)
    email = Column(String, index=True)
    senha = Column(String, index=True)
    telefone = Column(String, index=True)
    zona_id = Column(ForeignKey('zona.id'), index=True)
    cidade = Column(String, index=True)
    cargo_id = Column(ForeignKey('cargo.id'), index=True)
    salario = Column(String, index=True)
    is_adm = Column(Boolean)

    cargo = relationship('Cargo', back_populates = "usuario")
    zona = relationship('Zona')

    
    def create(user: pessoal.Schema_Usuario):
        db = get_db()
        new_user = Usuario(nome = user.nome,
                            cpf = user.cpf,
                            email = user.email,
                            senha = user.senha,
                            telefone = user.telefone,
                            zona_id = user.zona_id,
                            cidade = user.zona_id,
                            cargo_id = user.cargo_id,
                            salario = user.salario,
                            is_adm = user.adm)
        db.add(new_user)
        db.commit()
        return f"O usuario {new_user.nome} foi adicionado"

    def get_all():
        db = get_db()
        user_list = db.query(Usuario).all()
        return user_list

    def get(matricula:int):
        db = get_db()
        selected_user = db.query(Usuario).filter_by(matricula = matricula).first()
        if selected_user is None:
            selected_user = "Não conseguimos encontrar a zona solicitada."
        return selected_user

    def remove(matricula: int):
        db = get_db()
        user = db.query(Usuario).filter_by(matricula = matricula).first()
        db.delete(user)
        db.commit()
        return f"Usuário {user.matricula} foi deletado"
        
    def update(user: pessoal.Schema_Usuario):
        '''
        Essa edição está fazendo a alteração do id da zona. Era o parametro que eu precisava mudar quando fiz os testes
        '''
        db = get_db()

        user_updated = Usuario(nome = user.nome,
                            cpf = user.cpf,
                            email = user.email,
                            senha = user.senha,
                            telefone = user.telefone,
                            zona_id = user.zona_id,
                            cidade = user.zona_id,
                            cargo_id = user.cargo_id,
                            salario = user.salario,
                            is_adm = user.adm)

                            
        user_selected = db.query(Usuario).filter_by(nome=user.nome).first()
        user_selected = user_updated
        db.commit()
        return user_selected
