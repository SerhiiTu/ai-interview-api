from __future__ import annotations

from pathlib import Path

from alembic.config import Config
from alembic.script import ScriptDirectory
from sqlalchemy import inspect
from sqlalchemy.orm import DeclarativeBase

import app.models as models_module
from app.core.database import Base


EXPECTED_TABLES = {
    "answer_feedbacks",
    "code_writing_answers",
    "code_writing_questions",
    "interview_reviews",
    "interview_sessions",
    "interview_spheres",
    "interview_subspheres",
    "interview_topics",
    "interviews",
    "positions",
    "session_steps",
    "specializations",
    "spheres",
    "subsphere_specializations",
    "subspheres",
    "theoretical_answers",
    "theoretical_questions",
    "topics",
    "user_answers",
    "users",
}


def test_models_import_without_errors() -> None:
    assert models_module is not None
    assert "User" in models_module.__all__
    assert "Interview" in models_module.__all__


def test_all_expected_tables_are_registered() -> None:
    tables = set(Base.metadata.tables)
    assert EXPECTED_TABLES.issubset(tables)


def test_all_tables_have_primary_keys() -> None:
    for table_name in sorted(Base.metadata.tables):
        table = Base.metadata.tables[table_name]
        assert table.primary_key is not None
        assert len(table.primary_key.columns) >= 1


def test_association_tables_use_composite_primary_key() -> None:
    composite_tables = {
        "interview_topics",
        "interview_spheres",
        "interview_subspheres",
        "subsphere_specializations",
    }
    for table_name in composite_tables:
        table = Base.metadata.tables[table_name]
        assert len(table.primary_key.columns) == 2


def test_session_steps_have_unique_constraint_for_session_and_number() -> None:
    table = Base.metadata.tables["session_steps"]
    constraint_names = {constraint.name for constraint in table.constraints}
    assert "uq_session_steps_session_number" in constraint_names


def test_user_email_has_unique_constraint_or_index() -> None:
    table = Base.metadata.tables["users"]
    assert any(
        constraint.columns.keys() == {"email"} and getattr(constraint, "unique", False)
        for constraint in table.constraints
    ) or any(index.columns.keys() == ["email"] for index in table.indexes)


def test_foreign_keys_reference_existing_tables() -> None:
    for table in Base.metadata.sorted_tables:
        for fk in table.foreign_key_constraints:
            assert fk.elements is not None
            for element in fk.elements:
                assert element.column.table.name in Base.metadata.tables


def test_alembic_has_single_head_revision() -> None:
    alembic_cfg = Config(str(Path(__file__).resolve().parents[1] / "alembic.ini"))
    script = ScriptDirectory.from_config(alembic_cfg)
    heads = script.get_revisions("heads")
    assert len(heads) == 1


def test_alembic_env_imports_are_clean() -> None:
    env_text = (Path(__file__).resolve().parents[1] / "migrations" / "env.py").read_text(encoding="utf-8")
    assert env_text.count("from app.core.database import Base") == 1
    assert "import app.models" in env_text
