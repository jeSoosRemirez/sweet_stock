"""Schemas for storage."""

from datetime import date
from typing import Optional
from pydantic import BaseModel


class StorageSchema(BaseModel):
    """Schema for storage model representation."""

    id: str
    name: str
    address: str

    max_weight: float
    max_quantity: int
    storing_weight: float
    storing_quantity: int

    last_restock_dt: date


class CreateStorageSchema(BaseModel):
    """Schema for storage model creation."""

    name: str
    address: str

    max_weight: float
    max_quantity: int
    storing_weight: Optional[float]
    storing_quantity: Optional[int]

    last_restock_dt: Optional[date]


class UpdateStorageSchema(BaseModel):
    """Schema for storage model updating."""

    name: Optional[str]
    address: Optional[str]

    max_weight: Optional[float]
    max_quantity: Optional[int]
    storing_weight: Optional[float]
    storing_quantity: Optional[int]

    last_restock_dt: Optional[date]
