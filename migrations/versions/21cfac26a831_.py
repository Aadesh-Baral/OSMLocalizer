"""empty message

Revision ID: 21cfac26a831
Revises: 9e62b17b0250
Create Date: 2023-02-26 21:56:22.541160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "21cfac26a831"
down_revision = "9e62b17b0250"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("challenge", schema=None) as batch_op:
        batch_op.alter_column("created_by", existing_type=sa.BIGINT(), nullable=False)

    with op.batch_alter_table("feature", schema=None) as batch_op:
        batch_op.alter_column("locked_by", existing_type=sa.BIGINT(), nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("feature", schema=None) as batch_op:
        batch_op.alter_column("locked_by", existing_type=sa.BIGINT(), nullable=False)

    with op.batch_alter_table("challenge", schema=None) as batch_op:
        batch_op.alter_column("created_by", existing_type=sa.BIGINT(), nullable=True)

    # ### end Alembic commands ###
