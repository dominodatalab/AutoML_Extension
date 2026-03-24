"""Tests for the /export/deployment/zip endpoint and zip helpers.

Covers:
- POST /svc/v1/export/export/deployment/zip — combined build + download
- _zip_directory_to_spooled — directory zipping
- _zip_model_and_files — model + text files zipping
- _iter_spooled — chunked iteration
"""

import io
import os
import tempfile
import zipfile

import pytest

from app.api.routes.export import (
    _zip_directory_to_spooled,
    _zip_model_and_files,
    _iter_spooled,
)


def _spooled_to_zipfile(spooled):
    """Read a SpooledTemporaryFile into a BytesIO and open as ZipFile.

    Python 3.10's SpooledTemporaryFile lacks seekable(), which zipfile
    needs for reading. Work around by copying to BytesIO first.
    """
    data = spooled.read()
    spooled.close()
    return zipfile.ZipFile(io.BytesIO(data), "r")


# ---------------------------------------------------------------------------
# _zip_directory_to_spooled
# ---------------------------------------------------------------------------


class TestZipDirectoryToSpooled:

    def test_zips_directory_contents(self, tmp_path):
        (tmp_path / "file1.txt").write_text("hello")
        (tmp_path / "subdir").mkdir()
        (tmp_path / "subdir" / "file2.txt").write_text("world")

        spooled = _zip_directory_to_spooled(str(tmp_path))

        with _spooled_to_zipfile(spooled) as zf:
            names = zf.namelist()
            assert "file1.txt" in names
            assert os.path.join("subdir", "file2.txt") in names
            assert zf.read("file1.txt") == b"hello"

    def test_empty_directory(self, tmp_path):
        empty = tmp_path / "empty"
        empty.mkdir()

        spooled = _zip_directory_to_spooled(str(empty))

        with _spooled_to_zipfile(spooled) as zf:
            assert zf.namelist() == []


# ---------------------------------------------------------------------------
# _zip_model_and_files
# ---------------------------------------------------------------------------


class TestZipModelAndFiles:

    def test_includes_text_files_and_model(self, tmp_path):
        # Create a fake model directory
        model_dir = tmp_path / "model"
        model_dir.mkdir()
        (model_dir / "weights.bin").write_bytes(b"\x00\x01\x02")
        (model_dir / "config.json").write_text('{"type": "test"}')

        text_files = {
            "inference.py": "import autogluon\n",
            "requirements.txt": "autogluon==1.0\n",
            "Dockerfile": "FROM python:3.11\n",
        }

        spooled = _zip_model_and_files(str(model_dir), text_files)

        with _spooled_to_zipfile(spooled) as zf:
            names = zf.namelist()
            assert "inference.py" in names
            assert "requirements.txt" in names
            assert "Dockerfile" in names
            assert os.path.join("model", "weights.bin") in names
            assert os.path.join("model", "config.json") in names

            assert zf.read("inference.py") == b"import autogluon\n"
            assert zf.read(os.path.join("model", "weights.bin")) == b"\x00\x01\x02"

    def test_single_model_file(self, tmp_path):
        model_file = tmp_path / "model.pkl"
        model_file.write_bytes(b"pickle data")

        spooled = _zip_model_and_files(str(model_file), {"readme.txt": "info"})

        with _spooled_to_zipfile(spooled) as zf:
            names = zf.namelist()
            assert "readme.txt" in names
            assert os.path.join("model", "model.pkl") in names

    def test_empty_text_files(self, tmp_path):
        model_dir = tmp_path / "model"
        model_dir.mkdir()
        (model_dir / "data.bin").write_bytes(b"data")

        spooled = _zip_model_and_files(str(model_dir), {})

        with _spooled_to_zipfile(spooled) as zf:
            names = zf.namelist()
            assert os.path.join("model", "data.bin") in names
            assert len(names) == 1


# ---------------------------------------------------------------------------
# _iter_spooled
# ---------------------------------------------------------------------------


class TestIterSpooled:

    def test_yields_all_content(self):
        spooled = tempfile.SpooledTemporaryFile(max_size=1024)
        spooled.write(b"hello world")
        spooled.seek(0)

        chunks = list(_iter_spooled(spooled, chunk_size=5))
        content = b"".join(chunks)
        assert content == b"hello world"

    def test_handles_empty_content(self):
        spooled = tempfile.SpooledTemporaryFile(max_size=1024)
        spooled.seek(0)

        chunks = list(_iter_spooled(spooled, chunk_size=1024))
        assert chunks == []

    def test_closes_file_after_iteration(self):
        spooled = tempfile.SpooledTemporaryFile(max_size=1024)
        spooled.write(b"data")
        spooled.seek(0)

        list(_iter_spooled(spooled))
        assert spooled.closed


# ---------------------------------------------------------------------------
# API endpoint test (via app_client)
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_export_deployment_zip_with_model(app_client, tmp_path, db_session):
    """POST /svc/v1/export/export/deployment/zip builds and streams a zip."""
    from app.db.models import Job, JobStatus, ModelType
    from app.core.utils import utc_now

    # Create a fake model directory
    model_dir = tmp_path / "models" / "test-model"
    model_dir.mkdir(parents=True)
    (model_dir / "model.pkl").write_bytes(b"fake model data")
    (model_dir / "metadata.json").write_text('{"model": "test"}')

    # Create a completed job in the DB
    job = Job(
        id="zip-test-job-001",
        name="zip-test",
        status=JobStatus.COMPLETED,
        model_type=ModelType.TABULAR,
        data_source="upload",
        target_column="target",
        file_path="/tmp/test.csv",
        model_path=str(model_dir),
        owner="test",
        project_name="test-project",
        execution_target="local",
        preset="medium_quality_faster_train",
        time_limit=60,
        created_at=utc_now(),
        completed_at=utc_now(),
    )
    db_session.add(job)
    await db_session.commit()

    response = await app_client.post(
        "/svc/v1/export/export/deployment/zip",
        json={"job_id": "zip-test-job-001", "model_type": "tabular"},
    )

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/zip"
    assert "deployment_zip-test-job-001.zip" in response.headers.get("content-disposition", "")

    # Verify the zip contents
    import io
    with zipfile.ZipFile(io.BytesIO(response.content), "r") as zf:
        names = zf.namelist()
        # Should have deployment files
        assert "inference.py" in names
        assert "requirements.txt" in names
        assert "Dockerfile" in names
        assert "model_metadata.json" in names
        # Should have model files
        assert os.path.join("model", "model.pkl") in names
        assert os.path.join("model", "metadata.json") in names


@pytest.mark.asyncio
async def test_export_deployment_zip_job_not_found(app_client):
    """POST /svc/v1/export/export/deployment/zip with invalid job_id returns 404."""
    response = await app_client.post(
        "/svc/v1/export/export/deployment/zip",
        json={"job_id": "nonexistent-job-id"},
    )
    assert response.status_code == 404
