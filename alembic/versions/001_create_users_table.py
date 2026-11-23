from alembic import op
import sqlalchemy as sa


revision = "001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        "users",

        sa.Column(
            "id",
            sa.String(),
            primary_key=True
        ),

        sa.Column(
            "name",
            sa.String(255),
            nullable=False
        ),

        sa.Column(
            "email",
            sa.String(255),
            nullable=False,
            unique=True
        ),

        sa.Column(
            "password_hash",
            sa.String(),
            nullable=False
        ),

        sa.Column(
            "is_active",
            sa.Boolean(),
            default=True
        )
    )


def downgrade():

    op.drop_table("users")
