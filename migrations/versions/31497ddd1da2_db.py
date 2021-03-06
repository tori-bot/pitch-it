"""db

Revision ID: 31497ddd1da2
Revises: 3c2ef4d20979
Create Date: 2022-05-10 09:59:26.275367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31497ddd1da2'
down_revision = '3c2ef4d20979'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'pitches', ['pitch_id'], ['id'], ondelete='CASCADE')
    op.add_column('downvotes', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.add_column('downvotes', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'downvotes', 'pitches', ['pitch_id'], ['id'])
    op.create_foreign_key(None, 'downvotes', 'users', ['user_id'], ['id'])
    op.add_column('pitches', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'users', ['user_id'], ['id'])
    op.add_column('upvotes', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('upvotes', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'upvotes', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'upvotes', 'pitches', ['pitch_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'upvotes', type_='foreignkey')
    op.drop_constraint(None, 'upvotes', type_='foreignkey')
    op.drop_column('upvotes', 'pitch_id')
    op.drop_column('upvotes', 'user_id')
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'user_id')
    op.drop_constraint(None, 'downvotes', type_='foreignkey')
    op.drop_constraint(None, 'downvotes', type_='foreignkey')
    op.drop_column('downvotes', 'user_id')
    op.drop_column('downvotes', 'pitch_id')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'user_id')
    op.drop_column('comments', 'pitch_id')
    # ### end Alembic commands ###
