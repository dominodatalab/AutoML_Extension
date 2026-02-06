"""Data profiling service for analyzing datasets before training."""

import os
import logging
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple
from pathlib import Path
from datetime import datetime

import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)


class DataProfiler:
    """Service for profiling and analyzing datasets."""

    def __init__(self):
        pass

    def profile_file(
        self,
        file_path: str,
        sample_size: int = 50000,
        sampling_strategy: str = "random",
        stratify_column: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generate a comprehensive profile of a data file."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Load data
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith((".parquet", ".pq")):
            df = pd.read_parquet(file_path)
        elif file_path.endswith(".json"):
            df = pd.read_json(file_path)
        elif file_path.endswith((".xlsx", ".xls")):
            df = pd.read_excel(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_path}")

        return self.profile_dataframe(df, sample_size, sampling_strategy, stratify_column)

    def profile_dataframe(
        self,
        df: pd.DataFrame,
        sample_size: int = 50000,
        sampling_strategy: str = "random",
        stratify_column: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generate a comprehensive profile of a DataFrame."""
        total_rows = len(df)
        total_cols = len(df.columns)

        # Sample for large datasets
        if sampling_strategy == "full" or total_rows <= sample_size:
            sample_df = df
            sampled = total_rows > sample_size  # True for "full" on large data
        elif sampling_strategy == "head":
            sample_df = df.head(sample_size)
            sampled = True
        elif sampling_strategy == "stratified" and stratify_column and stratify_column in df.columns:
            try:
                frac = sample_size / total_rows
                sample_df = df.groupby(stratify_column, group_keys=False).apply(
                    lambda x: x.sample(frac=frac, random_state=42) if len(x) > 1 else x
                )
                if len(sample_df) > sample_size:
                    sample_df = sample_df.head(sample_size)
                sampled = True
            except Exception:
                sample_df = df.sample(n=sample_size, random_state=42)
                sampled = True
        else:
            # Default: random sampling
            sample_df = df.sample(n=sample_size, random_state=42)
            sampled = True

        # Basic statistics
        profile = {
            "summary": {
                "total_rows": total_rows,
                "total_columns": total_cols,
                "sampled": sampled,
                "sample_size": len(sample_df),
                "sampling_strategy": sampling_strategy,
                "memory_usage_mb": df.memory_usage(deep=True).sum() / (1024 * 1024),
                "duplicate_rows": int(df.duplicated().sum()),
                "duplicate_percentage": round(df.duplicated().sum() / total_rows * 100, 2) if total_rows > 0 else 0,
            },
            "columns": [],
            "correlations": {},
            "recommendations": [],
            "warnings": [],
        }

        # Analyze each column
        for col in df.columns:
            col_profile = self._profile_column(df[col], sample_df[col])
            profile["columns"].append(col_profile)

        # Compute correlations for numeric columns
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if len(numeric_cols) >= 2:
            try:
                corr_matrix = df[numeric_cols].corr()
                # Find highly correlated pairs
                high_corr = []
                for i, col1 in enumerate(numeric_cols):
                    for col2 in numeric_cols[i+1:]:
                        corr_val = corr_matrix.loc[col1, col2]
                        if abs(corr_val) > 0.8:
                            high_corr.append({
                                "column1": col1,
                                "column2": col2,
                                "correlation": round(corr_val, 4)
                            })
                profile["correlations"] = {
                    "matrix": corr_matrix.round(4).to_dict(),
                    "high_correlations": high_corr
                }
            except Exception as e:
                logger.warning(f"Could not compute correlations: {e}")

        # Generate recommendations
        profile["recommendations"] = self._generate_recommendations(profile)

        # Generate warnings
        profile["warnings"] = self._generate_warnings(profile)

        return profile

    def _profile_column(self, full_col: pd.Series, sample_col: pd.Series) -> Dict[str, Any]:
        """Profile a single column."""
        col_type = str(full_col.dtype)
        missing_count = int(full_col.isna().sum())
        missing_pct = round(missing_count / len(full_col) * 100, 2) if len(full_col) > 0 else 0

        profile = {
            "name": full_col.name,
            "dtype": col_type,
            "missing_count": missing_count,
            "missing_percentage": missing_pct,
            "unique_count": int(full_col.nunique()),
            "unique_percentage": round(full_col.nunique() / len(full_col) * 100, 2) if len(full_col) > 0 else 0,
        }

        # Infer semantic type
        profile["semantic_type"] = self._infer_semantic_type(full_col)

        # Type-specific statistics
        if pd.api.types.is_numeric_dtype(full_col):
            profile["statistics"] = self._numeric_stats(full_col)
            profile["histogram"] = self._compute_histogram(sample_col)
        elif pd.api.types.is_datetime64_any_dtype(full_col):
            profile["statistics"] = self._datetime_stats(full_col)
        elif pd.api.types.is_object_dtype(full_col) or pd.api.types.is_categorical_dtype(full_col):
            profile["statistics"] = self._categorical_stats(full_col)
            profile["value_counts"] = self._top_values(full_col, n=10)

        # Check for potential issues
        profile["issues"] = self._detect_column_issues(full_col)

        return profile

    def _numeric_stats(self, col: pd.Series) -> Dict[str, Any]:
        """Compute statistics for numeric columns."""
        clean_col = col.dropna()
        if len(clean_col) == 0:
            return {}

        stats = {
            "min": float(clean_col.min()),
            "max": float(clean_col.max()),
            "mean": float(clean_col.mean()),
            "median": float(clean_col.median()),
            "std": float(clean_col.std()) if len(clean_col) > 1 else 0,
            "variance": float(clean_col.var()) if len(clean_col) > 1 else 0,
            "skewness": float(clean_col.skew()) if len(clean_col) > 2 else 0,
            "kurtosis": float(clean_col.kurtosis()) if len(clean_col) > 3 else 0,
            "zeros_count": int((clean_col == 0).sum()),
            "zeros_percentage": round((clean_col == 0).sum() / len(clean_col) * 100, 2),
            "negative_count": int((clean_col < 0).sum()),
            "positive_count": int((clean_col > 0).sum()),
        }

        # Percentiles
        try:
            percentiles = clean_col.quantile([0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99]).to_dict()
            stats["percentiles"] = {f"p{int(k*100)}": round(v, 4) for k, v in percentiles.items()}
        except Exception:
            pass

        # Detect outliers using IQR
        q1, q3 = clean_col.quantile([0.25, 0.75])
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = ((clean_col < lower_bound) | (clean_col > upper_bound)).sum()
        stats["outliers_count"] = int(outliers)
        stats["outliers_percentage"] = round(outliers / len(clean_col) * 100, 2)

        return stats

    def _datetime_stats(self, col: pd.Series) -> Dict[str, Any]:
        """Compute statistics for datetime columns."""
        clean_col = col.dropna()
        if len(clean_col) == 0:
            return {}

        return {
            "min": str(clean_col.min()),
            "max": str(clean_col.max()),
            "range_days": (clean_col.max() - clean_col.min()).days if len(clean_col) > 0 else 0,
        }

    def _categorical_stats(self, col: pd.Series) -> Dict[str, Any]:
        """Compute statistics for categorical columns."""
        clean_col = col.dropna()
        if len(clean_col) == 0:
            return {}

        value_counts = clean_col.value_counts()

        return {
            "unique_count": int(col.nunique()),
            "most_common": str(value_counts.index[0]) if len(value_counts) > 0 else None,
            "most_common_count": int(value_counts.iloc[0]) if len(value_counts) > 0 else 0,
            "least_common": str(value_counts.index[-1]) if len(value_counts) > 0 else None,
            "least_common_count": int(value_counts.iloc[-1]) if len(value_counts) > 0 else 0,
            "avg_string_length": round(clean_col.astype(str).str.len().mean(), 2),
            "max_string_length": int(clean_col.astype(str).str.len().max()),
        }

    def _top_values(self, col: pd.Series, n: int = 10) -> List[Dict[str, Any]]:
        """Get top N value counts."""
        value_counts = col.value_counts().head(n)
        total = len(col)
        return [
            {
                "value": str(val),
                "count": int(count),
                "percentage": round(count / total * 100, 2)
            }
            for val, count in value_counts.items()
        ]

    def _compute_histogram(self, col: pd.Series, bins: int = 20) -> Dict[str, Any]:
        """Compute histogram for numeric columns."""
        clean_col = col.dropna()
        if len(clean_col) == 0:
            return {}

        try:
            counts, bin_edges = np.histogram(clean_col, bins=bins)
            return {
                "counts": counts.tolist(),
                "bin_edges": [round(x, 4) for x in bin_edges.tolist()],
            }
        except Exception:
            return {}

    def _infer_semantic_type(self, col: pd.Series) -> str:
        """Infer the semantic type of a column."""
        col_name = str(col.name).lower()

        # Check by name patterns
        if any(x in col_name for x in ['id', '_id', 'uuid', 'guid']):
            return "identifier"
        if any(x in col_name for x in ['date', 'time', 'timestamp', 'created', 'updated']):
            return "datetime"
        if any(x in col_name for x in ['email', 'mail']):
            return "email"
        if any(x in col_name for x in ['phone', 'tel', 'mobile']):
            return "phone"
        if any(x in col_name for x in ['url', 'link', 'website']):
            return "url"
        if any(x in col_name for x in ['lat', 'latitude']):
            return "latitude"
        if any(x in col_name for x in ['lon', 'lng', 'longitude']):
            return "longitude"
        if any(x in col_name for x in ['price', 'cost', 'amount', 'revenue', 'salary']):
            return "monetary"
        if any(x in col_name for x in ['percent', 'pct', 'ratio', 'rate']):
            return "percentage"
        if any(x in col_name for x in ['name', 'title', 'label']):
            return "name"
        if any(x in col_name for x in ['description', 'desc', 'comment', 'note', 'text']):
            return "text"
        if any(x in col_name for x in ['category', 'type', 'class', 'group', 'status']):
            return "category"
        if any(x in col_name for x in ['count', 'num', 'qty', 'quantity']):
            return "count"
        if any(x in col_name for x in ['flag', 'is_', 'has_', 'bool']):
            return "boolean"

        # Check by dtype
        if pd.api.types.is_bool_dtype(col):
            return "boolean"
        if pd.api.types.is_datetime64_any_dtype(col):
            return "datetime"
        if pd.api.types.is_numeric_dtype(col):
            if col.nunique() == 2:
                return "binary"
            if col.nunique() < 20 and col.nunique() / len(col) < 0.05:
                return "categorical_numeric"
            return "numeric"
        if pd.api.types.is_categorical_dtype(col):
            return "category"

        # String analysis
        if pd.api.types.is_object_dtype(col):
            sample = col.dropna().head(100)
            if len(sample) > 0:
                avg_len = sample.astype(str).str.len().mean()
                if avg_len > 100:
                    return "text"
                if col.nunique() < 50:
                    return "category"

        return "unknown"

    def _detect_column_issues(self, col: pd.Series) -> List[str]:
        """Detect potential issues with a column."""
        issues = []

        # High missing rate
        missing_pct = col.isna().sum() / len(col) * 100 if len(col) > 0 else 0
        if missing_pct > 50:
            issues.append(f"High missing rate ({missing_pct:.1f}%)")
        elif missing_pct > 20:
            issues.append(f"Significant missing values ({missing_pct:.1f}%)")

        # Constant column
        if col.nunique() <= 1:
            issues.append("Constant or near-constant column")

        # High cardinality for categorical
        if pd.api.types.is_object_dtype(col):
            if col.nunique() > 0.9 * len(col) and len(col) > 100:
                issues.append("High cardinality - may be an identifier")

        # Potential ID column
        if col.nunique() == len(col) and len(col) > 10:
            issues.append("All unique values - likely an identifier")

        # Numeric outliers
        if pd.api.types.is_numeric_dtype(col):
            clean_col = col.dropna()
            if len(clean_col) > 0:
                q1, q3 = clean_col.quantile([0.25, 0.75])
                iqr = q3 - q1
                if iqr > 0:
                    outlier_pct = ((clean_col < q1 - 3*iqr) | (clean_col > q3 + 3*iqr)).sum() / len(clean_col) * 100
                    if outlier_pct > 5:
                        issues.append(f"Extreme outliers detected ({outlier_pct:.1f}%)")

        return issues

    def _generate_recommendations(self, profile: Dict[str, Any]) -> List[Dict[str, str]]:
        """Generate recommendations based on the profile."""
        recommendations = []

        # Check for target column candidates
        binary_cols = [c for c in profile["columns"]
                      if c.get("semantic_type") == "binary" or
                      (c.get("unique_count", 0) == 2 and c.get("missing_percentage", 100) < 10)]
        if binary_cols:
            recommendations.append({
                "type": "target",
                "message": f"Potential binary classification targets: {', '.join(c['name'] for c in binary_cols[:3])}",
                "priority": "high"
            })

        # Check for categorical targets
        cat_cols = [c for c in profile["columns"]
                   if c.get("semantic_type") in ["category", "categorical_numeric"]
                   and 2 < c.get("unique_count", 0) < 20]
        if cat_cols:
            recommendations.append({
                "type": "target",
                "message": f"Potential multiclass targets: {', '.join(c['name'] for c in cat_cols[:3])}",
                "priority": "medium"
            })

        # Check for high missing columns
        high_missing = [c for c in profile["columns"] if c.get("missing_percentage", 0) > 30]
        if high_missing:
            recommendations.append({
                "type": "preprocessing",
                "message": f"Consider dropping or imputing columns with >30% missing: {', '.join(c['name'] for c in high_missing[:5])}",
                "priority": "medium"
            })

        # Check for ID columns to exclude
        id_cols = [c for c in profile["columns"] if c.get("semantic_type") == "identifier"]
        if id_cols:
            recommendations.append({
                "type": "preprocessing",
                "message": f"Exclude identifier columns from features: {', '.join(c['name'] for c in id_cols[:5])}",
                "priority": "high"
            })

        # Check for datetime columns (potential timeseries)
        dt_cols = [c for c in profile["columns"] if c.get("semantic_type") == "datetime"]
        if dt_cols:
            recommendations.append({
                "type": "model",
                "message": f"Datetime columns detected - consider TimeSeries model if forecasting: {', '.join(c['name'] for c in dt_cols[:3])}",
                "priority": "info"
            })

        # Check for text columns (potential multimodal)
        text_cols = [c for c in profile["columns"] if c.get("semantic_type") == "text"]
        if text_cols:
            recommendations.append({
                "type": "model",
                "message": f"Text columns detected - consider Multimodal model: {', '.join(c['name'] for c in text_cols[:3])}",
                "priority": "info"
            })

        # High correlation warning
        if profile.get("correlations", {}).get("high_correlations"):
            recommendations.append({
                "type": "preprocessing",
                "message": "Highly correlated features detected - AutoGluon will handle this automatically",
                "priority": "info"
            })

        return recommendations

    def _generate_warnings(self, profile: Dict[str, Any]) -> List[Dict[str, str]]:
        """Generate warnings based on the profile."""
        warnings = []

        # Small dataset warning
        if profile["summary"]["total_rows"] < 100:
            warnings.append({
                "type": "data_size",
                "message": "Very small dataset - model performance may be limited",
                "severity": "warning"
            })
        elif profile["summary"]["total_rows"] < 1000:
            warnings.append({
                "type": "data_size",
                "message": "Small dataset - consider using best_quality preset for better results",
                "severity": "info"
            })

        # Many columns warning
        if profile["summary"]["total_columns"] > 100:
            warnings.append({
                "type": "dimensionality",
                "message": "High dimensionality - training may take longer",
                "severity": "info"
            })

        # Duplicate rows
        if profile["summary"]["duplicate_percentage"] > 10:
            warnings.append({
                "type": "data_quality",
                "message": f"High duplicate rate ({profile['summary']['duplicate_percentage']}%) - consider deduplication",
                "severity": "warning"
            })

        # All columns have issues
        cols_with_issues = [c for c in profile["columns"] if c.get("issues")]
        if len(cols_with_issues) > len(profile["columns"]) * 0.5:
            warnings.append({
                "type": "data_quality",
                "message": "Many columns have data quality issues - review before training",
                "severity": "warning"
            })

        return warnings

    def suggest_target_column(self, profile: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Suggest potential target columns based on profile."""
        suggestions = []

        for col in profile["columns"]:
            score = 0
            reasons = []

            # Prefer columns with low missing values
            if col.get("missing_percentage", 100) < 5:
                score += 20
                reasons.append("Low missing rate")

            # Binary columns are good targets
            if col.get("unique_count") == 2:
                score += 30
                reasons.append("Binary classification candidate")

            # Low to medium cardinality for classification
            if 2 < col.get("unique_count", 0) < 20:
                score += 20
                reasons.append("Multiclass classification candidate")

            # Numeric columns for regression
            if col.get("dtype", "").startswith(("int", "float")):
                if col.get("unique_count", 0) > 20:
                    score += 15
                    reasons.append("Regression candidate")

            # Penalize identifiers
            if col.get("semantic_type") == "identifier":
                score -= 50
                reasons.append("Likely an identifier")

            # Penalize high cardinality text
            if col.get("semantic_type") == "text":
                score -= 20

            if score > 0:
                suggestions.append({
                    "column": col["name"],
                    "score": score,
                    "reasons": reasons,
                    "problem_type": self._suggest_problem_type(col)
                })

        # Sort by score
        suggestions.sort(key=lambda x: x["score"], reverse=True)
        return suggestions[:5]

    def _suggest_problem_type(self, col_profile: Dict[str, Any]) -> str:
        """Suggest problem type based on column profile."""
        unique_count = col_profile.get("unique_count", 0)
        dtype = col_profile.get("dtype", "")

        if unique_count == 2:
            return "binary"
        elif unique_count < 20:
            return "multiclass"
        elif dtype.startswith(("int", "float")):
            return "regression"
        return "unknown"


@lru_cache()
def get_data_profiler() -> DataProfiler:
    """Get the data profiler singleton (cached)."""
    return DataProfiler()
