"""empty message

Revision ID: 7f881f2ca3f2
Revises: 21ff805809b7
Create Date: 2020-04-24 19:50:04.442198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f881f2ca3f2'
down_revision = '21ff805809b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stream_game',
    sa.Column('hashid', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('hashid', name=op.f('pk_stream_game'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stream_game')
    # ### end Alembic commands ###