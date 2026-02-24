"""Tests for app.core.cleanup_service.

Covers:
- _dir_size
- find_orphans (filesystem scanning)
- find_orphans_checked (DB-validated filtering)
- delete_job_artifacts (model dir, upload file, logs; partial failures)
- preview_cleanup (dry-run summary)
- bulk_cleanup (full deletion)
"""

import os
import uuid
from datetime import timedelta
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
import pytest_asyncio

from app.core.cleanup_service import CleanupService, _dir_size
from app.core.utils import utc_now
from app.db import crud
from app.db.models import Job, JobLog, JobStatus, ModelType


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _write_file(path, size_bytes=100):
    """Create a file with the given size at *path*."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(b"x" * size_bytes)


def _make_model_dir(base_dir, job_id, file_sizes=None):
    """Create a fake model directory under *base_dir* with files.

    Returns the absolute path of the model directory.
    """
    if file_sizes is None:
        file_sizes = [100, 200]
    model_dir = os.path.join(base_dir, f"job_{job_id}")
    os.makedirs(model_dir, exist_ok=True)
    for i, size in enumerate(file_sizes):
        _write_file(os.path.join(model_dir, f"model_part_{i}.bin"), size)
    return model_dir


# ---------------------------------------------------------------------------
# _dir_size
# ---------------------------------------------------------------------------


class TestDirSize:
    """Test the _dir_size helper."""

    def test_single_file(self, tmp_path):
        _write_file(str(tmp_path / "a.bin"), 256)
        assert _dir_size(str(tmp_path)) == 256

    def test_multiple_files(self, tmp_path):
        _write_file(str(tmp_path / "a.bin"), 100)
        _write_file(str(tmp_path / "b.bin"), 200)
        assert _dir_size(str(tmp_path)) == 300

    def test_nested_dirs(self, tmp_path):
        _write_file(str(tmp_path / "sub" / "c.bin"), 50)
        _write_file(str(tmp_path / "d.bin"), 150)
        assert _dir_size(str(tmp_path)) == 200

    def test_empty_dir(self, tmp_path):
        empty = tmp_path / "empty"
        empty.mkdir()
        assert _dir_size(str(empty)) == 0

    def test_nonexistent_dir(self):
        """_dir_size returns 0 for a nonexistent path (OSError caught)."""
        assert _dir_size("/nonexistent/path/12345") == 0


# ---------------------------------------------------------------------------
# find_orphans (filesystem only, no DB)
# ---------------------------------------------------------------------------


class TestFindOrphans:
    """Test CleanupService.find_orphans scanning the filesystem."""

    def test_detects_orphaned_model_dirs(self, tmp_data_dir, monkeypatch):
        models_dir = str(tmp_data_dir["models"])
        uploads_dir = str(tmp_data_dir["uploads"])

        # Create two fake model dirs
        model_dir_1 = _make_model_dir(models_dir, "aaa-111", [100])
        model_dir_2 = _make_model_dir(models_dir, "bbb-222", [200, 300])

        svc = CleanupService()
        monkeypatch.setattr(svc.settings, "models_path", models_dir)
        monkeypatch.setattr(svc.settings, "uploads_path", uploads_dir)

        with patch(
            "app.core.cleanup_service._scan_mlruns_for_orphans", return_value=[]
        ):
            result = svc.find_orphans()

        assert len(result["orphaned_models"]) == 2
        names = {m["name"] for m in result["orphaned_models"]}
        assert "job_aaa-111" in names
        assert "job_bbb-222" in names
        assert result["total_orphaned_model_size_bytes"] == 100 + 200 + 300

    def test_detects_orphaned_upload_files(self, tmp_data_dir, monkeypatch):
        models_dir = str(tmp_data_dir["models"])
        uploads_dir = str(tmp_data_dir["uploads"])

        _write_file(os.path.join(uploads_dir, "abcd1234_data.csv"), 500)
        _write_file(os.path.join(uploads_dir, "efgh5678_data.parquet"), 750)

        svc = CleanupService()
        monkeypatch.setattr(svc.settings, "models_path", models_dir)
        monkeypatch.setattr(svc.settings, "uploads_path", uploads_dir)

        with patch(
            "app.core.cleanup_service._scan_mlruns_for_orphans", return_value=[]
        ):
            result = svc.find_orphans()

        assert len(result["orphaned_uploads"]) == 2
        assert result["total_orphaned_upload_size_bytes"] == 500 + 750

    def test_ignores_non_job_dirs(self, tmp_data_dir, monkeypatch):
        """Directories not starting with 'job_' should not appear as orphans."""
        models_dir = str(tmp_data_dir["models"])
        uploads_dir = str(tmp_data_dir["uploads"])

        os.makedirs(os.path.join(models_dir, "other_dir"))
        _make_model_dir(models_dir, "real-job", [50])

        svc = CleanupService()
        monkeypatch.setattr(svc.settings, "models_path", models_dir)
        monkeypatch.setattr(svc.settings, "uploads_path", uploads_dir)

        with patch(
            "app.core.cleanup_service._scan_mlruns_for_orphans", return_value=[]
        ):
            result = svc.find_orphans()

        assert len(result["orphaned_models"]) == 1
        assert result["orphaned_models"][0]["name"] == "job_real-job"

    def test_empty_directories(self, tmp_data_dir, monkeypatch):
        """No orphans when models and uploads dirs are empty."""
        svc = CleanupService()
        monkeypatch.setattr(svc.settings, "models_path", str(tmp_data_dir["models"]))
        monkeypatch.setattr(svc.settings, "uploads_path", str(tmp_data_dir["uploads"]))

        with patch(
            "app.core.cleanup_service._scan_mlruns_for_orphans", return_value=[]
        ):
            result = svc.find_orphans()

        assert result["orphaned_models"] == []
        assert result["orphaned_uploads"] == []
        assert result["total_orphaned_model_size_bytes"] == 0


# ---------------------------------------------------------------------------
# find_orphans_checked (with DB validation)
# ---------------------------------------------------------------------------


class TestFindOrphansChecked:
    """Test find_orphans_checked which filters orphans against the database."""

    @pytest.mark.asyncio
    async def test_filters_out_models_with_matching_jobs(
        self, tmp_data_dir, db_session, make_job, monkeypatch
    ):
        models_dir = str(tmp_data_dir["models"])
        uploads_dir = str(tmp_data_dir["uploads"])

        # Create a model dir on disk and a matching job in DB
        job = make_job(name="existing-job", status=JobStatus.COMPLETED)
        model_dir = _make_model_dir(models_dir, job.id, [100])
        job.model_path = model_dir
        db_session.add(job)
        await db_session.commit()

        # Also create an orphaned model dir (no matching job)
        _make_model_dir(models_dir, "no-match-id", [200])

        svc = CleanupService()
        monkeypatch.setattr(svc.settings, "models_path", models_dir)
        monkeypatch.setattr(svc.settings, "uploads_path", uploads_dir)

        with patch(
            "app.core.cleanup_service._scan_mlruns_for_orphans", return_value=[]
        ):
            result = await svc.find_orphans_checked(db_session)

        # Only the unmatched dir should appear
        assert len(result["orphaned_models"]) == 1
        assert result["orphaned_models"][0]["name"] == "job_no-match-id"

    @pytest.mark.asyncio
    async def test_filters_out_uploads_referenced_by_jobs(
        self, tmp_data_dir, db_session, make_job, monkeypatch
    ):
        models_dir = str(tmp_data_dir["models"])
        uploads_dir = str(tmp_data_dir["uploads"])

        referenced_file = os.path.join(uploads_dir, "referenced.csv")
        orphaned_file = os.path.join(uploads_dir, "orphaned.csv")
        _write_file(referenced_file, 100)
        _write_file(orphaned_file, 200)

        job = make_job(name="upload-job", file_path=referenced_file)
        db_session.add(job)
        await db_session.commit()

        svc = CleanupService()
        monkeypatch.setattr(svc.settings, "models_path", models_dir)
        monkeypatch.setattr(svc.settings, "uploads_path", uploads_dir)

        with patch(
            "app.core.cleanup_service._scan_mlruns_for_orphans", return_value=[]
        ):
            result = await svc.find_orphans_checked(db_session)

        orphan_paths = {u["path"] for u in result["orphaned_uploads"]}
        assert orphaned_file in orphan_paths
        assert referenced_file not in orphan_paths


# ---------------------------------------------------------------------------
# delete_job_artifacts
# ---------------------------------------------------------------------------


class TestDeleteJobArtifacts:
    """Test CleanupService.delete_job_artifacts."""

    @pytest.mark.asyncio
    async def test_deletes_model_dir(self, tmp_data_dir, db_session, make_job):
        models_dir = str(tmp_data_dir["models"])
        job = make_job(name="del-model", status=JobStatus.COMPLETED)
        model_dir = _make_model_dir(models_dir, job.id, [100, 200])
        job.model_path = model_dir

        svc = CleanupService()
        with patch("app.core.cleanup_service._delete_mlflow_runs", return_value=0), \
             patch.object(crud, "delete_job_logs", new_callable=AsyncMock, return_value=0):
            result = await svc.delete_job_artifacts(job, db_session)

        assert result["model_files_deleted"] is True
        assert result["model_files_size_bytes"] == 300
        assert not os.path.exists(model_dir)

    @pytest.mark.asyncio
    async def test_deletes_upload_file_when_sole_reference(
        self, tmp_data_dir, db_session, make_job
    ):
        uploads_dir = str(tmp_data_dir["uploads"])
        upload_path = os.path.join(uploads_dir, "solo.csv")
        _write_file(upload_path, 500)

        job = make_job(
            name="del-upload",
            data_source="upload",
            file_path=upload_path,
            status=JobStatus.FAILED,
        )
        db_session.add(job)
        await db_session.commit()

        svc = CleanupService()
        with patch("app.core.cleanup_service._delete_mlflow_runs", return_value=0), \
             patch.object(crud, "delete_job_logs", new_callable=AsyncMock, return_value=0):
            result = await svc.delete_job_artifacts(job, db_session)

        assert result["upload_file_deleted"] is True
        assert not os.path.exists(upload_path)

    @pytest.mark.asyncio
    async def test_skips_upload_when_shared(self, tmp_data_dir, db_session, make_job):
        """When multiple jobs share the same upload file, it should not be deleted."""
        uploads_dir = str(tmp_data_dir["uploads"])
        shared_path = os.path.join(uploads_dir, "shared.csv")
        _write_file(shared_path, 400)

        job1 = make_job(name="job1", data_source="upload", file_path=shared_path)
        job2 = make_job(name="job2", data_source="upload", file_path=shared_path)
        db_session.add_all([job1, job2])
        await db_session.commit()

        svc = CleanupService()
        with patch("app.core.cleanup_service._delete_mlflow_runs", return_value=0), \
             patch.object(crud, "delete_job_logs", new_callable=AsyncMock, return_value=0):
            result = await svc.delete_job_artifacts(job1, db_session)

        # File should still exist because job2 also references it
        assert result["upload_file_deleted"] is False
        assert os.path.exists(shared_path)

    @pytest.mark.asyncio
    async def test_handles_missing_model_path(self, db_session, make_job):
        """No error when model_path is None or does not exist."""
        job = make_job(name="no-model", model_path=None)

        svc = CleanupService()
        with patch("app.core.cleanup_service._delete_mlflow_runs", return_value=0), \
             patch.object(crud, "delete_job_logs", new_callable=AsyncMock, return_value=0):
            result = await svc.delete_job_artifacts(job, db_session)

        assert result["model_files_deleted"] is False
        assert result["model_files_size_bytes"] == 0

    @pytest.mark.asyncio
    async def test_partial_failure_reported_in_errors(
        self, tmp_data_dir, db_session, make_job
    ):
        """When model dir deletion fails, the error is captured but execution continues."""
        models_dir = str(tmp_data_dir["models"])
        job = make_job(name="partial-fail", status=JobStatus.COMPLETED)
        model_dir = _make_model_dir(models_dir, job.id, [50])
        job.model_path = model_dir

        with patch(
            "app.core.cleanup_service._delete_mlflow_runs",
            side_effect=RuntimeError("mlflow exploded"),
        ), patch.object(
            crud, "delete_job_logs", new_callable=AsyncMock, return_value=3
        ), patch(
            "shutil.rmtree", side_effect=PermissionError("denied")
        ):
            svc = CleanupService()
            result = await svc.delete_job_artifacts(job, db_session)

        assert result["model_files_deleted"] is False
        assert len(result["errors"]) >= 1
        assert any("model_files" in e for e in result["errors"])
        assert any("mlflow_runs" in e for e in result["errors"])
        # Logs deletion should still have succeeded
        assert result["job_logs_deleted"] == 3

    @pytest.mark.asyncio
    async def test_returns_correct_log_count(self, db_session, make_job):
        job = make_job(name="log-count")

        svc = CleanupService()
        with patch("app.core.cleanup_service._delete_mlflow_runs", return_value=0), \
             patch.object(crud, "delete_job_logs", new_callable=AsyncMock, return_value=7):
            result = await svc.delete_job_artifacts(job, db_session)

        assert result["job_logs_deleted"] == 7


# ---------------------------------------------------------------------------
# preview_cleanup (dry-run)
# ---------------------------------------------------------------------------


class TestPreviewCleanup:
    """Test CleanupService.preview_cleanup (dry-run summary)."""

    @pytest.mark.asyncio
    async def test_returns_summary_without_deleting(
        self, tmp_data_dir, db_session, make_job, monkeypatch
    ):
        models_dir = str(tmp_data_dir["models"])
        uploads_dir = str(tmp_data_dir["uploads"])

        # Create a completed job with model dir and upload
        job = make_job(
            name="preview-job",
            status=JobStatus.COMPLETED,
            data_source="upload",
        )
        model_dir = _make_model_dir(models_dir, job.id, [100, 200])
        job.model_path = model_dir
        upload_path = os.path.join(uploads_dir, "preview.csv")
        _write_file(upload_path, 400)
        job.file_path = upload_path

        db_session.add(job)
        await db_session.commit()

        svc = CleanupService()
        with patch("app.core.cleanup_service._count_mlflow_runs", return_value=2), \
             patch.object(crud, "count_job_logs", new_callable=AsyncMock, return_value=5):
            result = await svc.preview_cleanup(
                db_session,
                statuses=[JobStatus.COMPLETED],
            )

        assert result["job_count"] == 1
        assert result["total_model_size_bytes"] == 300
        assert result["total_upload_size_bytes"] == 400
        assert result["total_mlflow_runs"] == 2
        assert result["total_logs"] == 5
        assert len(result["jobs"]) == 1

        # Verify nothing was actually deleted
        assert os.path.exists(model_dir)
        assert os.path.exists(upload_path)

    @pytest.mark.asyncio
    async def test_no_matching_jobs(self, db_session):
        """When no jobs match the filter, counts should all be zero."""
        svc = CleanupService()
        result = await svc.preview_cleanup(
            db_session,
            statuses=[JobStatus.FAILED],
        )
        assert result["job_count"] == 0
        assert result["total_model_size_bytes"] == 0


# ---------------------------------------------------------------------------
# bulk_cleanup
# ---------------------------------------------------------------------------


class TestBulkCleanup:
    """Test CleanupService.bulk_cleanup."""

    @pytest.mark.asyncio
    async def test_deletes_jobs_and_artifacts(
        self, tmp_data_dir, db_session, make_job, monkeypatch
    ):
        models_dir = str(tmp_data_dir["models"])

        job1 = make_job(name="bulk-1", status=JobStatus.FAILED)
        model1 = _make_model_dir(models_dir, job1.id, [100])
        job1.model_path = model1
        db_session.add(job1)

        job2 = make_job(name="bulk-2", status=JobStatus.FAILED)
        model2 = _make_model_dir(models_dir, job2.id, [250])
        job2.model_path = model2
        db_session.add(job2)

        await db_session.commit()

        svc = CleanupService()
        with patch("app.core.cleanup_service._delete_mlflow_runs", return_value=0), \
             patch.object(crud, "delete_job_logs", new_callable=AsyncMock, return_value=0):
            result = await svc.bulk_cleanup(
                db_session,
                statuses=[JobStatus.FAILED],
            )

        assert result["jobs_deleted"] == 2
        assert set(result["deleted_job_ids"]) == {job1.id, job2.id}
        assert result["total_model_size_bytes"] == 100 + 250
        assert not os.path.exists(model1)
        assert not os.path.exists(model2)

    @pytest.mark.asyncio
    async def test_bulk_cleanup_accumulates_errors(
        self, tmp_data_dir, db_session, make_job
    ):
        """Errors from individual job cleanups accumulate in the result."""
        job = make_job(name="err-job", status=JobStatus.CANCELLED)
        db_session.add(job)
        await db_session.commit()

        svc = CleanupService()
        with patch(
            "app.core.cleanup_service._delete_mlflow_runs",
            side_effect=RuntimeError("boom"),
        ), patch.object(
            crud, "delete_job_logs", new_callable=AsyncMock, return_value=0
        ):
            result = await svc.bulk_cleanup(
                db_session,
                statuses=[JobStatus.CANCELLED],
            )

        assert result["jobs_deleted"] == 1
        assert len(result["errors"]) >= 1
