"""Pydantic encoders."""

from fastapi.encoders import jsonable_encoder
from datetime import date


def pyd_to_dict(pyd_data) -> dict:
    """Transforms pydantic model to dict."""
    data = jsonable_encoder(pyd_data)
    resp = {}
    for k, v in data.items():
        try:
            v = date.fromisoformat(v)
        except ValueError:
            ...
        except TypeError:
            ...
        finally:
            resp.update({k: v})
    return resp
