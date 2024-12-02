"""Business logic for managing order records."""

from models import Order
from repository.repos import OrderRepo, StorageRepo, ProductRepo
from schemas.order import OrderCreate, OrderUpdate
from utils.pydantic_encoder import pyd_to_dict
from typing import Optional


class OrderService:
    """Service class for managing orders."""

    @classmethod
    async def create_order(
        cls,
        body: OrderCreate,
    ) -> Order:
        """Create a new order record with product availability and max constraints checks."""
        # Ensure the foreign key references are valid
        storage = await StorageRepo.retrieve_by_id(id_value=body.storage_id)
        if not storage:
            raise ValueError(f"Storage with ID {body.storage_id} not found.")

        product = await ProductRepo.retrieve_by_id(id_value=body.product_id)
        if not product:
            raise ValueError(f"Product with ID {body.product_id} not found.")

        # Check if the product exists in the specified storage
        # product_in_storage = next(
        #     (p for p in storage.products if p.product_id == body.product_id), None
        # )
        # if not product_in_storage:
        #     raise ValueError(
        #         f"Product with ID {body.product_id} not found in storage {body.storage_id}."
        #     )

        # Check if the requested quantity/weight exceeds the available amount in storage
        # available_weight = product_in_storage.available_weight
        # available_quantity = product_in_storage.available_quantity
        available_weight = storage.max_weight - product.available_weight
        available_quantity = storage.max_quantity - product.available_quantity

        if body.weight and body.weight > available_weight:
            raise ValueError(
                f"Requested weight exceeds available weight of {available_weight} for product {body.product_id} in storage {body.storage_id}."
            )

        if body.quantity and body.quantity > available_quantity:
            raise ValueError(
                f"Requested quantity exceeds available quantity of {available_quantity} for product {body.product_id} in storage {body.storage_id}."
            )

        # Proceed with creating the order record
        order = await OrderRepo.create_one(pyd_to_dict(body))

        # Update storage records to reflect the order
        new_available_weight = available_weight - (body.weight or 0)
        new_available_quantity = available_quantity - (body.quantity or 0)

        await StorageRepo.update_by_id(
            storage.id,
            storing_weight=new_available_weight,
            storing_quantity=new_available_quantity,
        )

        return order

    @classmethod
    async def get_order(
        cls,
        order_id: str,
    ) -> Optional[Order]:
        """Retrieve an order record by its ID."""
        order = await OrderRepo.retrieve_by_id(id_value=order_id)
        if not order:
            raise ValueError(f"Order with ID {order_id} not found.")
        return order

    @classmethod
    async def list_orders(
        cls,
    ) -> list[Order]:
        """Retrieve an order record by its ID."""
        order = await OrderRepo.retrieve()
        return order

    @classmethod
    async def update_order(
        cls,
        order_id: str,
        body: OrderUpdate,
    ) -> Order:
        """Update an existing order record with product availability and max constraints checks."""
        # Ensure the order exists
        order = await OrderRepo.retrieve_by_id(id_value=order_id)
        if not order:
            raise ValueError(f"Order with ID {order_id} not found.")

        # Ensure the foreign key references are valid
        storage = await StorageRepo.retrieve_by_id(id_value=body.storage_id)
        if not storage:
            raise ValueError(f"Storage with ID {body.storage_id} not found.")

        product = await ProductRepo.retrieve_by_id(id_value=body.product_id)
        if not product:
            raise ValueError(f"Product with ID {body.product_id} not found.")

        # Check if the product exists in the specified storage
        product_in_storage = next(
            (p for p in storage.products if p.product_id == body.product_id), None
        )
        if not product_in_storage:
            raise ValueError(
                f"Product with ID {body.product_id} not found in storage {body.storage_id}."
            )

        # Check if the requested quantity/weight exceeds the available amount in storage
        available_weight = product_in_storage.available_weight
        available_quantity = product_in_storage.available_quantity

        if body.weight and body.weight > available_weight:
            raise ValueError(
                f"Requested weight exceeds available weight of {available_weight} for product {body.product_id} in storage {body.storage_id}."
            )

        if body.quantity and body.quantity > available_quantity:
            raise ValueError(
                f"Requested quantity exceeds available quantity of {available_quantity} for product {body.product_id} in storage {body.storage_id}."
            )

        # Proceed with updating the order record
        updated_order = await OrderRepo.update_by_id(
            id_value=order_id, **pyd_to_dict(body)
        )

        # Update storage records to reflect the order
        new_available_weight = available_weight - (body.weight or 0)
        new_available_quantity = available_quantity - (body.quantity or 0)

        await StorageRepo.update_by_id(
            storage.id,
            storing_weight=new_available_weight,
            storing_quantity=new_available_quantity,
        )

        return updated_order

    @classmethod
    async def delete_order(
        cls,
        order_id: str,
    ) -> Order:
        """Delete an order record by its ID."""
        order = await OrderRepo.retrieve_by_id(id_value=order_id)
        if not order:
            raise ValueError(f"Order with ID {order_id} not found.")

        # Proceed with deletion
        deleted_order = await OrderRepo.delete_by_id(id_value=order_id)

        # Update storage records to remove the order's effects
        storage = await StorageRepo.retrieve_by_id(id_value=order.storage_id)
        product_in_storage = next(
            (p for p in storage.products if p.product_id == order.product_id), None
        )

        if product_in_storage:
            new_available_weight = product_in_storage.available_weight + order.weight
            new_available_quantity = (
                product_in_storage.available_quantity + order.quantity
            )

            await StorageRepo.update_by_id(
                storage.id,
                storing_weight=new_available_weight,
                storing_quantity=new_available_quantity,
            )

        return deleted_order
