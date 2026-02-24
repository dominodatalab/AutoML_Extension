"""Tests for app.core.ts_profiler.TimeSeriesProfiler."""

import numpy as np
import pandas as pd
import pytest

from app.core.ts_profiler import TimeSeriesProfiler


@pytest.fixture
def profiler():
    return TimeSeriesProfiler()


# ---------------------------------------------------------------------------
# profile_timeseries_file
# ---------------------------------------------------------------------------


class TestProfileTimeseriesFile:
    """Tests for loading and profiling time series files."""

    def test_multi_series_csv(self, profiler, timeseries_csv):
        result = profiler.profile_timeseries_file(
            timeseries_csv,
            time_column="timestamp",
            target_column="value",
            id_column="item_id",
        )
        assert "temporal_summary" in result
        assert "gap_analysis" in result
        assert "target_statistics" in result
        assert "stationarity" in result
        assert "autocorrelation" in result
        assert "recommendations" in result
        assert "warnings" in result

    def test_single_series_csv(self, profiler, timeseries_single_csv):
        result = profiler.profile_timeseries_file(
            timeseries_single_csv,
            time_column="date",
            target_column="temperature",
        )
        assert result["temporal_summary"]["num_series"] == 1
        assert result["per_series_summary"] is None

    def test_file_not_found(self, profiler):
        with pytest.raises(FileNotFoundError, match="File not found"):
            profiler.profile_timeseries_file(
                "/nonexistent/data.csv",
                time_column="ts",
                target_column="val",
            )

    def test_unsupported_format(self, profiler, tmp_path):
        path = str(tmp_path / "bad.xyz")
        with open(path, "w") as f:
            f.write("dummy")
        with pytest.raises(ValueError, match="Unsupported file format"):
            profiler.profile_timeseries_file(path, time_column="ts", target_column="val")


# ---------------------------------------------------------------------------
# Temporal summary
# ---------------------------------------------------------------------------


class TestTemporalSummary:
    """Tests for the temporal_summary section."""

    def test_date_range(self, profiler, timeseries_csv):
        result = profiler.profile_timeseries_file(
            timeseries_csv,
            time_column="timestamp",
            target_column="value",
            id_column="item_id",
        )
        ts = result["temporal_summary"]
        assert ts["date_range_start"] is not None
        assert ts["date_range_end"] is not None
        # 2023-01-01 to 2023-06-29 (180 days)
        assert "2023-01-01" in ts["date_range_start"]
        assert "2023-06-29" in ts["date_range_end"]

    def test_num_series_multi(self, profiler, timeseries_csv):
        result = profiler.profile_timeseries_file(
            timeseries_csv,
            time_column="timestamp",
            target_column="value",
            id_column="item_id",
        )
        assert result["temporal_summary"]["num_series"] == 2

    def test_num_series_single(self, profiler, timeseries_single_csv):
        result = profiler.profile_timeseries_file(
            timeseries_single_csv,
            time_column="date",
            target_column="temperature",
        )
        assert result["temporal_summary"]["num_series"] == 1

    def test_inferred_frequency(self, profiler, timeseries_single_csv):
        result = profiler.profile_timeseries_file(
            timeseries_single_csv,
            time_column="date",
            target_column="temperature",
        )
        # Daily data should infer frequency "D"
        freq = result["temporal_summary"]["inferred_frequency"]
        assert freq is not None
        assert "D" in freq


# ---------------------------------------------------------------------------
# Gap analysis
# ---------------------------------------------------------------------------


class TestGapAnalysis:
    """Tests for gap detection."""

    def test_regular_data_no_gaps(self, profiler, timeseries_single_csv):
        result = profiler.profile_timeseries_file(
            timeseries_single_csv,
            time_column="date",
            target_column="temperature",
        )
        gaps = result["gap_analysis"]
        assert gaps["total_gaps"] == 0
        assert gaps["gaps"] == []

    def test_gapped_data_detected(self, profiler, tmp_path):
        """Create data with intentional 10-day gap and verify detection."""
        dates_before = pd.date_range("2024-01-01", periods=50, freq="D")
        dates_after = pd.date_range("2024-03-01", periods=50, freq="D")
        dates = dates_before.append(dates_after)
        rng = np.random.RandomState(0)
        df = pd.DataFrame({
            "ts": dates,
            "val": rng.normal(100, 10, len(dates)),
        })
        path = str(tmp_path / "gapped.csv")
        df.to_csv(path, index=False)

        result = profiler.profile_timeseries_file(
            path, time_column="ts", target_column="val"
        )
        gaps = result["gap_analysis"]
        assert gaps["total_gaps"] >= 1
        assert len(gaps["gaps"]) >= 1
        # The gap should have start and end timestamps
        gap = gaps["gaps"][0]
        assert "start" in gap
        assert "end" in gap
        assert "duration" in gap
        assert "missing_periods" in gap

    def test_irregular_intervals_flagged(self, profiler, tmp_path):
        """Irregular timestamps should set irregular_intervals to True."""
        rng = np.random.RandomState(42)
        # Create timestamps with random intervals
        base = pd.Timestamp("2024-01-01")
        deltas = rng.exponential(scale=2, size=100)
        timestamps = [base + pd.Timedelta(days=float(sum(deltas[:i+1]))) for i in range(100)]
        df = pd.DataFrame({
            "ts": timestamps,
            "val": rng.normal(0, 1, 100),
        })
        path = str(tmp_path / "irregular.csv")
        df.to_csv(path, index=False)

        result = profiler.profile_timeseries_file(
            path, time_column="ts", target_column="val"
        )
        assert result["gap_analysis"]["irregular_intervals"] is True


# ---------------------------------------------------------------------------
# Target statistics
# ---------------------------------------------------------------------------


class TestTargetStatistics:
    """Tests for target column statistics."""

    def test_stats_keys(self, profiler, timeseries_single_csv):
        result = profiler.profile_timeseries_file(
            timeseries_single_csv,
            time_column="date",
            target_column="temperature",
        )
        stats = result["target_statistics"]
        for key in ("mean", "std", "min", "max", "skewness", "kurtosis", "cv"):
            assert key in stats, f"Missing target stat: {key}"

    def test_stats_values_reasonable(self, profiler, timeseries_single_csv):
        result = profiler.profile_timeseries_file(
            timeseries_single_csv,
            time_column="date",
            target_column="temperature",
        )
        stats = result["target_statistics"]
        # Temperature data trends from ~50 to ~80
        assert 50 < stats["mean"] < 80
        assert stats["std"] > 0
        assert stats["min"] < stats["max"]


# ---------------------------------------------------------------------------
# Stationarity test
# ---------------------------------------------------------------------------


class TestStationarityTest:
    """Tests for the ADF stationarity test."""

    def test_stationary_series(self, profiler, tmp_path):
        """White noise should be stationary."""
        rng = np.random.RandomState(42)
        dates = pd.date_range("2024-01-01", periods=200, freq="D")
        df = pd.DataFrame({
            "ts": dates,
            "val": rng.normal(0, 1, 200),
        })
        path = str(tmp_path / "stationary.csv")
        df.to_csv(path, index=False)

        result = profiler.profile_timeseries_file(
            path, time_column="ts", target_column="val"
        )
        assert result["stationarity"] is not None
        assert result["stationarity"]["is_stationary"] is True
        assert result["stationarity"]["p_value"] < 0.05
        assert "Stationary" in result["stationarity"]["interpretation"]

    def test_non_stationary_series(self, profiler, tmp_path):
        """Random walk should be non-stationary."""
        rng = np.random.RandomState(42)
        n = 200
        dates = pd.date_range("2024-01-01", periods=n, freq="D")
        walk = np.cumsum(rng.normal(0, 1, n))
        df = pd.DataFrame({"ts": dates, "val": walk})
        path = str(tmp_path / "nonstationary.csv")
        df.to_csv(path, index=False)

        result = profiler.profile_timeseries_file(
            path, time_column="ts", target_column="val"
        )
        assert result["stationarity"] is not None
        assert result["stationarity"]["is_stationary"] is False

    def test_stationarity_keys(self, profiler, timeseries_single_csv):
        result = profiler.profile_timeseries_file(
            timeseries_single_csv,
            time_column="date",
            target_column="temperature",
        )
        stationarity = result["stationarity"]
        assert stationarity is not None
        for key in ("adf_statistic", "p_value", "num_observations", "critical_values",
                     "interpretation", "is_stationary"):
            assert key in stationarity, f"Missing stationarity key: {key}"


# ---------------------------------------------------------------------------
# Trend analysis
# ---------------------------------------------------------------------------


class TestTrendAnalysis:
    """Tests for trend direction detection."""

    def test_upward_trend(self, profiler, timeseries_single_csv):
        """The single-series fixture has a linear upward trend (50 -> 80)."""
        result = profiler.profile_timeseries_file(
            timeseries_single_csv,
            time_column="date",
            target_column="temperature",
        )
        trend = result["trend_analysis"]
        assert trend is not None
        assert trend["direction"] == "upward"
        assert trend["slope"] > 0
        assert "r_squared" in trend

    def test_downward_trend(self, profiler, tmp_path):
        rng = np.random.RandomState(42)
        n = 200
        dates = pd.date_range("2024-01-01", periods=n, freq="D")
        values = np.linspace(100, 10, n) + rng.normal(0, 1, n)
        df = pd.DataFrame({"ts": dates, "val": values.round(2)})
        path = str(tmp_path / "downtrend.csv")
        df.to_csv(path, index=False)

        result = profiler.profile_timeseries_file(
            path, time_column="ts", target_column="val"
        )
        assert result["trend_analysis"]["direction"] == "downward"
        assert result["trend_analysis"]["slope"] < 0

    def test_flat_trend(self, profiler, tmp_path):
        rng = np.random.RandomState(42)
        n = 200
        dates = pd.date_range("2024-01-01", periods=n, freq="D")
        values = np.full(n, 50.0)  # Constant values = flat
        df = pd.DataFrame({"ts": dates, "val": values})
        path = str(tmp_path / "flat.csv")
        df.to_csv(path, index=False)

        result = profiler.profile_timeseries_file(
            path, time_column="ts", target_column="val"
        )
        assert result["trend_analysis"]["direction"] == "flat"


# ---------------------------------------------------------------------------
# Seasonality decomposition
# ---------------------------------------------------------------------------


class TestSeasonalityDecomposition:
    """Tests for seasonal decomposition."""

    def test_seasonal_strength(self, profiler, timeseries_csv):
        """The multi-series fixture has sin-wave seasonality built in."""
        result = profiler.profile_timeseries_file(
            timeseries_csv,
            time_column="timestamp",
            target_column="value",
            id_column="item_id",
        )
        seasonality = result.get("seasonality")
        # Seasonality might be None if period detection fails, but for our data
        # with 180 points and clear sine wave it should work
        if seasonality is not None:
            assert "seasonal_strength" in seasonality
            assert "period" in seasonality
            assert "model" in seasonality
            assert seasonality["seasonal_strength"] >= 0

    def test_no_seasonality_short_series(self, profiler, tmp_path):
        """Very short series should return None for seasonality."""
        dates = pd.date_range("2024-01-01", periods=15, freq="D")
        df = pd.DataFrame({"ts": dates, "val": range(15)})
        path = str(tmp_path / "short.csv")
        df.to_csv(path, index=False)

        result = profiler.profile_timeseries_file(
            path, time_column="ts", target_column="val"
        )
        # Series < 30 points returns None
        assert result["seasonality"] is None


# ---------------------------------------------------------------------------
# Autocorrelation
# ---------------------------------------------------------------------------


class TestAutocorrelation:
    """Tests for ACF / PACF computation."""

    def test_acf_pacf_values(self, profiler, timeseries_single_csv):
        result = profiler.profile_timeseries_file(
            timeseries_single_csv,
            time_column="date",
            target_column="temperature",
        )
        ac = result["autocorrelation"]
        assert ac is not None
        assert "acf" in ac
        assert "pacf" in ac
        assert len(ac["acf"]) > 1
        assert len(ac["pacf"]) > 1
        # ACF at lag 0 should be 1.0
        assert abs(ac["acf"][0] - 1.0) < 0.01

    def test_confidence_interval(self, profiler, timeseries_single_csv):
        result = profiler.profile_timeseries_file(
            timeseries_single_csv,
            time_column="date",
            target_column="temperature",
        )
        ac = result["autocorrelation"]
        assert "confidence_interval" in ac
        assert ac["confidence_interval"] > 0

    def test_significant_lags(self, profiler, timeseries_single_csv):
        result = profiler.profile_timeseries_file(
            timeseries_single_csv,
            time_column="date",
            target_column="temperature",
        )
        ac = result["autocorrelation"]
        assert "significant_lags" in ac
        # The trending series should have significant autocorrelation
        assert len(ac["significant_lags"]) > 0

    def test_nlags(self, profiler, timeseries_single_csv):
        result = profiler.profile_timeseries_file(
            timeseries_single_csv,
            time_column="date",
            target_column="temperature",
        )
        ac = result["autocorrelation"]
        assert "nlags" in ac
        assert ac["nlags"] <= 40

    def test_no_autocorrelation_short_series(self, profiler, tmp_path):
        """Fewer than 20 points returns None."""
        dates = pd.date_range("2024-01-01", periods=10, freq="D")
        df = pd.DataFrame({"ts": dates, "val": range(10)})
        path = str(tmp_path / "tiny.csv")
        df.to_csv(path, index=False)

        result = profiler.profile_timeseries_file(
            path, time_column="ts", target_column="val"
        )
        assert result["autocorrelation"] is None


# ---------------------------------------------------------------------------
# Rolling statistics
# ---------------------------------------------------------------------------


class TestRollingStatistics:
    """Tests for rolling mean and std computation."""

    def test_rolling_stats_computed(self, profiler, timeseries_single_csv):
        result = profiler.profile_timeseries_file(
            timeseries_single_csv,
            time_column="date",
            target_column="temperature",
        )
        rs = result["rolling_statistics"]
        assert rs is not None
        assert "window_size" in rs
        assert "rolling_mean" in rs
        assert "rolling_std" in rs
        assert len(rs["rolling_mean"]) > 0
        assert len(rs["rolling_std"]) > 0

    def test_custom_rolling_window(self, profiler, timeseries_single_csv):
        result = profiler.profile_timeseries_file(
            timeseries_single_csv,
            time_column="date",
            target_column="temperature",
            rolling_window=14,
        )
        rs = result["rolling_statistics"]
        assert rs["window_size"] == 14

    def test_no_rolling_short_series(self, profiler, tmp_path):
        dates = pd.date_range("2024-01-01", periods=5, freq="D")
        df = pd.DataFrame({"ts": dates, "val": range(5)})
        path = str(tmp_path / "very_short.csv")
        df.to_csv(path, index=False)

        result = profiler.profile_timeseries_file(
            path, time_column="ts", target_column="val"
        )
        assert result["rolling_statistics"] is None


# ---------------------------------------------------------------------------
# Per-series summary
# ---------------------------------------------------------------------------


class TestPerSeriesSummary:
    """Tests for multi-series per-series summary."""

    def test_per_series_multi(self, profiler, timeseries_csv):
        result = profiler.profile_timeseries_file(
            timeseries_csv,
            time_column="timestamp",
            target_column="value",
            id_column="item_id",
        )
        pss = result["per_series_summary"]
        assert pss is not None
        assert len(pss) == 2
        ids = {s["id"] for s in pss}
        assert ids == {"item_A", "item_B"}
        for s in pss:
            assert "count" in s
            assert "date_range_start" in s
            assert "date_range_end" in s
            assert "mean" in s
            assert "std" in s
            assert "missing_rate" in s
            assert s["count"] == 180

    def test_per_series_single_is_none(self, profiler, timeseries_single_csv):
        result = profiler.profile_timeseries_file(
            timeseries_single_csv,
            time_column="date",
            target_column="temperature",
        )
        assert result["per_series_summary"] is None


# ---------------------------------------------------------------------------
# Sampling strategies
# ---------------------------------------------------------------------------


class TestTSSamplingStrategies:
    """Tests for time series sampling strategies."""

    @pytest.fixture
    def large_ts_csv(self, tmp_path):
        """Create a large single-series CSV to trigger sampling."""
        rng = np.random.RandomState(42)
        n = 500
        dates = pd.date_range("2020-01-01", periods=n, freq="D")
        df = pd.DataFrame({
            "ts": dates,
            "val": rng.normal(100, 10, n).round(2),
        })
        path = str(tmp_path / "large_ts.csv")
        df.to_csv(path, index=False)
        return path

    def test_recent_sampling(self, profiler, large_ts_csv):
        result = profiler.profile_timeseries_file(
            large_ts_csv,
            time_column="ts",
            target_column="val",
            sample_size=100,
            sampling_strategy="recent",
        )
        ts = result["temporal_summary"]
        assert ts["sampling_strategy"] == "recent"
        assert ts["total_observations"] == 100
        assert ts["total_rows"] == 500

    def test_oldest_sampling(self, profiler, large_ts_csv):
        result = profiler.profile_timeseries_file(
            large_ts_csv,
            time_column="ts",
            target_column="val",
            sample_size=100,
            sampling_strategy="oldest",
        )
        ts = result["temporal_summary"]
        assert ts["sampling_strategy"] == "oldest"
        assert ts["total_observations"] == 100

    def test_uniform_sampling(self, profiler, large_ts_csv):
        result = profiler.profile_timeseries_file(
            large_ts_csv,
            time_column="ts",
            target_column="val",
            sample_size=100,
            sampling_strategy="uniform",
        )
        ts = result["temporal_summary"]
        assert ts["sampling_strategy"] == "uniform"
        assert ts["total_observations"] <= 100

    def test_full_sampling(self, profiler, large_ts_csv):
        result = profiler.profile_timeseries_file(
            large_ts_csv,
            time_column="ts",
            target_column="val",
            sample_size=100,
            sampling_strategy="full",
        )
        ts = result["temporal_summary"]
        assert ts["sampling_strategy"] == "full"
        assert ts["total_observations"] == 500


# ---------------------------------------------------------------------------
# Recommendations
# ---------------------------------------------------------------------------


class TestTSRecommendations:
    """Tests for time series recommendations."""

    def test_non_stationary_recommendation(self, profiler, tmp_path):
        """Random walk => non-stationary => recommendation to difference."""
        rng = np.random.RandomState(42)
        n = 200
        dates = pd.date_range("2024-01-01", periods=n, freq="D")
        walk = np.cumsum(rng.normal(0, 1, n))
        df = pd.DataFrame({"ts": dates, "val": walk})
        path = str(tmp_path / "rw.csv")
        df.to_csv(path, index=False)

        result = profiler.profile_timeseries_file(
            path, time_column="ts", target_column="val"
        )
        rec_msgs = [r["message"] for r in result["recommendations"]]
        assert any("non-stationary" in m.lower() or "differencing" in m.lower() for m in rec_msgs)

    def test_gaps_recommendation(self, profiler, tmp_path):
        dates_before = pd.date_range("2024-01-01", periods=50, freq="D")
        dates_after = pd.date_range("2024-04-01", periods=50, freq="D")
        dates = dates_before.append(dates_after)
        rng = np.random.RandomState(0)
        df = pd.DataFrame({
            "ts": dates,
            "val": rng.normal(100, 10, len(dates)),
        })
        path = str(tmp_path / "gapped_rec.csv")
        df.to_csv(path, index=False)

        result = profiler.profile_timeseries_file(
            path, time_column="ts", target_column="val"
        )
        rec_msgs = [r["message"] for r in result["recommendations"]]
        assert any("gap" in m.lower() for m in rec_msgs)

    def test_autocorrelation_recommendation(self, profiler, timeseries_single_csv):
        """A trending series should have significant autocorrelation => recommendation."""
        result = profiler.profile_timeseries_file(
            timeseries_single_csv,
            time_column="date",
            target_column="temperature",
        )
        rec_msgs = [r["message"] for r in result["recommendations"]]
        assert any("autocorrelation" in m.lower() for m in rec_msgs)


# ---------------------------------------------------------------------------
# Warnings
# ---------------------------------------------------------------------------


class TestTSWarnings:
    """Tests for time series warnings."""

    def test_short_series_warning(self, profiler, tmp_path):
        """Fewer than 50 observations should trigger a short-series warning."""
        dates = pd.date_range("2024-01-01", periods=30, freq="D")
        rng = np.random.RandomState(0)
        df = pd.DataFrame({"ts": dates, "val": rng.normal(0, 1, 30)})
        path = str(tmp_path / "short_warn.csv")
        df.to_csv(path, index=False)

        result = profiler.profile_timeseries_file(
            path, time_column="ts", target_column="val"
        )
        warn_msgs = [w["message"] for w in result["warnings"]]
        assert any("short" in m.lower() or "<50" in m for m in warn_msgs)

    def test_many_gaps_warning(self, profiler, tmp_path):
        """Many gaps (>10) should produce a warning."""
        rng = np.random.RandomState(42)
        # Create data with many gaps by dropping random chunks
        dates = pd.date_range("2024-01-01", periods=400, freq="D")
        vals = rng.normal(100, 5, 400)
        df = pd.DataFrame({"ts": dates, "val": vals})
        # Remove blocks to create >10 gaps
        keep_mask = np.ones(400, dtype=bool)
        for start in range(20, 380, 30):
            keep_mask[start:start + 5] = False
        df = df[keep_mask].reset_index(drop=True)
        path = str(tmp_path / "many_gaps.csv")
        df.to_csv(path, index=False)

        result = profiler.profile_timeseries_file(
            path, time_column="ts", target_column="val"
        )
        warn_msgs = [w["message"] for w in result["warnings"]]
        assert any("gap" in m.lower() for m in warn_msgs)

    def test_irregular_intervals_warning(self, profiler, tmp_path):
        """Irregular intervals should produce an info-level warning."""
        rng = np.random.RandomState(42)
        base = pd.Timestamp("2024-01-01")
        deltas = rng.exponential(scale=2, size=100)
        timestamps = [base + pd.Timedelta(days=float(sum(deltas[:i+1]))) for i in range(100)]
        df = pd.DataFrame({"ts": timestamps, "val": rng.normal(0, 1, 100)})
        path = str(tmp_path / "irreg_warn.csv")
        df.to_csv(path, index=False)

        result = profiler.profile_timeseries_file(
            path, time_column="ts", target_column="val"
        )
        warn_msgs = [w["message"] for w in result["warnings"]]
        assert any("irregular" in m.lower() for m in warn_msgs)

    def test_sampling_warning(self, profiler, tmp_path):
        """Sampled data should produce a sampling info warning."""
        rng = np.random.RandomState(42)
        n = 500
        dates = pd.date_range("2020-01-01", periods=n, freq="D")
        df = pd.DataFrame({"ts": dates, "val": rng.normal(100, 10, n).round(2)})
        path = str(tmp_path / "large_for_warn.csv")
        df.to_csv(path, index=False)

        result = profiler.profile_timeseries_file(
            path, time_column="ts", target_column="val", sample_size=100
        )
        warn_msgs = [w["message"] for w in result["warnings"]]
        assert any("100" in m and "500" in m for m in warn_msgs)

    def test_zero_variance_warning(self, profiler, tmp_path):
        """Constant target should produce a zero-variance error warning."""
        dates = pd.date_range("2024-01-01", periods=100, freq="D")
        df = pd.DataFrame({"ts": dates, "val": [42.0] * 100})
        path = str(tmp_path / "constant_target.csv")
        df.to_csv(path, index=False)

        result = profiler.profile_timeseries_file(
            path, time_column="ts", target_column="val"
        )
        warn_msgs = [w["message"] for w in result["warnings"]]
        assert any("zero variance" in m.lower() or "constant" in m.lower() for m in warn_msgs)
