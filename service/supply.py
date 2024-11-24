"""Business logic for managing supply records."""

from models import Supply
from repository.repos import SupplyRepo, StorageRepo, ProductRepo, UserRepo
from schemas.supply import SupplyCreate, SupplyUpdate, SupplyType
from utils.pydantic_encoder import pyd_to_dict
from typing import Optional


class SupplyService:
    """Service class for managing supplies."""

    @classmethod
    async def create_supply(
        cls,
        body: SupplyCreate,
    ) -> Supply:
        """Create a new supply record with foreign key validation and max weight/quantity checks."""
        # Ensure the foreign key references are valid
        if body.supply_type == SupplyType.REDIRECTION.value:
            from_storage = await StorageRepo.retrieve_by_id(
                id_value=body.from_storage_id
            )
            if not from_storage:
                raise ValueError(f"Storage with ID {body.from_storage_id} not found.")

        to_storage = await StorageRepo.retrieve_by_id(id_value=body.to_storage_id)
        if not to_storage:
            raise ValueError(f"Storage with ID {body.to_storage_id} not found.")

        product = await ProductRepo.retrieve_by_id(id_value=body.product_id)
        if not product:
            raise ValueError(f"Product with ID {body.product_id} not found.")

        # Check if adding the supply would exceed the max weight/quantity in from_storage
        if body.supply_type == SupplyType.REDIRECTION.value:
            new_from_storage_weight = from_storage.storing_weight + (body.weight or 0)
            new_from_storage_quantity = from_storage.storing_quantity + (
                body.quantity or 0
            )
            if new_from_storage_weight > from_storage.max_weight:
                raise ValueError(
                    f"Adding supply exceeds the max weight of {from_storage.max_weight} in storage {from_storage.id}."
                )
            if new_from_storage_quantity > from_storage.max_quantity:
                raise ValueError(
                    f"Adding supply exceeds the max quantity of {from_storage.max_quantity} in storage {from_storage.id}."
                )

        # Check if adding the supply would exceed the max weight/quantity in to_storage
        new_to_storage_weight = to_storage.storing_weight + (body.weight or 0)
        new_to_storage_quantity = to_storage.storing_quantity + (body.quantity or 0)
        if new_to_storage_weight > to_storage.max_weight:
            raise ValueError(
                f"Adding supply exceeds the max weight of {to_storage.max_weight} in storage {to_storage.id}."
            )
        if new_to_storage_quantity > to_storage.max_quantity:
            raise ValueError(
                f"Adding supply exceeds the max quantity of {to_storage.max_quantity} in storage {to_storage.id}."
            )

        # Proceed with creating the supply record
        supply = await SupplyRepo.create_one(pyd_to_dict(body))

        # Update storage records with new values after the supply
        if body.supply_type == SupplyType.REDIRECTION.value:
            await StorageRepo.update_by_id(
                body.from_storage_id,
                storing_weight=from_storage.storing_weight - body.weight,
                storing_quantity=from_storage.storing_quantity - body.quantity,
            )

        await StorageRepo.update_by_id(
            body.to_storage_id,
            storing_weight=new_to_storage_weight,
            storing_quantity=new_to_storage_quantity,
        )

        return supply

    @classmethod
    async def get_supply(
        cls,
        supply_id: str,
    ) -> Optional[Supply]:
        """Retrieve a supply record by its ID."""
        supply = await SupplyRepo.retrieve_by_id(id_value=supply_id)
        if not supply:
            raise ValueError(f"Supply with ID {supply_id} not found.")
        return supply

    @classmethod
    async def list_supplies(
        cls,
    ) -> Optional[Supply]:
        """Retrieve a supply record by its ID."""
        supply = await SupplyRepo.retrieve()
        return supply

    @classmethod
    async def update_supply(
        cls,
        supply_id: str,
        body: SupplyUpdate,
    ) -> Supply:
        """Update an existing supply record with foreign key validation and max weight/quantity checks."""
        # Ensure the supply exists
        supply = await SupplyRepo.retrieve_by_id(id_value=supply_id)
        if not supply:
            raise ValueError(f"Supply with ID {supply_id} not found.")

        # Ensure the foreign key references are valid
        if supply.supply_type == SupplyType.REDIRECTION.value:
            from_storage = await StorageRepo.retrieve_by_id(
                id_value=body.from_storage_id
            )
            if not from_storage:
                raise ValueError(f"Storage with ID {body.from_storage_id} not found.")

        to_storage = await StorageRepo.retrieve_by_id(id_value=body.to_storage_id)
        if not to_storage:
            raise ValueError(f"Storage with ID {body.to_storage_id} not found.")

        product = await ProductRepo.retrieve_by_id(id_value=body.product_id)
        if not product:
            raise ValueError(f"Product with ID {body.product_id} not found.")

        user = await UserRepo.retrieve_by_id(id_value=body.user_id)
        if not user:
            raise ValueError(f"User with ID {body.user_id} not found.")

        if supply.supply_type == SupplyType.REDIRECTION.value:
            # Check if adding the supply would exceed the max weight/quantity in from_storage
            new_from_storage_weight = from_storage.storing_weight + (body.weight or 0)
            new_from_storage_quantity = from_storage.storing_quantity + (
                body.quantity or 0
            )
            if new_from_storage_weight > from_storage.max_weight:
                raise ValueError(
                    f"Adding supply exceeds the max weight of {from_storage.max_weight} in storage {from_storage.id}."
                )
            if new_from_storage_quantity > from_storage.max_quantity:
                raise ValueError(
                    f"Adding supply exceeds the max quantity of {from_storage.max_quantity} in storage {from_storage.id}."
                )

        # Check if adding the supply would exceed the max weight/quantity in to_storage
        new_to_storage_weight = to_storage.storing_weight + (body.weight or 0)
        new_to_storage_quantity = to_storage.storing_quantity + (body.quantity or 0)
        if new_to_storage_weight > to_storage.max_weight:
            raise ValueError(
                f"Adding supply exceeds the max weight of {to_storage.max_weight} in storage {to_storage.id}."
            )
        if new_to_storage_quantity > to_storage.max_quantity:
            raise ValueError(
                f"Adding supply exceeds the max quantity of {to_storage.max_quantity} in storage {to_storage.id}."
            )

        # Proceed with updating the supply record
        updated_supply = await SupplyRepo.update_by_id(
            id_value=supply_id, **pyd_to_dict(body)
        )

        # Update storage records with new values after the supply
        if supply.supply_type == SupplyType.REDIRECTION.value:
            await StorageRepo.update_by_id(
                body.from_storage_id,
                storing_weight=to_storage.storing_weight - body.weight,
                storing_quantity=to_storage.storing_quantity - body.quantity,
            )

        await StorageRepo.update_by_id(
            body.to_storage_id,
            storing_weight=new_to_storage_weight,
            storing_quantity=new_to_storage_quantity,
        )

        return updated_supply

    @classmethod
    async def delete_supply(
        cls,
        supply_id: str,
    ) -> Supply:
        """Delete a supply record by its ID."""
        supply = await SupplyRepo.retrieve_by_id(id_value=supply_id)
        if not supply:
            raise ValueError(f"Supply with ID {supply_id} not found.")

        # Proceed with deletion
        deleted_supply = await SupplyRepo.delete_by_id(id_value=supply_id)

        # Update storage records to remove the supply's effects
        if supply.supply_type == SupplyType.REDIRECTION.value:
            from_storage = await StorageRepo.retrieve_by_id(
                id_value=supply.from_storage_id
            )
            if from_storage:
                await StorageRepo.update_by_id(
                    supply.from_storage_id,
                    storing_weight=from_storage.storing_weight - supply.weight,
                    storing_quantity=from_storage.storing_quantity - supply.quantity,
                )

        to_storage = await StorageRepo.retrieve_by_id(id_value=supply.to_storage_id)
        if to_storage:
            await StorageRepo.update_by_id(
                supply.to_storage_id,
                storing_weight=to_storage.storing_weight - supply.weight,
                storing_quantity=to_storage.storing_quantity - supply.quantity,
            )

        return deleted_supply
