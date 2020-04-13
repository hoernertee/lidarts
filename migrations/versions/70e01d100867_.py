"""empty message

Revision ID: 70e01d100867
Revises: 0990320b48fe
Create Date: 2020-04-12 11:56:55.329208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70e01d100867'
down_revision = '0990320b48fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_statistic', sa.Column('matches30_40', sa.Integer(), nullable=True))
    op.add_column('user_statistic', sa.Column('matches40_50', sa.Integer(), nullable=True))
    op.add_column('user_statistic', sa.Column('matches50_60', sa.Integer(), nullable=True))
    op.add_column('user_statistic', sa.Column('matches60_70', sa.Integer(), nullable=True))
    op.add_column('user_statistic', sa.Column('matches70_80', sa.Integer(), nullable=True))
    op.add_column('user_statistic', sa.Column('matches80_90', sa.Integer(), nullable=True))
    op.add_column('user_statistic', sa.Column('matches_o90', sa.Integer(), nullable=True))
    op.add_column('user_statistic', sa.Column('matches_u30', sa.Integer(), nullable=True))
    op.add_column('user_statistic', sa.Column('wins30_40', sa.Integer(), nullable=True))
    op.add_column('user_statistic', sa.Column('wins40_50', sa.Integer(), nullable=True))
    op.add_column('user_statistic', sa.Column('wins50_60', sa.Integer(), nullable=True))
    op.add_column('user_statistic', sa.Column('wins60_70', sa.Integer(), nullable=True))
    op.add_column('user_statistic', sa.Column('wins70_80', sa.Integer(), nullable=True))
    op.add_column('user_statistic', sa.Column('wins80_90', sa.Integer(), nullable=True))
    op.add_column('user_statistic', sa.Column('wins_o90', sa.Integer(), nullable=True))
    op.add_column('user_statistic', sa.Column('wins_u30', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_statistic', 'wins_u30')
    op.drop_column('user_statistic', 'wins_o90')
    op.drop_column('user_statistic', 'wins80_90')
    op.drop_column('user_statistic', 'wins70_80')
    op.drop_column('user_statistic', 'wins60_70')
    op.drop_column('user_statistic', 'wins50_60')
    op.drop_column('user_statistic', 'wins40_50')
    op.drop_column('user_statistic', 'wins30_40')
    op.drop_column('user_statistic', 'matches_u30')
    op.drop_column('user_statistic', 'matches_o90')
    op.drop_column('user_statistic', 'matches80_90')
    op.drop_column('user_statistic', 'matches70_80')
    op.drop_column('user_statistic', 'matches60_70')
    op.drop_column('user_statistic', 'matches50_60')
    op.drop_column('user_statistic', 'matches40_50')
    op.drop_column('user_statistic', 'matches30_40')
    # ### end Alembic commands ###
