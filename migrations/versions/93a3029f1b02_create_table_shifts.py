"""Create Table Shifts

Revision ID: 93a3029f1b02
Revises: 75b9cd9f3c3f
Create Date: 2024-05-31 01:52:22.726038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93a3029f1b02'
down_revision = '75b9cd9f3c3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shifts',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.Column('break_out', sa.DateTime(), nullable=True),
    sa.Column('break_in', sa.DateTime(), nullable=True),
    sa.Column('overtime_before', sa.DateTime(), nullable=True),
    sa.Column('overtime_after', sa.DateTime(), nullable=True),
    sa.Column('is_default', sa.SmallInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shifts')
    # ### end Alembic commands ###