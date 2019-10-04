"""Location..

Revision ID: 997d43e73ade
Revises: 
Create Date: 2019-10-02 18:18:21.927787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '997d43e73ade'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('book', 'location',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('book', 'location',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
