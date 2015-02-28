"""Node feature

Revision ID: 43a5cdca0a62
Revises: f08sa66d495
Create Date: 2013-12-09 12:09:41.969339

"""

# revision identifiers, used by Alembic.
revision = '43a5cdca0a62'
down_revision = 'f08sa66d495'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('node', sa.Column('mayor', sa.Integer(), nullable=True))
    op.add_column('node', sa.Column('on_home', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('node', 'on_home')
    op.drop_column('node', 'mayor')
    ### end Alembic commands ###
