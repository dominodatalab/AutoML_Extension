"""Resolve Domino project metadata using the generated Public API client."""

import logging
from dataclasses import dataclass
from typing import Optional

from app.api.generated.domino_public_api_client.api.projects import get_project_by_id
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
        # Use raw HTTP instead of the generated parser to avoid enum
        # deserialization failures (e.g. GitServiceProviderV1 case mismatch).
        kwargs = get_project_by_id._get_kwargs(project_id=project_id)
        response = client.get_httpx_client().request(**kwargs)

        if response.status_code != 200:
            logger.warning(
                "Project %s lookup returned status %s",
                project_id,
                response.status_code,
            )
            return None

        data = response.json()
        name = data.get("name")
        owner = data.get("ownerUsername")

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
