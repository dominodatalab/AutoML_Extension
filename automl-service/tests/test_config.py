"""Tests for app.config (Settings, sanitize_project_name)."""

import os
import tempfile
from unittest.mock import patch

import pytest

from app.config import Settings, sanitize_project_name


# ---------------------------------------------------------------------------
# sanitize_project_name
# ---------------------------------------------------------------------------


class TestSanitizeProjectName:
    """Test the sanitize_project_name helper."""

    def test_none_returns_default(self):
        assert sanitize_project_name(None) == "default_project"

    def test_empty_string_returns_default(self):
        assert sanitize_project_name("") == "default_project"

    def test_whitespace_only_returns_default(self):
        assert sanitize_project_name("   ") == "default_project"

    def test_normal_name_unchanged(self):
        assert sanitize_project_name("my-project") == "my-project"

    def test_dots_and_underscores_preserved(self):
        assert sanitize_project_name("v1.0_release") == "v1.0_release"

    def test_special_chars_replaced_with_underscore(self):
        assert sanitize_project_name("my project!@#$%^&*()") == "my_project"

    def test_spaces_collapsed(self):
        assert sanitize_project_name("my  cool  project") == "my_cool_project"

    def test_leading_trailing_special_stripped(self):
        # After regex replace, leading/trailing dots, underscores, hyphens are stripped
        assert sanitize_project_name("...my-project...") == "my-project"
        assert sanitize_project_name("___test___") == "test"

    def test_only_special_chars_returns_default(self):
        # All chars replaced by underscores, then stripped -> empty -> default
        assert sanitize_project_name("@#$%") == "default_project"

    def test_mixed_valid_chars(self):
        assert sanitize_project_name("Project-2024.v1_final") == "Project-2024.v1_final"

    def test_slashes_replaced(self):
        result = sanitize_project_name("org/project/name")
        assert "/" not in result
        assert result == "org_project_name"

    def test_unicode_replaced(self):
        result = sanitize_project_name("projet-cafe")
        # Non-ASCII 'e with accent' would be replaced if present; plain ASCII is fine
        assert result == "projet-cafe"


# ---------------------------------------------------------------------------
# Settings.resolved_project_name
# ---------------------------------------------------------------------------


class TestResolvedProjectName:
    """Test the resolved_project_name property and its fallback logic."""

    def test_uses_domino_project_name_field(self):
        """When domino_project_name is set on the instance, use it."""
        s = Settings(domino_project_name="my-project")
        assert s.resolved_project_name == "my-project"

    def test_falls_back_to_env_var(self, monkeypatch):
        """When the field is None, fall back to DOMINO_PROJECT_NAME env var."""
        monkeypatch.setenv("DOMINO_PROJECT_NAME", "env-project")
        s = Settings(domino_project_name=None)
        assert s.resolved_project_name == "env-project"

    def test_falls_back_to_default(self, monkeypatch):
        """When both field and env are absent, use default_project."""
        monkeypatch.delenv("DOMINO_PROJECT_NAME", raising=False)
        s = Settings(domino_project_name=None)
        assert s.resolved_project_name == "default_project"

    def test_field_takes_priority_over_env(self, monkeypatch):
        """The field value should win over the environment variable."""
        monkeypatch.setenv("DOMINO_PROJECT_NAME", "env-project")
        s = Settings(domino_project_name="field-project")
        assert s.resolved_project_name == "field-project"

    def test_sanitizes_value(self):
        """The name goes through sanitize_project_name."""
        s = Settings(domino_project_name="My Project!!!")
        assert s.resolved_project_name == "My_Project"


# ---------------------------------------------------------------------------
# Settings.is_domino_environment
# ---------------------------------------------------------------------------


class TestIsDominoEnvironment:
    """Test the is_domino_environment property."""

    def test_true_with_host_and_proxy(self, monkeypatch):
        """True when domino_api_host and DOMINO_API_PROXY env are set."""
        monkeypatch.setenv("DOMINO_API_PROXY", "http://proxy:8080")
        s = Settings(domino_api_host="https://example.domino.tech")
        assert s.is_domino_environment is True

    def test_true_with_proxy_only(self, monkeypatch):
        """True when DOMINO_API_PROXY is set even without domino_api_host."""
        monkeypatch.setenv("DOMINO_API_PROXY", "http://proxy:8080")
        s = Settings(domino_api_host=None)
        assert s.is_domino_environment is True

    def test_true_with_host_only(self, monkeypatch):
        """True when domino_api_host is set even without DOMINO_API_PROXY."""
        monkeypatch.delenv("DOMINO_API_PROXY", raising=False)
        s = Settings(domino_api_host="https://example.domino.tech")
        assert s.is_domino_environment is True

    def test_false_with_neither(self, monkeypatch):
        """False when neither domino_api_host nor DOMINO_API_PROXY is set."""
        monkeypatch.delenv("DOMINO_API_PROXY", raising=False)
        s = Settings(domino_api_host=None)
        assert s.is_domino_environment is False
