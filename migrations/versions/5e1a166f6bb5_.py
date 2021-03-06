"""empty message

Revision ID: 5e1a166f6bb5
Revises: c8ab1d9eac4d
Create Date: 2017-04-14 02:41:29.316678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e1a166f6bb5'
down_revision = 'c8ab1d9eac4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'confirmed')
    # ### end Alembic commands ###
