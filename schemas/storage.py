from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class StorageRetrieve(BaseModel):
    """Model for retrieving a storage."""

    id: str
    name: str
    address: str
    max_weight: float
    max_quantity: int
    storing_weight: Optional[float]
    storing_quantity: Optional[int]
    last_restock_dt: Optional[datetime]
    created_at: Optional[str | datetime]
    updated_at: Optional[str | datetime]


class StorageCreate(BaseModel):
    """Model for creating a storage."""

    name: str = Field(..., max_length=64, description="Name of the storage")
    address: str = Field(..., max_length=256, description="Address of the storage")
    max_weight: float = Field(
        ..., ge=0, description="Maximum weight the storage can hold"
    )
    max_quantity: int = Field(
        ..., ge=0, description="Maximum quantity the storage can hold"
    )
    storing_weight: Optional[float] = Field(
        0, ge=0, description="Current stored weight, defaults to 0"
    )
    storing_quantity: Optional[int] = Field(
        0, ge=0, description="Current stored quantity, defaults to 0"
    )
    last_restock_dt: Optional[datetime] = Field(
        None, description="Date of the last restock, optional"
    )


class StorageUpdate(BaseModel):
    """Model for updating a storage."""

    name: Optional[str] = Field(
        None, max_length=64, description="Updated name of the storage"
    )
    address: Optional[str] = Field(
        None, max_length=256, description="Updated address of the storage"
    )
    max_weight: Optional[float] = Field(
        None, ge=0, description="Updated maximum weight the storage can hold"
    )
    max_quantity: Optional[int] = Field(
        None, ge=0, description="Updated maximum quantity the storage can hold"
    )
    storing_weight: Optional[float] = Field(
        None, ge=0, description="Updated stored weight"
    )
    storing_quantity: Optional[int] = Field(
        None, ge=0, description="Updated stored quantity"
    )
    last_restock_dt: Optional[datetime] = Field(
        None, description="Updated date of the last restock"
    )
