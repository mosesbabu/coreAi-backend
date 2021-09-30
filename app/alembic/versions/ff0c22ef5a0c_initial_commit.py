"""initial commit

Revision ID: ff0c22ef5a0c
Revises: 
Create Date: 2021-09-30 10:27:32.966134

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ff0c22ef5a0c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('amount',
    sa.Column('id', mysql.INTEGER(), nullable=False),
    sa.Column('amount', sa.String(length=16), nullable=True),
    sa.Column('amount_one', sa.String(length=16), nullable=True),
    sa.Column('amount_two', sa.String(length=16), nullable=True),
    sa.Column('amount_three', sa.String(length=16), nullable=True),
    sa.Column('amount_four', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dates',
    sa.Column('id', mysql.INTEGER(), nullable=False),
    sa.Column('date', sa.String(length=16), nullable=True),
    sa.Column('date_one', sa.String(length=16), nullable=True),
    sa.Column('date_two', sa.String(length=16), nullable=True),
    sa.Column('date_three', sa.String(length=16), nullable=True),
    sa.Column('date_four', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dates')
    op.drop_table('amount')
    # ### end Alembic commands ###