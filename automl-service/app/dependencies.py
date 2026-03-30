"""Dependency injection for FastAPI routes."""

from contextlib import asynccontextmanager
from typing import AsyncGenerator, Optional

from fastapi import HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import async_session_maker


def get_request_project_id(projectId: Optional[str] = Query(None)) -> str:
    """Require projectId query parameter, raising 400 if absent."""
    if not projectId:
        raise HTTPException(status_code=400, detail="projectId query parameter is required")
    return projectId


async def get_project_context(
    projectId: Optional[str] = Query(None),
) -> tuple[Optional[str], Optional[str], Optional[str]]:
    """Resolve project id/name/owner from projectId query param via Domino API.

    Returns (project_id, project_name, project_owner).
    """
    if not projectId:
        raise HTTPException(status_code=400, detail="projectId query parameter is required")

    from app.services.project_resolver import resolve_project

    info = await resolve_project(projectId)
    if info:
        return info.id, info.name, info.owner_username

    raise HTTPException(status_code=400, detail=f"Could not resolve project {projectId}")


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Get database session dependency."""
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()


@asynccontextmanager
async def get_db_session():
    """Get database session as async context manager for manual use."""
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()
