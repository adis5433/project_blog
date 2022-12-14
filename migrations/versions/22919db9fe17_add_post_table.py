"""Add Post table

Revision ID: 22919db9fe17
Revises: 
Create Date: 2022-08-17 15:11:41.552402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22919db9fe17'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=False),
    sa.Column('post_content', sa.String(length=100), nullable=False),
    sa.Column('pub_date', sa.DateTime(), nullable=False),
    sa.Column('is_public', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
