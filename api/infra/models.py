from datetime import datetime
from email.policy import default
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

    equipamento = relationship('Equipamento', back_populates = "tipo")

class TipoManutencao(Base):
    __tablename__ = "tipo_manutencao"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    chamado = relationship('Chamado', back_populates = "manutencao")

class TipoEmpresa(Base):
    __tablename__ = "natureza_empresa"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    contato = Column(String, nullable = True)
    natureza_id = Column(ForeignKey('natureza_empresa.id'), index=True, default = 1)

    natureza = relationship('TipoEmpresa')
    chamado = relationship('Chamado', back_populates = "cliente")
    contrato = relationship('Contrato', back_populates = "cliente")

    
    def create(client: negocio.Schema_Cliente):
        db = get_db()
        new_client = Cliente(nome = client.nome,
                            contato = client.contato,
                            natureza_id = client.natureza_id
                           )
        db.add(new_client)
        db.commit()
        return f"O cliente {new_client.nome} foi adicionado"

    def get_all():
        db = get_db()
        client_list = db.query(Cliente).all()
        return client_list

    def get(id:int):
        db = get_db()
        selected_client = db.query(Cliente).filter_by(id = id).first()
        if selected_client is None:
            selected_client = "Não conseguimos encontrar o cliente solicitado."
        return selected_client

    def remove(id: int):
        db = get_db()
        client = db.query(Cliente).filter_by(id = id).first()
        db.delete(client)
        db.commit()
        return f"Cliente {client.nome} foi deletado"
        
    def update(client: negocio.Schema_Cliente):
        '''
        
        '''
        db = get_db()

        client_updated = Cliente(id = client.id,
                            nome = client.nome,
                            contato = client.contato,
                            natureza_id = client.natureza_id
                           )

                            
        client_selected = db.query(Cliente).filter_by(id=client.id).first()
        db.delete(client_selected)
        db.add(client_updated)
        db.commit()
        return client_updated

    
class Cargo(Base):
    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True, index=True)
    cargo = Column(String, index=True)    

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
    chamado = relationship('Chamado', back_populates = "usuario")

    
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
        
        '''
        db = get_db()

        user_updated = Usuario(matricula = user.matricula,
                            nome = user.nome,
                            cpf = user.cpf,
                            email = user.email,
                            senha = user.senha,
                            telefone = user.telefone,
                            zona_id = user.zona_id,
                            cidade = user.zona_id,
                            cargo_id = user.cargo_id,
                            salario = user.salario,
                            is_adm = user.adm)

                            
        user_selected = db.query(Usuario).filter_by(matricula=user.matricula).first()
        db.delete(user_selected)
        db.add(user_updated)
        db.commit()
        return user_updated

class Equipamento(Base):
    
    __tablename__ = "equipamento"

    id = Column(Integer, primary_key=True, index=True)
    tipo_id = Column(ForeignKey('tipo_equipamento.id'), index=True)
    marca = Column(String, index=True)
    modelo = Column(String, index=True)
    num_serie = Column(String, index=True)
    contrato_id = Column(ForeignKey('contrato.id'), index=True)
    local = Column(String, index=True)
    capacidade = Column(String, default = None)
    velocidade = Column(String, default = None)

    tipo = relationship('TipoEquipamento', back_populates = "equipamento")
    contrato = relationship('Contrato')
    chamado = relationship('Chamado', back_populates = "equipamento")

    
    def create(equipament: negocio.Schema_Equipamento):
        db = get_db()
        new_equipament = Equipamento(tipo_id = equipament.tipo_id,
                                    marca = equipament.marca,
                                    modelo = equipament.modelo,
                                    num_serie = equipament.num_serie,
                                    contrato_id = equipament.contrato_id,
                                    local = equipament.local,
                                    capacidade = equipament.capacidade,
                                    velocidade = equipament.velocidade
                            
                           )
        db.add(new_equipament)
        db.commit()
        return f"O {new_equipament.marca} - {new_equipament.modelo} foi adicionado"

    def get_all():
        db = get_db()
        equipament_list = db.query(Equipamento).all()
        return equipament_list

    def get(id:int):
        db = get_db()
        selected_equipament = db.query(Equipamento).filter_by(id = id).first()
        if selected_equipament is None:
            selected_equipament = "Não conseguimos encontrar o equipamento solicitado."
        return selected_equipament

    def remove(id: int):
        db = get_db()
        equipament = db.query(Equipamento).filter_by(id = id).first()
        db.delete(equipament)
        db.commit()
        return f"O equipamento {equipament.marca} - {equipament.modelo} foi deletado"
        
    def update(equipament: negocio.Schema_Equipamento):
        '''
        
        '''
        db = get_db()

        equipament_updated = Equipamento(id = equipament.id,
                                    tipo_id = equipament.tipo_id,
                                    marca = equipament.marca,
                                    modelo = equipament.modelo,
                                    num_serie = equipament.num_serie,
                                    contrato_id = equipament.contrato_id,
                                    local = equipament.local,
                                    capacidade = equipament.capacidade,
                                    velocidade = equipament.velocidade
                            
                           )

                            
        equipament_selected = db.query(Equipamento).filter_by(id=equipament.id).first()
        db.delete(equipament_selected)
        db.add(equipament_updated)
        db.commit()
        return equipament_updated
    
class Contrato(Base):
    
    __tablename__ = "contrato"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(ForeignKey('cliente.id'), index=True)
    vencimento = Column(String, index=True)
    valor_contrato = Column(String, index=True)
    contato = Column(String, index=True)
    responsavel_nome = Column(String, default = None)
    zona_id = Column(ForeignKey('zona.id'), index=True)
    

    cliente = relationship('Cliente', back_populates = "contrato")
    zona = relationship('Zona', back_populates = "contrato")

    
    def create(deal: negocio.Schema_Contrato):
        db = get_db()
        new_deal = Contrato(client_id = deal.cliente_id,
                            vencimento = deal.vencimento,
                            valor_contrato = deal.valor_contrato,
                            contato = deal.contato,
                            responsavel_nome = deal.responsavel_nome,
                            zona_id = deal.zona_id
                           )
        db.add(new_deal)
        db.commit()
        return f"O contrato nº {new_deal.id} foi adicionado"

    def get_all():
        db = get_db()
        deal_list = db.query(Contrato).all()
        return deal_list

    def get(id:int):
        db = get_db()
        selected_deal = db.query(Contrato).filter_by(id = id).first()
        if selected_deal is None:
            selected_deal = "Não conseguimos encontrar o contrato solicitado."
        return selected_deal

    def remove(id: int):
        db = get_db()
        deal = db.query(Contrato).filter_by(id = id).first()
        db.delete(deal)
        db.commit()
        return f"O contrato nº {deal.id} foi deletado"
        
    def update(deal: negocio.Schema_Contrato):
        '''
        
        '''
        db = get_db()

        deal_updated = Contrato(id = deal.id,
                                    client_id = deal.cliente_id,
                                    vencimento = deal.vencimento,
                                    valor_contrato = deal.valor_contrato,
                                    contato = deal.contato,
                                    responsavel_nome = deal.responsavel_nome,
                                    zona_id = deal.zona_id
                           )

                            
        deal_selected = db.query(Contrato).filter_by(id=deal.id).first()
        db.delete(deal_selected)
        db.add(deal_updated)
        db.commit()
        return deal_updated
    
class Status_Chamado(Base):
    __tablename__ = "status_chamado"
    id = id = Column(Integer, primary_key=True, index=True)
    status = Column(String)

    chamado = relationship("Chamado", back_populates = "status")

class Chamado(Base):
    __tablename__ = "chamado"

    id = Column(Integer, primary_key=True, index=True)
    
    cliente_id = Column(ForeignKey('cliente.id'), index=True)
    equipamento_id = Column(ForeignKey('equipamento.id'), index=True)
    tipo_manutencao_id = Column(ForeignKey('tipo_manutencao.id'), index=True)
    acao = Column(String, index=True)

    data_hora_abertura = Column(String, index=True)
    data_hora_inicio = Column(String, index=True)
    data_hora_fim = Column(String, index=True)

    tecnico_matricula = Column(ForeignKey('usuario.matricula'), index=True)
    observacao = Column(String, index=True)
    status_id = Column(Integer, ForeignKey('status_chamado.id'), index = True)

    status = relationship('Status_Chamado', back_populates = "chamado")
    cliente = relationship('Cliente', back_populates = "chamado")
    equipamento = relationship('Equipamento', back_populates = "chamado")
    manutencao = relationship('TipoManutencao', back_populates = "chamado")
    usuario =  relationship('Usuario', back_populates = "chamado")

    
    def create(ticket: negocio.Schema_Chamado):
        db = get_db()

        hora = datetime.now().strftime('%d/%m/%Y %H:%M')
        new_ticket = Chamado(client_id = ticket.cliente_id,
                            equipamento = ticket.equipamento_id,
                            tipo_manutencao_id = ticket.tipo_manutencao_id,
                            acao = ticket.acao,
                            data_hora_abertura = hora,
                            data_hora_inicio = ticket.data_hora_inicio,
                            data_hora_fim = ticket.data_hora_fim,
                            tecnico_matricula = ticket.tecnico_matricula,
                            observacao = ticket.observacao,
                            status = 1

                            
                           )
        db.add(new_ticket)
        db.commit()
        return f"O contrato nº {new_ticket.id} foi adicionado"

    def get_all():
        db = get_db()
        deal_list = db.query(Chamado).all()
        return deal_list

    def get(id:int):
        db = get_db()
        selected_ticket = db.query(Chamado).filter_by(id = id).first()
        if selected_ticket is None:
            selected_ticket = "Não conseguimos encontrar o contrato solicitado."
        return selected_ticket


    def acept(id:int):
        db = get_db()
        ticket = db.query(Chamado).filter_by(id = id).first()
        if ticket is None:
            ticket = "Não conseguimos encontrar o contrato solicitado."
        hora = datetime.now().strftime('%d/%m/%Y %H:%M')
        ticket.data_hora_inicio = hora
        return ticket

    def close(id:int):
        db = get_db()
        ticket = db.query(Chamado).filter_by(id = id).first()
        if ticket is None:
            ticket = "Não conseguimos encontrar o contrato solicitado."
        hora = datetime.now().strftime('%d/%m/%Y %H:%M')
        ticket.data_hora_fim = hora
        return ticket

    def remove(id: int):
        db = get_db()
        ticket = db.query(Chamado).filter_by(id = id).first()
        db.delete(ticket)
        db.commit()
        return f"O contrato nº {ticket.id} foi deletado"
        
    def update(ticket: negocio.Schema_Chamado):
        '''
        
        '''
        db = get_db()

        ticket_updated = Chamado(id = ticket.id,
                                client_id = ticket.cliente_id,
                                equipamento = ticket.equipamento_id,
                                tipo_manutencao_id = ticket.tipo_manutencao_id,
                                acao = ticket.acao,
                                data_hora_abertura = ticket.data_hora_abertura,
                                data_hora_inicio = ticket.data_hora_inicio,
                                data_hora_fim = ticket.data_hora_fim,
                                tecnico_matricula = ticket.tecnico_matricula,
                                observacao = ticket.observacao,
                                status = 1
                           )

                            
        ticket_selected = db.query(Chamado).filter_by(id=ticket.id).first()
        db.delete(ticket_selected)
        db.add(ticket_updated)
        db.commit()
        return ticket_updated
    