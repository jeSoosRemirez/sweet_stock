"""Helpers for database, sqlalchemy, etc."""

from sqlalchemy import String
from sqlalchemy.sql.type_api import TypeEngine


def get_pk_col_type() -> TypeEngine:
    """Returns SqlAlchemy column type for guid(uuid4) primary key field.

    Returns:
        TypeEngine: object that can be used as Column type for sqlalchemy
    """
    return String(36)
