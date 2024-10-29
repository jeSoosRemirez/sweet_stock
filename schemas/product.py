"""Schemas for product."""

from datetime import date
from typing import Optional
from pydantic import BaseModel


class ProductSchema(BaseModel):
    """Schema for product model representation."""

    id: str
    name: str
    provider_price: float
    sell_price: float
    available_weight: float
    available_quantity: int
    storage: str
    delivery_dt: date
    expiration_dt: date
    provider_id: str


class CreateProductSchema(BaseModel):
    """Schema for product creation."""

    name: str
    provider_price: float
    sell_price: float
    available_weight: Optional[float]
    available_quantity: Optional[int]
    storage: str
    delivery_dt: Optional[date]
    expiration_dt: Optional[date]
    provider_id: str


class UpdateProductSchema(BaseModel):
    """Schema for product updating."""

    name: Optional[str]
    provider_price: Optional[float]
    sell_price: Optional[float]
    available_weight: Optional[float]
    available_quantity: Optional[int]
    storage: Optional[str]
    delivery_dt: Optional[date]
    expiration_dt: Optional[date]
    provider_id: Optional[str]
