"""Helpers for low-latency tabular file metadata, preview, and sampling."""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache
from io import BytesIO
from typing import Any, BinaryIO

import numpy as np
import pandas as pd

try:
    import pyarrow as pa
    import pyarrow.parquet as pq
except Exception:  # pragma: no cover - parquet tests cover the happy path
    pa = None
    pq = None


SUPPORTED_TABULAR_EXTENSIONS = (".csv", ".parquet", ".pq")
DEFAULT_DTYPE_SAMPLE_ROWS = 1000


@dataclass(frozen=True)
class TabularFileMetadata:
    """Basic metadata needed by preview/schema/quick-profile paths."""

    columns: list[str]
    dtypes: dict[str, str]
    total_rows: int


def _sanitize_preview_df(df: pd.DataFrame) -> pd.DataFrame:
    """Replace NaN and infinities so preview rows are JSON-safe."""
    return df.replace({np.nan: None, np.inf: None, -np.inf: None})


def _csv_cache_key(file_path: str) -> tuple[str, int, int]:
    stat = os.stat(file_path)
    return file_path, stat.st_mtime_ns, stat.st_size


def _parquet_cache_key(file_path: str) -> tuple[str, int, int]:
    stat = os.stat(file_path)
    return file_path, stat.st_mtime_ns, stat.st_size


@lru_cache(maxsize=256)
def _count_csv_rows_cached(file_path: str, mtime_ns: int, size_bytes: int) -> int:
    """Count CSV rows once per file version."""
    del mtime_ns, size_bytes
    total = -1
    with open(file_path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            total += chunk.count(b"\n")
    return max(total, 0)


def count_csv_rows(file_path: str) -> int:
    """Return the number of data rows in a CSV file."""
    return _count_csv_rows_cached(*_csv_cache_key(file_path))


@lru_cache(maxsize=256)
def _read_parquet_metadata_cached(
    file_path: str,
    mtime_ns: int,
    size_bytes: int,
) -> TabularFileMetadata:
    """Read parquet metadata once per file version."""
    del mtime_ns, size_bytes
    if pq is None:
        df = pd.read_parquet(file_path)
        return TabularFileMetadata(
            columns=list(df.columns),
            dtypes={col: str(dtype) for col, dtype in df.dtypes.items()},
            total_rows=len(df),
        )

    parquet_file = pq.ParquetFile(file_path)
    schema = parquet_file.schema_arrow
    return TabularFileMetadata(
        columns=list(schema.names),
        dtypes={field.name: str(field.type) for field in schema},
        total_rows=parquet_file.metadata.num_rows,
    )


def _read_csv_dtype_sample(file_path: str, sample_rows: int) -> pd.DataFrame:
    rows = max(1, sample_rows)
    return pd.read_csv(file_path, nrows=rows)


def get_tabular_metadata(
    file_path: str,
    *,
    dtype_sample_rows: int = DEFAULT_DTYPE_SAMPLE_ROWS,
) -> TabularFileMetadata:
    """Return columns, inferred dtypes, and row counts for a tabular file."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".csv":
        sample_df = _read_csv_dtype_sample(file_path, dtype_sample_rows)
        return TabularFileMetadata(
            columns=list(sample_df.columns),
            dtypes={col: str(dtype) for col, dtype in sample_df.dtypes.items()},
            total_rows=count_csv_rows(file_path),
        )
    if ext in {".parquet", ".pq"}:
        return _read_parquet_metadata_cached(*_parquet_cache_key(file_path))
    raise ValueError(f"Unsupported file format: {file_path}")


def _read_csv_preview(file_path: str, limit: int, offset: int) -> pd.DataFrame:
    if offset > 0:
        return pd.read_csv(file_path, skiprows=range(1, offset + 1), nrows=limit)
    return pd.read_csv(file_path, nrows=limit)


def _read_parquet_preview(file_path: str, limit: int, offset: int) -> pd.DataFrame:
    if pq is None:
        return pd.read_parquet(file_path).iloc[offset : offset + limit]

    parquet_file = pq.ParquetFile(file_path)
    remaining_skip = offset
    remaining_take = limit
    frames: list[pd.DataFrame] = []
    batch_size = max(limit, 1024)

    for batch in parquet_file.iter_batches(batch_size=batch_size):
        rows_in_batch = batch.num_rows
        if remaining_skip >= rows_in_batch:
            remaining_skip -= rows_in_batch
            continue

        start = remaining_skip
        remaining_skip = 0
        length = min(rows_in_batch - start, remaining_take)
        sliced = batch.slice(start, length)
        frames.append(sliced.to_pandas())
        remaining_take -= length
        if remaining_take <= 0:
            break

    if not frames:
        return pd.DataFrame(columns=list(parquet_file.schema_arrow.names))
    return pd.concat(frames, ignore_index=True)


def read_tabular_preview(
    file_path: str,
    *,
    limit: int,
    offset: int = 0,
    include_dtypes: bool = False,
) -> dict[str, Any]:
    """Return a paginated preview payload without fully loading the file."""
    metadata = get_tabular_metadata(file_path)
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".csv":
        df = _read_csv_preview(file_path, limit, offset)
    elif ext in {".parquet", ".pq"}:
        df = _read_parquet_preview(file_path, limit, offset)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")

    payload: dict[str, Any] = {
        "columns": metadata.columns,
        "rows": _sanitize_preview_df(df).to_dict(orient="records"),
        "total_rows": metadata.total_rows,
        "preview_rows": len(df),
    }
    if include_dtypes:
        payload["dtypes"] = metadata.dtypes
    return payload


def read_tabular_schema(file_path: str) -> dict[str, Any]:
    """Return schema metadata for a local CSV/Parquet file."""
    metadata = get_tabular_metadata(file_path)
    return {
        "columns": [
            {"name": column_name, "dtype": metadata.dtypes.get(column_name, "object")}
            for column_name in metadata.columns
        ],
        "row_count": metadata.total_rows,
    }


def read_tabular_sample(
    file_path: str,
    *,
    sample_rows: int,
) -> pd.DataFrame:
    """Read a small sample without loading the full dataset."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".csv":
        return pd.read_csv(file_path, nrows=max(1, sample_rows))
    if ext in {".parquet", ".pq"}:
        return _read_parquet_preview(file_path, limit=max(1, sample_rows), offset=0)
    if ext == ".json":
        return pd.read_json(file_path).head(sample_rows)
    if ext in {".xlsx", ".xls"}:
        return pd.read_excel(file_path, nrows=max(1, sample_rows))
    raise ValueError(f"Unsupported file format: {file_path}")


def estimate_tabular_memory_mb(
    file_path: str,
    *,
    sample_rows: int = DEFAULT_DTYPE_SAMPLE_ROWS,
) -> float:
    """Estimate in-memory size from a small sample."""
    metadata = get_tabular_metadata(file_path)
    sample_df = read_tabular_sample(file_path, sample_rows=sample_rows)
    if sample_df.empty or metadata.total_rows <= 0:
        return 0.0
    sample_memory = sample_df.memory_usage(deep=True).sum()
    estimated_total = sample_memory * (metadata.total_rows / max(len(sample_df), 1))
    return float(estimated_total / (1024 * 1024))


def read_upload_metadata(content: bytes, file_ext: str) -> tuple[list[str], int]:
    """Extract columns and row count for uploaded CSV/Parquet bytes."""
    if file_ext == ".csv":
        header_df = pd.read_csv(BytesIO(content), nrows=1)
        return list(header_df.columns), max(content.count(b"\n") - 1, 0)

    if file_ext in {".parquet", ".pq"}:
        if pq is None:
            df = pd.read_parquet(BytesIO(content))
            return list(df.columns), len(df)

        parquet_file = pq.ParquetFile(BytesIO(content))
        schema = parquet_file.schema_arrow
        return list(schema.names), parquet_file.metadata.num_rows

    raise ValueError(f"Unsupported file format: {file_ext}")


def read_parquet_metadata_from_buffer(buffer: BinaryIO) -> TabularFileMetadata:
    """Return parquet metadata from an in-memory buffer."""
    if pq is None:
        df = pd.read_parquet(buffer)
        return TabularFileMetadata(
            columns=list(df.columns),
            dtypes={col: str(dtype) for col, dtype in df.dtypes.items()},
            total_rows=len(df),
        )

    parquet_file = pq.ParquetFile(buffer)
    schema = parquet_file.schema_arrow
    return TabularFileMetadata(
        columns=list(schema.names),
        dtypes={field.name: str(field.type) for field in schema},
        total_rows=parquet_file.metadata.num_rows,
    )
