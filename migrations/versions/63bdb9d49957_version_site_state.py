"""Version site state

Revision ID: 63bdb9d49957
Revises: 09f776ea71f0
Create Date: 2024-05-25 10:13:43.911027

"""

# revision identifiers, used by Alembic.
revision = '63bdb9d49957'
down_revision = '09f776ea71f0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('site_state_version',
    sa.Column('name', sa.String(), autoincrement=False, nullable=False),
    sa.Column('state', sa.String(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('name', 'transaction_id', name=op.f('pk_site_state_version'))
    )
    op.create_index(op.f('ix_site_state_version_operation_type'), 'site_state_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_site_state_version_transaction_id'), 'site_state_version', ['transaction_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_site_state_version_transaction_id'), table_name='site_state_version')
    op.drop_index(op.f('ix_site_state_version_operation_type'), table_name='site_state_version')
    op.drop_table('site_state_version')
    # ### end Alembic commands ###