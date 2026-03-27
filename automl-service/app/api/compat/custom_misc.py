"""Miscellaneous custom compatibility routes."""

from datetime import datetime
from typing import Optional

from fastapi import FastAPI, Request

from app.api.compat.common import lazy_import


def register_custom_misc_routes(app: FastAPI) -> None:
    """Register miscellaneous /svc* routes."""

    @app.get("/svcuser")
    async def svc_user(projectId: Optional[str] = None):
        return await lazy_import("app.api.routes.health", "get_current_user")(projectId)

    @app.get("/svccapabilities")
    async def svc_capabilities(request: Request):
        return await lazy_import("app.api.routes.health", "get_capabilities")(request)

    @app.get("/svcping")
    async def svc_ping():
        return {"success": True, "message": "pong", "timestamp": datetime.now().isoformat()}
