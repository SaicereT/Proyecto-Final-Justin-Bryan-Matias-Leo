"""empty message

<<<<<<<< HEAD:migrations/versions/def4c9e31b69_.py
Revision ID: def4c9e31b69
Revises: 
Create Date: 2023-01-15 11:18:40.320953
========
Revision ID: 269e5e2e2389
Revises: 
Create Date: 2023-01-14 23:29:25.790899
>>>>>>>> 8096f66ec707708d13c5049926e48616a659306a:migrations/versions/269e5e2e2389_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:migrations/versions/def4c9e31b69_.py
revision = 'def4c9e31b69'
========
revision = '269e5e2e2389'
>>>>>>>> 8096f66ec707708d13c5049926e48616a659306a:migrations/versions/269e5e2e2389_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token_blocklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_token_blocklist_jti'), 'token_blocklist', ['jti'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=1000), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('firstname', sa.String(length=40), nullable=False),
    sa.Column('lastname', sa.String(length=120), nullable=False),
    sa.Column('telnumber', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.Column('country', sa.String(length=120), nullable=False),
    sa.Column('age', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('telnumber')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=40), nullable=False),
    sa.Column('make', sa.String(length=120), nullable=False),
    sa.Column('model', sa.String(length=120), nullable=False),
    sa.Column('style', sa.String(length=120), nullable=False),
    sa.Column('fuel', sa.String(length=120), nullable=False),
    sa.Column('transmission', sa.String(length=120), nullable=False),
    sa.Column('financing', sa.Boolean(), nullable=False),
    sa.Column('doors', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=240), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Fav_posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Fav_posts')
    op.drop_table('posts')
    op.drop_table('users')
    op.drop_index(op.f('ix_token_blocklist_jti'), table_name='token_blocklist')
    op.drop_table('token_blocklist')
    # ### end Alembic commands ###
