"""add tool label bings

Revision ID: 3b18fea55204
Revises: 7bdef072e63a
Create Date: 2024-05-14 09:27:18.857890

"""
import sqlalchemy as sa
from alembic import op

import models.types

# revision identifiers, used by Alembic.
revision = '3b18fea55204'
down_revision = '7bdef072e63a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tool_label_bindings',
    sa.Column('id', models.types.StringUUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('tool_id', sa.String(length=64), nullable=False),
    sa.Column('tool_type', sa.String(length=40), nullable=False),
    sa.Column('label_name', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id', name='tool_label_bind_pkey')
    )

    with op.batch_alter_table('tool_workflow_providers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('privacy_policy', sa.String(length=255), server_default='', nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tool_workflow_providers', schema=None) as batch_op:
        batch_op.drop_column('privacy_policy')

    op.drop_table('tool_label_bindings')
    # ### end Alembic commands ###
