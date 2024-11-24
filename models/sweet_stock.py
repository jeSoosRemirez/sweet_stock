"""Models for product and categories."""

from typing import Optional
from sqlalchemy import String, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from database.mixins import GuidPKMixin, CreatedUpdatedMixin

from models.base import BaseModel
from sqlalchemy import Enum as SaEnum
from enum import Enum


class SupplyType(str, Enum):
    """Enum for supply type."""

    SUPPLY = "SUPPLY"  # supply to exact storage
    REDIRECTION = "REDIRECTION"  # redirected product from storage to storage


class RoleType(str, Enum):
    """Enum for user roles."""

    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    WORKER = "WORKER"


class Product(GuidPKMixin, CreatedUpdatedMixin, BaseModel):
    """Class for product model."""

    __tablename__ = "product"

    name: Mapped[str] = mapped_column(String(64), nullable=False)
    provider_price: Mapped[Integer] = mapped_column(Integer, nullable=False)
    sell_price: Mapped[Integer] = mapped_column(Integer, nullable=False)
    available_weight: Mapped[float] = mapped_column(Float, nullable=True)
    available_quantity: Mapped[int] = mapped_column(Integer, nullable=True)
    delivery_dt: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    expiration_dt: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    provider_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("provider.id"), nullable=False
    )

    storage: Mapped[str] = mapped_column(
        String(36), ForeignKey("storage.id"), nullable=False
    )


class Storage(GuidPKMixin, CreatedUpdatedMixin, BaseModel):
    """Class for storage model."""

    __tablename__ = "storage"

    name: Mapped[str] = mapped_column(String(64), nullable=False)
    address: Mapped[str] = mapped_column(String(256), nullable=False)

    max_weight: Mapped[float] = mapped_column(Float, nullable=False)
    max_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    storing_weight: Mapped[float] = mapped_column(
        Float, nullable=True, server_default="0"
    )
    storing_quantity: Mapped[int] = mapped_column(
        Integer, nullable=True, server_default="0"
    )

    last_restock_dt: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Provider(GuidPKMixin, CreatedUpdatedMixin, BaseModel):
    """Class for provider model."""

    __tablename__ = "provider"

    name: Mapped[str] = mapped_column(String(64), nullable=False)
    telephone_number: Mapped[str] = mapped_column(String(32), nullable=True)
    address: Mapped[str] = mapped_column(String(256), nullable=False)
    email: Mapped[str] = mapped_column(String(64), nullable=False)


class Order(GuidPKMixin, CreatedUpdatedMixin, BaseModel):
    """Class for order model."""

    __tablename__ = "order"

    price: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=True)

    storage_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("storage.id"), nullable=False
    )
    product_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("product.id"), nullable=False
    )


class Supply(GuidPKMixin, CreatedUpdatedMixin, BaseModel):
    """Class for supply model."""

    __tablename__ = "supply"

    supply_type: Mapped[SupplyType] = mapped_column(SaEnum(SupplyType))
    weight: Mapped[float] = mapped_column(Float, nullable=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=True)

    from_storage_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("storage.id"), nullable=True
    )
    to_storage_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("storage.id"), nullable=True
    )
    product_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("product.id"), nullable=False
    )


class User(GuidPKMixin, CreatedUpdatedMixin, BaseModel):
    """Class for user model."""

    __tablename__ = "user"

    role: Mapped[RoleType] = mapped_column(SaEnum(RoleType))
    username: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
    full_name: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
