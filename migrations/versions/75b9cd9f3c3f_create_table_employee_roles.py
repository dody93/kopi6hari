"""Create Table Employee_Roles

Revision ID: 75b9cd9f3c3f
Revises: 44a1899da849
Create Date: 2024-05-31 01:47:38.443719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75b9cd9f3c3f'
down_revision = '44a1899da849'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee__roles',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('employee_id', sa.BigInteger(), nullable=True),
    sa.Column('role_id', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee__roles')
    # ### end Alembic commands ###
