"""Resolve Domino project metadata using the generated Public API client."""

import logging
from dataclasses import dataclass
from typing import Optional

from app.api.generated.domino_public_api_client.api.projects import get_project_by_id
from app.api.generated.domino_public_api_client.models.project_envelope_v1 import (
    ProjectEnvelopeV1,
)
from app.core.domino_http import get_domino_public_api_client_sync

logger = logging.getLogger(__name__)

# In-memory cache — project metadata is immutable for the app's lifetime.
_cache: dict[str, "ProjectInfo"] = {}


@dataclass(frozen=True)
class ProjectInfo:
    id: str
    name: str
    owner_username: str


async def resolve_project(project_id: str) -> Optional[ProjectInfo]:
    """Resolve project name and owner from the Domino Projects API.

    Returns cached ProjectInfo on success, None on any failure.
    """
    if project_id in _cache:
        return _cache[project_id]

    try:
        client = get_domino_public_api_client_sync()
        result = get_project_by_id.sync(project_id, client=client)

        if not isinstance(result, ProjectEnvelopeV1):
            logger.warning(
                "Project %s lookup returned unexpected type: %s",
                project_id,
                type(result).__name__,
            )
            return None

        project = result.project
        name = project.name
        owner = project.owner_username

        if not name or not owner:
            logger.warning(
                "Project %s response missing name/owner",
                project_id,
            )
            return None

        info = ProjectInfo(id=project_id, name=name, owner_username=owner)
        _cache[project_id] = info
        logger.info("Resolved project %s → %s/%s", project_id, owner, name)
        return info

    except Exception as exc:
        logger.exception("Error resolving project %s: %s", project_id, exc)
        return None
