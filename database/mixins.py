"""Mixins for models, database related classes, etc."""

import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .helpers import get_pk_col_type


def generate_guid() -> str:
    """Generates GUID.

    Returns:
        str: GUID string value
    """
    return str(uuid.uuid4())


class GuidPKMixin:
    """Mixin with primary key for SqlAlchemy models.

    Attributes:
        id (sqlalchemy.orm.MappedColumn): Primary key field
    """

    id: Mapped[str] = mapped_column(
        get_pk_col_type(),
        primary_key=True,
        unique=True,
        index=True,
        default=generate_guid,
    )


class CreatedUpdatedMixin:
    """Mixin with created_at, updated_at fields for SqlAlchemy models.

    Attributes:
        created_at (sqlalchemy.orm.MappedColumn): field with datatime of row creation
        updated_at (sqlalchemy.orm.MappedColumn): field with datatime of row updating
    """

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
    )


class SoftDeleteMixin:
    """Mixin class for product with soft delete method."""

    deleted: Mapped[bool] = mapped_column(
        Boolean,
        index=False,
        default=False,
        server_default="false",
        nullable=False,
    )

    def delete(self):
        """Sets deleted field to True."""
        self.deleted = True
