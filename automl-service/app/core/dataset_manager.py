"""Domino dataset management using REST API."""

import logging
import os
from typing import Any, Optional

import httpx
import pandas as pd

from app.config import get_settings
from app.api.schemas.dataset import (
    DatasetResponse,
    DatasetPreviewResponse,
    DatasetSchemaResponse,
)

logger = logging.getLogger(__name__)


class DominoDatasetManager:
    """Manages Domino datasets using the Domino REST API."""

    def __init__(self):
        self.settings = get_settings()
        self._http_client: Optional[httpx.AsyncClient] = None

    @property
    def api_headers(self) -> dict:
        """Get headers for Domino API requests."""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if self.settings.effective_api_key:
            headers["X-Domino-Api-Key"] = self.settings.effective_api_key
        return headers

    @property
    def api_base_url(self) -> str:
        """Get Domino API base URL."""
        host = self.settings.domino_api_host or ""
        return host.rstrip("/")

    async def _get_client(self) -> httpx.AsyncClient:
        """Get or create HTTP client."""
        if self._http_client is None or self._http_client.is_closed:
            self._http_client = httpx.AsyncClient(timeout=30.0)
        return self._http_client

    async def _api_request(self, method: str, endpoint: str, **kwargs) -> dict:
        """Make a request to the Domino API."""
        client = await self._get_client()
        url = f"{self.api_base_url}{endpoint}"

        logger.info(f"Domino API request: {method} {url}")

        response = await client.request(
            method=method,
            url=url,
            headers=self.api_headers,
            **kwargs
        )

        logger.info(f"Domino API response: {response.status_code}")

        if response.status_code >= 400:
            logger.error(f"Domino API error: {response.text}")
            response.raise_for_status()

        return response.json() if response.text else {}

    async def list_datasets(self) -> list[DatasetResponse]:
        """List available datasets from /domino/datasets/local/ only."""
        # Only list datasets from /domino/datasets/local/ - this is the only
        # location we support for training data
        datasets = await self._list_local_datasets()
        logger.info(f"Found {len(datasets)} datasets in /domino/datasets/local/")
        return datasets

    async def _list_local_datasets(self) -> list[DatasetResponse]:
        """List datasets from /domino/datasets/local/ directory only."""
        datasets = []
        # Only scan /domino/datasets/local/ - this is where Domino mounts datasets
        domino_dataset_path = "/domino/datasets/local"

        if os.path.exists(domino_dataset_path):
            # List subdirectories (each is a mounted dataset)
            for item in os.listdir(domino_dataset_path):
                item_path = os.path.join(domino_dataset_path, item)
                if os.path.isdir(item_path):
                    # This is a dataset directory - find files inside
                    files = []
                    total_size = 0
                    for root, _, filenames in os.walk(item_path):
                        for filename in filenames:
                            if filename.endswith((".csv", ".parquet", ".pq")):
                                file_path = os.path.join(root, filename)
                                rel_path = os.path.relpath(file_path, item_path)
                                file_stat = os.stat(file_path)
                                files.append({
                                    "name": rel_path,
                                    "path": file_path,
                                    "size": file_stat.st_size,
                                })
                                total_size += file_stat.st_size

                    if files:  # Only add if there are CSV/Parquet files
                        datasets.append(
                            DatasetResponse(
                                id=f"domino:{item}",
                                name=item,
                                description="Domino dataset",
                                size_bytes=total_size,
                                file_count=len(files),
                                files=files,
                            )
                        )
                elif os.path.isfile(item_path) and item.endswith((".csv", ".parquet", ".pq")):
                    # File directly in /domino/datasets/local/
                    stat = os.stat(item_path)
                    datasets.append(
                        DatasetResponse(
                            id=f"domino:{item}",
                            name=item,
                            description="Domino dataset",
                            size_bytes=stat.st_size,
                            file_count=1,
                            files=[{"name": item, "path": item_path, "size": stat.st_size}],
                        )
                    )

        logger.info(f"Found {len(datasets)} datasets in /domino/datasets/local/")
        return datasets

    async def get_dataset(self, dataset_id: str) -> Optional[DatasetResponse]:
        """Get dataset details using REST API."""
        if dataset_id.startswith("local:"):
            # Local dataset
            file_name = dataset_id.replace("local:", "")
            file_path = os.path.join(self.settings.datasets_path, file_name)

            if os.path.exists(file_path):
                stat = os.stat(file_path)
                return DatasetResponse(
                    id=dataset_id,
                    name=file_name,
                    description="Local dataset",
                    size_bytes=stat.st_size,
                    file_count=1,
                    files=[file_name],
                )
            return None

        # Domino dataset - use REST API
        if self.settings.is_domino_environment:
            try:
                result = await self._api_request("GET", f"/api/datasetrw/v1/datasets/{dataset_id}")
                return DatasetResponse(
                    id=result.get("datasetId", result.get("id", dataset_id)),
                    name=result.get("datasetName", result.get("name", "")),
                    description=result.get("description", ""),
                    size_bytes=result.get("sizeInBytes", result.get("size", 0)),
                    created_at=result.get("createdAt"),
                    updated_at=result.get("lastUpdatedAt", result.get("updatedAt")),
                    file_count=result.get("fileCount", 0),
                    files=result.get("files", []),
                )
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 404:
                    return None
                logger.error(f"HTTP error getting dataset: {e.response.status_code}")
            except Exception as e:
                logger.error(f"Failed to get dataset details: {e}")

        return None

    async def get_dataset_file_path(
        self,
        dataset_id: str,
        file_name: Optional[str] = None,
    ) -> str:
        """Get the file path for a dataset file."""
        if dataset_id.startswith("local:"):
            file_name = dataset_id.replace("local:", "")
            return os.path.join(self.settings.datasets_path, file_name)

        if dataset_id.startswith("domino:"):
            # Domino dataset from /domino/datasets/local/
            dataset_name = dataset_id.replace("domino:", "")
            dataset_path = f"/domino/datasets/local/{dataset_name}"
            if file_name:
                return os.path.join(dataset_path, file_name)
            # Check if it's a file directly
            if os.path.isfile(dataset_path):
                return dataset_path
            # It's a directory - find first CSV/Parquet file
            if os.path.isdir(dataset_path):
                for root, _, files in os.walk(dataset_path):
                    for f in files:
                        if f.endswith((".csv", ".parquet", ".pq")):
                            return os.path.join(root, f)
            raise FileNotFoundError(f"No data files found in dataset: {dataset_id}")

        # For other Domino datasets, files are mounted at /domino/datasets/local/{dataset_name}
        dataset = await self.get_dataset(dataset_id)
        if dataset:
            dataset_path = f"/domino/datasets/local/{dataset.name}"
            if file_name:
                return os.path.join(dataset_path, file_name)
            elif dataset.files:
                # Return first CSV/Parquet file
                for f in dataset.files:
                    if isinstance(f, dict):
                        return f.get("path", "")
                    elif f.endswith((".csv", ".parquet", ".pq")):
                        return os.path.join(dataset_path, f)
            return dataset_path

        raise FileNotFoundError(f"Dataset not found: {dataset_id}")

    async def preview_dataset(
        self,
        dataset_id: str,
        file_name: Optional[str] = None,
        rows: int = 100,
    ) -> DatasetPreviewResponse:
        """Preview dataset content."""
        file_path = await self.get_dataset_file_path(dataset_id, file_name)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Read file
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith((".parquet", ".pq")):
            df = pd.read_parquet(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_path}")

        total_rows = len(df)
        preview_df = df.head(rows)

        return DatasetPreviewResponse(
            dataset_id=dataset_id,
            file_name=os.path.basename(file_path),
            columns=list(df.columns),
            rows=preview_df.to_dict(orient="records"),
            total_rows=total_rows,
            preview_rows=len(preview_df),
        )

    async def get_schema(
        self,
        dataset_id: str,
        file_name: Optional[str] = None,
    ) -> DatasetSchemaResponse:
        """Get dataset schema (column names and types)."""
        file_path = await self.get_dataset_file_path(dataset_id, file_name)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Read file
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith((".parquet", ".pq")):
            df = pd.read_parquet(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_path}")

        columns = [
            {"name": col, "dtype": str(df[col].dtype)}
            for col in df.columns
        ]

        return DatasetSchemaResponse(
            dataset_id=dataset_id,
            file_name=os.path.basename(file_path),
            columns=columns,
            row_count=len(df),
        )
