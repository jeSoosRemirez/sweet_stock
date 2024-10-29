"""Models for product and categories."""

from sqlalchemy import String, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from database.mixins import GuidPKMixin, CreatedUpdatedMixin

from models.base import BaseModel


class Product(GuidPKMixin, CreatedUpdatedMixin, BaseModel):
    """Class for product model."""

    __tablename__ = "product"

    name: Mapped[str] = mapped_column(String(64), nullable=False)
    provider_price: Mapped[float] = mapped_column(Float, nullable=False)
    sell_price: Mapped[float] = mapped_column(Float, nullable=False)
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


# class ProductStat(BaseModel):
#     """Class for product statistics model."""

#     __tablename__ = "product_stat"


# class Order(BaseModel):
#     """Class for order model."""

#     __tablename__ = "order"

#     id: str
#     provider_price: float
#     sell_price: float
#     sold_weight: float
#     sold_quantity: int
#     total_sum: float
#     sold_at: datetime
