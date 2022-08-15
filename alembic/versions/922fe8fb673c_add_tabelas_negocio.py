"""add tabelas negocio

Revision ID: 922fe8fb673c
Revises: 45cbd68b7fee
Create Date: 2022-08-15 00:11:41.971612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '922fe8fb673c'
down_revision = '45cbd68b7fee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('contato', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Cliente_id'), 'Cliente', ['id'], unique=False)
    op.create_index(op.f('ix_Cliente_nome'), 'Cliente', ['nome'], unique=False)
    op.create_table('tipo_equipamento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tipo_equipamento_id'), 'tipo_equipamento', ['id'], unique=False)
    op.create_index(op.f('ix_tipo_equipamento_nome'), 'tipo_equipamento', ['nome'], unique=False)
    op.create_table('tipo_manutencao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tipo_manutencao_id'), 'tipo_manutencao', ['id'], unique=False)
    op.create_index(op.f('ix_tipo_manutencao_nome'), 'tipo_manutencao', ['nome'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tipo_manutencao_nome'), table_name='tipo_manutencao')
    op.drop_index(op.f('ix_tipo_manutencao_id'), table_name='tipo_manutencao')
    op.drop_table('tipo_manutencao')
    op.drop_index(op.f('ix_tipo_equipamento_nome'), table_name='tipo_equipamento')
    op.drop_index(op.f('ix_tipo_equipamento_id'), table_name='tipo_equipamento')
    op.drop_table('tipo_equipamento')
    op.drop_index(op.f('ix_Cliente_nome'), table_name='Cliente')
    op.drop_index(op.f('ix_Cliente_id'), table_name='Cliente')
    op.drop_table('Cliente')
    # ### end Alembic commands ###
