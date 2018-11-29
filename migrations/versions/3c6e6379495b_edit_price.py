"""edit price

Revision ID: 3c6e6379495b
Revises: 3ad74e4b417f
Create Date: 2018-11-27 09:03:52.446880

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3c6e6379495b'
down_revision = '3ad74e4b417f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('price', sa.Integer(), nullable=True))
    op.drop_column('items', 'priice')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('priice', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('items', 'price')
    # ### end Alembic commands ###
