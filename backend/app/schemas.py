from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl


# ---------------------------------------------------------------------------
# User
# ---------------------------------------------------------------------------

class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str = Field(min_length=5, max_length=50)
    email: EmailStr


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = Field(default=None, min_length=5, max_length=50)
    email: Optional[EmailStr] = None


class UserRead(UserBase):
    id: UUID


# ---------------------------------------------------------------------------
# Product
# ---------------------------------------------------------------------------

class ProductBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str = Field(min_length=10, max_length=100)
    description: str = Field(min_length=10, max_length=500)
    image_url: HttpUrl


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: Optional[str] = Field(default=None, min_length=10, max_length=100)
    description: Optional[str] = Field(default=None, min_length=10, max_length=500)
    image_url: Optional[HttpUrl] = None


class ProductRead(ProductBase):
    id: UUID


# ---------------------------------------------------------------------------
# Review
# ---------------------------------------------------------------------------

class ReviewBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    rating: int = Field(ge=1, le=5)
    comment: str = Field(min_length=1, max_length=1000)


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    rating: Optional[int] = Field(default=None, ge=1, le=5)
    comment: Optional[str] = Field(default=None, min_length=1, max_length=1000)


class ReviewRead(ReviewBase):
    id: UUID
    product_id: UUID
    user_id: UUID
    created_at: datetime
