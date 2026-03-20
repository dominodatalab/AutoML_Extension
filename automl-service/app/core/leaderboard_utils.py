"""Helpers for normalizing leaderboard payloads across AutoGluon model types."""

from __future__ import annotations

from typing import Any, Optional


def normalize_leaderboard_rows(
    rows: Optional[list[dict[str, Any]]],
) -> Optional[list[dict[str, Any]]]:
    """Normalize leaderboard rows to expose common timing keys.

    AutoGluon TimeSeries leaderboards expose ``fit_time_marginal`` but not
    ``fit_time``. Our UI expects ``fit_time`` for the training-time chart and
    leaderboard table, so copy the marginal value into ``fit_time`` when the
    cumulative field is absent.
    """
    if rows is None:
        return None

    normalized_rows: list[dict[str, Any]] = []
    for row in rows:
        normalized = dict(row)

        if normalized.get("fit_time") is None and normalized.get("fit_time_marginal") is not None:
            normalized["fit_time"] = normalized["fit_time_marginal"]

        if normalized.get("pred_time_val") is None and normalized.get("pred_time_val_marginal") is not None:
            normalized["pred_time_val"] = normalized["pred_time_val_marginal"]

        normalized_rows.append(normalized)

    return normalized_rows


def normalize_leaderboard_payload(payload: Any) -> Any:
    """Normalize leaderboard payloads stored as either lists or dict wrappers."""
    if isinstance(payload, list):
        return normalize_leaderboard_rows(payload)

    if isinstance(payload, dict) and isinstance(payload.get("models"), list):
        normalized = dict(payload)
        normalized["models"] = normalize_leaderboard_rows(payload["models"])
        return normalized

    return payload
