"""create quiz attempt tables

Revision ID: 5f8c8148a0a0
Revises: c134bd8e32b7
Create Date: 2026-07-12 14:45:52.073176
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers
revision: str = "5f8c8148a0a0"
down_revision: Union[str, Sequence[str], None] = "c134bd8e32b7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "quiz_attempts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("quiz_id", sa.Integer(), nullable=False),
        sa.Column("score", sa.Integer(), nullable=False),
        sa.Column("total_questions", sa.Integer(), nullable=False),
        sa.Column("correct_answers", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(length=20), nullable=False),
        sa.Column("completed_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["quiz_id"], ["quizzes.id"]),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        op.f("ix_quiz_attempts_id"),
        "quiz_attempts",
        ["id"],
        unique=False,
    )

    op.create_table(
        "question_attempts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("quiz_attempt_id", sa.Integer(), nullable=False),
        sa.Column("question_id", sa.Integer(), nullable=False),
        sa.Column("selected_answer_option_id", sa.Integer(), nullable=False),
        sa.Column("is_correct", sa.Boolean(), nullable=False),
        sa.Column("points_awarded", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["quiz_attempt_id"],
            ["quiz_attempts.id"],
        ),
        sa.ForeignKeyConstraint(
            ["question_id"],
            ["questions.id"],
        ),
        sa.ForeignKeyConstraint(
            ["selected_answer_option_id"],
            ["answer_options.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        op.f("ix_question_attempts_id"),
        "question_attempts",
        ["id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        op.f("ix_question_attempts_id"),
        table_name="question_attempts",
    )

    op.drop_table("question_attempts")

    op.drop_index(
        op.f("ix_quiz_attempts_id"),
        table_name="quiz_attempts",
    )

    op.drop_table("quiz_attempts")
