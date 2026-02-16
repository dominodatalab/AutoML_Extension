"""Launch and manage external Domino Jobs for AutoML workflows."""

import logging
import os
import shlex
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
    def _build_module_command(module: str, args: dict[str, Any]) -> str:
        parts = ["python", "-m", module]
        for key, value in args.items():
            if value is None:
                continue
            flag = f"--{key.replace('_', '-')}"
            parts.extend([flag, str(value)])
        return " ".join(shlex.quote(part) for part in parts)

    def _build_command(self, module: str, args: dict[str, Any]) -> str:
        """Build a Domino Job command that works from repo root or service dir."""
        module_command = self._build_module_command(module, args)
        service_dir = os.environ.get("AUTOML_SERVICE_DIR", "automl-service")
        quoted_service_dir = shlex.quote(service_dir)
        shell_script = (
            f"if [ -d {quoted_service_dir} ]; then "
            f"cd {quoted_service_dir}; "
            "elif [ ! -f app/main.py ]; then "
            "echo 'Unable to locate AutoML service directory. "
            "Set AUTOML_SERVICE_DIR to the backend path.' >&2; "
            "exit 1; "
            "fi; "
            f"{module_command}"
        )
        return f"bash -lc {shlex.quote(shell_script)}"

    @staticmethod
    def _extract_job_id(response: dict[str, Any]) -> Optional[str]:
        return (
            response.get("id")
            or response.get("jobId")
            or response.get("runId")
            or response.get("job_id")
            or response.get("run_id")
        )

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
            response = domino.job_start(
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
            return {"success": False, "error": str(e)}

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
            response = domino.job_start(
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
            return {"success": False, "error": str(e)}

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
