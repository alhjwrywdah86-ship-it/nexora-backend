from alembic import op
import sqlalchemy as sa


revision = "002"
down_revision = "001"
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        "goals",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column(
            "user_id",
            sa.String(),
            sa.ForeignKey("users.id"),
            nullable=False
        ),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("deadline", sa.String(), nullable=True),
        sa.Column("status", sa.String(), nullable=True),
        sa.Column("progress", sa.Integer(), nullable=True),
    )
    op.create_index("ix_goals_user_id", "goals", ["user_id"])

    op.create_table(
        "tasks",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column(
            "goal_id",
            sa.String(),
            sa.ForeignKey("goals.id"),
            nullable=False
        ),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("status", sa.String(), nullable=True),
        sa.Column("due_date", sa.String(), nullable=True),
        sa.Column("completed_at", sa.String(), nullable=True),
    )
    op.create_index("ix_tasks_goal_id", "tasks", ["goal_id"])


def downgrade():

    op.drop_index("ix_tasks_goal_id", table_name="tasks")
    op.drop_table("tasks")
    op.drop_index("ix_goals_user_id", table_name="goals")
    op.drop_table("goals")
