"""Create Table Office

Revision ID: 16526b2f7e87
Revises: 86eeb30ec84e
Create Date: 2024-05-31 01:17:38.552916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16526b2f7e87'
down_revision = '86eeb30ec84e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('office',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('address', sa.Text(), nullable=False),
    sa.Column('phone', sa.String(length=16), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('office')
    # ### end Alembic commands ###
