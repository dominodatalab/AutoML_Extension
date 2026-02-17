"""Launch and manage external Domino Jobs for AutoML workflows."""

import json
import logging
import os
import shlex
import subprocess
from functools import lru_cache
from typing import Any, Optional

from domino import Domino

from app.config import get_settings

logger = logging.getLogger(__name__)


class DominoJobLauncher:
    """Wrapper around python-domino job lifecycle APIs."""

    def __init__(self):
        self.settings = get_settings()
        self._domino_client: Optional[Domino] = None

    def _project_ref(self) -> Optional[str]:
        owner = self.settings.domino_project_owner or os.environ.get("DOMINO_PROJECT_OWNER")
        project_name = self.settings.domino_project_name or os.environ.get("DOMINO_PROJECT_NAME")
        if not owner or not project_name:
            return None
        return f"{owner}/{project_name}"

    def _host(self) -> Optional[str]:
        return self.settings.domino_api_host or os.environ.get("DOMINO_API_HOST")

    def _build_domino_client(self) -> Domino:
        project_ref = self._project_ref()
        host = self._host()
        if not project_ref:
            raise ValueError("DOMINO_PROJECT_OWNER and DOMINO_PROJECT_NAME are required")
        if not host:
            raise ValueError("DOMINO_API_HOST is required")

        kwargs: dict[str, Any] = {"project": project_ref, "host": host}
        api_proxy = os.environ.get("DOMINO_API_PROXY")
        if api_proxy:
            kwargs["api_proxy"] = api_proxy

        token_file = os.environ.get("DOMINO_TOKEN_FILE")
        if token_file:
            kwargs["domino_token_file"] = token_file
        else:
            api_key = self.settings.domino_user_api_key or os.environ.get("DOMINO_USER_API_KEY")
            if api_key:
                kwargs["api_key"] = api_key
            elif self.settings.effective_api_key:
                # Fallback for Domino deployments configured with bearer-style tokens.
                kwargs["auth_token"] = self.settings.effective_api_key

        return Domino(**kwargs)

    def _get_domino_client(self) -> Domino:
        if self._domino_client is None:
            self._domino_client = self._build_domino_client()
        return self._domino_client

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

        Domino's /v4/jobs/start endpoint can reject complex shell wrappers
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
        return (
            response.get("id")
            or response.get("jobId")
            or response.get("runId")
            or response.get("job_id")
            or response.get("run_id")
        )

    @staticmethod
    def _resolve_launch_commit_id() -> tuple[Optional[str], Optional[str]]:
        """Resolve commit used for child Domino jobs.

        Priority:
        1) Explicit env override
        2) Current checked-out git commit
        """
        for key in (
            "DOMINO_JOB_COMMIT_ID",
            "AUTOML_DOMINO_JOB_COMMIT_ID",
            "DOMINO_STARTING_COMMIT_ID",
            "DOMINO_COMMIT_ID",
            "DOMINO_GIT_COMMIT",
        ):
            value = os.environ.get(key)
            if value:
                return value.strip(), key

        try:
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                check=True,
                capture_output=True,
                text=True,
            )
            commit_id = result.stdout.strip()
            return (commit_id, "git_head") if commit_id else (None, None)
        except Exception:
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

    def _job_start(
        self,
        domino: Domino,
        *,
        command: str,
        title: str,
        hardware_tier_name: Optional[str],
        environment_id: Optional[str],
    ) -> Any:
        """Launch a Domino job while pinning to the current commit when possible."""
        kwargs: dict[str, Any] = {
            "command": command,
            "title": title,
            "hardware_tier_name": hardware_tier_name,
            "environment_id": environment_id,
        }
        commit_id, commit_source = self._resolve_launch_commit_id()
        if commit_id:
            kwargs["commit_id"] = commit_id
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

        try:
            return domino.job_start(**kwargs)
        except TypeError as e:
            message = str(e)
            if kwargs.get("commit_id") and "commit_id" in message and "unexpected keyword argument" in message:
                # Older python-domino versions may not expose commit_id.
                kwargs.pop("commit_id", None)
                return domino.job_start(**kwargs)
            raise
        except Exception as e:
            pinned_commit = kwargs.get("commit_id")
            # If git-derived HEAD cannot be resolved by Domino's repo mirror,
            # fall back to project default instead of hard failing submission.
            if (
                pinned_commit
                and commit_source == "git_head"
                and (
                    self._is_commit_not_found_error(e)
                    or self._is_uninformative_bad_request(e)
                )
            ):
                logger.warning(
                    "Domino could not resolve git-derived commit %s (%s). "
                    "Retrying launch without commit pin.",
                    str(pinned_commit)[:12],
                    self._summarize_error(e),
                )
                kwargs.pop("commit_id", None)
                return domino.job_start(**kwargs)
            raise

    def _run_url(self, job_id: str) -> Optional[str]:
        host = self._host()
        project_ref = self._project_ref()
        if not host or not project_ref:
            return None
        return f"{host.rstrip('/')}/projects/{project_ref}/runs/{job_id}"

    def start_training_job(
        self,
        job_id: str,
        title: Optional[str] = None,
        hardware_tier_name: Optional[str] = None,
        environment_id: Optional[str] = None,
    ) -> dict[str, Any]:
        """Launch a training job in Domino."""
        if not self.settings.is_domino_environment:
            return {
                "success": False,
                "error": "Domino environment not configured for external job execution",
            }

        try:
            domino = self._get_domino_client()
            command = self._build_command(
                "app.workers.domino_training_runner",
                {"job_id": job_id},
            )
            response = self._job_start(
                domino,
                command=command,
                title=title or f"AutoML Training {job_id[:8]}",
                hardware_tier_name=hardware_tier_name,
                environment_id=environment_id,
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

    def start_eda_job(
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
    ) -> dict[str, Any]:
        """Launch an async EDA job in Domino."""
        if not self.settings.is_domino_environment:
            return {
                "success": False,
                "error": "Domino environment not configured for external EDA execution",
            }

        try:
            domino = self._get_domino_client()
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
                },
            )
            response = self._job_start(
                domino,
                command=command,
                title=f"AutoML EDA {request_id[:8]}",
                hardware_tier_name=hardware_tier_name,
                environment_id=environment_id,
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

    def get_job_status(self, domino_job_id: str) -> dict[str, Any]:
        """Fetch Domino job status."""
        if not self.settings.is_domino_environment:
            return {
                "success": False,
                "error": "Domino environment not configured",
            }
        try:
            response = self._get_domino_client().job_status(domino_job_id)
            execution_status = (
                response.get("statuses", {}).get("executionStatus")
                if isinstance(response, dict)
                else None
            )
            return {
                "success": True,
                "domino_job_id": domino_job_id,
                "domino_job_status": execution_status,
                "raw_response": response,
            }
        except Exception as e:
            logger.exception("Failed to fetch Domino job status")
            return {"success": False, "error": str(e), "domino_job_id": domino_job_id}

    def stop_job(self, domino_job_id: str, commit_results: bool = False) -> dict[str, Any]:
        """Stop an external Domino job."""
        if not self.settings.is_domino_environment:
            return {"success": False, "error": "Domino environment not configured"}
        try:
            response = self._get_domino_client().job_stop(domino_job_id, commit_results=commit_results)
            status_code = getattr(response, "status_code", None)
            success = status_code is None or 200 <= status_code < 300
            return {
                "success": success,
                "domino_job_id": domino_job_id,
                "status_code": status_code,
                "body": getattr(response, "text", None),
            }
        except Exception as e:
            logger.exception("Failed to stop Domino job")
            return {"success": False, "error": str(e), "domino_job_id": domino_job_id}


@lru_cache()
def get_domino_job_launcher() -> DominoJobLauncher:
    """Get cached launcher instance."""
    return DominoJobLauncher()
