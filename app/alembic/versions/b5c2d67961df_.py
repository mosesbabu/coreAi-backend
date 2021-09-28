"""empty message

Revision ID: b5c2d67961df
Revises: 
Create Date: 2021-09-28 22:39:52.345729

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b5c2d67961df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dataset',
    sa.Column('id', mysql.INTEGER(), nullable=False),
    sa.Column('amount', mysql.INTEGER(), nullable=True),
    sa.Column('date', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dataset')
    # ### end Alembic commands ###