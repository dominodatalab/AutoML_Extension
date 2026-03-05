"""Health check endpoints."""

import os
from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.config import get_settings
from app.dependencies import get_db

router = APIRouter()


@router.get("/user")
async def get_current_user(request: Request):
    """Get current user and project context from Domino headers/environment.

    Returns:
        - username: The authenticated user from domino-username header
        - initials: User initials for UI display
        - project_id: Current project ID from DOMINO_PROJECT_ID
        - project_name: Current project name from DOMINO_PROJECT_NAME

    This information determines which jobs are shown by default in listings.
    """
    settings = get_settings()

    # Domino injects the username in the domino-username header
    username = request.headers.get("domino-username", "Anonymous")

    # Generate initials from username
    if username and username != "Anonymous":
        parts = username.replace(".", " ").replace("_", " ").split()
        if len(parts) >= 2:
            initials = (parts[0][0] + parts[-1][0]).upper()
        else:
            initials = username[:2].upper()
    else:
        initials = "?"

    # Get project info from environment
    project_id = settings.domino_project_id or os.environ.get("DOMINO_PROJECT_ID")
    project_name = settings.domino_project_name or os.environ.get("DOMINO_PROJECT_NAME")
    project_owner = settings.domino_project_owner or os.environ.get("DOMINO_PROJECT_OWNER")

    return {
        "username": username,
        "initials": initials,
        "project_id": project_id,
        "project_name": project_name,
        "project_owner": project_owner,
        "is_domino_environment": settings.is_domino_environment,
    }


@router.get("/capabilities")
async def get_capabilities():
    """Return platform capabilities for frontend feature gating."""
    settings = get_settings()
    standalone = settings.standalone_mode
    return {
        "standalone_mode": standalone,
        "domino_jobs": not standalone,
        "mlflow_tracking": not standalone,
        "model_registry": not standalone,
        "model_deployment": not standalone,
    }


@router.get("")
async def health_check():
    """Basic health check endpoint."""
    settings = get_settings()
    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.app_version,
    }


@router.get("/ready")
async def readiness_check(db: AsyncSession = Depends(get_db)):
    """Readiness check - verifies database and dependencies."""
    settings = get_settings()
    checks = {
        "database": False,
        "domino": False,
    }

    # Check database connection
    try:
        await db.execute(text("SELECT 1"))
        checks["database"] = True
    except Exception as e:
        checks["database"] = str(e)

    # Check Domino connectivity
    if settings.is_domino_environment:
        checks["domino"] = True
    else:
        checks["domino"] = "Not in Domino environment"

    all_healthy = all(v is True for v in checks.values())

    return {
        "status": "ready" if all_healthy else "degraded",
        "checks": checks,
    }
