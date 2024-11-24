from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from enum import Enum
from datetime import datetime


class RoleType(str, Enum):
    """Enum for user roles."""

    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    WORKER = "WORKER"


class UserRetrieve(BaseModel):
    """Model for retrieving a user."""

    id: str
    role: RoleType
    username: str
    email: EmailStr
    full_name: Optional[str]
    created_at: Optional[str | datetime]
    updated_at: Optional[str | datetime]

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    """Model for creating a user."""

    role: RoleType = Field(..., description="Role of the user")
    username: str = Field(..., max_length=64, description="Unique username")
    email: EmailStr = Field(..., description="Unique email address")
    full_name: Optional[str] = Field(
        None, max_length=128, description="Full name of the user"
    )
    password: str = Field(
        ..., min_length=8, max_length=128, description="User password"
    )


class UserUpdate(BaseModel):
    """Model for updating a user."""

    role: Optional[RoleType] = Field(None, description="Updated role of the user")
    username: Optional[str] = Field(None, max_length=64, description="Updated username")
    email: Optional[EmailStr] = Field(None, description="Updated email address")
    full_name: Optional[str] = Field(
        None, max_length=128, description="Updated full name"
    )
    password: Optional[str] = Field(
        None, min_length=8, max_length=128, description="Updated password"
    )
