"""Create requests table

Revision ID: 8e053b181ab3
Revises:
Create Date: 2023-01-12 03:18:07.266018

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "8e053b181ab3"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "endpoint",
        sa.Column(
            "id", sqlalchemy_utils.types.uuid.UUIDType(), server_default=sa.text("uuid_generate_v4()"), nullable=False
        ),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("url", sa.String(), nullable=False),
        sa.Column("elapsed", sa.Numeric(), nullable=False),
        sa.Column("status_code", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("temp")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "temp",
        sa.Column(
            "id", postgresql.UUID(), server_default=sa.text("uuid_generate_v4()"), autoincrement=False, nullable=False
        ),
        sa.Column("ep_name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("created_at", postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
        sa.Column("url", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("elapsed", sa.NUMERIC(), autoincrement=False, nullable=False),
        sa.Column("status_code", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="temp_pkey"),
    )
    op.drop_table("endpoint")
    # ### end Alembic commands ###
