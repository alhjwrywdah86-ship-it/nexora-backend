from alembic import op
import sqlalchemy as sa


revision = "003"
down_revision = "002"
branch_labels = None
depends_on = None


def _to_timestamptz(table, column):
    op.alter_column(
        table,
        column,
        type_=sa.DateTime(timezone=True),
        existing_type=sa.String(),
        existing_nullable=True,
        postgresql_using=f"NULLIF({column}, '')::timestamptz",
    )


def _to_string(table, column):
    op.alter_column(
        table,
        column,
        type_=sa.String(),
        existing_type=sa.DateTime(timezone=True),
        existing_nullable=True,
        postgresql_using=f"{column}::text",
    )


def upgrade():

    _to_timestamptz("goals", "deadline")
    _to_timestamptz("tasks", "due_date")
    _to_timestamptz("tasks", "completed_at")


def downgrade():

    _to_string("tasks", "completed_at")
    _to_string("tasks", "due_date")
    _to_string("goals", "deadline")
