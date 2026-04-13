"""Shared helpers for file-backed profilers."""

from abc import ABC, abstractmethod
from io import BytesIO
from typing import Optional

import pandas as pd


class BaseProfiler(ABC):
    """Common file-loading logic for profilers."""

    @abstractmethod
    async def _fetch_file_bytes(self, dataset_id: str, file_path: str) -> bytes:
        """Fetch file bytes for a dataset-backed file path."""

    async def _load_dataframe(
        self,
        file_path: str,
        dataset_id: Optional[str] = None,
        parse_dates: Optional[list[str]] = None,
    ) -> pd.DataFrame:
        """Load a supported tabular file from a dataset or local filesystem.

        dataset_id may be omitted when the profiler is running in a Domino Job, but MUST
        be provided when running in the main application"""
        content: str | BytesIO = file_path
        normalized_file_path = file_path.lower()

        if dataset_id:
            file_bytes = await self._fetch_file_bytes(dataset_id=dataset_id, file_path=file_path)
            content = BytesIO(file_bytes)

        csv_kwargs = {"parse_dates": parse_dates} if parse_dates else {}
        excel_kwargs = {"parse_dates": parse_dates} if parse_dates else {}

        try:
            if normalized_file_path.endswith(".csv"):
                return pd.read_csv(content, **csv_kwargs)
            if normalized_file_path.endswith((".parquet", ".pq")):
                return pd.read_parquet(content)
            if normalized_file_path.endswith(".json"):
                return pd.read_json(content)
            if normalized_file_path.endswith((".xlsx", ".xls")):
                return pd.read_excel(content, **excel_kwargs)
            raise ValueError(f"Unsupported file format: {file_path}")
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"File not found: {file_path}") from exc
