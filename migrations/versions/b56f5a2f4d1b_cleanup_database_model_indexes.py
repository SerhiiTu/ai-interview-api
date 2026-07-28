"""Cleanup redundant database indexes.

Revision ID: b56f5a2f4d1b
Revises: 4d253e9f5916
Create Date: 2026-07-29 00:01:00.000000

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


revision: str = "b56f5a2f4d1b"
down_revision: Union[str, Sequence[str], None] = "4d253e9f5916"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def _index_exists(bind: sa.engine.Connection, table_name: str, index_name: str) -> bool:
    inspector = sa.inspect(bind)
    indexes = {index["name"] for index in inspector.get_indexes(table_name)}
    return index_name in indexes


def _drop_index_if_exists(table_name: str, index_name: str) -> None:
    bind = op.get_bind()
    if _index_exists(bind, table_name, index_name):
        op.drop_index(index_name, table_name=table_name)


def upgrade() -> None:
    _drop_index_if_exists("positions", "ix_positions_id")

    _drop_index_if_exists("specializations", "ix_specializations_id")
    _drop_index_if_exists("spheres", "ix_spheres_id")
    _drop_index_if_exists("topics", "ix_topics_id")
    _drop_index_if_exists("users", "ix_users_id")
    _drop_index_if_exists("interviews", "ix_interviews_id")
    _drop_index_if_exists("subspheres", "ix_subspheres_id")
    _drop_index_if_exists("interview_reviews", "ix_interview_reviews_id")
    _drop_index_if_exists("interview_sessions", "ix_interview_sessions_id")
    _drop_index_if_exists("session_steps", "ix_session_steps_id")
    _drop_index_if_exists("user_answers", "ix_user_answers_id")
    _drop_index_if_exists("answer_feedbacks", "ix_answer_feedbacks_id")

    op.create_index(op.f("ix_interview_topics_topic_id"), "interview_topics", ["topic_id"], unique=False)
    op.create_index(op.f("ix_interview_spheres_sphere_id"), "interview_spheres", ["sphere_id"], unique=False)
    op.create_index(op.f("ix_interview_subspheres_subsphere_id"), "interview_subspheres", ["subsphere_id"], unique=False)
    op.create_index(op.f("ix_subsphere_specializations_specialization_id"), "subsphere_specializations", ["specialization_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_subsphere_specializations_specialization_id"), table_name="subsphere_specializations")
    op.drop_index(op.f("ix_interview_subspheres_subsphere_id"), table_name="interview_subspheres")
    op.drop_index(op.f("ix_interview_spheres_sphere_id"), table_name="interview_spheres")
    op.drop_index(op.f("ix_interview_topics_topic_id"), table_name="interview_topics")

    op.create_index(op.f("ix_positions_id"), "positions", ["id"], unique=False)
