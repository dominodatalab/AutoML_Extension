"""Launch and manage external Domino Jobs for AutoML workflows.

Uses the public Domino Jobs v1/beta API for launch and status polling,
and the internal v4 stop endpoint (no public alternative).
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
    resolve_domino_nucleus_host,
    resolve_domino_project_id,
)

logger = logging.getLogger(__name__)


class DominoJobLauncher:
    """Wrapper around Domino Jobs REST API (public v1/beta + internal v4 stop)."""

    def __init__(self):
        self.settings = get_settings()

    @staticmethod
    def _remap_db_url_for_target(database_url: str, target_project_id: Optional[str] = None) -> str:
        """Pre-remap the database URL for a cross-project Domino Job.

        The App's DB lives at e.g. ``/mnt/data/automl_shared_db/automl.db``
        (local mount). A Job running in a *different* project sees the
        App's data under ``/mnt/imported/data/`` instead. Swap the prefix
        now so the job command contains the correct path from the start.

        When ``target_project_id`` matches the App's own project
        (``DOMINO_PROJECT_ID``), no remap is needed — the job runs in
        the same project and sees the same mounts.
        """
        # Same-project job — no remap needed
        app_project_id = os.environ.get("DOMINO_PROJECT_ID")
        if app_project_id and target_project_id and app_project_id == target_project_id:
            return database_url

        prefix = "sqlite:////"
        if not database_url.startswith(prefix):
            return database_url
        db_path = "/" + database_url[len(prefix):]

        # /mnt/data/<project>/ → /mnt/imported/data/<project>/
        if db_path.startswith("/mnt/data/"):
            remapped = "/mnt/imported/data/" + db_path[len("/mnt/data/"):]
            return f"sqlite:////{remapped.lstrip('/')}"

        # /domino/datasets/local/<name>/ → /domino/datasets/<name>/
        if db_path.startswith("/domino/datasets/local/"):
            remapped = "/domino/datasets/" + db_path[len("/domino/datasets/local/"):]
            return f"sqlite:////{remapped.lstrip('/')}"

        return database_url

    def _project_ref(self) -> Optional[str]:
        owner = self.settings.domino_project_owner or os.environ.get("DOMINO_PROJECT_OWNER")
        project_name = self.settings.domino_project_name or os.environ.get("DOMINO_PROJECT_NAME")
        if not owner or not project_name:
            return None
        return f"{owner}/{project_name}"

    def _host(self) -> Optional[str]:
        return self.settings.domino_api_host or os.environ.get("DOMINO_API_HOST")

    @staticmethod
    def _job_api_base_urls() -> list[Optional[str]]:
        """Prefer the direct Domino host for Jobs API calls, then fall back."""
        base_urls: list[Optional[str]] = []
        nucleus = resolve_domino_nucleus_host()
        if nucleus:
            base_urls.append(nucleus)
        base_urls.append(None)
        return base_urls

    async def _job_api_request(self, method: str, path: str, **kwargs) -> httpx.Response:
        """Call a Jobs API endpoint, preferring the direct host over the proxy."""
        last_exc: Optional[Exception] = None
        base_urls = self._job_api_base_urls()

        for index, base_url in enumerate(base_urls):
            request_kwargs = dict(kwargs)
            if base_url is not None:
                # Fail fast on the direct host so we can still fall back to the
                # proxy/default host when the direct route is unavailable.
                request_kwargs.setdefault("max_retries", 0)
            is_last = index == len(base_urls) - 1
            try:
                return await domino_request(
                    method,
                    path,
                    base_url=base_url,
                    **request_kwargs,
                )
            except httpx.HTTPStatusError as exc:
                last_exc = exc
                if is_last:
                    raise
                logger.warning(
                    "Domino Jobs API %s %s returned HTTP %s via direct host; "
                    "falling back to the default host",
                    method,
                    path,
                    exc.response.status_code,
                )
            except Exception as exc:
                last_exc = exc
                if is_last:
                    raise
                logger.warning(
                    "Domino Jobs API %s %s failed via direct host (%s); "
                    "falling back to the default host",
                    method,
                    path,
                    exc,
                )

        raise last_exc or RuntimeError(f"Domino Jobs API {method} {path} failed")

    @staticmethod
    def _build_cli_args(args: dict[str, Any]) -> list[str]:
        parts: list[str] = []
        for key, value in args.items():
            if value is None:
                continue
            flag = f"--{key.replace('_', '-')}"
            parts.extend([flag, str(value)])
        return parts

    def _build_command(self, module: str, args: dict[str, Any]) -> str:
        """Build a Domino Job command using a direct Python script invocation.

        Domino's job start endpoint can reject complex shell wrappers
        (for example, `bash -lc 'if ...'`) as invalid commands. Keep the
        command string simple and explicit.
        """
        cli_args = self._build_cli_args(args)
        script_rel_path = f"{module.replace('.', '/')}.py"
        service_dir = os.environ.get("AUTOML_SERVICE_DIR", "automl-service")
        normalized_service_dir = (service_dir or "").strip().rstrip("/")
        if not normalized_service_dir or normalized_service_dir in {".", "./"}:
            runner_path = script_rel_path
        else:
            runner_path = f"{normalized_service_dir}/{script_rel_path}"

        parts = ["python", runner_path, *cli_args]
        return " ".join(shlex.quote(part) for part in parts)

    @staticmethod
    def _extract_job_id(response: dict[str, Any]) -> Optional[str]:
        # v1 API wraps as {"job": {"id": ...}, "metadata": {...}}
        job = response.get("job", response)
        return (
            job.get("id")
            or job.get("jobId")
            or job.get("runId")
            or job.get("job_id")
            or job.get("run_id")
        )

    @staticmethod
    def _extract_execution_status(response: Any) -> Optional[str]:
        """Best-effort status extraction across Domino API response variants.

        Handles both v1/beta envelope (``{"job": {"status": {"executionStatus": ...}}}``)
        and legacy v4 flat responses.
        """
        if not isinstance(response, dict):
            return None

        # v1/beta API wraps as {"job": {...}}
        job = response.get("job", response)

        # v1/beta: job.status is an object with executionStatus, isCompleted, etc.
        status_obj = job.get("status") if isinstance(job.get("status"), dict) else {}
        if status_obj:
            es = status_obj.get("executionStatus")
            if isinstance(es, str) and es.strip():
                return es

        # Legacy v4: flat statuses dict
        statuses = job.get("statuses") if isinstance(job.get("statuses"), dict) else {}

        for candidate in (
            statuses.get("completionStatus"),
            job.get("completionStatus"),
            statuses.get("executionStatus"),
            job.get("executionStatus"),
            statuses.get("status"),
            statuses.get("lifecycleStatus"),
            job.get("lifecycleStatus"),
            statuses.get("state"),
            job.get("state"),
        ):
            if isinstance(candidate, str) and candidate.strip():
                return candidate

        # Fall back to status booleans (v1/beta or v4).
        bools = status_obj or statuses
        if bools.get("isFailed"):
            return "Failed"
        if bools.get("isStopped"):
            return "Stopped"
        if bools.get("isCompleted") or bools.get("isSuccess"):
            return "Succeeded"
        if bools.get("isRunning"):
            return "Running"
        if bools.get("isQueued") or bools.get("isPending"):
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

    async def _job_start(
        self,
        *,
        command: str,
        title: str,
        hardware_tier_name: Optional[str],
        environment_id: Optional[str],
        project_id: Optional[str] = None,
    ) -> dict[str, Any]:
        """Launch a Domino job via the public v1 Jobs API.

        Uses ``POST /api/jobs/v1/jobs`` which accepts the hardware tier
        name directly (no ID resolution needed).
        """
        env_project_id = resolve_domino_project_id()
        resolved_project_id = project_id or env_project_id
        logger.info(
            "[JOB LAUNCH] project_id arg=%s, env=%s, resolved=%s",
            project_id,
            env_project_id,
            resolved_project_id,
        )
        project_id = resolved_project_id

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
            "runCommand": command,
        }
        if commit_id:
            payload["commitId"] = commit_id
        if hardware_tier_name:
            payload["hardwareTier"] = hardware_tier_name
        if environment_id:
            payload["environmentId"] = environment_id
        if title:
            payload["title"] = title

        logger.info("[JOB LAUNCH] POST /api/jobs/v1/jobs payload: %s", json.dumps(payload, default=str))
        try:
            resp = await self._job_api_request("POST", "/api/jobs/v1/jobs", json=payload)
            result = resp.json()
            logger.info("[JOB LAUNCH] Response: %s", json.dumps(result, default=str)[:500])
            return result
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
                resp = await self._job_api_request("POST", "/api/jobs/v1/jobs", json=payload)
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
        job_config: Optional[dict] = None,
        title: Optional[str] = None,
        hardware_tier_name: Optional[str] = None,
        environment_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> dict[str, Any]:
        """Launch a training job in Domino."""
        if not self.settings.is_domino_environment:
            return {
                "success": False,
                "error": "Domino environment not configured for external job execution",
            }

        try:
            args: dict[str, Any] = {"job_id": job_id, "database_url": self._remap_db_url_for_target(self.settings.database_url, project_id)}
            if job_config is not None:
                args["job_config"] = json.dumps(job_config)

            command = self._build_command(
                "app.workers.domino_training_runner",
                args,
            )
            response = await self._job_start(
                command=command,
                title=title or f"AutoML Training {job_id[:8]}",
                hardware_tier_name=hardware_tier_name,
                environment_id=environment_id,
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
        environment_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> dict[str, Any]:
        """Launch an async EDA job in Domino."""
        if not self.settings.is_domino_environment:
            return {
                "success": False,
                "error": "Domino environment not configured for external EDA execution",
            }

        try:
            command = self._build_command(
                "app.workers.domino_eda_runner",
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
                    "database_url": self._remap_db_url_for_target(self.settings.database_url, project_id),
                    "project_id": project_id,
                },
            )
            response = await self._job_start(
                command=command,
                title=f"AutoML EDA {request_id[:8]}",
                hardware_tier_name=hardware_tier_name,
                environment_id=environment_id,
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
        """Fetch Domino job status via the public beta Jobs API."""
        if not self.settings.is_domino_environment:
            return {
                "success": False,
                "error": "Domino environment not configured",
            }
        try:
            resp = await self._job_api_request("GET", f"/api/jobs/beta/jobs/{domino_job_id}")
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
            resp = await self._job_api_request(
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
