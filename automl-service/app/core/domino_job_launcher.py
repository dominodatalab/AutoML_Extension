"""Launch and manage external Domino Jobs for AutoML workflows.

Uses the generated Domino Public API client for job start and status,
and the internal v4 stop endpoint (no public alternative).
"""

import json
import logging
import os
import shlex
from functools import lru_cache
from typing import Any, Optional

from app.config import get_settings
from app.core.domino_http import (
    domino_request,
    get_domino_public_api_client_sync,
    resolve_domino_api_host,
    resolve_domino_project_id,
)

logger = logging.getLogger(__name__)


class DominoJobLauncher:
    """Wrapper around Domino Jobs REST API (public v1/beta + internal v4 stop)."""

    def __init__(self):
        self.settings = get_settings()

        # The App container always has these env vars — they identify the
        # compute environment used to build the App image.  Child jobs must
        # use the same environment so the AutoML code and its dependencies
        # are available.
        self.environment_id: Optional[str] = os.environ.get("DOMINO_ENVIRONMENT_ID")
        self.environment_revision_id: Optional[str] = os.environ.get("DOMINO_ENVIRONMENT_REVISION_ID")
        if not self.environment_id:
            logger.warning(
                "DOMINO_ENVIRONMENT_ID not set — child jobs will use the project default environment"
            )

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
        project_id: Optional[str] = None,
    ) -> dict[str, Any]:
        """Launch a Domino job via the generated public API client.

        Uses the ``start_job`` endpoint from the generated client which
        posts to ``POST /api/jobs/v1/jobs``.

        The environment is pinned to the App's own environment via
        ``DOMINO_ENVIRONMENT_ID`` / ``DOMINO_ENVIRONMENT_REVISION_ID``
        so that child jobs have the same dependencies available.
        """
        from app.api.generated.domino_public_api_client.api.jobs import start_job
        from app.api.generated.domino_public_api_client.models.new_job_v1 import NewJobV1
        from app.api.generated.domino_public_api_client.types import UNSET

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

        body = NewJobV1(
            project_id=project_id,
            run_command=command,
            commit_id=commit_id if commit_id else UNSET,
            hardware_tier=hardware_tier_name if hardware_tier_name else UNSET,
            environment_id=self.environment_id if self.environment_id else UNSET,
            title=title if title else UNSET,
        )

        logger.info("[JOB LAUNCH] POST /api/jobs/v1/jobs body: %s", body.to_dict())
        client = get_domino_public_api_client_sync()
        try:
            response = await start_job.asyncio_detailed(client=client, body=body)
            result = response.parsed
            if result is None:
                raise RuntimeError(
                    f"Domino Jobs API returned unexpected status {response.status_code}"
                )
            result_dict = result.to_dict() if hasattr(result, "to_dict") else dict(result)
            logger.info("[JOB LAUNCH] Response: %s", json.dumps(result_dict, default=str)[:500])
            return result_dict
        except Exception as e:
            pinned_commit = commit_id
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
                body.commit_id = UNSET
                response = await start_job.asyncio_detailed(client=client, body=body)
                result = response.parsed
                if result is None:
                    raise RuntimeError(
                        f"Domino Jobs API returned unexpected status {response.status_code}"
                    )
                return result.to_dict() if hasattr(result, "to_dict") else dict(result)
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
        job_config: Optional[dict] = None,
        title: Optional[str] = None,
        hardware_tier_name: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> dict[str, Any]:
        """Launch a training job in Domino.

        *file_path* is the resolved path to the training data file as it
        will appear inside the Domino Job container (e.g.
        ``/domino/datasets/local/my-dataset/train.csv``).  The path is
        resolved at job-creation time so the worker doesn't need dataset
        API access.
        """
        if not self.settings.is_domino_environment:
            return {
                "success": False,
                "error": "Domino environment not configured for external job execution",
            }

        try:
            args: dict[str, Any] = {
                "job_id": job_id,
                "file_path": file_path,
                "database_url": self.settings.database_url,
            }
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
                    "database_url": self.settings.database_url,
                    "project_id": project_id,
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
        """Fetch Domino job status via the generated public API client."""
        if not self.settings.is_domino_environment:
            return {
                "success": False,
                "error": "Domino environment not configured",
            }
        try:
            from app.api.generated.domino_public_api_client.api.jobs import get_job_details

            client = get_domino_public_api_client_sync()
            response = await get_job_details.asyncio_detailed(
                job_id=domino_job_id, client=client,
            )
            data = response.parsed
            if data is None:
                return {
                    "success": False,
                    "error": f"Domino Jobs API returned status {response.status_code}",
                    "domino_job_id": domino_job_id,
                }
            data_dict = data.to_dict() if hasattr(data, "to_dict") else dict(data)
            execution_status = self._extract_execution_status(data_dict)
            return {
                "success": True,
                "domino_job_id": domino_job_id,
                "domino_job_status": execution_status,
                "raw_response": data_dict,
            }
        except Exception as e:
            logger.exception("Failed to fetch Domino job status")
            return {"success": False, "error": str(e), "domino_job_id": domino_job_id}

    async def stop_job(self, domino_job_id: str, commit_results: bool = False, project_id: Optional[str] = None) -> dict[str, Any]:
        """Stop an external Domino job.

        Uses the internal v4 endpoint — no public API alternative exists.
        """
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
