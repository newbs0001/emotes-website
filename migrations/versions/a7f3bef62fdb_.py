"""Adds the shared emote association table.

Revision ID: a7f3bef62fdb
Revises: 4af4c837801f
Create Date: 2016-08-27 23:42:16.954777

"""

# revision identifiers, used by Alembic.
revision = 'a7f3bef62fdb'
down_revision = '4af4c837801f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shared_emotes_link',
    sa.Column('guild_id', sa.BigInteger(), nullable=False),
    sa.Column('emote_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['emote_id'], ['emote.id'], ),
    sa.ForeignKeyConstraint(['guild_id'], ['guild.id'], )
    )
    op.create_index(op.f('ix_shared_emotes_link_emote_id'), 'shared_emotes_link', ['emote_id'], unique=False)
    op.create_index(op.f('ix_shared_emotes_link_guild_id'), 'shared_emotes_link', ['guild_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_shared_emotes_link_guild_id'), table_name='shared_emotes_link')
    op.drop_index(op.f('ix_shared_emotes_link_emote_id'), table_name='shared_emotes_link')
    op.drop_table('shared_emotes_link')
    ### end Alembic commands ###
