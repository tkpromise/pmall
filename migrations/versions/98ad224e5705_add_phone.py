"""add phone

Revision ID: 98ad224e5705
Revises: 1ed46a6f865c
Create Date: 2018-11-27 14:03:12.427739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98ad224e5705'
down_revision = '1ed46a6f865c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('exchanges', sa.Column('phone', sa.String(length=129), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('exchanges', 'phone')
    # ### end Alembic commands ###
