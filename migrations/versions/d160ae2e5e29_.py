"""empty message

Revision ID: d160ae2e5e29
Revises: None
Create Date: 2016-07-15 09:26:56.242998

"""

# revision identifiers, used by Alembic.
revision = 'd160ae2e5e29'
down_revision = None

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('meetup_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_dance_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('provider', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('token', sqlalchemy_utils.types.json.JSONType(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('github_name', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('presentation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['flask_dance_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('presentation')
    op.drop_table('flask_dance_user')
    op.drop_table('event')
    ### end Alembic commands ###