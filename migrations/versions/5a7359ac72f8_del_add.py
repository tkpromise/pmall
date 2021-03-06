"""del add


Revision ID: 5a7359ac72f8
Revises: 610d4402e0b3
Create Date: 2018-11-27 13:58:04.584553

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5a7359ac72f8'
down_revision = '610d4402e0b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('exchanges', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('exchanges', sa.Column('address', mysql.VARCHAR(length=128), nullable=True))
    # ### end Alembic commands ###
