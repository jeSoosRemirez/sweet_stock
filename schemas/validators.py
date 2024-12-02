"""Module for custom field validators."""


def quantity_weight_validator(quantity: int | None, weight: float | None):
    """Validates only one field presence."""
    if quantity and weight:
        raise ValueError("Should be provided either quantity or weight.")
