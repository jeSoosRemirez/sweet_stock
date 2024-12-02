"""Business logic for managing products."""

from models import Product
from repository.repos import ProductRepo, StorageRepo
from schemas.product import ProductCreate, ProductUpdate
from utils.pydantic_encoder import pyd_to_dict
from typing import Optional


class ProductService:
    """Class for handling product business logic."""

    @classmethod
    async def create_product(
        cls,
        body: ProductCreate,
    ) -> Product:
        """Create a new product and update storage accordingly."""
        storage = await StorageRepo.retrieve_by_id(id_value=body.storage)
        if not storage:
            raise ValueError(f"Storage with ID {body.storage} not found.")

        res_weight = storage.storing_weight + (body.available_weight or 0)
        res_quantity = storage.storing_quantity + (body.available_quantity or 0)

        if res_weight > storage.max_weight:
            raise ValueError(
                f"Exceeded max weight of storage: {res_weight} > {storage.max_weight}."
            )
        if res_quantity > storage.max_quantity:
            raise ValueError(
                f"Exceeded max quantity of storage: {res_quantity} > {storage.max_quantity}."
            )

        await StorageRepo.update_by_id(
            id_value=body.storage,
            storing_weight=res_weight,
            storing_quantity=res_quantity,
        )

        product = await ProductRepo.create_one(pyd_to_dict(body))
        return product

    @classmethod
    async def get_product(
        cls,
        product_id: str,
    ) -> Optional[Product]:
        """Retrieve a product by its ID."""
        product = await ProductRepo.retrieve_by_id(id_value=product_id)
        if not product:
            raise ValueError(f"Product with ID {product_id} not found.")
        return product

    @classmethod
    async def list_products(
        cls,
    ) -> list[Product]:
        """Retrieve a product by its ID."""
        product = await ProductRepo.retrieve()
        return product

    @classmethod
    async def update_product(
        cls,
        product_id: str,
        body: ProductUpdate,
    ) -> Product:
        """Update an existing product."""
        existing_product = await ProductRepo.retrieve_by_id(id_value=product_id)
        if not existing_product:
            raise ValueError(f"Product with ID {product_id} not found.")

        updated_product = await ProductRepo.update_by_id(
            id_value=product_id,
            **pyd_to_dict(body),
        )
        return updated_product

    @classmethod
    async def delete_product(
        cls,
        product_id: str,
    ) -> Product:
        """Delete a product by its ID."""
        product = await ProductRepo.retrieve_by_id(id_value=product_id)
        if not product:
            raise ValueError(f"Product with ID {product_id} not found.")

        deleted_product = await ProductRepo.delete_by_id(id_value=product_id)
        return deleted_product
