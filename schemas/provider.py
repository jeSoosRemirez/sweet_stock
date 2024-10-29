"""Schemas for product."""

from typing import Optional
from pydantic import BaseModel


class ProviderSchema(BaseModel):
    """Schema for provider model representation."""

    id: str
    name: str
    telephone_number: str | None
    address: str
    email: str


class CreateProviderSchema(BaseModel):
    """Schema for provider model creation."""

    name: str
    telephone_number: Optional[str] = None
    address: str
    email: str


class UpdateProviderSchema(BaseModel):
    """Schema for provider model updating."""

    name: Optional[str]
    telephone_number: Optional[str]
    address: Optional[str]
    email: Optional[str]
