"""Launch and manage external Domino Jobs for AutoML workflows.

Uses direct Domino REST API calls via httpx instead of the python-domino SDK.
"""

import json
import logging
import os
import shlex
from functools import lru_cache
from typing import Any, Optional

import httpx

from app.config import get_settings
from app.core.domino_http import (
    domino_request,
    resolve_domino_project_id,
)

logger = logging.getLogger(__name__)


class DominoJobLauncher:
    """Wrapper around Domino V4 Jobs REST API."""

    _RUNNER_BASE = "/home/ubuntu/AutoML_Extension/automl-service/app/workers"
    TRAINING_RUNNER_PATH = f"{_RUNNER_BASE}/domino_training_runner.py"
    EDA_RUNNER_PATH = f"{_RUNNER_BASE}/domino_eda_runner.py"

    def __init__(self):
        self.settings = get_settings()
        environment_id = os.environ.get("DOMINO_ENVIRONMENT_ID")
        environment_revision_id = os.environ.get("DOMINO_ENVIRONMENT_REVISION_ID")
        if not environment_id or not environment_revision_id:
            raise RuntimeError(
                "DOMINO_ENVIRONMENT_ID and DOMINO_ENVIRONMENT_REVISION_ID must be set. "
                f"Got DOMINO_ENVIRONMENT_ID={environment_id!r}, "
                f"DOMINO_ENVIRONMENT_REVISION_ID={environment_revision_id!r}"
            )
        self.environment_id: str = environment_id
        self.environment_revision_id: str = environment_revision_id

    def _project_ref(self) -> Optional[str]:
        owner = self.settings.domino_project_owner or os.environ.get("DOMINO_PROJECT_OWNER")
        project_name = self.settings.domino_project_name or os.environ.get("DOMINO_PROJECT_NAME")
        if not owner or not project_name:
            return None
        return f"{owner}/{project_name}"

    def _host(self) -> Optional[str]:
        return self.settings.domino_api_host or os.environ.get("DOMINO_API_HOST")

    @staticmethod
    def _build_cli_args(args: dict[str, Any]) -> list[str]:
        parts: list[str] = []
        for key, value in args.items():
            if value is None:
                continue
            flag = f"--{key.replace('_', '-')}"
            parts.extend([flag, str(value)])
        return parts

    @staticmethod
    def _build_command_from_path(script_path: str, args: dict[str, Any]) -> str:
        """Build a Domino Job command referencing an absolute script path.

        Domino's /v4/jobs/start endpoint can reject complex shell wrappers
        (for example, `bash -lc 'if ...'`) as invalid commands. Keep the
        command string simple and explicit.
        """
        cli_args = DominoJobLauncher._build_cli_args(args)
        parts = ["python", script_path, *cli_args]
        return " ".join(shlex.quote(part) for part in parts)

    @staticmethod
    def _extract_job_id(response: dict[str, Any]) -> Optional[str]:
        return (
            response.get("id")
            or response.get("jobId")
            or response.get("runId")
            or response.get("job_id")
            or response.get("run_id")
        )

    @staticmethod
    def _extract_execution_status(response: Any) -> Optional[str]:
        """Best-effort status extraction across Domino API response variants."""
        if not isinstance(response, dict):
            return None

        statuses = response.get("statuses") if isinstance(response.get("statuses"), dict) else {}

        # Prefer terminal/completion fields when available.
        for candidate in (
            statuses.get("completionStatus"),
            response.get("completionStatus"),
            statuses.get("executionStatus"),
            response.get("executionStatus"),
            statuses.get("status"),
            response.get("status"),
            statuses.get("lifecycleStatus"),
            response.get("lifecycleStatus"),
            statuses.get("state"),
            response.get("state"),
        ):
            if isinstance(candidate, str) and candidate.strip():
                return candidate

        # Fall back to status booleans if present.
        if statuses.get("isFailed"):
            return "Failed"
        if statuses.get("isStopped"):
            return "Stopped"
        if statuses.get("isCompleted") or statuses.get("isSuccess"):
            return "Succeeded"
        if statuses.get("isRunning"):
            return "Running"
        if statuses.get("isQueued") or statuses.get("isPending"):
            return "Pending"

        return None

    @staticmethod
    def _resolve_launch_commit_id() -> tuple[Optional[str], Optional[str]]:
        """Resolve commit used for child Domino jobs.

        Only uses Domino-provided env vars which are guaranteed to exist in
        Domino's repo mirror.  Local ``git rev-parse HEAD`` is intentionally
        skipped because it may return commits that haven't been synced to
        Domino yet (e.g. after a push from a workspace).
        """
        for key in (
            "DOMINO_JOB_COMMIT_ID",
            "DOMINO_STARTING_COMMIT_ID",
        ):
            value = os.environ.get(key)
            if value:
                return value.strip(), key

        return None, None

    @staticmethod
    def _is_commit_not_found_error(error: Exception) -> bool:
        """Best-effort matcher for Domino commit-resolution failures."""
        message = DominoJobLauncher._error_context(error).lower()
        has_commit_hint = "commit" in message or "revision" in message
        has_lookup_failure_hint = any(
            hint in message
            for hint in (
                "not found",
                "unknown",
                "could not resolve",
                "cannot resolve",
                "invalid",
                "does not exist",
                "no such",
            )
        )
        return has_commit_hint and has_lookup_failure_hint

    @staticmethod
    def _response_status_code(error: Exception) -> Optional[int]:
        response = getattr(error, "response", None)
        status_code = getattr(response, "status_code", None)
        return status_code if isinstance(status_code, int) else None

    @staticmethod
    def _response_body(error: Exception) -> str:
        response = getattr(error, "response", None)
        if response is None:
            return ""

        candidates: list[str] = []

        response_text = getattr(response, "text", None)
        if isinstance(response_text, str) and response_text.strip():
            candidates.append(response_text.strip())

        try:
            payload = response.json()
        except Exception:
            payload = None

        if payload not in (None, "", [], {}):
            try:
                candidates.append(json.dumps(payload, ensure_ascii=True, sort_keys=True))
            except Exception:
                candidates.append(str(payload))

        deduped: list[str] = []
        for candidate in candidates:
            if candidate not in deduped:
                deduped.append(candidate)
        return " | ".join(deduped)

    @classmethod
    def _error_context(cls, error: Exception) -> str:
        parts: list[str] = []
        message = str(error).strip()
        if message:
            parts.append(message)
        status_code = cls._response_status_code(error)
        if status_code is not None:
            parts.append(f"http_status={status_code}")
        response_body = cls._response_body(error)
        if response_body:
            parts.append(response_body)
        return " | ".join(parts)

    @classmethod
    def _is_uninformative_bad_request(cls, error: Exception) -> bool:
        return cls._response_status_code(error) == 400 and not cls._response_body(error)

    @classmethod
    def _summarize_error(cls, error: Exception, *, max_chars: int = 2000) -> str:
        summary = cls._error_context(error) or str(error)
        return summary if len(summary) <= max_chars else f"{summary[:max_chars]}..."

    async def _resolve_hardware_tier_id(
        self, project_id: str, name: str
    ) -> Optional[str]:
        """Resolve a hardware tier name to its ID via the Domino API."""
        try:
            resp = await domino_request(
                "GET", f"/v4/projects/{project_id}/hardwareTiers"
            )
            for tier in resp.json():
                hw = tier.get("hardwareTier", tier)
                if hw.get("name") == name:
                    return hw.get("id")
            logger.warning(
                "Hardware tier '%s' not found in project %s; "
                "passing name as-is to job start",
                name,
                project_id,
            )
        except Exception:
            logger.warning(
                "Failed to resolve hardware tier '%s'; passing name as-is",
                name,
                exc_info=True,
            )
        return None

    async def _job_start(
        self,
        *,
        command: str,
        title: str,
        hardware_tier_name: Optional[str],
        project_id: Optional[str] = None,
    ) -> dict[str, Any]:
        """Launch a Domino job while pinning to the current commit and environment revision."""
        project_id = project_id or resolve_domino_project_id()

        # Resolve hardware tier name → ID (the SDK did this internally).
        hardware_tier_id = None
        if hardware_tier_name:
            hardware_tier_id = await self._resolve_hardware_tier_id(
                project_id, hardware_tier_name
            )

        commit_id, commit_source = self._resolve_launch_commit_id()
        if commit_id:
            logger.info(
                "Launching Domino child job pinned to commit %s (source=%s)",
                commit_id[:12],
                commit_source,
            )
        else:
            logger.warning(
                "No commit id resolved for Domino child job launch; "
                "Domino will use the project default branch/commit."
            )

        payload: dict[str, Any] = {
            "projectId": project_id,
            "commandToRun": command,
            "environmentId": self.environment_id,
            "environmentRevisionId": self.environment_revision_id,
        }
        if commit_id:
            payload["commitId"] = commit_id
        if hardware_tier_id:
            payload["overrideHardwareTierId"] = hardware_tier_id
        elif hardware_tier_name:
            # Fallback: pass name directly in case Domino accepts it.
            payload["overrideHardwareTierId"] = hardware_tier_name
        if title:
            payload["title"] = title

        try:
            resp = await domino_request("POST", "/v4/jobs/start", json=payload)
            return resp.json()
        except (httpx.HTTPStatusError, Exception) as e:
            pinned_commit = payload.get("commitId")
            # If the pinned commit cannot be resolved by Domino's repo mirror,
            # fall back to the project default instead of hard failing.
            if pinned_commit and (
                self._is_commit_not_found_error(e)
                or self._is_uninformative_bad_request(e)
            ):
                logger.warning(
                    "Domino could not resolve commit %s (%s). "
                    "Retrying launch without commit pin.",
                    str(pinned_commit)[:12],
                    self._summarize_error(e),
                )
                payload.pop("commitId", None)
                resp = await domino_request("POST", "/v4/jobs/start", json=payload)
                return resp.json()
            raise

    def _run_url(self, job_id: str) -> Optional[str]:
        host = self._host()
        project_ref = self._project_ref()
        if not host or not project_ref:
            return None
        return f"{host.rstrip('/')}/projects/{project_ref}/runs/{job_id}"

    async def start_training_job(
        self,
        job_id: str,
        file_path: str,
        title: Optional[str] = None,
        hardware_tier_name: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> dict[str, Any]:
        """Launch a training job in Domino."""
        if not self.settings.is_domino_environment:
            return {
                "success": False,
                "error": "Domino environment not configured for external job execution",
            }

        try:
            command = self._build_command_from_path(
                self.TRAINING_RUNNER_PATH,
                {"job_id": job_id, "file_path": file_path},
            )
            response = await self._job_start(
                command=command,
                title=title or f"AutoML Training {job_id[:8]}",
                hardware_tier_name=hardware_tier_name,
                project_id=project_id,
            )
            if not isinstance(response, dict):
                return {"success": False, "error": f"Unexpected response type: {type(response)}"}

            domino_job_id = self._extract_job_id(response)
            if not domino_job_id:
                return {"success": False, "error": f"Unable to parse Domino job id: {response}"}

            return {
                "success": True,
                "domino_job_id": domino_job_id,
                "domino_job_status": "Submitted",
                "domino_job_url": self._run_url(domino_job_id),
                "raw_response": response,
            }
        except Exception as e:
            logger.exception("Failed to launch Domino training job")
            return {"success": False, "error": self._summarize_error(e)}

    async def start_eda_job(
        self,
        request_id: str,
        mode: str,
        file_path: str,
        sample_size: int,
        sampling_strategy: str,
        stratify_column: Optional[str] = None,
        time_column: Optional[str] = None,
        target_column: Optional[str] = None,
        id_column: Optional[str] = None,
        rolling_window: Optional[int] = None,
        hardware_tier_name: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> dict[str, Any]:
        """Launch an async EDA job in Domino."""
        if not self.settings.is_domino_environment:
            return {
                "success": False,
                "error": "Domino environment not configured for external EDA execution",
            }

        try:
            command = self._build_command_from_path(
                self.EDA_RUNNER_PATH,
                {
                    "request_id": request_id,
                    "mode": mode,
                    "file_path": file_path,
                    "sample_size": sample_size,
                    "sampling_strategy": sampling_strategy,
                    "stratify_column": stratify_column,
                    "time_column": time_column,
                    "target_column": target_column,
                    "id_column": id_column,
                    "rolling_window": rolling_window,
                },
            )
            response = await self._job_start(
                command=command,
                title=f"AutoML EDA {request_id[:8]}",
                hardware_tier_name=hardware_tier_name,
                project_id=project_id,
            )
            if not isinstance(response, dict):
                return {"success": False, "error": f"Unexpected response type: {type(response)}"}

            domino_job_id = self._extract_job_id(response)
            if not domino_job_id:
                return {"success": False, "error": f"Unable to parse Domino job id: {response}"}

            return {
                "success": True,
                "domino_job_id": domino_job_id,
                "domino_job_status": "Submitted",
                "domino_job_url": self._run_url(domino_job_id),
                "raw_response": response,
            }
        except Exception as e:
            logger.exception("Failed to launch Domino EDA job")
            return {"success": False, "error": self._summarize_error(e)}

    async def get_job_status(self, domino_job_id: str) -> dict[str, Any]:
        """Fetch Domino job status."""
        if not self.settings.is_domino_environment:
            return {
                "success": False,
                "error": "Domino environment not configured",
            }
        try:
            resp = await domino_request("GET", f"/v4/jobs/{domino_job_id}")
            data = resp.json()
            execution_status = self._extract_execution_status(data)
            return {
                "success": True,
                "domino_job_id": domino_job_id,
                "domino_job_status": execution_status,
                "raw_response": data,
            }
        except Exception as e:
            logger.exception("Failed to fetch Domino job status")
            return {"success": False, "error": str(e), "domino_job_id": domino_job_id}

    async def stop_job(self, domino_job_id: str, commit_results: bool = False, project_id: Optional[str] = None) -> dict[str, Any]:
        """Stop an external Domino job."""
        if not self.settings.is_domino_environment:
            return {"success": False, "error": "Domino environment not configured"}
        try:
            project_id = project_id or resolve_domino_project_id()
            resp = await domino_request(
                "POST",
                "/v4/jobs/stop",
                json={
                    "projectId": project_id,
                    "jobId": domino_job_id,
                    "commitResults": commit_results,
                },
            )
            return {
                "success": True,
                "domino_job_id": domino_job_id,
                "status_code": resp.status_code,
                "body": resp.text,
            }
        except Exception as e:
            logger.exception("Failed to stop Domino job")
            return {"success": False, "error": str(e), "domino_job_id": domino_job_id}


@lru_cache()
def get_domino_job_launcher() -> DominoJobLauncher:
    """Get cached launcher instance."""
    return DominoJobLauncher()
