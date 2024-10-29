"""Endpoints for the product."""

from typing import Annotated
from fastapi import APIRouter, Query
from schemas.product import ProductSchema, CreateProductSchema
from service.product import ProductService

router = APIRouter(prefix="/product", tags=["product"])


@router.post("")
async def create_product(body: CreateProductSchema) -> ProductSchema:
    """Create method for Product model."""
    product = await ProductService.create_product(
        body=body,
    )

    if not product:
        return {"message": "Something went wrong."}

    return product


@router.get("/{id}")
async def get_product(product_id: Annotated[str, Query(alias="id")]) -> ProductSchema:
    """Get method for Product model."""
    product = await ProductService.get_product(
        product_id=product_id,
    )

    if not product:
        return {"message": "Something went wrong."}

    return product
