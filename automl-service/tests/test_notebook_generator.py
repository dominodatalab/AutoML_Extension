"""Tests for app.core.notebook_generator."""

import enum
from types import SimpleNamespace

import pytest

from app.core.notebook_generator import (
    make_cell,
    generate_binary_classification_notebook,
    generate_tabular_notebook,
    generate_timeseries_notebook,
    _normalize_timeseries_preset,
    _normalize_tabular_problem_type,
    _resolve_data_path,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

class _FakePreset(str, enum.Enum):
    MEDIUM = "medium_quality_faster_train"


def _make_job(**overrides) -> SimpleNamespace:
    """Return a minimal mock job with all attributes the generators read."""
    defaults = dict(
        id="job-001",
        name="Test Job",
        description="A test training job",
        target_column="target",
        file_path="/data/train.csv",
        preset=_FakePreset.MEDIUM,
        time_limit=120,
        eval_metric="accuracy",
        autogluon_config=None,
        experiment_name=None,
        problem_type=None,
        # Time series fields
        time_column="timestamp",
        id_column="item_id",
        prediction_length=7,
    )
    defaults.update(overrides)
    return SimpleNamespace(**defaults)


# ---------------------------------------------------------------------------
# make_cell
# ---------------------------------------------------------------------------

class TestMakeCell:
    def test_code_cell_has_outputs_and_execution_count(self):
        cell = make_cell("code", ["print('hi')"])
        assert cell["cell_type"] == "code"
        assert "outputs" in cell
        assert isinstance(cell["outputs"], list)
        assert "execution_count" in cell

    def test_markdown_cell_has_no_outputs_or_execution_count(self):
        cell = make_cell("markdown", ["# Title"])
        assert cell["cell_type"] == "markdown"
        assert "outputs" not in cell
        assert "execution_count" not in cell

    def test_source_is_preserved(self):
        src = ["line1\n", "line2\n"]
        cell = make_cell("code", src)
        assert cell["source"] == src

    def test_execution_count_can_be_set(self):
        cell = make_cell("code", ["x = 1"], execution_count=5)
        assert cell["execution_count"] == 5


# ---------------------------------------------------------------------------
# generate_tabular_notebook
# ---------------------------------------------------------------------------

class TestGenerateTabularNotebook:
    def test_valid_notebook_structure(self):
        job = _make_job()
        nb = generate_tabular_notebook(job)

        assert nb["nbformat"] == 4
        assert isinstance(nb["cells"], list)
        assert len(nb["cells"]) > 0
        assert nb["metadata"]["job_id"] == "job-001"
        assert nb["metadata"]["job_name"] == "Test Job"
        assert nb["metadata"]["model_type"] == "tabular"

    def test_cells_contain_code_and_markdown(self):
        job = _make_job()
        nb = generate_tabular_notebook(job)
        types = {c["cell_type"] for c in nb["cells"]}
        assert "code" in types
        assert "markdown" in types

    def test_data_path_override(self):
        job = _make_job()
        nb = generate_tabular_notebook(job, data_path="/custom/path.csv")
        # The config cell should reference the custom path
        all_source = "".join(
            "".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "code"
        )
        assert "/custom/path.csv" in all_source

    def test_experiment_name_fallback(self):
        job = _make_job(experiment_name=None, name="My Job")
        nb = generate_tabular_notebook(job)
        all_source = "".join(
            "".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "code"
        )
        assert "My_Job" in all_source


# ---------------------------------------------------------------------------
# generate_timeseries_notebook
# ---------------------------------------------------------------------------

class TestGenerateTimeseriesNotebook:
    def test_valid_notebook_structure(self):
        job = _make_job()
        nb = generate_timeseries_notebook(job)

        assert nb["nbformat"] == 4
        assert isinstance(nb["cells"], list)
        assert len(nb["cells"]) > 0
        assert nb["metadata"]["job_id"] == "job-001"
        assert nb["metadata"]["model_type"] == "timeseries"

    def test_includes_time_series_specific_cells(self):
        job = _make_job()
        nb = generate_timeseries_notebook(job)
        all_source = "".join(
            "".join(c["source"]) for c in nb["cells"]
        )
        assert "TimeSeriesPredictor" in all_source
        assert "TimeSeriesDataFrame" in all_source
        assert "prediction_length" in all_source

    def test_data_path_override(self):
        job = _make_job()
        nb = generate_timeseries_notebook(job, data_path="/ts/data.csv")
        all_source = "".join(
            "".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "code"
        )
        assert "/ts/data.csv" in all_source


# ---------------------------------------------------------------------------
# generate_binary_classification_notebook
# ---------------------------------------------------------------------------

class TestGenerateBinaryClassificationNotebook:
    def test_valid_notebook_structure(self):
        job = _make_job()
        nb = generate_binary_classification_notebook(job)

        assert nb["nbformat"] == 4
        assert isinstance(nb["cells"], list)
        assert len(nb["cells"]) > 0
        assert nb["metadata"]["job_id"] == "job-001"
        assert nb["metadata"]["job_name"] == "Test Job"

    def test_includes_roc_and_pr_curve_cells(self):
        job = _make_job()
        nb = generate_binary_classification_notebook(job)
        all_source = "".join(
            "".join(c["source"]) for c in nb["cells"]
        )
        assert "ROC" in all_source or "roc_curve" in all_source
        assert "Precision-Recall" in all_source or "precision_recall_curve" in all_source

    def test_advanced_config_included_when_present(self):
        job = _make_job(
            autogluon_config={
                "advanced": {
                    "num_bag_folds": 5,
                    "num_stack_levels": 2,
                }
            }
        )
        nb = generate_binary_classification_notebook(job)
        all_source = "".join(
            "".join(c["source"]) for c in nb["cells"]
        )
        assert "num_bag_folds" in all_source
        assert "num_stack_levels" in all_source


# ---------------------------------------------------------------------------
# _normalize_timeseries_preset
# ---------------------------------------------------------------------------

class TestNormalizeTimeseriesPreset:
    def test_maps_medium_quality_faster_train(self):
        assert _normalize_timeseries_preset("medium_quality_faster_train") == "medium_quality"

    def test_maps_good_quality(self):
        assert _normalize_timeseries_preset("good_quality") == "medium_quality"

    def test_maps_optimize_for_deployment(self):
        assert _normalize_timeseries_preset("optimize_for_deployment") == "fast_training"

    def test_passthrough_for_unknown(self):
        assert _normalize_timeseries_preset("best_quality") == "best_quality"

    def test_passthrough_for_already_valid(self):
        assert _normalize_timeseries_preset("fast_training") == "fast_training"
        assert _normalize_timeseries_preset("medium_quality") == "medium_quality"


# ---------------------------------------------------------------------------
# _normalize_tabular_problem_type
# ---------------------------------------------------------------------------

class TestNormalizeTabularProblemType:
    def test_none_returns_auto(self):
        job = _make_job(problem_type=None)
        assert _normalize_tabular_problem_type(job) == "auto"

    def test_enum_value_extracted(self):
        class FakePT(str, enum.Enum):
            BINARY = "binary"

        job = _make_job(problem_type=FakePT.BINARY)
        assert _normalize_tabular_problem_type(job) == "binary"

    def test_string_returned_as_is(self):
        job = _make_job(problem_type="regression")
        assert _normalize_tabular_problem_type(job) == "regression"

    def test_missing_attribute_returns_auto(self):
        """If the job object has no problem_type attribute at all."""
        job = SimpleNamespace(id="x", name="x")
        assert _normalize_tabular_problem_type(job) == "auto"


# ---------------------------------------------------------------------------
# _resolve_data_path
# ---------------------------------------------------------------------------

class TestResolveDataPath:
    def test_resolved_data_path_takes_priority(self):
        job = _make_job(file_path="/original/path.csv")
        result = _resolve_data_path(job, resolved_data_path="/override/path.csv")
        assert result == "/override/path.csv"

    def test_falls_back_to_job_file_path(self):
        job = _make_job(file_path="/data/file.csv")
        result = _resolve_data_path(job)
        assert result == "/data/file.csv"

    def test_default_when_no_path_available(self):
        job = SimpleNamespace(id="x", name="x")  # no file_path attribute
        result = _resolve_data_path(job)
        assert result == "path/to/your/data.csv"

    def test_default_when_file_path_is_none(self):
        job = _make_job(file_path=None)
        result = _resolve_data_path(job)
        assert result == "path/to/your/data.csv"
