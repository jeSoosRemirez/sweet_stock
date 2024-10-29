"""Schemas for product statistics."""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class ProductRaw(BaseModel):
    """Raw product record."""

    product_id: str
    name: str
    # amount: float
    total_sum: int
    updated_at: datetime


class CategoryStat(BaseModel):
    """Stat representation based on category type."""

    total_sum: int
    combined_products: Optional[dict[str, ProductRaw]] = Field(default_factory=dict)


class ProductPeriod(BaseModel):
    """Product data for a specific time period."""

    dt: datetime
    raw: List[ProductRaw]
    total_sum: int
    combined_stat: List[CategoryStat]


class Product(BaseModel):
    """Product data over time periods."""

    last_update_dt: Optional[datetime] = None
    raw: List[ProductRaw] = Field(default_factory=list)
    years: List[ProductPeriod] = Field(default_factory=list)
    months: List[ProductPeriod] = Field(default_factory=list)
    days: List[ProductPeriod] = Field(default_factory=list)
    hours: List[ProductPeriod] = Field(default_factory=list)
