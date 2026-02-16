"""File-backed metadata/result store for async EDA jobs."""

import json
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any, Optional

from app.config import get_settings


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class EDAJobStore:
    """Persist async EDA job state in a shared filesystem path."""

    def __init__(self):
        settings = get_settings()
        self.base_dir = Path(settings.eda_results_path)
        self.meta_dir = self.base_dir / "meta"
        self.result_dir = self.base_dir / "results"
        self.error_dir = self.base_dir / "errors"
        self._ensure_dirs()

    def _ensure_dirs(self) -> None:
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.meta_dir.mkdir(parents=True, exist_ok=True)
        self.result_dir.mkdir(parents=True, exist_ok=True)
        self.error_dir.mkdir(parents=True, exist_ok=True)

    def _meta_path(self, request_id: str) -> Path:
        return self.meta_dir / f"{request_id}.json"

    def _result_path(self, request_id: str) -> Path:
        return self.result_dir / f"{request_id}.json"

    def _error_path(self, request_id: str) -> Path:
        return self.error_dir / f"{request_id}.txt"

    @staticmethod
    def _write_json(path: Path, payload: dict[str, Any]) -> None:
        tmp_path = path.with_suffix(path.suffix + ".tmp")
        with tmp_path.open("w", encoding="utf-8") as f:
            json.dump(payload, f)
        tmp_path.replace(path)

    def create_request(
        self,
        request_id: str,
        mode: str,
        request_payload: dict[str, Any],
    ) -> dict[str, Any]:
        meta = {
            "request_id": request_id,
            "status": "pending",
            "mode": mode,
            "request": request_payload,
            "domino_job_id": None,
            "created_at": _utc_now_iso(),
            "updated_at": _utc_now_iso(),
            "error": None,
        }
        self._write_json(self._meta_path(request_id), meta)
        return meta

    def get_request(self, request_id: str) -> Optional[dict[str, Any]]:
        path = self._meta_path(request_id)
        if not path.exists():
            return None
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def update_request(self, request_id: str, **updates: Any) -> Optional[dict[str, Any]]:
        current = self.get_request(request_id)
        if current is None:
            return None
        current.update(updates)
        current["updated_at"] = _utc_now_iso()
        self._write_json(self._meta_path(request_id), current)
        return current

    def write_result(self, request_id: str, mode: str, result: dict[str, Any]) -> None:
        payload = {
            "request_id": request_id,
            "mode": mode,
            "result": result,
            "completed_at": _utc_now_iso(),
        }
        self._write_json(self._result_path(request_id), payload)

    def get_result(self, request_id: str) -> Optional[dict[str, Any]]:
        path = self._result_path(request_id)
        if not path.exists():
            return None
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def write_error(self, request_id: str, error_message: str) -> None:
        with self._error_path(request_id).open("w", encoding="utf-8") as f:
            f.write(error_message)

    def get_error(self, request_id: str) -> Optional[str]:
        path = self._error_path(request_id)
        if not path.exists():
            return None
        with path.open("r", encoding="utf-8") as f:
            return f.read()


@lru_cache()
def get_eda_job_store() -> EDAJobStore:
    """Get cached EDA job store."""
    return EDAJobStore()
