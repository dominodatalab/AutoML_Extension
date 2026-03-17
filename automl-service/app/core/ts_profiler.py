"""Time series profiling service for analyzing temporal datasets."""

import logging
import os
from functools import lru_cache
from typing import Any, Dict, List, Optional

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


class TimeSeriesProfiler:
    """Service for profiling time series datasets."""

    def __init__(self):
        pass

    def _load_timeseries_dataframe(
        self,
        file_path: str,
        time_column: str,
        target_column: str,
        id_column: Optional[str] = None,
    ) -> pd.DataFrame:
        """Load only the columns required for time-series analysis."""
        required_columns = [time_column, target_column]
        if id_column:
            required_columns.append(id_column)

        if file_path.endswith(".csv"):
            return pd.read_csv(
                file_path,
                usecols=required_columns,
                parse_dates=[time_column],
            )

        if file_path.endswith((".parquet", ".pq")):
            df = pd.read_parquet(file_path, columns=required_columns)
        elif file_path.endswith(".json"):
            df = pd.read_json(file_path)
            df = df[required_columns]
        elif file_path.endswith((".xlsx", ".xls")):
            df = pd.read_excel(file_path, usecols=required_columns, parse_dates=[time_column])
        else:
            raise ValueError(f"Unsupported file format: {file_path}")

        if not pd.api.types.is_datetime64_any_dtype(df[time_column]):
            df[time_column] = pd.to_datetime(df[time_column], errors="coerce")
        return df

    def _sample_timeseries_dataframe(
        self,
        df: pd.DataFrame,
        time_column: str,
        sample_size: int,
        strategy: str,
    ) -> tuple[pd.DataFrame, str]:
        """Apply sampling while minimizing full-frame sorting where possible."""
        if strategy == "full" or len(df) <= sample_size:
            return df.sort_values(time_column).reset_index(drop=True), strategy

        if strategy == "recent":
            sampled = df.nlargest(sample_size, time_column)
            return sampled.sort_values(time_column).reset_index(drop=True), "recent"

        if strategy == "oldest":
            sampled = df.nsmallest(sample_size, time_column)
            return sampled.sort_values(time_column).reset_index(drop=True), "oldest"

        if strategy == "uniform":
            sorted_df = df.sort_values(time_column).reset_index(drop=True)
            step = max(1, len(sorted_df) // sample_size)
            return sorted_df.iloc[::step].head(sample_size).reset_index(drop=True), "uniform"

        sampled = df.nlargest(sample_size, time_column)
        return sampled.sort_values(time_column).reset_index(drop=True), "recent"

    def profile_timeseries_file(
        self,
        file_path: str,
        time_column: str,
        target_column: str,
        id_column: Optional[str] = None,
        sample_size: int = 100000,
        sampling_strategy: str = "recent",
        rolling_window: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Generate a comprehensive time series profile."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        df = self._load_timeseries_dataframe(
            file_path=file_path,
            time_column=time_column,
            target_column=target_column,
            id_column=id_column,
        )

        # Ensure time column is datetime
        if not pd.api.types.is_datetime64_any_dtype(df[time_column]):
            df[time_column] = pd.to_datetime(df[time_column], errors="coerce")

        # Ensure target is numeric
        if not pd.api.types.is_numeric_dtype(df[target_column]):
            df[target_column] = pd.to_numeric(df[target_column], errors="coerce")

        total_rows = len(df)

        # Gap detection uses all timestamps before sampling
        all_timestamps = df[time_column].dropna()

        # Apply sampling
        df, used_strategy = self._sample_timeseries_dataframe(
            df,
            time_column,
            sample_size,
            sampling_strategy,
        )

        result: Dict[str, Any] = {}
        result["temporal_summary"] = self._temporal_summary(
            df, time_column, target_column, id_column, total_rows, used_strategy
        )
        result["gap_analysis"] = self._gap_analysis(all_timestamps)
        result["target_statistics"] = self._target_statistics(df, target_column)

        # Determine the analysis series (longest series for multi-series)
        analysis_series = self._get_analysis_series(df, time_column, target_column, id_column)

        result["stationarity"] = self._stationarity_test(analysis_series)
        result["trend_analysis"] = self._trend_analysis(analysis_series)
        result["seasonality"] = self._seasonality_decomposition(
            analysis_series, result["temporal_summary"].get("inferred_frequency")
        )
        result["autocorrelation"] = self._autocorrelation(analysis_series)
        result["rolling_statistics"] = self._rolling_statistics(analysis_series, rolling_window)
        result["per_series_summary"] = self._per_series_summary(
            df, time_column, target_column, id_column
        )
        result["recommendations"] = self._generate_recommendations(result)
        result["warnings"] = self._generate_warnings(result, total_rows, len(df))

        return result

    def _apply_sampling(
        self, df: pd.DataFrame, sample_size: int, strategy: str
    ) -> tuple:
        """Apply sampling strategy. Returns (sampled_df, strategy_used)."""
        if strategy == "full" or len(df) <= sample_size:
            return df, strategy

        if strategy == "recent":
            return df.tail(sample_size).reset_index(drop=True), "recent"
        elif strategy == "oldest":
            return df.head(sample_size).reset_index(drop=True), "oldest"
        elif strategy == "uniform":
            step = max(1, len(df) // sample_size)
            return df.iloc[::step].head(sample_size).reset_index(drop=True), "uniform"
        else:
            return df.tail(sample_size).reset_index(drop=True), "recent"

    def _get_analysis_series(
        self,
        df: pd.DataFrame,
        time_column: str,
        target_column: str,
        id_column: Optional[str],
    ) -> pd.Series:
        """Get the time series to use for statistical analysis (longest series for multi-series)."""
        if id_column and id_column in df.columns:
            counts = df.groupby(id_column).size()
            longest_id = counts.idxmax()
            subset = df[df[id_column] == longest_id].set_index(time_column)[target_column]
        else:
            subset = df.set_index(time_column)[target_column]

        return subset.dropna().sort_index()

    def _temporal_summary(
        self,
        df: pd.DataFrame,
        time_column: str,
        target_column: str,
        id_column: Optional[str],
        total_rows: int,
        sampling_strategy: str,
    ) -> Dict[str, Any]:
        """Compute temporal summary statistics."""
        times = df[time_column].dropna()
        num_series = 1
        if id_column and id_column in df.columns:
            num_series = df[id_column].nunique()

        freq = None
        try:
            inferred = pd.infer_freq(times.sort_values().unique()[:1000])
            freq = inferred
        except Exception:
            pass

        return {
            "num_series": num_series,
            "total_observations": len(df),
            "total_rows": total_rows,
            "date_range_start": str(times.min()) if len(times) > 0 else None,
            "date_range_end": str(times.max()) if len(times) > 0 else None,
            "inferred_frequency": freq,
            "sampling_strategy": sampling_strategy,
        }

    def _gap_analysis(self, timestamps: pd.Series) -> Dict[str, Any]:
        """Detect gaps in the time series."""
        if len(timestamps) < 2:
            return {"gaps": [], "total_gaps": 0, "irregular_intervals": False}

        sorted_ts = timestamps.sort_values().reset_index(drop=True)
        diffs = sorted_ts.diff().dropna()

        if len(diffs) == 0:
            return {"gaps": [], "total_gaps": 0, "irregular_intervals": False}

        median_diff = diffs.median()
        # A gap is >2x the median interval
        threshold = median_diff * 2
        gap_mask = diffs > threshold

        gaps = []
        if gap_mask.any():
            gap_indices = gap_mask[gap_mask].index
            for idx in gap_indices[:50]:  # Cap at 50 gaps
                gap_start = sorted_ts.iloc[idx - 1]
                gap_end = sorted_ts.iloc[idx]
                gap_duration = gap_end - gap_start
                missing_periods = int(gap_duration / median_diff) - 1 if median_diff.total_seconds() > 0 else 0
                gaps.append({
                    "start": str(gap_start),
                    "end": str(gap_end),
                    "duration": str(gap_duration),
                    "missing_periods": max(0, missing_periods),
                })

        # Check for irregular intervals
        if len(diffs) > 1:
            cv = diffs.std() / diffs.mean() if diffs.mean().total_seconds() > 0 else 0
            irregular = float(cv) > 0.1
        else:
            irregular = False

        return {
            "gaps": gaps,
            "total_gaps": len(gaps),
            "irregular_intervals": irregular,
        }

    def _stationarity_test(self, series: pd.Series) -> Optional[Dict[str, Any]]:
        """Run Augmented Dickey-Fuller test for stationarity."""
        if len(series) < 20:
            return None
        try:
            from statsmodels.tsa.stattools import adfuller

            result = adfuller(series.values, autolag="AIC")
            statistic, pvalue, _, nobs, critical_values, _ = result

            if pvalue < 0.01:
                interpretation = "Stationary (strong evidence)"
            elif pvalue < 0.05:
                interpretation = "Stationary (moderate evidence)"
            elif pvalue < 0.1:
                interpretation = "Weakly non-stationary"
            else:
                interpretation = "Non-stationary"

            return {
                "adf_statistic": round(float(statistic), 4),
                "p_value": round(float(pvalue), 6),
                "num_observations": int(nobs),
                "critical_values": {k: round(float(v), 4) for k, v in critical_values.items()},
                "interpretation": interpretation,
                "is_stationary": bool(pvalue < 0.05),
            }
        except Exception as e:
            logger.warning(f"ADF test failed: {e}")
            return None

    def _trend_analysis(self, series: pd.Series) -> Optional[Dict[str, Any]]:
        """Analyze trend via linear fit."""
        if len(series) < 10:
            return None
        try:
            y = series.values.astype(float)
            x = np.arange(len(y), dtype=float)
            # Remove NaN/inf
            mask = np.isfinite(y)
            x, y = x[mask], y[mask]
            if len(x) < 10:
                return None

            coeffs = np.polyfit(x, y, 1)
            slope = float(coeffs[0])

            # R-squared
            y_pred = np.polyval(coeffs, x)
            ss_res = np.sum((y - y_pred) ** 2)
            ss_tot = np.sum((y - np.mean(y)) ** 2)
            r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0

            if abs(slope) < 1e-10:
                direction = "flat"
            elif slope > 0:
                direction = "upward"
            else:
                direction = "downward"

            return {
                "direction": direction,
                "slope": round(slope, 6),
                "r_squared": round(float(r_squared), 4),
            }
        except Exception as e:
            logger.warning(f"Trend analysis failed: {e}")
            return None

    def _seasonality_decomposition(
        self, series: pd.Series, inferred_freq: Optional[str]
    ) -> Optional[Dict[str, Any]]:
        """Decompose time series into trend, seasonal, and residual components."""
        if len(series) < 30:
            return None
        try:
            from statsmodels.tsa.seasonal import seasonal_decompose

            # Determine period
            period = self._estimate_period(series, inferred_freq)
            if period is None or period < 2 or period >= len(series) // 2:
                return None

            # Try additive first, then multiplicative
            model_type = "additive"
            if series.min() > 0:
                model_type = "multiplicative"

            try:
                decomposition = seasonal_decompose(
                    series, model=model_type, period=period, extrapolate_trend="freq"
                )
            except Exception:
                model_type = "additive"
                decomposition = seasonal_decompose(
                    series, model="additive", period=period, extrapolate_trend="freq"
                )

            # Downsample for visualization (max 500 points).
            # Drop NaN first, then downsample, so timestamps and values stay aligned.
            trend_clean = decomposition.trend.dropna()
            seasonal_clean = decomposition.seasonal.dropna()
            residual_clean = decomposition.resid.dropna()
            step = max(1, len(trend_clean) // 500)
            trend_vals = trend_clean.iloc[::step]
            seasonal_vals = seasonal_clean.iloc[::step]
            residual_vals = residual_clean.iloc[::step]

            # Seasonal strength
            var_resid = np.var(decomposition.resid.dropna())
            var_seasonal = np.var(decomposition.seasonal.dropna())
            seasonal_strength = 0.0
            if (var_seasonal + var_resid) > 0:
                seasonal_strength = float(var_seasonal / (var_seasonal + var_resid))

            return {
                "model": model_type,
                "period": period,
                "seasonal_strength": round(seasonal_strength, 4),
                "trend": {
                    "timestamps": [str(t) for t in trend_vals.index],
                    "values": [round(float(v), 4) if np.isfinite(v) else None for v in trend_vals.values],
                },
                "seasonal": {
                    "timestamps": [str(t) for t in seasonal_vals.index],
                    "values": [round(float(v), 4) if np.isfinite(v) else None for v in seasonal_vals.values],
                },
                "residual": {
                    "timestamps": [str(t) for t in residual_vals.index],
                    "values": [round(float(v), 4) if np.isfinite(v) else None for v in residual_vals.values],
                },
            }
        except Exception as e:
            logger.warning(f"Seasonal decomposition failed: {e}")
            return None

    def _estimate_period(self, series: pd.Series, inferred_freq: Optional[str]) -> Optional[int]:
        """Estimate the seasonal period from frequency string or data."""
        freq_to_period = {
            "H": 24,
            "h": 24,
            "T": 60,
            "min": 60,
            "D": 7,
            "B": 5,
            "W": 52,
            "M": 12,
            "MS": 12,
            "Q": 4,
            "QS": 4,
            "Y": 1,
            "YS": 1,
            "A": 1,
            "AS": 1,
        }
        if inferred_freq:
            # Strip numeric prefix (e.g., "2H" -> "H")
            base_freq = "".join(c for c in inferred_freq if c.isalpha())
            if base_freq in freq_to_period:
                return freq_to_period[base_freq]

        # Fallback: try to detect from autocorrelation
        if len(series) > 50:
            try:
                from statsmodels.tsa.stattools import acf

                nlags = min(len(series) // 2 - 1, 200)
                acf_vals = acf(series.values, nlags=nlags, fft=True)
                # Find first significant peak after lag 1
                for i in range(2, len(acf_vals)):
                    is_peak = (
                        acf_vals[i] > acf_vals[i - 1]
                        and (acf_vals[i] > acf_vals[i + 1] if i + 1 < len(acf_vals) else True)
                    )
                    if is_peak and acf_vals[i] > 0.1:
                        return i
            except Exception:
                pass

        # Last resort: 7 (weekly) if enough data
        if len(series) > 14:
            return 7
        return None

    def _autocorrelation(self, series: pd.Series) -> Optional[Dict[str, Any]]:
        """Compute ACF and PACF values."""
        if len(series) < 20:
            return None
        try:
            from statsmodels.tsa.stattools import acf, pacf

            nlags = min(40, len(series) // 2 - 1)
            if nlags < 1:
                return None

            acf_values, acf_ci = acf(series.values, nlags=nlags, alpha=0.05, fft=True)
            pacf_values, pacf_ci = pacf(series.values, nlags=nlags, alpha=0.05)

            # statsmodels returns confidence intervals around the ACF estimate.
            # A lag is significant when that interval excludes zero.
            significant_lags = []
            for i in range(1, len(acf_values)):
                lower, upper = acf_ci[i]
                if lower > 0 or upper < 0:
                    significant_lags.append(i)

            # Report the approximate CI width for frontend visualization
            ci = 1.96 / np.sqrt(len(series))

            return {
                "acf": [round(float(v), 4) for v in acf_values],
                "pacf": [round(float(v), 4) for v in pacf_values],
                "confidence_interval": round(float(ci), 4),
                "significant_lags": significant_lags[:20],
                "nlags": nlags,
            }
        except Exception as e:
            logger.warning(f"ACF/PACF computation failed: {e}")
            return None

    def _target_statistics(self, df: pd.DataFrame, target_column: str) -> Dict[str, Any]:
        """Compute basic statistics for the target column.

        Always returns all expected fields so the frontend TargetStatistics
        interface is satisfied even when data is empty.
        """
        col = df[target_column].dropna()
        if len(col) == 0:
            return {
                "mean": 0, "std": 0, "cv": 0,
                "min": 0, "max": 0, "skewness": 0, "kurtosis": 0,
            }

        mean = float(col.mean())
        std = float(col.std()) if len(col) > 1 else 0.0
        cv = abs(std / mean) if abs(mean) > 1e-10 else 0.0

        return {
            "mean": round(mean, 4),
            "std": round(std, 4),
            "cv": round(cv, 4),
            "min": round(float(col.min()), 4),
            "max": round(float(col.max()), 4),
            "skewness": round(float(col.skew()), 4) if len(col) > 2 else 0,
            "kurtosis": round(float(col.kurtosis()), 4) if len(col) > 3 else 0,
        }

    def _rolling_statistics(self, series: pd.Series, rolling_window: Optional[int] = None) -> Optional[Dict[str, Any]]:
        """Compute rolling mean and std for visualization."""
        if len(series) < 10:
            return None

        window = rolling_window if rolling_window else max(2, len(series) // 20)
        rolling_mean = series.rolling(window=window, center=True).mean().dropna()
        rolling_std = series.rolling(window=window, center=True).std().dropna()

        # Downsample to ~500 points
        step = max(1, len(rolling_mean) // 500)
        rm = rolling_mean.iloc[::step]
        rs = rolling_std.iloc[::step]

        return {
            "window_size": window,
            "timestamps": [str(t) for t in rm.index],
            "rolling_mean": [round(float(v), 4) if np.isfinite(v) else None for v in rm.values],
            "rolling_std": [round(float(v), 4) if np.isfinite(v) else None for v in rs.values],
        }

    def _per_series_summary(
        self,
        df: pd.DataFrame,
        time_column: str,
        target_column: str,
        id_column: Optional[str],
    ) -> Optional[List[Dict[str, Any]]]:
        """Compute per-series summary for multi-series data."""
        if not id_column or id_column not in df.columns:
            return None

        grouped = df.groupby(id_column)
        summaries = []

        for name, group in grouped:
            target = group[target_column].dropna()
            times = group[time_column].dropna()
            missing_rate = group[target_column].isna().sum() / len(group) if len(group) > 0 else 0

            summaries.append({
                "id": str(name),
                "count": len(group),
                "date_range_start": str(times.min()) if len(times) > 0 else None,
                "date_range_end": str(times.max()) if len(times) > 0 else None,
                "missing_rate": round(float(missing_rate), 4),
                "mean": round(float(target.mean()), 4) if len(target) > 0 else None,
                "std": round(float(target.std()), 4) if len(target) > 1 else None,
            })

        # Sort by count descending, cap at 100
        summaries.sort(key=lambda x: x["count"], reverse=True)
        return summaries[:100]

    def _generate_recommendations(self, result: Dict[str, Any]) -> List[Dict[str, str]]:
        """Generate time series-specific recommendations."""
        recs = []

        stationarity = result.get("stationarity")
        if stationarity and not stationarity.get("is_stationary"):
            recs.append({
                "type": "preprocessing",
                "message": "Series is non-stationary — consider differencing or log transform before modeling",
                "priority": "high",
            })

        seasonality = result.get("seasonality")
        if seasonality:
            period = seasonality.get("period")
            strength = seasonality.get("seasonal_strength", 0)
            if strength > 0.3 and period:
                recs.append({
                    "type": "model",
                    "message": f"Seasonality detected (period={period}, strength={strength:.2f}) — models with seasonal components recommended",
                    "priority": "medium",
                })

        gap_analysis = result.get("gap_analysis", {})
        if gap_analysis.get("total_gaps", 0) > 0:
            recs.append({
                "type": "preprocessing",
                "message": f"{gap_analysis['total_gaps']} gaps detected — consider imputation or gap-aware models",
                "priority": "medium",
            })

        trend = result.get("trend_analysis")
        if trend and trend.get("direction") != "flat" and trend.get("r_squared", 0) > 0.5:
            recs.append({
                "type": "model",
                "message": f"Strong {trend['direction']} trend detected (R²={trend['r_squared']:.2f})",
                "priority": "info",
            })

        autocorrelation = result.get("autocorrelation")
        if autocorrelation and autocorrelation.get("significant_lags"):
            sig_lags = autocorrelation["significant_lags"][:5]
            recs.append({
                "type": "model",
                "message": f"Significant autocorrelation at lags: {sig_lags}",
                "priority": "info",
            })

        return recs

    def _generate_warnings(
        self, result: Dict[str, Any], total_rows: int, sampled_rows: int
    ) -> List[Dict[str, str]]:
        """Generate time series-specific warnings."""
        warnings = []

        summary = result.get("temporal_summary", {})
        if summary.get("total_observations", 0) < 50:
            warnings.append({
                "type": "data_size",
                "message": "Very short time series (<50 observations) — model performance may be limited",
                "severity": "warning",
            })

        gap_analysis = result.get("gap_analysis", {})
        if gap_analysis.get("total_gaps", 0) > 10:
            warnings.append({
                "type": "data_quality",
                "message": f"Many gaps detected ({gap_analysis['total_gaps']}) — check data completeness",
                "severity": "warning",
            })

        if gap_analysis.get("irregular_intervals"):
            warnings.append({
                "type": "data_quality",
                "message": "Irregular time intervals detected — ensure consistent frequency",
                "severity": "info",
            })

        per_series = result.get("per_series_summary")
        if per_series:
            short_series = [s for s in per_series if s["count"] < 20]
            if len(short_series) > len(per_series) * 0.3:
                warnings.append({
                    "type": "data_quality",
                    "message": f"{len(short_series)} of {len(per_series)} series have <20 observations",
                    "severity": "warning",
                })

        if total_rows > sampled_rows:
            warnings.append({
                "type": "sampling",
                "message": f"Analysis based on {sampled_rows:,} of {total_rows:,} total rows",
                "severity": "info",
            })

        target_stats = result.get("target_statistics", {})
        if target_stats.get("std", 1) == 0 or target_stats.get("cv", 1) == 0:
            warnings.append({
                "type": "data_quality",
                "message": "Target column has zero variance — check if data is constant",
                "severity": "error",
            })

        return warnings


@lru_cache()
def get_ts_profiler() -> TimeSeriesProfiler:
    """Get the time series profiler singleton (cached)."""
    return TimeSeriesProfiler()
