"""Initial settings

Revision ID: 58526c90f092
Revises:
Create Date: 2022-07-12 20:47:22.358585

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "58526c90f092"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "masters",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_masters_id"), "masters", ["id"], unique=False)
    op.create_index(op.f("ix_masters_name"), "masters", ["name"], unique=True)
    op.create_table(
        "slaves",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("owner_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["masters.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_slaves_id"), "slaves", ["id"], unique=False)
    op.create_index(op.f("ix_slaves_name"), "slaves", ["name"], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_slaves_name"), table_name="slaves")
    op.drop_index(op.f("ix_slaves_id"), table_name="slaves")
    op.drop_table("slaves")
    op.drop_index(op.f("ix_masters_name"), table_name="masters")
    op.drop_index(op.f("ix_masters_id"), table_name="masters")
    op.drop_table("masters")
    # ### end Alembic commands ###