"""empty message

Revision ID: 624f6dde9804
Revises: a765038c55f9
Create Date: 2021-05-15 08:13:53.688263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '624f6dde9804'
down_revision = 'a765038c55f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('sm_image_url', sa.String(length=250), nullable=False))
    op.add_column('product', sa.Column('lg_image_url', sa.String(length=250), nullable=False))
    op.drop_column('product', 'image_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('image_url', sa.VARCHAR(length=250), nullable=False))
    op.drop_column('product', 'lg_image_url')
    op.drop_column('product', 'sm_image_url')
    # ### end Alembic commands ###
