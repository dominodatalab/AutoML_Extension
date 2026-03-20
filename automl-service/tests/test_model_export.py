"""Tests for app.core.model_export."""

import json
import os

import pytest

from app.core.model_export import ModelExporter, get_model_exporter


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def exporter():
    return ModelExporter()


# ---------------------------------------------------------------------------
# generate_deployment_files – key presence
# ---------------------------------------------------------------------------

class TestGenerateDeploymentFiles:
    """Tests for ModelExporter.generate_deployment_files."""

    EXPECTED_KEYS = {"inference.py", "requirements.txt", "Dockerfile", "model_metadata.json"}

    def test_tabular_returns_correct_keys(self, exporter):
        files = exporter.generate_deployment_files("tabular")
        assert set(files.keys()) == self.EXPECTED_KEYS

    def test_timeseries_returns_correct_keys(self, exporter):
        files = exporter.generate_deployment_files("timeseries")
        assert set(files.keys()) == self.EXPECTED_KEYS

    # -- inference.py content ------------------------------------------------

    def test_tabular_inference_imports_tabular_predictor(self, exporter):
        files = exporter.generate_deployment_files("tabular")
        assert "from autogluon.tabular import TabularPredictor" in files["inference.py"]

    def test_timeseries_inference_imports_timeseries_predictor(self, exporter):
        files = exporter.generate_deployment_files("timeseries")
        assert "from autogluon.timeseries import TimeSeriesPredictor" in files["inference.py"]

    def test_tabular_inference_does_not_contain_timeseries(self, exporter):
        files = exporter.generate_deployment_files("tabular")
        assert "TimeSeriesPredictor" not in files["inference.py"]

    def test_timeseries_inference_does_not_contain_tabular(self, exporter):
        files = exporter.generate_deployment_files("timeseries")
        assert "TabularPredictor" not in files["inference.py"]

    # -- requirements.txt content -------------------------------------------

    def test_tabular_requirements_includes_tabular_package(self, exporter):
        files = exporter.generate_deployment_files("tabular")
        assert "autogluon.tabular" in files["requirements.txt"]

    def test_timeseries_requirements_includes_timeseries_package(self, exporter):
        files = exporter.generate_deployment_files("timeseries")
        assert "autogluon.timeseries" in files["requirements.txt"]

    def test_requirements_includes_base_deps(self, exporter):
        files = exporter.generate_deployment_files("tabular")
        reqs = files["requirements.txt"]
        assert "autogluon>=1.0.0" in reqs
        assert "pandas>=" in reqs
        assert "numpy>=" in reqs

    # -- Dockerfile content -------------------------------------------------

    def test_dockerfile_has_from_directive(self, exporter):
        files = exporter.generate_deployment_files("tabular")
        assert files["Dockerfile"].startswith("FROM ")

    def test_dockerfile_copies_inference_script(self, exporter):
        files = exporter.generate_deployment_files("tabular")
        assert "COPY inference.py" in files["Dockerfile"]

    def test_dockerfile_installs_requirements(self, exporter):
        files = exporter.generate_deployment_files("tabular")
        assert "requirements.txt" in files["Dockerfile"]

    def test_dockerfile_exposes_port(self, exporter):
        files = exporter.generate_deployment_files("tabular")
        assert "EXPOSE" in files["Dockerfile"]

    # -- model_metadata.json content ----------------------------------------

    def test_metadata_is_valid_json_with_model_type(self, exporter):
        files = exporter.generate_deployment_files("tabular")
        metadata = json.loads(files["model_metadata.json"])
        assert metadata["model_type"] == "tabular"
        assert metadata["framework"] == "autogluon"

    def test_metadata_timeseries(self, exporter):
        files = exporter.generate_deployment_files("timeseries")
        metadata = json.loads(files["model_metadata.json"])
        assert metadata["model_type"] == "timeseries"
        assert metadata["framework"] == "autogluon"

    # -- unsupported model type ---------------------------------------------

    def test_unsupported_model_type_raises_value_error(self, exporter):
        with pytest.raises(ValueError, match="Unsupported model type"):
            exporter.generate_deployment_files("unsupported")


# ---------------------------------------------------------------------------
# export_for_deployment
# ---------------------------------------------------------------------------

class TestExportForDeployment:
    """Tests for ModelExporter.export_for_deployment."""

    def _make_model_dir(self, tmp_path):
        """Create a fake model directory with an artifact file."""
        model_dir = tmp_path / "fake_model"
        model_dir.mkdir()
        (model_dir / "model.pkl").write_text("fake-model-bytes")
        return str(model_dir)

    def test_creates_deployment_package_directory(self, exporter, tmp_path):
        model_path = self._make_model_dir(tmp_path)
        output_dir = str(tmp_path / "output")
        os.makedirs(output_dir)

        result = exporter.export_for_deployment(model_path, "tabular", output_dir)

        assert result["success"] is True
        assert os.path.isdir(result["output_dir"])

    def test_creates_expected_files_on_disk(self, exporter, tmp_path):
        model_path = self._make_model_dir(tmp_path)
        output_dir = str(tmp_path / "output")
        os.makedirs(output_dir)

        result = exporter.export_for_deployment(model_path, "tabular", output_dir)
        deploy_dir = result["output_dir"]

        assert os.path.isfile(os.path.join(deploy_dir, "inference.py"))
        assert os.path.isfile(os.path.join(deploy_dir, "requirements.txt"))
        assert os.path.isfile(os.path.join(deploy_dir, "Dockerfile"))
        assert os.path.isfile(os.path.join(deploy_dir, "model_metadata.json"))

    def test_result_files_list(self, exporter, tmp_path):
        model_path = self._make_model_dir(tmp_path)
        output_dir = str(tmp_path / "output")
        os.makedirs(output_dir)

        result = exporter.export_for_deployment(model_path, "tabular", output_dir)

        assert "model/" in result["files"]
        assert "inference.py" in result["files"]
        assert "requirements.txt" in result["files"]
        assert "model_metadata.json" in result["files"]
        assert "Dockerfile" in result["files"]

    def test_copies_model_directory(self, exporter, tmp_path):
        model_path = self._make_model_dir(tmp_path)
        output_dir = str(tmp_path / "output")
        os.makedirs(output_dir)

        result = exporter.export_for_deployment(model_path, "tabular", output_dir)
        copied_model = os.path.join(result["output_dir"], "model")

        assert os.path.isdir(copied_model)
        assert os.path.isfile(os.path.join(copied_model, "model.pkl"))

    def test_copies_single_file_model(self, exporter, tmp_path):
        model_file = tmp_path / "model.pkl"
        model_file.write_text("single-file-model")
        output_dir = str(tmp_path / "output")
        os.makedirs(output_dir)

        result = exporter.export_for_deployment(str(model_file), "tabular", output_dir)
        copied_model_dir = os.path.join(result["output_dir"], "model")

        assert os.path.isdir(copied_model_dir)
        assert os.path.isfile(os.path.join(copied_model_dir, "model.pkl"))

    def test_metadata_json_on_disk_is_valid(self, exporter, tmp_path):
        model_path = self._make_model_dir(tmp_path)
        output_dir = str(tmp_path / "output")
        os.makedirs(output_dir)

        result = exporter.export_for_deployment(model_path, "timeseries", output_dir)
        meta_path = os.path.join(result["output_dir"], "model_metadata.json")

        with open(meta_path) as f:
            metadata = json.load(f)

        assert metadata["model_type"] == "timeseries"
        assert metadata["framework"] == "autogluon"

    def test_handles_error_gracefully(self, exporter, tmp_path):
        """Providing a non-existent model path should not raise but return error."""
        output_dir = str(tmp_path / "output")
        os.makedirs(output_dir)

        result = exporter.export_for_deployment("/no/such/model", "tabular", output_dir)

        assert result["success"] is False
        assert result["error"] is not None

    def test_handles_unsupported_type_gracefully(self, exporter, tmp_path):
        model_path = self._make_model_dir(tmp_path)
        output_dir = str(tmp_path / "output")
        os.makedirs(output_dir)

        result = exporter.export_for_deployment(model_path, "unsupported", output_dir)

        assert result["success"] is False
        assert result["error"] is not None


# ---------------------------------------------------------------------------
# _remove_path_if_exists
# ---------------------------------------------------------------------------

class TestRemovePathIfExists:
    """Tests for ModelExporter._remove_path_if_exists."""

    def test_removes_file(self, tmp_path):
        f = tmp_path / "file.txt"
        f.write_text("data")
        ModelExporter._remove_path_if_exists(str(f))
        assert not f.exists()

    def test_removes_directory(self, tmp_path):
        d = tmp_path / "subdir"
        d.mkdir()
        (d / "child.txt").write_text("x")
        ModelExporter._remove_path_if_exists(str(d))
        assert not d.exists()

    def test_removes_symlink(self, tmp_path):
        target = tmp_path / "target.txt"
        target.write_text("target")
        link = tmp_path / "link.txt"
        link.symlink_to(target)

        ModelExporter._remove_path_if_exists(str(link))

        assert not link.exists() and not link.is_symlink()
        # Original target should still exist
        assert target.exists()

    def test_removes_broken_symlink(self, tmp_path):
        target = tmp_path / "gone.txt"
        link = tmp_path / "broken_link"
        target.write_text("temp")
        link.symlink_to(target)
        target.unlink()  # break the symlink

        ModelExporter._remove_path_if_exists(str(link))
        assert not link.is_symlink()

    def test_noop_for_nonexistent_path(self, tmp_path):
        # Should not raise
        ModelExporter._remove_path_if_exists(str(tmp_path / "does_not_exist"))


# ---------------------------------------------------------------------------
# get_model_exporter singleton
# ---------------------------------------------------------------------------

class TestGetModelExporter:

    def test_returns_model_exporter_instance(self):
        instance = get_model_exporter()
        assert isinstance(instance, ModelExporter)

    def test_returns_same_instance(self):
        a = get_model_exporter()
        b = get_model_exporter()
        assert a is b
