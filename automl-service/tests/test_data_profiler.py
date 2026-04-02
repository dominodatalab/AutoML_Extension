"""Tests for app.core.data_profiler.DataProfiler."""

import numpy as np
import pandas as pd
import pytest

from app.core.data_profiler import DataProfiler


@pytest.fixture
def profiler():
    return DataProfiler()


# ---------------------------------------------------------------------------
# profile_file
# ---------------------------------------------------------------------------


class TestProfileFile:
    """Tests for DataProfiler.profile_file."""

    @pytest.mark.asyncio
    async def test_reads_dataset_file_bytes_via_data_api(self, profiler, monkeypatch):
        calls = []

        async def fake_fetch(dataset_id: str, file_path: str) -> bytes:
            calls.append((dataset_id, file_path))
            return b"id,feature,target\n1,10,0\n2,20,1\n"

        monkeypatch.setattr(
            "app.core.data_profiler.dataset_file_bytes.fetch",
            fake_fetch,
        )

        result = await profiler.profile_file(
            dataset_id="ds-123",
            file_path="folder/train.csv",
        )

        assert calls == [("ds-123", "folder/train.csv")]
        assert result["summary"]["total_rows"] == 2
        assert result["summary"]["total_columns"] == 3
        assert isinstance(result["columns"], list)
        assert len(result["columns"]) == 3


# ---------------------------------------------------------------------------
# profile_dataframe — summary
# ---------------------------------------------------------------------------


class TestProfileDataframeSummary:
    """Tests for profile_dataframe summary section."""

    def test_summary_keys(self, profiler, tabular_df):
        result = profiler.profile_dataframe(tabular_df)
        summary = result["summary"]
        assert summary["total_rows"] == 200
        assert summary["total_columns"] == 8
        assert isinstance(summary["memory_usage_mb"], float)
        assert summary["memory_usage_mb"] > 0
        assert isinstance(summary["duplicate_rows"], int)
        assert isinstance(summary["duplicate_percentage"], float)

    def test_not_sampled_when_small(self, profiler, tabular_df):
        """200 rows with default sample_size=50000 should not be sampled."""
        result = profiler.profile_dataframe(tabular_df)
        assert result["summary"]["sampled"] is False
        assert result["summary"]["sample_size"] == 200


# ---------------------------------------------------------------------------
# Sampling strategies
# ---------------------------------------------------------------------------


class TestSamplingStrategies:
    """Tests for the four sampling strategies."""

    @pytest.fixture
    def large_df(self):
        """A DataFrame large enough to trigger sampling."""
        rng = np.random.RandomState(0)
        n = 500
        return pd.DataFrame({
            "x": rng.normal(size=n),
            "cat": rng.choice(["A", "B", "C"], size=n),
        })

    def test_random_sampling(self, profiler, large_df):
        result = profiler.profile_dataframe(large_df, sample_size=100, sampling_strategy="random")
        assert result["summary"]["sampled"] is True
        assert result["summary"]["sample_size"] == 100
        assert result["summary"]["sampling_strategy"] == "random"

    def test_head_sampling(self, profiler, large_df):
        result = profiler.profile_dataframe(large_df, sample_size=50, sampling_strategy="head")
        assert result["summary"]["sampled"] is True
        assert result["summary"]["sample_size"] == 50
        assert result["summary"]["sampling_strategy"] == "head"

    def test_stratified_sampling(self, profiler, large_df):
        result = profiler.profile_dataframe(
            large_df, sample_size=100, sampling_strategy="stratified", stratify_column="cat"
        )
        assert result["summary"]["sampled"] is True
        assert result["summary"]["sample_size"] <= 100
        assert result["summary"]["sampling_strategy"] == "stratified"

    def test_full_no_sampling(self, profiler, large_df):
        result = profiler.profile_dataframe(large_df, sample_size=100, sampling_strategy="full")
        # full strategy uses all rows regardless of sample_size
        assert result["summary"]["sample_size"] == len(large_df)
        assert result["summary"]["sampling_strategy"] == "full"

    def test_stratified_falls_back_on_missing_column(self, profiler, large_df):
        """Stratified with a non-existent column should fall back to random."""
        result = profiler.profile_dataframe(
            large_df, sample_size=100, sampling_strategy="stratified", stratify_column="nope"
        )
        # Falls through to the random branch
        assert result["summary"]["sampled"] is True
        assert result["summary"]["sample_size"] == 100


# ---------------------------------------------------------------------------
# Column profiling — numeric
# ---------------------------------------------------------------------------


class TestNumericColumnProfile:
    """Tests for numeric column statistics."""

    def test_numeric_stats_present(self, profiler, tabular_df):
        result = profiler.profile_dataframe(tabular_df)
        income_col = next(c for c in result["columns"] if c["name"] == "income")
        stats = income_col["statistics"]
        for key in ("min", "max", "mean", "median", "std", "variance", "skewness", "kurtosis"):
            assert key in stats, f"Missing numeric stat: {key}"

    def test_percentiles(self, profiler, tabular_df):
        result = profiler.profile_dataframe(tabular_df)
        income_col = next(c for c in result["columns"] if c["name"] == "income")
        percentiles = income_col["statistics"]["percentiles"]
        assert "p25" in percentiles
        assert "p50" in percentiles
        assert "p75" in percentiles
        assert percentiles["p25"] <= percentiles["p50"] <= percentiles["p75"]

    def test_outlier_detection(self, profiler):
        """Inject extreme outliers and verify they are counted."""
        rng = np.random.RandomState(0)
        values = np.concatenate([rng.normal(50, 2, 200), [500, -400]])
        df = pd.DataFrame({"val": values})
        result = profiler.profile_dataframe(df)
        val_col = next(c for c in result["columns"] if c["name"] == "val")
        assert val_col["statistics"]["outliers_count"] >= 2

    def test_histogram(self, profiler, tabular_df):
        result = profiler.profile_dataframe(tabular_df)
        age_col = next(c for c in result["columns"] if c["name"] == "age")
        histogram = age_col.get("histogram", {})
        assert "counts" in histogram
        assert "bin_edges" in histogram
        assert len(histogram["bin_edges"]) == len(histogram["counts"]) + 1


# ---------------------------------------------------------------------------
# Column profiling — categorical
# ---------------------------------------------------------------------------


class TestCategoricalColumnProfile:
    """Tests for categorical column statistics."""

    def test_categorical_stats_present(self, profiler, tabular_df):
        result = profiler.profile_dataframe(tabular_df)
        cat_col = next(c for c in result["columns"] if c["name"] == "category")
        stats = cat_col["statistics"]
        for key in ("unique_count", "most_common", "most_common_count", "least_common",
                     "least_common_count", "avg_string_length", "max_string_length"):
            assert key in stats, f"Missing categorical stat: {key}"

    def test_value_counts_top_10(self, profiler, tabular_df):
        result = profiler.profile_dataframe(tabular_df)
        cat_col = next(c for c in result["columns"] if c["name"] == "category")
        vc = cat_col.get("value_counts", [])
        assert len(vc) > 0
        assert len(vc) <= 10
        assert all("value" in v and "count" in v and "percentage" in v for v in vc)


# ---------------------------------------------------------------------------
# Column profiling — datetime
# ---------------------------------------------------------------------------


class TestDatetimeColumnProfile:
    """Tests for datetime column statistics."""

    def test_datetime_stats_present(self, profiler):
        dates = pd.date_range("2024-01-01", periods=100, freq="D")
        df = pd.DataFrame({"dt": dates, "val": range(100)})
        result = profiler.profile_dataframe(df)
        dt_col = next(c for c in result["columns"] if c["name"] == "dt")
        stats = dt_col["statistics"]
        assert "min" in stats
        assert "max" in stats
        assert "range_days" in stats
        assert stats["range_days"] == 99


# ---------------------------------------------------------------------------
# _infer_semantic_type
# ---------------------------------------------------------------------------


class TestInferSemanticType:
    """Tests for semantic type inference."""

    def test_name_patterns(self, profiler):
        cases = [
            ("user_id", [1, 2, 3], "identifier"),
            ("created_date", ["2024-01-01", "2024-01-02", "2024-01-03"], "datetime"),
            ("email_address", ["a@b.com", "c@d.com", "e@f.com"], "email"),
            ("price_usd", [10.0, 20.0, 30.0], "monetary"),
            ("pct_change", [0.1, 0.2, 0.3], "percentage"),
            ("user_name", ["Alice", "Bob", "Charlie"], "name"),
            ("product_category", ["A", "B", "C"], "category"),
            ("is_active", [True, False, True], "boolean"),
        ]
        for col_name, data, expected_type in cases:
            col = pd.Series(data, name=col_name)
            assert profiler._infer_semantic_type(col) == expected_type, (
                f"Expected '{expected_type}' for column '{col_name}'"
            )

    def test_dtype_binary(self, profiler):
        col = pd.Series([0, 1, 0, 1, 0, 1], name="flag_col_x")
        # Name doesn't match patterns; dtype is numeric with 2 unique => binary
        # Actually "flag" matches the boolean pattern, use a different name
        col = pd.Series([0, 1, 0, 1, 0, 1], name="outcome")
        assert profiler._infer_semantic_type(col) == "binary"

    def test_dtype_numeric(self, profiler):
        col = pd.Series(list(range(100)), name="measurement")
        assert profiler._infer_semantic_type(col) == "numeric"

    def test_dtype_datetime(self, profiler):
        col = pd.Series(pd.date_range("2024-01-01", periods=5), name="my_col")
        assert profiler._infer_semantic_type(col) == "datetime"

    def test_object_low_cardinality_is_category(self, profiler):
        col = pd.Series(["red", "green", "blue"] * 50, name="color")
        assert profiler._infer_semantic_type(col) in ("category",)

    def test_object_long_strings_is_text(self, profiler):
        col = pd.Series(["x" * 150] * 10, name="content")
        assert profiler._infer_semantic_type(col) == "text"


# ---------------------------------------------------------------------------
# _detect_column_issues
# ---------------------------------------------------------------------------


class TestDetectColumnIssues:
    """Tests for column issue detection."""

    def test_high_missing(self, profiler):
        col = pd.Series([np.nan] * 60 + [1.0] * 40, name="mostly_null")
        issues = profiler._detect_column_issues(col)
        assert any("High missing rate" in i for i in issues)

    def test_significant_missing(self, profiler):
        col = pd.Series([np.nan] * 25 + [1.0] * 75, name="some_null")
        issues = profiler._detect_column_issues(col)
        assert any("Significant missing values" in i for i in issues)

    def test_constant_column(self, profiler):
        col = pd.Series([42] * 100, name="constant")
        issues = profiler._detect_column_issues(col)
        assert any("Constant" in i for i in issues)

    def test_high_cardinality_string(self, profiler):
        col = pd.Series([f"val_{i}" for i in range(200)], name="high_card")
        issues = profiler._detect_column_issues(col)
        assert any("High cardinality" in i for i in issues)

    def test_all_unique_identifier(self, profiler):
        col = pd.Series(list(range(100)), name="seq")
        issues = profiler._detect_column_issues(col)
        assert any("All unique values" in i for i in issues)

    def test_no_issues_clean_column(self, profiler):
        rng = np.random.RandomState(0)
        col = pd.Series(rng.normal(0, 1, 200), name="clean")
        issues = profiler._detect_column_issues(col)
        # A clean, normally distributed column should have no issues (or minimal)
        high_severity = [i for i in issues if "High missing" in i or "Constant" in i or "High cardinality" in i]
        assert len(high_severity) == 0


# ---------------------------------------------------------------------------
# _generate_recommendations
# ---------------------------------------------------------------------------


class TestGenerateRecommendations:
    """Tests for recommendation generation."""

    def test_binary_target_recommendation(self, profiler, tabular_df):
        profile = profiler.profile_dataframe(tabular_df)
        rec_messages = [r["message"] for r in profile["recommendations"]]
        assert any("binary classification" in m.lower() for m in rec_messages)

    def test_high_missing_recommendation(self, profiler):
        rng = np.random.RandomState(0)
        df = pd.DataFrame({
            "good": rng.normal(size=200),
            "bad": [np.nan] * 80 + list(rng.normal(size=120)),
        })
        profile = profiler.profile_dataframe(df)
        rec_messages = [r["message"] for r in profile["recommendations"]]
        assert any(">30% missing" in m for m in rec_messages)

    def test_id_column_recommendation(self, profiler, tabular_df):
        profile = profiler.profile_dataframe(tabular_df)
        rec_messages = [r["message"] for r in profile["recommendations"]]
        assert any("identifier" in m.lower() for m in rec_messages)

    def test_datetime_column_recommendation(self, profiler):
        df = pd.DataFrame({
            "dt": pd.date_range("2024-01-01", periods=200, freq="D"),
            "val": range(200),
        })
        profile = profiler.profile_dataframe(df)
        rec_messages = [r["message"] for r in profile["recommendations"]]
        assert any("datetime" in m.lower() or "timeseries" in m.lower() for m in rec_messages)


# ---------------------------------------------------------------------------
# _generate_warnings
# ---------------------------------------------------------------------------


class TestGenerateWarnings:
    """Tests for warning generation."""

    def test_small_dataset_warning(self, profiler):
        df = pd.DataFrame({"a": range(50), "b": range(50)})
        profile = profiler.profile_dataframe(df)
        warn_msgs = [w["message"] for w in profile["warnings"]]
        assert any("small dataset" in m.lower() or "very small dataset" in m.lower() for m in warn_msgs)

    def test_high_duplicate_warning(self, profiler):
        df = pd.DataFrame({"a": [1, 2] * 50, "b": [3, 4] * 50})
        profile = profiler.profile_dataframe(df)
        warn_msgs = [w["message"] for w in profile["warnings"]]
        assert any("duplicate" in m.lower() for m in warn_msgs)

    def test_no_warning_for_decent_dataset(self, profiler, tabular_df):
        profile = profiler.profile_dataframe(tabular_df)
        # 200 rows should give an info-level warning at most (< 1000)
        warning_severities = [w.get("severity") for w in profile["warnings"]]
        # Should not have data_size "warning" (that's for < 100)
        data_size_warnings = [
            w for w in profile["warnings"]
            if w.get("type") == "data_size" and w.get("severity") == "warning"
        ]
        assert len(data_size_warnings) == 0


# ---------------------------------------------------------------------------
# suggest_target_column
# ---------------------------------------------------------------------------


class TestSuggestTargetColumn:
    """Tests for target column suggestion."""

    def test_target_is_top_suggestion(self, profiler, tabular_df):
        profile = profiler.profile_dataframe(tabular_df)
        suggestions = profiler.suggest_target_column(profile)
        assert len(suggestions) > 0
        # "target" column (binary, low missing) should score highest
        col_names = [s["column"] for s in suggestions]
        assert "target" in col_names
        # It should be near the top
        target_rank = col_names.index("target")
        assert target_rank < 3

    def test_identifiers_penalized(self, profiler, tabular_df):
        profile = profiler.profile_dataframe(tabular_df)
        suggestions = profiler.suggest_target_column(profile)
        id_suggestions = [s for s in suggestions if s["column"] == "id"]
        # id column should not appear (score <= 0 after -50 penalty)
        assert len(id_suggestions) == 0

    def test_problem_type_in_suggestion(self, profiler, tabular_df):
        profile = profiler.profile_dataframe(tabular_df)
        suggestions = profiler.suggest_target_column(profile)
        for s in suggestions:
            assert "problem_type" in s
            assert s["problem_type"] in ("binary", "multiclass", "regression", "unknown")

    def test_returns_max_5(self, profiler):
        """Even with many candidate columns, returns at most 5."""
        rng = np.random.RandomState(0)
        df = pd.DataFrame({f"col_{i}": rng.choice([0, 1], 200) for i in range(20)})
        profile = profiler.profile_dataframe(df)
        suggestions = profiler.suggest_target_column(profile)
        assert len(suggestions) <= 5


# ---------------------------------------------------------------------------
# Correlations
# ---------------------------------------------------------------------------


class TestCorrelations:
    """Tests for correlation detection."""

    def test_high_correlation_detected(self, profiler):
        rng = np.random.RandomState(0)
        x = rng.normal(size=200)
        df = pd.DataFrame({
            "a": x,
            "b": x + rng.normal(0, 0.05, 200),  # Nearly identical
            "c": rng.normal(size=200),
        })
        result = profiler.profile_dataframe(df)
        high_corrs = result["correlations"].get("high_correlations", [])
        assert len(high_corrs) >= 1
        pair = high_corrs[0]
        assert abs(pair["correlation"]) > 0.8

    def test_correlation_matrix_structure(self, profiler, tabular_df):
        result = profiler.profile_dataframe(tabular_df)
        corr = result.get("correlations", {})
        if corr:
            assert "matrix" in corr
            assert "high_correlations" in corr

    def test_no_correlations_single_numeric(self, profiler):
        df = pd.DataFrame({"x": [1, 2, 3], "cat": ["a", "b", "c"]})
        result = profiler.profile_dataframe(df)
        # Only one numeric column => no correlation matrix
        assert result["correlations"] == {}
