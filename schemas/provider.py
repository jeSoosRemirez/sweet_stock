from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


class ProviderRetrieve(BaseModel):
    """Model for retrieving a provider."""

    id: str
    name: str
    telephone_number: Optional[str]
    address: str
    email: EmailStr
    created_at: Optional[str | datetime]
    updated_at: Optional[str | datetime]


class ProviderCreate(BaseModel):
    """Model for creating a provider."""

    name: str = Field(..., max_length=64, description="Name of the provider")
    telephone_number: Optional[str] = Field(
        None, max_length=32, description="Telephone number of the provider"
    )
    address: str = Field(..., max_length=256, description="Address of the provider")
    email: EmailStr = Field(..., description="Email address of the provider")


class ProviderUpdate(BaseModel):
    """Model for updating a provider."""

    name: Optional[str] = Field(
        None, max_length=64, description="Updated name of the provider"
    )
    telephone_number: Optional[str] = Field(
        None, max_length=32, description="Updated telephone number of the provider"
    )
    address: Optional[str] = Field(
        None, max_length=256, description="Updated address of the provider"
    )
    email: Optional[EmailStr] = Field(
        None, description="Updated email address of the provider"
    )
