"""Tests for app.core.tabular_data — tabular file metadata, preview, and sampling helpers."""

from io import BytesIO

import numpy as np
import pandas as pd
import pytest

from app.core.tabular_data import (
    TabularFileMetadata,
    _sanitize_preview_df,
    count_csv_rows,
    estimate_tabular_memory_mb,
    get_tabular_metadata,
    read_parquet_metadata_from_buffer,
    read_tabular_preview,
    read_tabular_sample,
    read_tabular_schema,
    read_upload_metadata,
)

EXPECTED_COLUMNS = [
    "id", "age", "income", "score", "category", "target",
    "email_address", "created_date",
]
EXPECTED_ROW_COUNT = 200


# ---------------------------------------------------------------------------
# _sanitize_preview_df
# ---------------------------------------------------------------------------

class TestSanitizePreviewDf:
    def test_nan_replaced_with_none(self):
        df = pd.DataFrame({"a": [1.0, np.nan, 3.0]})
        result = _sanitize_preview_df(df)
        assert result["a"].tolist() == [1.0, None, 3.0]

    def test_positive_inf_replaced_with_none(self):
        df = pd.DataFrame({"a": [np.inf]})
        result = _sanitize_preview_df(df)
        assert result["a"].tolist() == [None]

    def test_negative_inf_replaced_with_none(self):
        df = pd.DataFrame({"a": [-np.inf]})
        result = _sanitize_preview_df(df)
        assert result["a"].tolist() == [None]

    def test_clean_data_unchanged(self):
        df = pd.DataFrame({"x": [1, 2, 3], "y": ["a", "b", "c"]})
        result = _sanitize_preview_df(df)
        pd.testing.assert_frame_equal(result, df)

    def test_mixed_nan_and_inf(self):
        df = pd.DataFrame({"v": [np.nan, np.inf, -np.inf, 42.0]})
        result = _sanitize_preview_df(df)
        assert result["v"].tolist() == [None, None, None, 42.0]

    def test_empty_dataframe(self):
        df = pd.DataFrame()
        result = _sanitize_preview_df(df)
        assert result.empty


# ---------------------------------------------------------------------------
# count_csv_rows
# ---------------------------------------------------------------------------

class TestCountCsvRows:
    def test_counts_data_rows_excluding_header(self, tabular_csv):
        assert count_csv_rows(tabular_csv) == EXPECTED_ROW_COUNT

    def test_empty_csv_returns_zero(self, tmp_path):
        path = str(tmp_path / "empty.csv")
        with open(path, "w") as f:
            f.write("col_a,col_b\n")
        assert count_csv_rows(path) == 0

    def test_single_row_csv(self, tmp_path):
        path = str(tmp_path / "one.csv")
        with open(path, "w") as f:
            f.write("a,b\n1,2\n")
        assert count_csv_rows(path) == 1


# ---------------------------------------------------------------------------
# get_tabular_metadata — CSV
# ---------------------------------------------------------------------------

class TestGetTabularMetadataCsv:
    def test_returns_tabular_file_metadata(self, tabular_csv):
        meta = get_tabular_metadata(tabular_csv)
        assert isinstance(meta, TabularFileMetadata)

    def test_columns_match(self, tabular_csv):
        meta = get_tabular_metadata(tabular_csv)
        assert meta.columns == EXPECTED_COLUMNS

    def test_total_rows(self, tabular_csv):
        meta = get_tabular_metadata(tabular_csv)
        assert meta.total_rows == EXPECTED_ROW_COUNT

    def test_dtypes_dict_keys_match_columns(self, tabular_csv):
        meta = get_tabular_metadata(tabular_csv)
        assert set(meta.dtypes.keys()) == set(EXPECTED_COLUMNS)

    def test_dtypes_are_strings(self, tabular_csv):
        meta = get_tabular_metadata(tabular_csv)
        for dtype_str in meta.dtypes.values():
            assert isinstance(dtype_str, str)


# ---------------------------------------------------------------------------
# get_tabular_metadata — Parquet
# ---------------------------------------------------------------------------

class TestGetTabularMetadataParquet:
    def test_returns_tabular_file_metadata(self, parquet_file):
        meta = get_tabular_metadata(parquet_file)
        assert isinstance(meta, TabularFileMetadata)

    def test_columns_match(self, parquet_file):
        meta = get_tabular_metadata(parquet_file)
        assert meta.columns == EXPECTED_COLUMNS

    def test_total_rows(self, parquet_file):
        meta = get_tabular_metadata(parquet_file)
        assert meta.total_rows == EXPECTED_ROW_COUNT

    def test_dtypes_present(self, parquet_file):
        meta = get_tabular_metadata(parquet_file)
        assert len(meta.dtypes) == len(EXPECTED_COLUMNS)


# ---------------------------------------------------------------------------
# get_tabular_metadata — unsupported format
# ---------------------------------------------------------------------------

def test_get_tabular_metadata_unsupported_format(tmp_path):
    path = str(tmp_path / "data.xlsx")
    with open(path, "w") as f:
        f.write("")
    with pytest.raises(ValueError, match="Unsupported file format"):
        get_tabular_metadata(path)


# ---------------------------------------------------------------------------
# read_tabular_preview
# ---------------------------------------------------------------------------

class TestReadTabularPreview:
    def test_csv_preview_basic(self, tabular_csv):
        result = read_tabular_preview(tabular_csv, limit=10)
        assert result["columns"] == EXPECTED_COLUMNS
        assert result["total_rows"] == EXPECTED_ROW_COUNT
        assert result["preview_rows"] == 10
        assert len(result["rows"]) == 10

    def test_csv_preview_with_offset(self, tabular_csv):
        page1 = read_tabular_preview(tabular_csv, limit=5, offset=0)
        page2 = read_tabular_preview(tabular_csv, limit=5, offset=5)
        ids_page1 = [r["id"] for r in page1["rows"]]
        ids_page2 = [r["id"] for r in page2["rows"]]
        assert ids_page1 != ids_page2
        assert len(set(ids_page1) & set(ids_page2)) == 0

    def test_csv_preview_include_dtypes(self, tabular_csv):
        result = read_tabular_preview(tabular_csv, limit=5, include_dtypes=True)
        assert "dtypes" in result
        assert isinstance(result["dtypes"], dict)
        assert set(result["dtypes"].keys()) == set(EXPECTED_COLUMNS)

    def test_csv_preview_dtypes_excluded_by_default(self, tabular_csv):
        result = read_tabular_preview(tabular_csv, limit=5)
        assert "dtypes" not in result

    def test_parquet_preview_basic(self, parquet_file):
        result = read_tabular_preview(parquet_file, limit=10)
        assert result["columns"] == EXPECTED_COLUMNS
        assert result["total_rows"] == EXPECTED_ROW_COUNT
        assert result["preview_rows"] == 10

    def test_parquet_preview_with_offset(self, parquet_file):
        page1 = read_tabular_preview(parquet_file, limit=5, offset=0)
        page2 = read_tabular_preview(parquet_file, limit=5, offset=5)
        ids_page1 = [r["id"] for r in page1["rows"]]
        ids_page2 = [r["id"] for r in page2["rows"]]
        assert len(set(ids_page1) & set(ids_page2)) == 0

    def test_preview_nan_values_are_none(self, tabular_csv):
        # The fixture injects NaN into the income column; preview should have None
        result = read_tabular_preview(tabular_csv, limit=200)
        none_count = sum(1 for r in result["rows"] if r["income"] is None)
        assert none_count > 0, "Expected None values for NaN income entries"

    def test_preview_offset_beyond_data(self, parquet_file):
        result = read_tabular_preview(parquet_file, limit=10, offset=999)
        assert result["preview_rows"] == 0
        assert result["rows"] == []

    def test_unsupported_format_raises(self, tmp_path):
        path = str(tmp_path / "data.txt")
        with open(path, "w") as f:
            f.write("a,b\n1,2\n")
        with pytest.raises(ValueError, match="Unsupported file format"):
            read_tabular_preview(path, limit=10)


# ---------------------------------------------------------------------------
# read_tabular_schema
# ---------------------------------------------------------------------------

class TestReadTabularSchema:
    def test_csv_schema_structure(self, tabular_csv):
        schema = read_tabular_schema(tabular_csv)
        assert "columns" in schema
        assert "row_count" in schema
        assert schema["row_count"] == EXPECTED_ROW_COUNT

    def test_csv_schema_columns_format(self, tabular_csv):
        schema = read_tabular_schema(tabular_csv)
        for col_info in schema["columns"]:
            assert "name" in col_info
            assert "dtype" in col_info
            assert isinstance(col_info["name"], str)
            assert isinstance(col_info["dtype"], str)

    def test_csv_schema_column_names(self, tabular_csv):
        schema = read_tabular_schema(tabular_csv)
        names = [c["name"] for c in schema["columns"]]
        assert names == EXPECTED_COLUMNS

    def test_parquet_schema(self, parquet_file):
        schema = read_tabular_schema(parquet_file)
        assert schema["row_count"] == EXPECTED_ROW_COUNT
        names = [c["name"] for c in schema["columns"]]
        assert names == EXPECTED_COLUMNS


# ---------------------------------------------------------------------------
# read_tabular_sample
# ---------------------------------------------------------------------------

class TestReadTabularSample:
    def test_csv_sample_returns_dataframe(self, tabular_csv):
        df = read_tabular_sample(tabular_csv, sample_rows=20)
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 20

    def test_csv_sample_columns(self, tabular_csv):
        df = read_tabular_sample(tabular_csv, sample_rows=5)
        assert list(df.columns) == EXPECTED_COLUMNS

    def test_parquet_sample(self, parquet_file):
        df = read_tabular_sample(parquet_file, sample_rows=15)
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 15

    def test_sample_rows_clamped_to_at_least_one(self, tabular_csv):
        df = read_tabular_sample(tabular_csv, sample_rows=0)
        assert len(df) >= 1

    def test_json_sample(self, tmp_path):
        path = str(tmp_path / "data.json")
        pd.DataFrame({"a": range(50), "b": range(50)}).to_json(path)
        df = read_tabular_sample(path, sample_rows=10)
        assert len(df) == 10

    def test_unsupported_format_raises(self, tmp_path):
        path = str(tmp_path / "data.txt")
        with open(path, "w") as f:
            f.write("x")
        with pytest.raises(ValueError, match="Unsupported file format"):
            read_tabular_sample(path, sample_rows=5)


# ---------------------------------------------------------------------------
# estimate_tabular_memory_mb
# ---------------------------------------------------------------------------

class TestEstimateTabularMemoryMb:
    def test_csv_returns_positive_float(self, tabular_csv):
        est = estimate_tabular_memory_mb(tabular_csv)
        assert isinstance(est, float)
        assert est > 0

    def test_parquet_returns_positive_float(self, parquet_file):
        est = estimate_tabular_memory_mb(parquet_file)
        assert isinstance(est, float)
        assert est > 0

    def test_estimate_is_reasonable(self, tabular_csv):
        # 200 rows x 8 columns — should be well under 10 MB
        est = estimate_tabular_memory_mb(tabular_csv)
        assert est < 10.0


# ---------------------------------------------------------------------------
# read_upload_metadata
# ---------------------------------------------------------------------------

class TestReadUploadMetadata:
    def test_csv_bytes(self, tabular_csv):
        with open(tabular_csv, "rb") as f:
            content = f.read()
        columns, row_count = read_upload_metadata(content, ".csv")
        assert columns == EXPECTED_COLUMNS
        assert row_count == EXPECTED_ROW_COUNT

    def test_parquet_bytes(self, parquet_file):
        with open(parquet_file, "rb") as f:
            content = f.read()
        columns, row_count = read_upload_metadata(content, ".parquet")
        assert set(columns) == set(EXPECTED_COLUMNS)
        assert row_count == EXPECTED_ROW_COUNT

    def test_pq_extension(self, parquet_file):
        with open(parquet_file, "rb") as f:
            content = f.read()
        columns, row_count = read_upload_metadata(content, ".pq")
        assert row_count == EXPECTED_ROW_COUNT

    def test_unsupported_extension_raises(self):
        with pytest.raises(ValueError, match="Unsupported file format"):
            read_upload_metadata(b"data", ".xlsx")

    def test_csv_empty_body(self):
        content = b"col_a,col_b\n"
        columns, row_count = read_upload_metadata(content, ".csv")
        assert columns == ["col_a", "col_b"]
        assert row_count == 0


# ---------------------------------------------------------------------------
# read_parquet_metadata_from_buffer
# ---------------------------------------------------------------------------

class TestReadParquetMetadataFromBuffer:
    def test_returns_metadata(self, parquet_file):
        with open(parquet_file, "rb") as f:
            meta = read_parquet_metadata_from_buffer(f)
        assert isinstance(meta, TabularFileMetadata)
        assert meta.columns == EXPECTED_COLUMNS
        assert meta.total_rows == EXPECTED_ROW_COUNT

    def test_dtypes_populated(self, parquet_file):
        with open(parquet_file, "rb") as f:
            meta = read_parquet_metadata_from_buffer(f)
        assert len(meta.dtypes) == len(EXPECTED_COLUMNS)
        for v in meta.dtypes.values():
            assert isinstance(v, str)

    def test_bytes_io_buffer(self, parquet_file):
        with open(parquet_file, "rb") as f:
            buf = BytesIO(f.read())
        meta = read_parquet_metadata_from_buffer(buf)
        assert meta.total_rows == EXPECTED_ROW_COUNT


# ---------------------------------------------------------------------------
# TabularFileMetadata frozen dataclass
# ---------------------------------------------------------------------------

def test_metadata_is_frozen():
    meta = TabularFileMetadata(columns=["a"], dtypes={"a": "int64"}, total_rows=1)
    with pytest.raises(AttributeError):
        meta.total_rows = 99
