"""Schemas for product."""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ProductRetrieve(BaseModel):
    """Model for retrieving a product."""

    id: str
    name: str
    provider_price: int
    sell_price: int
    available_weight: Optional[float]
    available_quantity: Optional[int]
    delivery_dt: Optional[datetime]
    expiration_dt: Optional[datetime]
    provider_id: str
    storage: str
    created_at: Optional[str | datetime]
    updated_at: Optional[str | datetime]


class ProductCreate(BaseModel):
    """Model for creating a product."""

    name: str = Field(..., max_length=64, description="Name of the product")
    provider_price: int = Field(
        ..., ge=0, description="Provider price, must be non-negative"
    )
    sell_price: int = Field(
        ..., ge=0, description="Selling price, must be non-negative"
    )
    available_weight: Optional[float] = Field(
        None, ge=0, description="Available weight, optional"
    )
    available_quantity: Optional[int] = Field(
        None, ge=0, description="Available quantity, optional"
    )
    delivery_dt: Optional[datetime] = Field(None, description="Delivery date, optional")
    expiration_dt: Optional[datetime] = Field(
        None, description="Expiration date, optional"
    )
    provider_id: str = Field(..., description="ID of the provider")
    storage: str = Field(..., description="ID of the storage")


class ProductUpdate(BaseModel):
    """Model for updating a product."""

    name: Optional[str] = Field(
        None, max_length=64, description="Updated name of the product"
    )
    provider_price: Optional[int] = Field(
        None, ge=0, description="Updated provider price"
    )
    sell_price: Optional[int] = Field(None, ge=0, description="Updated selling price")
    available_weight: Optional[float] = Field(
        None, ge=0, description="Updated available weight"
    )
    available_quantity: Optional[int] = Field(
        None, ge=0, description="Updated available quantity"
    )
    delivery_dt: Optional[datetime] = Field(None, description="Updated delivery date")
    expiration_dt: Optional[datetime] = Field(
        None, description="Updated expiration date"
    )
    provider_id: Optional[str] = Field(None, description="Updated provider ID")
    storage: Optional[str] = Field(None, description="Updated storage ID")
