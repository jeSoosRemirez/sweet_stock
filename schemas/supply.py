from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime


class SupplyType(str, Enum):
    """Enum for supply type."""

    SUPPLY = "SUPPLY"  # supply to exact storage
    REDIRECTION = "REDIRECTION"  # redirected product from storage to storage


class SupplyRetrieve(BaseModel):
    """Model for retrieving a supply."""

    id: str
    supply_type: SupplyType
    weight: Optional[float]
    quantity: Optional[int]
    from_storage_id: str | None
    to_storage_id: str
    product_id: str
    created_at: Optional[str | datetime]
    updated_at: Optional[str | datetime]


class SupplyCreate(BaseModel):
    """Model for creating a supply."""

    supply_type: SupplyType = Field(..., description="Type of supply")
    weight: Optional[float] = Field(
        0, ge=0, description="Weight of the supply, optional and non-negative"
    )
    quantity: Optional[int] = Field(
        0, ge=0, description="Quantity of the supply, optional and non-negative"
    )
    from_storage_id: str = Field(None, description="ID of the source storage")
    to_storage_id: str = Field(..., description="ID of the destination storage")
    product_id: str = Field(..., description="ID of the product being supplied")


class SupplyUpdate(BaseModel):
    """Model for updating a supply."""

    supply_type: Optional[SupplyType] = Field(
        None, description="Updated type of supply"
    )
    weight: Optional[float] = Field(0, ge=0, description="Updated weight of the supply")
    quantity: Optional[int] = Field(
        0, ge=0, description="Updated quantity of the supply"
    )
    from_storage_id: Optional[str] = Field(
        None, description="Updated source storage ID"
    )
    to_storage_id: Optional[str] = Field(
        None, description="Updated destination storage ID"
    )
    product_id: Optional[str] = Field(None, description="Updated product ID")
