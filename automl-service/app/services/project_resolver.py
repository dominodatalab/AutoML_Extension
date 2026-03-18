"""Resolve Domino project metadata from the V4 projects API using domino_http."""

import logging
from dataclasses import dataclass
from typing import Optional

from app.core.domino_http import domino_request

logger = logging.getLogger(__name__)

# In-memory cache — project metadata is immutable for the app's lifetime.
_cache: dict[str, "ProjectInfo"] = {}


@dataclass(frozen=True)
class ProjectInfo:
    id: str
    name: str
    owner_username: str


async def resolve_project(project_id: str) -> Optional[ProjectInfo]:
    """Resolve project name and owner from the Domino V4 projects API.

    Returns cached ProjectInfo on success, None on any failure.
    """
    if project_id in _cache:
        return _cache[project_id]

    try:
        # Use shared domino_http helper (handles host and auth acquisition + retries)
        resp = await domino_request("GET", f"/v4/projects/{project_id}")
        data = resp.json() if resp.text else {}
        name = data.get("name")
        owner = data.get("ownerUsername") or data.get("owner", {}).get("userName")

        if not name or not owner:
            logger.warning(
                "Project %s response missing name/owner: %s",
                project_id,
                {k: data.get(k) for k in ("name", "ownerUsername", "owner")},
            )
            return None

        info = ProjectInfo(id=project_id, name=name, owner_username=owner)
        _cache[project_id] = info
        logger.info("Resolved project %s → %s/%s", project_id, owner, name)
        return info

    except Exception as exc:
        logger.exception("Error resolving project %s: %s", project_id, exc)
        return None
