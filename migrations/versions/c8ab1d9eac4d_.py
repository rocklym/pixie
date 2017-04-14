"""empty message

Revision ID: c8ab1d9eac4d
Revises: 
Create Date: 2017-04-14 00:44:29.579259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8ab1d9eac4d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_column('user', 'password_hash')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###