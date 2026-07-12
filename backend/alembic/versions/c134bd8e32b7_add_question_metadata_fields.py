"""add question metadata fields

Revision ID: c134bd8e32b7
Revises: ad820f6413d4
Create Date: 2026-07-12 10:33:27.598781

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "c134bd8e32b7"
down_revision: Union[str, Sequence[str], None] = "ad820f6413d4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "answer_options",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("question_id", sa.Integer(), nullable=False),
        sa.Column("option_text", sa.String(length=255), nullable=False),
        sa.Column("is_correct", sa.Boolean(), nullable=False),
        sa.Column("display_order", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["question_id"], ["questions.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        op.f("ix_answer_options_id"),
        "answer_options",
        ["id"],
        unique=False,
    )

    # Add new columns with temporary defaults
    op.add_column(
        "questions",
        sa.Column(
            "question_type",
            sa.String(length=30),
            nullable=False,
            server_default="MCQ",
        ),
    )

    op.add_column(
        "questions",
        sa.Column(
            "points",
            sa.Integer(),
            nullable=False,
            server_default="1",
        ),
    )

    op.add_column(
        "questions",
        sa.Column(
            "explanation",
            sa.Text(),
            nullable=True,
        ),
    )

    op.add_column(
        "questions",
        sa.Column(
            "hint",
            sa.Text(),
            nullable=True,
        ),
    )

    # Remove database defaults after existing rows are updated
    op.alter_column(
        "questions",
        "question_type",
        server_default=None,
    )

    op.alter_column(
        "questions",
        "points",
        server_default=None,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column("questions", "hint")
    op.drop_column("questions", "explanation")
    op.drop_column("questions", "points")
    op.drop_column("questions", "question_type")

    op.drop_index(
        op.f("ix_answer_options_id"),
        table_name="answer_options",
    )

    op.drop_table("answer_options")
