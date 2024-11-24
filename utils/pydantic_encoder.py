"""Pydantic encoders."""

from fastapi.encoders import jsonable_encoder
from datetime import datetime


def pyd_to_dict(pyd_data, skip_date: bool = False) -> dict:
    """Transforms pydantic model to dict."""
    data = jsonable_encoder(pyd_data)
    resp = {}
    if not skip_date:
        for k, v in data.items():
            try:
                v = datetime.fromisoformat(v)
            except ValueError:
                ...
            except TypeError:
                ...
            finally:
                resp.update({k: v})
        return resp
    return data
