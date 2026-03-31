"""Tests for app.services.dataset_service helpers.

Covers:
- normalize_preview_pagination
- build_preview_payload
- _safe_int
- coerce_preview_response
- NaN / inf handling in preview rows
"""

import math
import os
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest
from fastapi import HTTPException

from app.api.generated.domino_public_api_client.models.dataset_rw_info_dto_v1 import DatasetRwInfoDtoV1
from app.api.generated.domino_public_api_client.models.dataset_rw_envelope_v1 import DatasetRwEnvelopeV1
from app.api.generated.domino_public_api_client.models.dataset_rw_details_v1 import DatasetRwDetailsV1
from app.api.generated.domino_public_api_client.models.metadata_v1 import MetadataV1
from app.api.generated.domino_public_api_client.models.paginated_dataset_rw_envelope_v2 import (
    PaginatedDatasetRwEnvelopeV2,
)
from app.api.generated.domino_public_api_client.models.paginated_metadata_v1 import PaginatedMetadataV1
from app.services.dataset_service import (
    DEFAULT_PREVIEW_LIMIT,
    MAX_PREVIEW_LIMIT,
    _safe_int,
    build_preview_payload,
    build_compat_dataset_preview_payload,
    coerce_preview_response,
    list_dataset_files_response,
    list_datasets_response,
    normalize_preview_pagination,
)
from app.api.schemas.dataset import CompatDatasetPreviewRequest


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _build_local_preview_payload(file_path: str, **kwargs):
    """Call build_preview_payload with the current local-file contract."""
    return build_preview_payload(dataset_id=file_path, file_path=file_path, **kwargs)


# ---------------------------------------------------------------------------
# _safe_int
# ---------------------------------------------------------------------------


class TestSafeInt:
    """Test the _safe_int helper that converts values to int or raises HTTP 400."""

    def test_valid_int(self):
        assert _safe_int(42, "test") == 42

    def test_valid_string_int(self):
        assert _safe_int("10", "test") == 10

    def test_valid_float_truncates(self):
        assert _safe_int(3.9, "test") == 3

    def test_none_raises_400(self):
        with pytest.raises(HTTPException) as exc_info:
            _safe_int(None, "limit")
        assert exc_info.value.status_code == 400
        assert "limit must be an integer" in exc_info.value.detail

    def test_non_numeric_string_raises_400(self):
        with pytest.raises(HTTPException) as exc_info:
            _safe_int("abc", "offset")
        assert exc_info.value.status_code == 400
        assert "offset must be an integer" in exc_info.value.detail

    def test_empty_string_raises_400(self):
        with pytest.raises(HTTPException):
            _safe_int("", "field")

    def test_zero(self):
        assert _safe_int(0, "test") == 0

    def test_negative(self):
        assert _safe_int(-5, "test") == -5


# ---------------------------------------------------------------------------
# normalize_preview_pagination
# ---------------------------------------------------------------------------


class TestNormalizePreviewPagination:
    """Test normalize_preview_pagination with various parameter combinations."""

    def test_defaults(self):
        """No arguments should return (DEFAULT_PREVIEW_LIMIT, 0)."""
        limit, offset = normalize_preview_pagination()
        assert limit == DEFAULT_PREVIEW_LIMIT
        assert offset == 0

    def test_custom_limit(self):
        limit, offset = normalize_preview_pagination(limit=50)
        assert limit == 50
        assert offset == 0

    def test_custom_rows_as_fallback(self):
        """When limit is None, rows is used as the effective limit."""
        limit, offset = normalize_preview_pagination(limit=None, rows=25)
        assert limit == 25
        assert offset == 0

    def test_limit_takes_priority_over_rows(self):
        """When both limit and rows are provided, limit wins."""
        limit, offset = normalize_preview_pagination(limit=30, rows=25)
        assert limit == 30

    def test_negative_offset_clamped_to_zero(self):
        limit, offset = normalize_preview_pagination(offset=-10)
        assert offset == 0

    def test_large_limit_clamped_to_max(self):
        limit, offset = normalize_preview_pagination(limit=5000)
        assert limit == MAX_PREVIEW_LIMIT

    def test_limit_exactly_max(self):
        limit, offset = normalize_preview_pagination(limit=MAX_PREVIEW_LIMIT)
        assert limit == MAX_PREVIEW_LIMIT

    def test_zero_limit_falls_back_to_default(self):
        """A limit of 0 is treated as falsy, falling back to default."""
        limit, offset = normalize_preview_pagination(limit=0)
        assert limit == DEFAULT_PREVIEW_LIMIT

    def test_negative_limit_falls_back_to_default(self):
        """A negative limit (< 1) resets to default."""
        limit, offset = normalize_preview_pagination(limit=-5)
        assert limit == DEFAULT_PREVIEW_LIMIT

    def test_string_values_converted(self):
        """String-typed limit and offset should be converted to int."""
        limit, offset = normalize_preview_pagination(limit="50", offset="10")
        assert limit == 50
        assert offset == 10

    def test_non_integer_limit_raises(self):
        with pytest.raises(HTTPException) as exc_info:
            normalize_preview_pagination(limit="abc")
        assert exc_info.value.status_code == 400

    def test_non_integer_offset_raises(self):
        with pytest.raises(HTTPException) as exc_info:
            normalize_preview_pagination(offset="xyz")
        assert exc_info.value.status_code == 400

    def test_none_offset_defaults_to_zero(self):
        limit, offset = normalize_preview_pagination(offset=None)
        assert offset == 0


# ---------------------------------------------------------------------------
# build_preview_payload — CSV
# ---------------------------------------------------------------------------


class TestBuildPreviewPayloadCSV:
    """Test build_preview_payload with CSV files."""

    def test_basic_csv_preview(self, tabular_csv):
        payload = _build_local_preview_payload(tabular_csv)
        assert payload["file_path"] == tabular_csv
        assert payload["file_name"] == os.path.basename(tabular_csv)
        assert "columns" in payload
        assert len(payload["columns"]) > 0
        assert payload["preview_rows"] <= DEFAULT_PREVIEW_LIMIT
        assert payload["total_rows"] == 200  # tabular_csv fixture has 200 rows
        assert isinstance(payload["rows"], list)

    def test_csv_custom_limit(self, tabular_csv):
        payload = _build_local_preview_payload(tabular_csv, limit=10)
        assert payload["preview_rows"] == 10
        assert len(payload["rows"]) == 10

    def test_csv_offset(self, tabular_csv):
        payload = _build_local_preview_payload(tabular_csv, limit=5, offset=10)
        assert payload["preview_rows"] == 5
        assert len(payload["rows"]) == 5

    def test_csv_includes_dtypes(self, tabular_csv):
        payload = _build_local_preview_payload(tabular_csv, include_dtypes=True)
        assert "dtypes" in payload
        assert isinstance(payload["dtypes"], dict)
        assert len(payload["dtypes"]) == len(payload["columns"])

    def test_csv_without_dtypes(self, tabular_csv):
        payload = _build_local_preview_payload(tabular_csv, include_dtypes=False)
        assert "dtypes" not in payload

    def test_csv_dataset_id_equals_file_path(self, tabular_csv):
        payload = _build_local_preview_payload(tabular_csv)
        assert payload["dataset_id"] == tabular_csv


# ---------------------------------------------------------------------------
# build_preview_payload — Parquet
# ---------------------------------------------------------------------------


class TestBuildPreviewPayloadParquet:
    """Test build_preview_payload with Parquet files."""

    def test_basic_parquet_preview(self, parquet_file):
        payload = _build_local_preview_payload(parquet_file)
        assert payload["file_path"] == parquet_file
        assert payload["file_name"] == os.path.basename(parquet_file)
        assert payload["total_rows"] == 200
        assert payload["preview_rows"] <= DEFAULT_PREVIEW_LIMIT

    def test_parquet_offset(self, parquet_file):
        payload = _build_local_preview_payload(parquet_file, limit=5, offset=195)
        assert payload["preview_rows"] == 5
        assert len(payload["rows"]) == 5

    def test_parquet_offset_beyond_end(self, parquet_file):
        """Offset past the end of the file should return zero rows."""
        payload = _build_local_preview_payload(parquet_file, limit=10, offset=9999)
        assert payload["preview_rows"] == 0
        assert len(payload["rows"]) == 0


# ---------------------------------------------------------------------------
# build_preview_payload — error cases
# ---------------------------------------------------------------------------


class TestBuildPreviewPayloadErrors:
    """Test build_preview_payload error handling."""

    def test_file_not_found(self):
        with pytest.raises(HTTPException) as exc_info:
            _build_local_preview_payload("/nonexistent/path/data.csv")
        assert exc_info.value.status_code == 404
        assert "file not found" in exc_info.value.detail

    def test_empty_file_path(self):
        with pytest.raises(HTTPException) as exc_info:
            _build_local_preview_payload("")
        assert exc_info.value.status_code == 400
        assert "file_path is required" in exc_info.value.detail

    def test_unsupported_format(self, tmp_path):
        unsupported = tmp_path / "data.json"
        unsupported.write_text('{"key": "value"}')
        with pytest.raises(HTTPException) as exc_info:
            _build_local_preview_payload(str(unsupported))
        assert exc_info.value.status_code == 400
        assert "Unsupported file format" in exc_info.value.detail


# ---------------------------------------------------------------------------
# NaN / inf handling in preview rows
# ---------------------------------------------------------------------------


class TestNaNInfHandling:
    """Verify that NaN/inf values in data are replaced with None in preview rows."""

    def test_nan_becomes_none(self, tabular_csv):
        """The tabular_csv fixture injects NaN in income and category columns."""
        payload = _build_local_preview_payload(tabular_csv, limit=200)
        # Check that no row contains actual float NaN
        for row in payload["rows"]:
            for key, value in row.items():
                if isinstance(value, float):
                    assert not math.isnan(value), f"Found NaN in column {key}"
                    assert not math.isinf(value), f"Found inf in column {key}"

    def test_inf_becomes_none(self, tmp_path):
        """Explicitly create a CSV with inf values and verify they become None."""
        df = pd.DataFrame({
            "a": [1.0, np.inf, -np.inf, np.nan, 5.0],
            "b": [10, 20, 30, 40, 50],
        })
        csv_path = str(tmp_path / "inf_test.csv")
        df.to_csv(csv_path, index=False)

        payload = _build_local_preview_payload(csv_path, limit=10)
        for row in payload["rows"]:
            val_a = row["a"]
            if val_a is not None:
                assert not math.isinf(val_a)
                assert not math.isnan(val_a)

        # Rows 1, 2, 3 should have None for column "a"
        assert payload["rows"][1]["a"] is None  # was inf
        assert payload["rows"][2]["a"] is None  # was -inf
        assert payload["rows"][3]["a"] is None  # was NaN


# ---------------------------------------------------------------------------
# coerce_preview_response
# ---------------------------------------------------------------------------


class TestCoercePreviewResponse:
    """Test coerce_preview_response with different input types."""

    def test_dict_passthrough(self):
        data = {
            "dataset_id": "ds-1",
            "file_path": "/tmp/data.csv",
            "columns": ["a", "b"],
            "rows": [{"a": 1, "b": 2}],
        }
        result = coerce_preview_response(data)
        assert result["dataset_id"] == "ds-1"
        assert result["file_path"] == "/tmp/data.csv"

    def test_dict_file_path_defaults_to_dataset_id(self):
        """When file_path is missing, it defaults to dataset_id."""
        data = {"dataset_id": "ds-42", "columns": []}
        result = coerce_preview_response(data)
        assert result["file_path"] == "ds-42"

    def test_dict_include_dtypes(self):
        data = {"dataset_id": "ds-1"}
        result = coerce_preview_response(data, include_dtypes=True)
        assert "dtypes" in result
        assert result["dtypes"] == {}

    def test_dict_existing_dtypes_not_overwritten(self):
        data = {"dataset_id": "ds-1", "dtypes": {"col1": "int64"}}
        result = coerce_preview_response(data, include_dtypes=True)
        assert result["dtypes"] == {"col1": "int64"}

    def test_pydantic_model(self):
        """Test with an object that has model_dump (Pydantic v2 style)."""

        class FakeModel:
            def model_dump(self):
                return {
                    "dataset_id": "pydantic-ds",
                    "file_path": "/pydantic/path.csv",
                    "columns": ["x"],
                    "rows": [],
                }

        result = coerce_preview_response(FakeModel())
        assert result["dataset_id"] == "pydantic-ds"
        assert result["file_path"] == "/pydantic/path.csv"

    def test_object_with_dict_method(self):
        """Test with an object that has .dict() (Pydantic v1 style)."""

        class LegacyModel:
            def dict(self):
                return {
                    "dataset_id": "legacy-ds",
                    "columns": ["y"],
                    "rows": [],
                }

        result = coerce_preview_response(LegacyModel())
        assert result["dataset_id"] == "legacy-ds"
        # file_path should default to dataset_id
        assert result["file_path"] == "legacy-ds"

    def test_object_with_model_dump_takes_priority(self):
        """When both model_dump and dict exist, model_dump wins."""

        class DualModel:
            def model_dump(self):
                return {"dataset_id": "from-model-dump"}

            def dict(self):
                return {"dataset_id": "from-dict"}

        result = coerce_preview_response(DualModel())
        assert result["dataset_id"] == "from-model-dump"


# ---------------------------------------------------------------------------
# build_compat_dataset_preview_payload
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_build_compat_dataset_preview_payload_fetches_dataset_file_over_api(monkeypatch):
    calls = []

    async def fake_get_snapshots(dataset_id):
        calls.append(("snapshots", dataset_id))
        return [
            {"id": "snap-old", "version": 1, "creationTime": 100},
            {"id": "snap-new", "version": 2, "creationTime": 200},
        ]

    async def fake_get_file_metadata(snapshot_id, path):
        calls.append(("metadata", snapshot_id, path))
        return {"fileSize": 14, "exceedsSizeLimit": False}

    async def fake_get_file_raw(snapshot_id, path):
        calls.append(("raw", snapshot_id, path))
        return b"id,target\n1,0\n"

    monkeypatch.setattr(
        "app.services.dataset_service.domino_http.domino_get_dataset_rw_snapshots",
        fake_get_snapshots,
    )
    monkeypatch.setattr(
        "app.services.dataset_service.domino_http.domino_get_dataset_snapshot_file_metadata",
        fake_get_file_metadata,
    )
    monkeypatch.setattr(
        "app.services.dataset_service.domino_http.domino_get_dataset_snapshot_file_raw",
        fake_get_file_raw,
    )

    result = await build_compat_dataset_preview_payload(
        body=CompatDatasetPreviewRequest(**{
            "dataset_id": "ds-123",
            "file_path": "folder/train.csv",
            "limit": 25,
            "offset": 0,
        }),
    )

    assert calls == [
        ("snapshots", "ds-123"),
        ("metadata", "snap-new", "folder/train.csv"),
        ("raw", "snap-new", "folder/train.csv"),
    ]
    assert result["dataset_id"] == "ds-123"
    assert result["file_path"] == "folder/train.csv"
    assert result["file_name"] == "train.csv"
    assert result["columns"] == ["id", "target"]
    assert result["rows"] == [{"id": 1, "target": 0}]
    assert result["dtypes"] == {"id": "int64", "target": "int64"}
    assert result["total_rows"] == 1
    assert result["preview_rows"] == 1


@pytest.mark.asyncio
async def test_build_compat_dataset_preview_payload_rejects_large_remote_file(monkeypatch):
    calls = []

    async def fake_get_snapshots(dataset_id):
        calls.append(("snapshots", dataset_id))
        return [{"id": "snap-large", "version": 7, "creationTime": 700}]

    async def fake_get_file_metadata(snapshot_id, path):
        calls.append(("metadata", snapshot_id, path))
        return {"fileSize": 524288001, "exceedsSizeLimit": False}

    async def fake_get_file_raw(snapshot_id, path):
        raise AssertionError("raw file download should not happen for oversized previews")

    monkeypatch.setattr(
        "app.services.dataset_service.domino_http.domino_get_dataset_rw_snapshots",
        fake_get_snapshots,
    )
    monkeypatch.setattr(
        "app.services.dataset_service.domino_http.domino_get_dataset_snapshot_file_metadata",
        fake_get_file_metadata,
    )
    monkeypatch.setattr(
        "app.services.dataset_service.domino_http.domino_get_dataset_snapshot_file_raw",
        fake_get_file_raw,
    )

    with pytest.raises(HTTPException) as exc_info:
        await build_compat_dataset_preview_payload(
            body=CompatDatasetPreviewRequest(
                dataset_id="ds-large",
                file_path="folder/huge.parquet",
            ),
        )

    assert exc_info.value.status_code == 413
    assert "Dataset file is too large to preview over API" in exc_info.value.detail
    assert calls == [
        ("snapshots", "ds-large"),
        ("metadata", "snap-large", "folder/huge.parquet"),
    ]


@pytest.mark.asyncio
async def test_build_compat_dataset_preview_payload_rejects_incomplete_request():
    with pytest.raises(HTTPException) as exc_info:
        await build_compat_dataset_preview_payload(
            body=CompatDatasetPreviewRequest(
                dataset_id="ds-456",
                file_path="",
                limit=7,
            ),
        )

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "file_path is required"


# ---------------------------------------------------------------------------
# list_datasets_response
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_list_datasets_response_builds_from_domino_payload_only(monkeypatch):
    dataset_info = DatasetRwInfoDtoV1.from_dict(
        {
            "dataset": {
                "id": "ds-123",
                "name": "Training Dataset",
                "createdAt": "2024-01-02T03:04:05Z",
                "description": "Tabular training data",
                "snapshotIds": ["snap-1"],
                "tags": {},
                "updatedAt": "2024-01-03T04:05:06Z",
                "path": "/api/datasets/training-dataset",
                "sizeBytes": 12345,
                "fileCount": 2,
                "files": [
                    {
                        "name": "train.csv",
                        "path": "/api/datasets/training-dataset/train.csv",
                        "size": 12000,
                    },
                    {
                        "fileName": "metadata.json",
                        "filePath": "/api/datasets/training-dataset/metadata.json",
                        "sizeInBytes": 345,
                    },
                ],
            },
            "projectInfo": {
                "projectId": "project-123",
                "projectName": "My Project",
                "projectOwnerUsername": "owner",
            },
        }
    )
    response = PaginatedDatasetRwEnvelopeV2(
        datasets=[dataset_info],
        metadata=PaginatedMetadataV1(
            notices=[],
            request_id="req-1",
            limit=100,
            offset=0,
            total_count=1,
        ),
    )

    monkeypatch.setattr(
        "app.core.domino_http.get_domino_public_api_client_sync",
        lambda: object(),
    )

    async def fake_get_datasets(*, client, minimum_permission, project_ids_to_include, **kwargs):
        assert project_ids_to_include == ["project-123"]
        return response

    monkeypatch.setattr(
        "app.api.generated.domino_public_api_client.api.dataset_rw.get_datasets_v2.asyncio",
        fake_get_datasets,
    )

    result = await list_datasets_response(
        project_id="project-123",
    )

    assert result.total == 1
    assert len(result.datasets) == 1

    dataset = result.datasets[0]
    assert dataset.id == "ds-123"
    assert dataset.name == "Training Dataset"
    assert dataset.description == "Tabular training data"
    assert dataset.path is None
    assert dataset.size_bytes == 0
    assert dataset.file_count == 0
    assert dataset.created_at.isoformat() == "2024-01-02T03:04:05+00:00"
    assert dataset.updated_at is None
    assert dataset.files == []


@pytest.mark.asyncio
async def test_list_datasets_response_defaults_missing_api_fields(monkeypatch):
    dataset_info = DatasetRwInfoDtoV1.from_dict(
        {
            "dataset": {
                "id": "ds-456",
                "name": "Bare Dataset",
                "createdAt": "2024-02-01T00:00:00Z",
                "snapshotIds": [],
                "tags": {},
            }
        }
    )
    response = PaginatedDatasetRwEnvelopeV2(
        datasets=[dataset_info],
        metadata=PaginatedMetadataV1(
            notices=[],
            request_id="req-2",
            limit=100,
            offset=0,
        ),
    )

    monkeypatch.setattr(
        "app.core.domino_http.get_domino_public_api_client_sync",
        lambda: object(),
    )

    async def fake_get_datasets(*, client, project_ids_to_include, **kwargs):
        assert project_ids_to_include == ["resolved-project"]
        return response

    monkeypatch.setattr(
        "app.api.generated.domino_public_api_client.api.dataset_rw.get_datasets_v2.asyncio",
        fake_get_datasets,
    )

    result = await list_datasets_response(
        project_id="resolved-project",
    )

    assert result.total == 1
    dataset = result.datasets[0]
    assert dataset.id == "ds-456"
    assert dataset.name == "Bare Dataset"
    assert dataset.description is None
    assert dataset.path is None
    assert dataset.size_bytes == 0
    assert dataset.file_count == 0
    assert dataset.files == []
    assert dataset.updated_at is None


def _make_dataset_envelope(*, dataset_id: str, name: str, snapshot_ids: list[str], tags: dict[str, str], description: str | None = None):
    dataset_payload = {
        "id": dataset_id,
        "name": name,
        "createdAt": "2024-02-01T00:00:00Z",
        "snapshotIds": snapshot_ids,
        "tags": tags,
    }
    if description is not None:
        dataset_payload["description"] = description

    return DatasetRwEnvelopeV1(
        dataset=DatasetRwDetailsV1.from_dict(dataset_payload),
        metadata=MetadataV1.from_dict({"requestId": "req-1", "notices": []}),
    )


def _file_row(name: str, size: int) -> SimpleNamespace:
    return SimpleNamespace(
        name=SimpleNamespace(file_name=name, sortable_name=name, label=name),
        size=SimpleNamespace(in_bytes=size, size_in_bytes=size, label=str(size)),
    )


@pytest.mark.asyncio
async def test_list_dataset_files_response_uses_default_snapshot_listing(monkeypatch):
    dataset_envelope = _make_dataset_envelope(
        dataset_id="ds-1",
        name="Example Dataset",
        snapshot_ids=["snap-1"],
        tags={"default": "snap-default"},
        description="Dataset description",
    )

    monkeypatch.setattr(
        "app.core.domino_http.get_domino_public_api_client_sync",
        lambda: object(),
    )
    monkeypatch.setattr(
        "app.core.domino_http.get_domino_private_api_client_sync",
        lambda: object(),
    )

    async def fake_get_dataset(*, dataset_id, client):
        assert dataset_id == "ds-1"
        return dataset_envelope

    async def fake_get_files_in_snapshot(*, snapshot_id, client, path):
        assert snapshot_id == "snap-1"
        assert path == ""
        return SimpleNamespace(rows=[_file_row("train.csv", 101), _file_row("test.csv", 202)])

    monkeypatch.setattr(
        "app.api.generated.domino_public_api_client.api.dataset_rw.get_dataset.asyncio",
        fake_get_dataset,
    )
    monkeypatch.setattr(
        "app.api.generated_private.domino_data_lab_api_v_4_client.api.dataset_rw.get_files_in_snapshot.asyncio",
        fake_get_files_in_snapshot,
    )

    result = await list_dataset_files_response(dataset_id="ds-1")

    assert result.total == 1
    assert len(result.datasets) == 1
    dataset = result.datasets[0]
    assert dataset.id == "ds-1"
    assert dataset.name == "Example Dataset"
    assert dataset.description == "Dataset description"
    assert dataset.file_count == 2
    assert dataset.size_bytes == 303
    assert [file.name for file in dataset.files] == ["train.csv", "test.csv"]
    assert [file.path for file in dataset.files] == ["train.csv", "test.csv"]
    assert [file.size for file in dataset.files] == [101, 202]


@pytest.mark.asyncio
async def test_list_dataset_files_response_falls_back_to_first_snapshot(monkeypatch):
    dataset_envelope = _make_dataset_envelope(
        dataset_id="ds-2",
        name="Fallback Dataset",
        snapshot_ids=["snap-first", "snap-second"],
        tags={},
    )

    monkeypatch.setattr(
        "app.core.domino_http.get_domino_public_api_client_sync",
        lambda: object(),
    )
    monkeypatch.setattr(
        "app.core.domino_http.get_domino_private_api_client_sync",
        lambda: object(),
    )

    async def fake_get_dataset(*, dataset_id, client):
        assert dataset_id == "ds-2"
        return dataset_envelope

    async def fake_get_files_in_snapshot(*, snapshot_id, client, path):
        assert snapshot_id == "snap-first"
        assert path == ""
        return SimpleNamespace(rows=[_file_row("nested/data.parquet", 4096)])

    monkeypatch.setattr(
        "app.api.generated.domino_public_api_client.api.dataset_rw.get_dataset.asyncio",
        fake_get_dataset,
    )
    monkeypatch.setattr(
        "app.api.generated_private.domino_data_lab_api_v_4_client.api.dataset_rw.get_files_in_snapshot.asyncio",
        fake_get_files_in_snapshot,
    )

    result = await list_dataset_files_response(dataset_id="ds-2")

    assert result.total == 1
    dataset = result.datasets[0]
    assert dataset.id == "ds-2"
    assert dataset.file_count == 1
    assert dataset.size_bytes == 4096
    assert dataset.files[0].name == "nested/data.parquet"
    assert dataset.files[0].path == "nested/data.parquet"
    assert dataset.files[0].size == 4096
