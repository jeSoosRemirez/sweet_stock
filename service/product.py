"""Business-logic for products."""

from models import Product
from repository.product import ProductRepo
from repository.storage import StorageRepo
from schemas.product import CreateProductSchema, UpdateProductSchema
from utils.pydantic_encoder import pyd_to_dict


class ProductService:
    """Class for products business-logic."""

    @classmethod
    async def create_product(
        cls,
        body: CreateProductSchema,
    ) -> Product:
        """Create product record."""
        storage = await StorageRepo.retrieve_by_id(id_value=body.storage)
        res_weight = storage.storing_weight + body.available_weight
        res_quantity = storage.storing_quantity + body.available_quantity
        if (res_quantity > storage.max_quantity) or (res_weight > storage.max_weight):
            raise ValueError

        await StorageRepo.update_by_id(
            body.storage,
            **{
                "storing_weight": res_weight,
                "storing_quantity": res_quantity,
            },
        )
        product = await ProductRepo.create_one(
            pyd_to_dict(body),
        )
        return product

    @classmethod
    async def get_product(
        cls,
        product_id: str,
    ) -> Product:
        """Get product record."""
        product = await ProductRepo.retrieve_by_id(id_value=product_id)
        return product

    @classmethod
    async def update_product(
        cls,
        product_id: str,
        body: UpdateProductSchema,
    ) -> Product:
        """Update product record."""
        product = await ProductRepo.update_by_id(
            product_id,
            **body,
        )
        return product

    @classmethod
    async def delete_product(
        cls,
        product_id: str,
    ) -> Product:
        """Update product record."""
        product = await ProductRepo.delete_by_id(id_value=product_id)
        return product
