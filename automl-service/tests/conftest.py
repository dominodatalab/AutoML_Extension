"""Shared test fixtures for the AutoML service test suite.

Provides:
- Async in-memory SQLite database
- Test Settings overrides
- Synthetic tabular and time series datasets (CSV files)
- FastAPI TestClient with dependency overrides
- Cleanup utilities
"""

import asyncio
import os
import shutil
import subprocess
import tempfile
import uuid
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import AsyncGenerator

import numpy as np
import pandas as pd
import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)

# ---------------------------------------------------------------------------
# Ensure the app package is importable from tests/
# ---------------------------------------------------------------------------
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.db.database import Base
from app.db.models import Job, JobLog, JobStatus, ModelType, ProblemType, RegisteredModel
from app.core.utils import utc_now

# ---------------------------------------------------------------------------
# Dynamic HTML report path — saved to /mnt/artifacts so Domino persists it
# ---------------------------------------------------------------------------

def _git_short_sha() -> str:
    """Return the short git SHA, or 'unknown' if not in a repo."""
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except Exception:
        return "unknown"


def pytest_configure(config):
    """Set --html to a timestamped path under /mnt/artifacts (Domino) or local fallback."""
    # Only set if not already provided via CLI
    if config.getoption("htmlpath", default=None):
        return

    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    sha = _git_short_sha()
    filename = f"test_report_{ts}_{sha}.html"

    artifacts_dir = Path("/mnt/artifacts/results")
    if artifacts_dir.exists():
        report_dir = artifacts_dir
    else:
        # Local dev fallback — save next to the tests
        report_dir = Path(__file__).resolve().parent.parent / "test-reports"
        report_dir.mkdir(exist_ok=True)

    config.option.htmlpath = str(report_dir / filename)


# ---------------------------------------------------------------------------
# Auto-skip markers when optional packages are absent
# ---------------------------------------------------------------------------

_HAS_DOMINO = False
try:
    import domino  # noqa: F401
    _HAS_DOMINO = True
except ImportError:
    pass


def pytest_collection_modifyitems(config, items):
    """Auto-skip tests that require unavailable optional packages."""
    skip_domino = pytest.mark.skip(reason="requires 'domino' package (run in Domino environment)")
    for item in items:
        if "domino" in item.keywords and not _HAS_DOMINO:
            item.add_marker(skip_domino)


# ---------------------------------------------------------------------------
# pytest-html report customization
# ---------------------------------------------------------------------------

# Collect per-module stats as tests run so we can build a summary table.
_module_stats = defaultdict(
    lambda: {"passed": 0, "failed": 0, "skipped": 0, "error": 0, "duration": 0.0}
)


def pytest_runtest_logreport(report):
    """Accumulate per-module pass/fail/skip/error counts."""
    # Count call-phase results (the actual test) and setup-phase skips/errors.
    if report.when == "call":
        module = report.nodeid.split("::")[0]
        if report.passed:
            _module_stats[module]["passed"] += 1
        elif report.skipped:
            _module_stats[module]["skipped"] += 1
        elif report.failed:
            _module_stats[module]["failed"] += 1
        _module_stats[module]["duration"] += getattr(report, "duration", 0.0)
    elif report.when == "setup":
        module = report.nodeid.split("::")[0]
        if report.skipped:
            _module_stats[module]["skipped"] += 1
        elif report.failed:
            _module_stats[module]["error"] += 1


@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    """Set a concise report title."""
    report.title = "AutoML Service — Test Report"


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix, session):
    """Inject a per-module summary table at the top of the report."""
    if not _module_stats:
        return

    total_p = sum(s["passed"] for s in _module_stats.values())
    total_f = sum(s["failed"] for s in _module_stats.values())
    total_s = sum(s["skipped"] for s in _module_stats.values())
    total_e = sum(s["error"] for s in _module_stats.values())
    total_d = sum(s["duration"] for s in _module_stats.values())
    total_tests = total_p + total_f + total_s + total_e

    # Build the HTML summary table.
    rows = []
    for module in sorted(_module_stats):
        s = _module_stats[module]
        count = s["passed"] + s["failed"] + s["skipped"] + s["error"]
        name = module.replace("tests/", "")

        # Row color: red if any failures/errors, orange if all skipped, green otherwise.
        if s["failed"] or s["error"]:
            color = "#d32f2f"
        elif s["passed"] == 0 and s["skipped"] > 0:
            color = "#f57c00"
        else:
            color = "#388e3c"

        status_icon = "&#10004;" if not (s["failed"] or s["error"]) else "&#10008;"
        rows.append(
            f'<tr style="color:{color}">'
            f"<td>{status_icon} {name}</td>"
            f'<td style="text-align:right">{count}</td>'
            f'<td style="text-align:right">{s["passed"]}</td>'
            f'<td style="text-align:right">{s["failed"]}</td>'
            f'<td style="text-align:right">{s["skipped"]}</td>'
            f'<td style="text-align:right">{s["error"]}</td>'
            f'<td style="text-align:right">{s["duration"]:.2f}s</td>'
            f"</tr>"
        )

    table_html = (
        "<h3>Module Summary</h3>"
        '<table style="border-collapse:collapse;width:100%;font-size:13px;margin-bottom:16px">'
        '<thead><tr style="background:#f5f5f5;border-bottom:2px solid #ccc;text-align:left">'
        "<th>Module</th>"
        '<th style="text-align:right">Total</th>'
        '<th style="text-align:right">Passed</th>'
        '<th style="text-align:right">Failed</th>'
        '<th style="text-align:right">Skipped</th>'
        '<th style="text-align:right">Errors</th>'
        '<th style="text-align:right">Duration</th>'
        "</tr></thead><tbody>"
        + "\n".join(rows)
        + '<tr style="border-top:2px solid #ccc;font-weight:bold">'
        f'<td>TOTAL</td>'
        f'<td style="text-align:right">{total_tests}</td>'
        f'<td style="text-align:right">{total_p}</td>'
        f'<td style="text-align:right">{total_f}</td>'
        f'<td style="text-align:right">{total_s}</td>'
        f'<td style="text-align:right">{total_e}</td>'
        f'<td style="text-align:right">{total_d:.2f}s</td>'
        f"</tr></tbody></table>"
    )

    # CSS/JS to hide the environment table and collapse passing tests by default.
    style_and_script = (
        "<style>"
        "#environment { display: none !important; }"
        ".summary__data { margin-bottom: 12px; }"
        "</style>"
        "<script>"
        "document.addEventListener('DOMContentLoaded', function() {"
        "  // Uncheck the 'Passed' filter checkbox so only failures/skips show."
        "  var checkboxes = document.querySelectorAll("
        "    'input[data-test-result=\"passed\"], "
        "    .filter input[value=\"passed\"]'"
        "  );"
        "  checkboxes.forEach(function(cb) {"
        "    if (cb.checked) { cb.click(); }"
        "  });"
        "  // Also try pytest-html 4.x filter buttons."
        "  var buttons = document.querySelectorAll('.filter button, .filter label');"
        "  buttons.forEach(function(btn) {"
        "    if (btn.textContent.trim().toLowerCase().indexOf('passed') !== -1) {"
        "      var input = btn.querySelector('input') || btn.previousElementSibling;"
        "      if (input && input.checked) { input.click(); }"
        "    }"
        "  });"
        "});"
        "</script>"
    )

    prefix.extend([style_and_script, table_html])


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    """Remove the Links column from the results table."""
    # pytest-html 4.x: cells are strings. Remove the last one if it's "Links".
    if cells and "Links" in str(cells[-1]):
        cells.pop()


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    """Remove the Links cell to match the header."""
    if cells and len(cells) > 3:
        cells.pop()


# ---------------------------------------------------------------------------
# Database fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def event_loop():
    """Use a single event loop for the entire test session."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def async_engine():
    """Create an async in-memory SQLite engine for each test."""
    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:",
        echo=False,
        future=True,
    )
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest_asyncio.fixture
async def db_session(async_engine) -> AsyncGenerator[AsyncSession, None]:
    """Provide an async DB session bound to the in-memory engine."""
    session_factory = async_sessionmaker(
        async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with session_factory() as session:
        yield session
        await session.rollback()


# ---------------------------------------------------------------------------
# Temp directory fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def tmp_data_dir(tmp_path):
    """Create a temporary directory tree for test data/models/uploads."""
    dirs = {
        "root": tmp_path,
        "models": tmp_path / "models",
        "uploads": tmp_path / "uploads",
        "datasets": tmp_path / "datasets",
        "temp": tmp_path / "temp",
        "eda_results": tmp_path / "eda_results",
    }
    for d in dirs.values():
        d.mkdir(parents=True, exist_ok=True)
    return dirs


# ---------------------------------------------------------------------------
# Synthetic data fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def tabular_csv(tmp_path) -> str:
    """Generate a synthetic tabular CSV with mixed column types.

    200 rows, columns: id, age, income, category, target (binary 0/1),
    email_address, created_date.
    """
    rng = np.random.RandomState(42)
    n = 200
    df = pd.DataFrame({
        "id": range(1, n + 1),
        "age": rng.randint(18, 80, size=n),
        "income": rng.normal(50000, 15000, size=n).round(2),
        "score": rng.uniform(0, 100, size=n).round(2),
        "category": rng.choice(["A", "B", "C", "D"], size=n),
        "target": rng.choice([0, 1], size=n, p=[0.6, 0.4]),
        "email_address": [f"user{i}@test.com" for i in range(n)],
        "created_date": pd.date_range("2024-01-01", periods=n, freq="D"),
    })
    # Inject some missing values
    df.loc[rng.choice(n, 10, replace=False), "income"] = np.nan
    df.loc[rng.choice(n, 5, replace=False), "category"] = np.nan

    path = str(tmp_path / "tabular_test.csv")
    df.to_csv(path, index=False)
    return path


@pytest.fixture
def tabular_df(tabular_csv) -> pd.DataFrame:
    """Load the synthetic tabular CSV as a DataFrame."""
    return pd.read_csv(tabular_csv)


@pytest.fixture
def multiclass_csv(tmp_path) -> str:
    """Generate a synthetic multiclass CSV."""
    rng = np.random.RandomState(42)
    n = 300
    df = pd.DataFrame({
        "feature_1": rng.normal(0, 1, n),
        "feature_2": rng.normal(5, 2, n),
        "feature_3": rng.uniform(0, 10, n),
        "label": rng.choice(["cat", "dog", "bird", "fish"], size=n),
    })
    path = str(tmp_path / "multiclass_test.csv")
    df.to_csv(path, index=False)
    return path


@pytest.fixture
def regression_csv(tmp_path) -> str:
    """Generate a synthetic regression CSV."""
    rng = np.random.RandomState(42)
    n = 250
    x1 = rng.normal(0, 1, n)
    x2 = rng.normal(0, 1, n)
    noise = rng.normal(0, 0.5, n)
    target = 3 * x1 + 2 * x2 + noise
    df = pd.DataFrame({
        "x1": x1,
        "x2": x2,
        "x3": rng.uniform(-1, 1, n),
        "target": target.round(4),
    })
    path = str(tmp_path / "regression_test.csv")
    df.to_csv(path, index=False)
    return path


@pytest.fixture
def timeseries_csv(tmp_path) -> str:
    """Generate a synthetic time series CSV with multiple series.

    2 series (item_A, item_B), 180 daily timestamps each, with trend and noise.
    """
    rng = np.random.RandomState(42)
    dates = pd.date_range("2023-01-01", periods=180, freq="D")
    rows = []
    for item_id in ["item_A", "item_B"]:
        base = 100 if item_id == "item_A" else 200
        trend = np.linspace(0, 20, 180)
        noise = rng.normal(0, 5, 180)
        seasonal = 10 * np.sin(np.linspace(0, 4 * np.pi, 180))
        values = base + trend + seasonal + noise
        for i, (date, value) in enumerate(zip(dates, values)):
            rows.append({
                "timestamp": date,
                "item_id": item_id,
                "value": round(value, 2),
            })

    df = pd.DataFrame(rows)
    path = str(tmp_path / "timeseries_test.csv")
    df.to_csv(path, index=False)
    return path


@pytest.fixture
def timeseries_single_csv(tmp_path) -> str:
    """Generate a single-series time series CSV (no id column)."""
    rng = np.random.RandomState(42)
    n = 200
    dates = pd.date_range("2023-06-01", periods=n, freq="D")
    trend = np.linspace(50, 80, n)
    noise = rng.normal(0, 3, n)
    values = trend + noise
    df = pd.DataFrame({
        "date": dates,
        "temperature": values.round(2),
    })
    path = str(tmp_path / "timeseries_single.csv")
    df.to_csv(path, index=False)
    return path


@pytest.fixture
def parquet_file(tmp_path, tabular_csv) -> str:
    """Generate a Parquet version of the tabular CSV."""
    df = pd.read_csv(tabular_csv)
    path = str(tmp_path / "tabular_test.parquet")
    df.to_parquet(path, index=False)
    return path


# ---------------------------------------------------------------------------
# Job model factory
# ---------------------------------------------------------------------------

@pytest.fixture
def make_job():
    """Factory fixture for creating Job ORM instances with sensible defaults."""

    def _make(
        name: str = "test-job",
        status: JobStatus = JobStatus.PENDING,
        model_type: ModelType = ModelType.TABULAR,
        problem_type: ProblemType = None,
        data_source: str = "upload",
        target_column: str = "target",
        file_path: str = "/tmp/test.csv",
        owner: str = "test-user",
        project_name: str = "test-project",
        execution_target: str = "local",
        preset: str = "medium_quality_faster_train",
        time_limit: int = 60,
        **kwargs,
    ) -> Job:
        return Job(
            id=str(uuid.uuid4()),
            name=name,
            status=status,
            model_type=model_type,
            problem_type=problem_type,
            data_source=data_source,
            target_column=target_column,
            file_path=file_path,
            owner=owner,
            project_name=project_name,
            execution_target=execution_target,
            preset=preset,
            time_limit=time_limit,
            created_at=utc_now(),
            **kwargs,
        )

    return _make


# ---------------------------------------------------------------------------
# FastAPI test client (for API integration tests)
# ---------------------------------------------------------------------------

@pytest_asyncio.fixture
async def app_client(async_engine, tmp_data_dir, monkeypatch):
    """Provide an async HTTP test client for the FastAPI app.

    Overrides the DB dependency and settings for isolated testing.
    """
    # Override settings before importing the app
    monkeypatch.setenv("DATABASE_URL", "sqlite:///:memory:")
    monkeypatch.setenv("MODELS_PATH", str(tmp_data_dir["models"]))
    monkeypatch.setenv("UPLOADS_PATH", str(tmp_data_dir["uploads"]))
    monkeypatch.setenv("DATASETS_PATH", str(tmp_data_dir["datasets"]))
    monkeypatch.setenv("TEMP_PATH", str(tmp_data_dir["temp"]))
    monkeypatch.setenv("EDA_RESULTS_PATH", str(tmp_data_dir["eda_results"]))

    # Reset cached settings singleton
    import app.config as config_module
    config_module._settings_instance = None

    from app.main import create_app
    from app.dependencies import get_db

    app = create_app()

    # Override DB dependency to use test engine
    test_session_factory = async_sessionmaker(
        async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async def override_get_db():
        async with test_session_factory() as session:
            try:
                yield session
            finally:
                await session.close()

    app.dependency_overrides[get_db] = override_get_db

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client

    # Restore settings singleton
    config_module._settings_instance = None
