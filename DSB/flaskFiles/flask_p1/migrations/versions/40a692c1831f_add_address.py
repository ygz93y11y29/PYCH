"""add_address

Revision ID: 40a692c1831f
Revises: 
Create Date: 2020-05-28 15:24:39.644597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40a692c1831f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ods_p1_Post', sa.Column('address', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ods_p1_Post', 'address')
    # ### end Alembic commands ###
