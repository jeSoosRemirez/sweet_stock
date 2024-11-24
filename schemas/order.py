from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class OrderRetrieve(BaseModel):
    """Model for retrieving an order."""

    id: str
    price: int
    weight: Optional[float]
    quantity: Optional[int]
    storage_id: str
    product_id: str
    created_at: Optional[str | datetime]
    updated_at: Optional[str | datetime]


class OrderCreate(BaseModel):
    """Model for creating an order."""

    price: int = Field(
        ..., ge=0, description="Price of the order, must be non-negative"
    )
    weight: Optional[float] = Field(
        None, ge=0, description="Weight of the order, optional"
    )
    quantity: Optional[int] = Field(
        None, ge=0, description="Quantity of the order, must be at least 1"
    )
    storage_id: str = Field(..., description="ID of the storage")
    product_id: str = Field(..., description="ID of the product")


class OrderUpdate(BaseModel):
    """Model for updating an order."""

    price: Optional[int] = Field(None, ge=0, description="Updated price of the order")
    weight: Optional[float] = Field(
        None, ge=0, description="Updated weight of the order"
    )
    quantity: Optional[int] = Field(
        None, ge=0, description="Updated quantity of the order"
    )
    storage_id: Optional[str] = Field(None, description="Updated storage ID")
    product_id: Optional[str] = Field(None, description="Updated product ID")
