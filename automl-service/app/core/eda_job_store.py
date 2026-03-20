"""DB-backed metadata/result store for async EDA jobs."""

import logging
from typing import Any, Optional

from app.core.utils import utc_now

logger = logging.getLogger(__name__)


def _utc_now_iso() -> str:
    return utc_now().isoformat()


class EDAJobStore:
    """Persist async EDA job state in the shared SQLite database."""

    async def create_request(
        self,
        db,
        request_id: str,
        mode: str,
        request_payload: dict[str, Any],
        owner: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> dict[str, Any]:
        from app.db import crud

        eda = await crud.create_eda_request(
            db, request_id, mode, request_payload, owner=owner, project_id=project_id,
        )
        return self._to_dict(eda)

    async def get_request(self, db, request_id: str) -> Optional[dict[str, Any]]:
        from app.db import crud

        eda = await crud.get_eda_request(db, request_id)
        if eda is None:
            return None
        return self._to_dict(eda)

    async def update_request(
        self, db, request_id: str, **updates: Any
    ) -> Optional[dict[str, Any]]:
        from app.db import crud

        eda = await crud.update_eda_request(db, request_id, **updates)
        if eda is None:
            return None
        return self._to_dict(eda)

    async def write_result(
        self, db, request_id: str, mode: str, result: dict[str, Any]
    ) -> None:
        from app.db import crud

        await crud.write_eda_result(db, request_id, mode, result)

    async def get_result(self, db, request_id: str) -> Optional[dict[str, Any]]:
        from app.db import crud

        result_payload = await crud.get_eda_result(db, request_id)
        if result_payload is None:
            return None
        # Return in the same shape the filesystem store used
        eda = await crud.get_eda_request(db, request_id)
        return {
            "request_id": request_id,
            "mode": eda.mode if eda else None,
            "result": result_payload,
        }

    async def write_error(self, db, request_id: str, error_message: str) -> None:
        from app.db import crud

        await crud.write_eda_error(db, request_id, error_message)

    async def get_error(self, db, request_id: str) -> Optional[str]:
        from app.db import crud

        eda = await crud.get_eda_request(db, request_id)
        if eda is None:
            return None
        return eda.error

    @staticmethod
    def _to_dict(eda) -> dict[str, Any]:
        """Convert EDAResult ORM object to dict matching the old filesystem format."""
        return {
            "request_id": eda.id,
            "status": eda.status,
            "mode": eda.mode,
            "owner": getattr(eda, "owner", None),
            "project_id": getattr(eda, "project_id", None),
            "domino_job_id": eda.domino_job_id,
            "domino_job_status": eda.domino_job_status,
            "domino_job_url": getattr(eda, "domino_job_url", None),
            "error": eda.error,
            "created_at": str(eda.created_at) if eda.created_at else None,
            "updated_at": str(eda.updated_at) if eda.updated_at else None,
        }


_store_instance: Optional[EDAJobStore] = None


def get_eda_job_store() -> EDAJobStore:
    """Get cached EDA job store."""
    global _store_instance
    if _store_instance is None:
        _store_instance = EDAJobStore()
    return _store_instance
