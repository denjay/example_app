"""empty message

Revision ID: 60d673575c2e
Revises: 
Create Date: 2018-01-31 10:39:24.138444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60d673575c2e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=60), nullable=False),
    sa.Column('user_password', sa.String(length=128), nullable=False),
    sa.Column('user_email', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('article',
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('article_title', sa.String(length=50), nullable=False),
    sa.Column('article_content', sa.String(length=5000), nullable=False),
    sa.Column('article_date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('article_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article')
    op.drop_table('user')
    # ### end Alembic commands ###
