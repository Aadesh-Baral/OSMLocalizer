"""empty message

Revision ID: 7b247be5e731
Revises: 21cfac26a831
Create Date: 2023-03-01 21:49:24.547925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7b247be5e731"
down_revision = "21cfac26a831"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("feature", schema=None) as batch_op:
        batch_op.alter_column(
            "id",
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=False,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("feature", schema=None) as batch_op:
        batch_op.alter_column(
            "id",
            existing_type=sa.BigInteger(),
            type_=sa.INTEGER(),
            existing_nullable=False,
        )

    # ### end Alembic commands ###
