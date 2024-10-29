"""Schemas for order."""

from datetime import datetime
from pydantic import BaseModel


class OrderSchema(BaseModel):
    """Schema for order model representation."""

    id: str
    provider_price: float
    sell_price: float
    sold_weight: float | None
    sold_quantity: int | None
    total_sum: float
    sold_at: datetime
