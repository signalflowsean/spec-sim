"""empty message

Revision ID: dda107804f15
Revises: 56f2fdee2291
Create Date: 2020-01-18 19:56:59.219985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dda107804f15'
down_revision = '56f2fdee2291'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.drop_index('ix_user_usernamewxw', table_name='user')
    op.drop_column('user', 'usernamewxw')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('usernamewxw', sa.VARCHAR(length=64), nullable=True))
    op.create_index('ix_user_usernamewxw', 'user', ['usernamewxw'], unique=1)
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###