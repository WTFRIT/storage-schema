"""initial migration

Revision ID: 5f68459a94bb
Revises: 
Create Date: 2023-02-26 04:46:17.105054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f68459a94bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vibes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('contents', sa.Text(), nullable=False),
    sa.Column('upvotes', sa.Integer(), nullable=True),
    sa.Column('sentiment', sa.Integer(), nullable=True),
    sa.Column('source_url', sa.String(), nullable=False),
    sa.Column('last_updated', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vibes')
    # ### end Alembic commands ###
