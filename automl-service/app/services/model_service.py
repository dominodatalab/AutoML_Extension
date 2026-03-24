"""Service helpers for model registry routes."""

from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.model import RegisteredModelResponse
from app.db import crud


async def list_registered_models_response(
    db: AsyncSession,
    project_id: Optional[str] = None,
    owner: Optional[str] = None,
) -> list[RegisteredModelResponse]:
    """Return all registered models in API response shape, optionally scoped by project/owner."""
    models = await crud.get_registered_models(db, project_id=project_id, owner=owner)
    return [RegisteredModelResponse.model_validate(m) for m in models]
