"""Artifact cleanup service for jobs.

Handles deletion of model files, MLflow runs, upload files, logs,
and registered model records. Also detects and cleans orphaned artifacts.
"""

import logging
import os
import shutil
from functools import lru_cache
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.config import get_settings
from app.db import crud
from app.db.models import Job, JobStatus

logger = logging.getLogger(__name__)


class CleanupService:
    """Manages artifact cleanup for training jobs."""

    def __init__(self):
        self.settings = get_settings()

    async def delete_job_artifacts(self, job: Job, db: AsyncSession) -> dict:
        """Delete all artifacts for a single job.

        Each step is wrapped in try/except so partial failures don't block the rest.
        """
        errors = []
        model_files_deleted = False
        model_files_size_bytes = 0
        upload_file_deleted = False
        mlflow_runs_deleted = 0
        job_logs_deleted = 0
        registered_model_deleted = False

        # 1. Model files
        if job.model_path and os.path.exists(job.model_path):
            try:
                model_files_size_bytes = _dir_size(job.model_path)
                shutil.rmtree(job.model_path)
                model_files_deleted = True
                logger.info(f"Deleted model dir {job.model_path} ({model_files_size_bytes} bytes)")
            except Exception as e:
                errors.append(f"model_files: {e}")
                logger.warning(f"Failed to delete model dir {job.model_path}: {e}")

        # 2. Upload file (only if data_source == "upload" and no other job shares it)
        if (
            job.data_source == "upload"
            and job.file_path
        ):
            try:
                ref_count = await crud.count_jobs_with_file_path(db, job.file_path)
                # ref_count includes the current job (not yet deleted from DB)
                if ref_count <= 1:
                    # Delete from local filesystem if present
                    if os.path.exists(job.file_path):
                        os.remove(job.file_path)
                        upload_file_deleted = True
                        logger.info(f"Deleted upload file {job.file_path}")

                    # Also delete from the Domino dataset snapshot (best-effort)
                    await self._delete_file_from_dataset(job, errors)
                    if not upload_file_deleted:
                        upload_file_deleted = True
                else:
                    logger.info(
                        f"Skipped upload file {job.file_path} — "
                        f"shared by {ref_count} jobs"
                    )
            except Exception as e:
                errors.append(f"upload_file: {e}")
                logger.warning(f"Failed to delete upload file {job.file_path}: {e}")

        # 3. MLflow runs (tagged with job_id)
        try:
            mlflow_runs_deleted = _delete_mlflow_runs(job.id)
        except Exception as e:
            errors.append(f"mlflow_runs: {e}")
            logger.warning(f"Failed to delete MLflow runs for job {job.id}: {e}")

        # 4. Job logs
        try:
            job_logs_deleted = await crud.delete_job_logs(db, job.id)
        except Exception as e:
            errors.append(f"job_logs: {e}")
            logger.warning(f"Failed to delete logs for job {job.id}: {e}")

        # 5. Registered model
        if job.is_registered and job.registered_model_name:
            try:
                _delete_mlflow_registered_model(job.registered_model_name)
                registered_model_deleted = True
            except Exception as e:
                errors.append(f"mlflow_registered_model: {e}")
                logger.warning(
                    f"Failed to delete MLflow registered model "
                    f"{job.registered_model_name}: {e}"
                )
            try:
                await crud.delete_registered_models_for_job(db, job.id)
            except Exception as e:
                errors.append(f"db_registered_model: {e}")
                logger.warning(f"Failed to delete DB registered model for job {job.id}: {e}")

        return {
            "model_files_deleted": model_files_deleted,
            "model_files_size_bytes": model_files_size_bytes,
            "upload_file_deleted": upload_file_deleted,
            "mlflow_runs_deleted": mlflow_runs_deleted,
            "job_logs_deleted": job_logs_deleted,
            "registered_model_deleted": registered_model_deleted,
            "errors": errors,
        }

    async def preview_cleanup(
        self,
        db: AsyncSession,
        statuses: list[JobStatus],
        older_than_days: Optional[int] = None,
        project_id: Optional[str] = None,
    ) -> dict:
        """Dry-run: summarize what would be deleted without actually deleting."""
        jobs = await crud.get_jobs_for_cleanup(db, statuses, older_than_days, project_id=project_id)

        total_model_size = 0
        total_upload_size = 0
        total_mlflow_runs = 0
        total_logs = 0
        job_summaries = []

        for job in jobs:
            model_size = 0
            if job.model_path and os.path.exists(job.model_path):
                model_size = _dir_size(job.model_path)
            total_model_size += model_size

            upload_size = 0
            if (
                job.data_source == "upload"
                and job.file_path
                and os.path.exists(job.file_path)
            ):
                ref_count = await crud.count_jobs_with_file_path(db, job.file_path)
                if ref_count <= 1:
                    upload_size = os.path.getsize(job.file_path)
            total_upload_size += upload_size

            mlflow_count = _count_mlflow_runs(job.id)
            total_mlflow_runs += mlflow_count

            log_count = await crud.count_job_logs(db, job.id)
            total_logs += log_count

            job_summaries.append({
                "job_id": job.id,
                "name": job.name,
                "status": job.status.value,
                "created_at": job.created_at.isoformat(),
                "model_size_bytes": model_size,
                "upload_size_bytes": upload_size,
                "mlflow_runs": mlflow_count,
                "log_count": log_count,
            })

        return {
            "job_count": len(jobs),
            "total_model_size_bytes": total_model_size,
            "total_upload_size_bytes": total_upload_size,
            "total_mlflow_runs": total_mlflow_runs,
            "total_logs": total_logs,
            "jobs": job_summaries,
        }

    async def bulk_cleanup(
        self,
        db: AsyncSession,
        statuses: list[JobStatus],
        older_than_days: Optional[int] = None,
        project_id: Optional[str] = None,
    ) -> dict:
        """Delete artifacts and DB rows for all matching jobs."""
        jobs = await crud.get_jobs_for_cleanup(db, statuses, older_than_days, project_id=project_id)

        total_model_size = 0
        total_upload_files = 0
        total_mlflow_runs = 0
        total_logs = 0
        all_errors = []
        deleted_job_ids = []

        for job in jobs:
            result = await self.delete_job_artifacts(job, db)
            total_model_size += result["model_files_size_bytes"]
            if result["upload_file_deleted"]:
                total_upload_files += 1
            total_mlflow_runs += result["mlflow_runs_deleted"]
            total_logs += result["job_logs_deleted"]
            all_errors.extend(result["errors"])

            await crud.delete_job(db, job.id)
            deleted_job_ids.append(job.id)

        return {
            "jobs_deleted": len(deleted_job_ids),
            "deleted_job_ids": deleted_job_ids,
            "total_model_size_bytes": total_model_size,
            "total_upload_files_deleted": total_upload_files,
            "total_mlflow_runs_deleted": total_mlflow_runs,
            "total_logs_deleted": total_logs,
            "errors": all_errors,
        }

    async def _delete_file_from_dataset(self, job: Job, errors: list) -> None:
        """Best-effort deletion of an uploaded file from the Domino dataset snapshot."""
        try:
            from app.services.storage_resolver import get_storage_resolver, DATASET_NAME

            dataset_id = getattr(job, "dataset_id", None)
            file_path = job.file_path or ""

            if not dataset_id or not file_path:
                return

            # Derive the relative path within the dataset.
            # Mount paths end with /{dataset_name}/, so split on that.
            marker = f"/{DATASET_NAME}/"
            if marker in file_path:
                relative_path = file_path.split(marker, 1)[1]
            else:
                # Fallback: use just the uploads/... portion
                parts = file_path.split("/uploads/", 1)
                if len(parts) == 2:
                    relative_path = f"uploads/{parts[1]}"
                else:
                    logger.debug(
                        "Cannot derive relative dataset path from %s", file_path
                    )
                    return

            resolver = get_storage_resolver()
            rw_sid = await resolver.get_rw_snapshot_id(dataset_id)
            if not rw_sid:
                logger.debug(
                    "No RW snapshot ID for dataset %s, skipping dataset file deletion",
                    dataset_id,
                )
                return

            await resolver.delete_snapshot_files(rw_sid, [relative_path])
        except Exception as e:
            errors.append(f"dataset_file_delete: {e}")
            logger.warning(
                "Failed to delete file from dataset snapshot for job %s: %s",
                job.id,
                e,
            )

    def _collect_artifact_roots(self) -> tuple[list[str], list[str]]:
        """Return (model_roots, upload_roots) including dataset mount paths."""
        from app.services.storage_resolver import _MOUNT_TEMPLATES, DATASET_NAME

        model_roots = [self.settings.models_path]
        upload_roots = [self.settings.uploads_path]

        # Probe known dataset mount locations for automl-extension
        for template in _MOUNT_TEMPLATES:
            mount = template.format(name=DATASET_NAME)
            models_candidate = os.path.join(mount, "models")
            uploads_candidate = os.path.join(mount, "uploads")
            if os.path.isdir(models_candidate) and models_candidate not in model_roots:
                model_roots.append(models_candidate)
            if os.path.isdir(uploads_candidate) and uploads_candidate not in upload_roots:
                upload_roots.append(uploads_candidate)

        return model_roots, upload_roots

    def find_orphans(self) -> dict:
        """Scan model, upload, and mlruns directories for orphaned artifacts.

        Orphans are dirs/files on disk with no matching job in the DB.
        Note: This is a sync method since it only reads the filesystem.
        The caller should pass DB-checked results for job existence.
        """
        orphaned_models = []
        orphaned_uploads = []

        model_roots, upload_roots = self._collect_artifact_roots()

        # Scan models directories for job_* dirs
        for models_path in model_roots:
            if os.path.isdir(models_path):
                for entry in os.scandir(models_path):
                    if entry.is_dir() and entry.name.startswith("job_"):
                        size = _dir_size(entry.path)
                        orphaned_models.append({
                            "path": entry.path,
                            "size_bytes": size,
                            "name": entry.name,
                        })

        # Scan uploads directories
        for uploads_path in upload_roots:
            if os.path.isdir(uploads_path):
                for entry in os.scandir(uploads_path):
                    if entry.is_file():
                        orphaned_uploads.append({
                            "path": entry.path,
                            "size_bytes": entry.stat().st_size,
                            "name": entry.name,
                        })

        # Scan mlruns directory for run folders
        orphaned_mlflow_runs = _scan_mlruns_for_orphans()

        return {
            "orphaned_models": orphaned_models,
            "orphaned_uploads": orphaned_uploads,
            "orphaned_mlflow_runs": orphaned_mlflow_runs,
            "total_orphaned_model_size_bytes": sum(
                m["size_bytes"] for m in orphaned_models
            ),
            "total_orphaned_upload_size_bytes": sum(
                u["size_bytes"] for u in orphaned_uploads
            ),
            "total_orphaned_mlflow_run_size_bytes": sum(
                r["size_bytes"] for r in orphaned_mlflow_runs
            ),
        }

    async def find_orphans_checked(self, db: AsyncSession) -> dict:
        """Find orphans with DB validation (async)."""
        raw = self.find_orphans()

        # Filter models: only keep dirs whose job_id doesn't exist in DB
        checked_models = []
        for entry in raw["orphaned_models"]:
            # Extract job_id: dir name format is job_{uuid}_{date} or job_{uuid}
            name = entry["name"]
            parts = name.split("_", 2)  # ["job", "{uuid-start}", ...]
            if len(parts) >= 2:
                # Try to reconstruct the job_id (UUID) from the dir name
                # Dir format: job_{job_id}_{timestamp} — but job_id itself contains hyphens
                # Safer approach: strip "job_" prefix and check if any job has model_path == this path
                job = await _find_job_for_model_path(db, entry["path"])
                if job is None:
                    checked_models.append(entry)

        # Filter uploads: only keep files not referenced by any job
        checked_uploads = []
        for entry in raw["orphaned_uploads"]:
            ref_count = await crud.count_jobs_with_file_path(db, entry["path"])
            if ref_count == 0:
                checked_uploads.append(entry)

        # Filter mlflow runs: only keep runs whose job_id tag doesn't match any DB job
        checked_mlflow_runs = []
        for entry in raw["orphaned_mlflow_runs"]:
            job_id = entry.get("job_id")
            if job_id:
                job = await crud.get_job(db, job_id)
                if job is None:
                    checked_mlflow_runs.append(entry)
            else:
                # No job_id tag — consider it orphaned
                checked_mlflow_runs.append(entry)

        return {
            "orphaned_models": checked_models,
            "orphaned_uploads": checked_uploads,
            "orphaned_mlflow_runs": checked_mlflow_runs,
            "total_orphaned_model_size_bytes": sum(
                m["size_bytes"] for m in checked_models
            ),
            "total_orphaned_upload_size_bytes": sum(
                u["size_bytes"] for u in checked_uploads
            ),
            "total_orphaned_mlflow_run_size_bytes": sum(
                r["size_bytes"] for r in checked_mlflow_runs
            ),
        }

    async def delete_orphans(self, db: AsyncSession) -> dict:
        """Delete orphaned model dirs, upload files, and MLflow run folders."""
        orphans = await self.find_orphans_checked(db)
        deleted_models = []
        deleted_uploads = []
        deleted_mlflow_runs = []
        errors = []

        for entry in orphans["orphaned_models"]:
            try:
                shutil.rmtree(entry["path"])
                deleted_models.append(entry)
                logger.info(f"Deleted orphaned model dir: {entry['path']}")
            except Exception as e:
                errors.append(f"model {entry['path']}: {e}")

        for entry in orphans["orphaned_uploads"]:
            try:
                os.remove(entry["path"])
                deleted_uploads.append(entry)
                logger.info(f"Deleted orphaned upload: {entry['path']}")
            except Exception as e:
                errors.append(f"upload {entry['path']}: {e}")

        for entry in orphans["orphaned_mlflow_runs"]:
            try:
                run_path = entry["path"]
                shutil.rmtree(run_path)
                deleted_mlflow_runs.append(entry)
                logger.info(f"Deleted orphaned MLflow run: {run_path}")
                # Remove experiment directory if empty (only meta.yaml remains)
                exp_dir = os.path.dirname(run_path)
                if os.path.isdir(exp_dir):
                    remaining = [e for e in os.listdir(exp_dir) if e != "meta.yaml"]
                    if not remaining:
                        shutil.rmtree(exp_dir)
                        logger.info(f"Deleted empty MLflow experiment dir: {exp_dir}")
            except Exception as e:
                errors.append(f"mlflow_run {entry['path']}: {e}")

        return {
            "models_deleted": len(deleted_models),
            "uploads_deleted": len(deleted_uploads),
            "mlflow_runs_deleted": len(deleted_mlflow_runs),
            "total_size_freed_bytes": (
                sum(m["size_bytes"] for m in deleted_models)
                + sum(u["size_bytes"] for u in deleted_uploads)
                + sum(r["size_bytes"] for r in deleted_mlflow_runs)
            ),
            "errors": errors,
        }


# ── Helpers ──────────────────────────────────────────────────────────

def _dir_size(path: str) -> int:
    """Calculate total size of a directory tree in bytes."""
    total = 0
    try:
        for dirpath, _dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.isfile(fp):
                    total += os.path.getsize(fp)
    except OSError:
        pass
    return total


def _delete_mlflow_runs(job_id: str) -> int:
    """Delete all MLflow runs tagged with job_id. Returns count deleted.

    client.delete_run() works against both remote (Domino) and local tracking
    servers. On remote servers that's the full cleanup — the server manages its
    own storage. For local file-based MLflow, delete_run() only soft-deletes
    (marks as deleted in meta.yaml), so we additionally remove run folders and
    .trash entries from disk. _remove_mlflow_run_from_disk() is a no-op when
    the artifact URI is non-local (e.g. https://, s3://). After runs are
    removed, this also attempts to delete touched non-default experiments that
    have no active runs remaining.
    """
    try:
        from mlflow import MlflowClient
        client = MlflowClient()
        runs = client.search_runs(
            experiment_ids=["0"],  # default experiment
            filter_string=f"tags.job_id = '{job_id}'",
        )
        # Also search all experiments
        try:
            experiments = client.search_experiments()
            exp_ids = [e.experiment_id for e in experiments]
            if exp_ids:
                runs = client.search_runs(
                    experiment_ids=exp_ids,
                    filter_string=f"tags.job_id = '{job_id}'",
                )
        except Exception:
            pass  # Fall back to default experiment runs

        count = 0
        touched_experiment_ids = set()
        for run in runs:
            run_id = run.info.run_id
            experiment_id = getattr(run.info, "experiment_id", None)
            if experiment_id is not None:
                touched_experiment_ids.add(str(experiment_id))
            client.delete_run(run_id)
            _remove_mlflow_run_from_disk(run)
            count += 1

        experiments_deleted = _delete_empty_mlflow_experiments(
            client=client,
            experiment_ids=touched_experiment_ids,
        )
        if experiments_deleted > 0:
            logger.info(
                "Deleted %s MLflow experiment(s) after cleaning runs for job %s",
                experiments_deleted,
                job_id,
            )
        return count
    except ImportError:
        logger.debug("MLflow not available, skipping run cleanup")
        return 0
    except Exception as e:
        logger.warning(f"MLflow run cleanup failed for job {job_id}: {e}")
        raise


def _remove_mlflow_run_from_disk(run) -> None:
    """Remove an MLflow run's folder and .trash entry from disk.

    artifact_uri is typically file:///abs/path/mlruns/{exp_id}/{run_id}/artifacts.
    We go up one level to get the run folder, then also check .trash/.
    """
    try:
        artifact_uri = run.info.artifact_uri or ""
        if not artifact_uri.startswith("file:"):
            return  # Remote storage — nothing to delete locally

        from urllib.parse import unquote
        from pathlib import Path

        # file:///path/to/mlruns/exp_id/run_id/artifacts → run folder
        artifact_path = Path(unquote(artifact_uri.removeprefix("file://")))
        run_folder = artifact_path.parent  # …/mlruns/{exp_id}/{run_id}

        if run_folder.is_dir():
            shutil.rmtree(run_folder)
            logger.info(f"Deleted MLflow run folder: {run_folder}")

        # Clean .trash entry: mlruns/.trash/{run_id}
        mlruns_dir = run_folder.parent.parent  # …/mlruns
        trash_folder = mlruns_dir / ".trash" / run.info.run_id
        if trash_folder.is_dir():
            shutil.rmtree(trash_folder)
            logger.info(f"Deleted MLflow trash entry: {trash_folder}")

        # Remove experiment directory if empty (only meta.yaml remains)
        exp_dir = run_folder.parent  # …/mlruns/{exp_id}
        if exp_dir.is_dir():
            remaining = [e.name for e in exp_dir.iterdir() if e.name != "meta.yaml"]
            if not remaining:
                shutil.rmtree(exp_dir)
                logger.info(f"Deleted empty MLflow experiment dir: {exp_dir}")
    except Exception as e:
        logger.warning(f"Failed to remove MLflow run folder from disk: {e}")


def _delete_empty_mlflow_experiments(client, experiment_ids: set[str]) -> int:
    """Delete touched experiments that have no active runs left."""
    deleted = 0
    for experiment_id in experiment_ids:
        exp_id = str(experiment_id)
        if exp_id == "0":
            # Never delete MLflow default experiment.
            continue

        try:
            remaining_active_runs = client.search_runs(
                experiment_ids=[exp_id],
                max_results=1,
            )
        except Exception as e:
            logger.warning(
                "Failed checking remaining MLflow runs for experiment %s: %s",
                exp_id,
                e,
            )
            continue

        if remaining_active_runs:
            continue

        try:
            experiment = client.get_experiment(exp_id)
        except Exception as e:
            logger.warning(
                "Failed fetching MLflow experiment %s for cleanup: %s",
                exp_id,
                e,
            )
            continue

        if not experiment or getattr(experiment, "lifecycle_stage", "active") != "active":
            continue

        try:
            client.delete_experiment(exp_id)
            deleted += 1
            logger.info("Deleted empty MLflow experiment %s", exp_id)
        except Exception as e:
            logger.warning(
                "Failed to delete MLflow experiment %s after run cleanup: %s",
                exp_id,
                e,
            )

    return deleted


def _count_mlflow_runs(job_id: str) -> int:
    """Count MLflow runs tagged with job_id."""
    try:
        from mlflow import MlflowClient
        client = MlflowClient()
        try:
            experiments = client.search_experiments()
            exp_ids = [e.experiment_id for e in experiments]
            if exp_ids:
                runs = client.search_runs(
                    experiment_ids=exp_ids,
                    filter_string=f"tags.job_id = '{job_id}'",
                )
                return len(runs)
        except Exception:
            pass
        runs = client.search_runs(
            experiment_ids=["0"],
            filter_string=f"tags.job_id = '{job_id}'",
        )
        return len(runs)
    except ImportError:
        return 0
    except Exception:
        return 0


def _delete_mlflow_registered_model(model_name: str):
    """Delete an MLflow registered model."""
    try:
        from mlflow import MlflowClient
        client = MlflowClient()
        client.delete_registered_model(model_name)
        logger.info(f"Deleted MLflow registered model: {model_name}")
    except ImportError:
        logger.debug("MLflow not available, skipping registered model cleanup")
    except Exception as e:
        logger.warning(f"Failed to delete MLflow registered model {model_name}: {e}")
        raise


def _scan_mlruns_for_orphans() -> list[dict]:
    """Scan mlruns/ directory for run folders and return their metadata.

    Each entry includes path, size_bytes, run_id, experiment_id, and job_id
    (read from the run's tags/ directory on disk).
    """
    try:
        from mlflow import MlflowClient
        client = MlflowClient()
        tracking_uri = client.tracking_uri or ""
    except ImportError:
        return []
    except Exception:
        return []

    # Resolve mlruns directory from tracking URI
    if tracking_uri.startswith("file:"):
        from urllib.parse import unquote
        mlruns_dir = unquote(tracking_uri.removeprefix("file://"))
    elif not tracking_uri or tracking_uri == "":
        mlruns_dir = os.path.join(os.getcwd(), "mlruns")
    else:
        # Remote tracking server — can't scan disk
        return []

    if not os.path.isdir(mlruns_dir):
        return []

    results = []
    for exp_entry in os.scandir(mlruns_dir):
        # Skip .trash, non-dirs, and hidden dirs
        if not exp_entry.is_dir() or exp_entry.name.startswith("."):
            continue

        for run_entry in os.scandir(exp_entry.path):
            if not run_entry.is_dir() or run_entry.name.startswith("."):
                continue

            run_id = run_entry.name
            # Read job_id tag from tags/ directory
            job_id = None
            tag_file = os.path.join(run_entry.path, "tags", "job_id")
            if os.path.isfile(tag_file):
                try:
                    with open(tag_file) as f:
                        job_id = f.read().strip()
                except OSError:
                    pass

            results.append({
                "path": run_entry.path,
                "size_bytes": _dir_size(run_entry.path),
                "run_id": run_id,
                "experiment_id": exp_entry.name,
                "job_id": job_id,
            })

    return results


async def _find_job_for_model_path(db: AsyncSession, model_path: str):
    """Check if any job has this model_path."""
    from sqlalchemy import select
    from app.db.models import Job
    result = await db.execute(select(Job).where(Job.model_path == model_path).limit(1))
    return result.scalar_one_or_none()


@lru_cache()
def get_cleanup_service() -> CleanupService:
    """Singleton accessor for CleanupService."""
    return CleanupService()
