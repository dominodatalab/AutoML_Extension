"""Tests for app.config (Settings, sanitize_project_name) and _is_truthy.

_is_truthy lives in app.main, but importing that module pulls in the full
FastAPI app (including the ``domino`` SDK).  To keep tests lightweight we
extract the function via importlib without executing the module top-level.
"""

import ast
import importlib
import os
import textwrap
import tempfile
import types
from typing import Optional
from unittest.mock import patch

import pytest

from app.config import Settings, sanitize_project_name


# ---------------------------------------------------------------------------
# Extract _is_truthy from app/main.py without triggering full module import
# ---------------------------------------------------------------------------

def _load_is_truthy():
    """Parse _is_truthy from source to avoid importing the full app.main module."""
    import pathlib
    main_path = pathlib.Path(__file__).resolve().parents[1] / "app" / "main.py"
    source = main_path.read_text()
    tree = ast.parse(source)

    # Find the function definition
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "_is_truthy":
            func_source = ast.get_source_segment(source, node)
            break
    else:
        raise RuntimeError("Could not find _is_truthy in app/main.py")

    # Compile and execute in an isolated namespace
    ns: dict = {"Optional": Optional}
    exec(compile(func_source, "<_is_truthy>", "exec"), ns)
    return ns["_is_truthy"]


_is_truthy = _load_is_truthy()


class TestIsTruthy:
    """Test the _is_truthy helper used for env-var parsing."""

    @pytest.mark.parametrize(
        "value, expected",
        [
            ("1", True),
            ("true", True),
            ("True", True),
            ("TRUE", True),
            ("yes", True),
            ("Yes", True),
            ("y", True),
            ("Y", True),
            ("on", True),
            ("ON", True),
            # With surrounding whitespace
            ("  true  ", True),
            (" 1 ", True),
        ],
    )
    def test_truthy_values(self, value, expected):
        assert _is_truthy(value) is expected

    @pytest.mark.parametrize(
        "value",
        ["0", "false", "False", "no", "off", "", "random", "2", "enabled"],
    )
    def test_falsy_values(self, value):
        assert _is_truthy(value) is False

    def test_none(self):
        assert _is_truthy(None) is False


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
# Settings.effective_api_key
# ---------------------------------------------------------------------------


class TestEffectiveApiKey:
    """Test the effective_api_key property and its priority chain."""

    def test_domino_api_key_first_priority(self):
        """domino_api_key takes highest priority."""
        s = Settings(
            domino_api_key="key-a",
            domino_user_api_key="key-b",
        )
        assert s.effective_api_key == "key-a"

    def test_domino_user_api_key_second_priority(self):
        """domino_user_api_key is used when domino_api_key is absent."""
        s = Settings(
            domino_api_key=None,
            domino_user_api_key="key-b",
        )
        assert s.effective_api_key == "key-b"

    def test_token_file_third_priority(self, monkeypatch, tmp_path):
        """Falls back to reading DOMINO_TOKEN_FILE when both keys are absent."""
        token_file = tmp_path / "token"
        token_file.write_text("file-token-123")
        monkeypatch.setenv("DOMINO_TOKEN_FILE", str(token_file))

        s = Settings(domino_api_key=None, domino_user_api_key=None)
        assert s.effective_api_key == "file-token-123"

    def test_token_file_strips_whitespace(self, monkeypatch, tmp_path):
        """Token file contents should be stripped of whitespace."""
        token_file = tmp_path / "token"
        token_file.write_text("  my-token  \n")
        monkeypatch.setenv("DOMINO_TOKEN_FILE", str(token_file))

        s = Settings(domino_api_key=None, domino_user_api_key=None)
        assert s.effective_api_key == "my-token"

    def test_empty_token_file_returns_none(self, monkeypatch, tmp_path):
        """An empty token file should result in None."""
        token_file = tmp_path / "token"
        token_file.write_text("   ")
        monkeypatch.setenv("DOMINO_TOKEN_FILE", str(token_file))

        s = Settings(domino_api_key=None, domino_user_api_key=None)
        assert s.effective_api_key is None

    def test_missing_token_file_returns_none(self, monkeypatch):
        """A non-existent token file should result in None (OSError caught)."""
        monkeypatch.setenv("DOMINO_TOKEN_FILE", "/nonexistent/path/token")

        s = Settings(domino_api_key=None, domino_user_api_key=None)
        assert s.effective_api_key is None

    def test_no_token_file_env_returns_none(self, monkeypatch):
        """When DOMINO_TOKEN_FILE is not set and no keys, return None."""
        monkeypatch.delenv("DOMINO_TOKEN_FILE", raising=False)

        s = Settings(domino_api_key=None, domino_user_api_key=None)
        assert s.effective_api_key is None

    def test_api_key_preferred_over_token_file(self, monkeypatch, tmp_path):
        """domino_api_key wins even when DOMINO_TOKEN_FILE exists."""
        token_file = tmp_path / "token"
        token_file.write_text("file-token")
        monkeypatch.setenv("DOMINO_TOKEN_FILE", str(token_file))

        s = Settings(domino_api_key="direct-key", domino_user_api_key=None)
        assert s.effective_api_key == "direct-key"


# ---------------------------------------------------------------------------
# Settings.is_domino_environment
# ---------------------------------------------------------------------------


class TestIsDominoEnvironment:
    """Test the is_domino_environment property."""

    def test_true_with_host_and_api_key(self, monkeypatch):
        """True when domino_api_host and an API key are present."""
        monkeypatch.delenv("DOMINO_API_PROXY", raising=False)
        s = Settings(
            domino_api_host="https://example.domino.tech",
            domino_api_key="some-key",
        )
        assert s.is_domino_environment is True

    def test_true_with_host_and_proxy(self, monkeypatch):
        """True when domino_api_host and DOMINO_API_PROXY env are set."""
        monkeypatch.setenv("DOMINO_API_PROXY", "http://proxy:8080")
        s = Settings(
            domino_api_host="https://example.domino.tech",
            domino_api_key=None,
            domino_user_api_key=None,
        )
        assert s.is_domino_environment is True

    def test_false_without_host(self, monkeypatch):
        """False when domino_api_host is not set, even with keys."""
        monkeypatch.delenv("DOMINO_API_PROXY", raising=False)
        s = Settings(
            domino_api_host=None,
            domino_api_key="some-key",
        )
        assert s.is_domino_environment is False

    def test_false_without_auth(self, monkeypatch):
        """False when host is set but neither proxy nor key auth exists."""
        monkeypatch.delenv("DOMINO_API_PROXY", raising=False)
        monkeypatch.delenv("DOMINO_TOKEN_FILE", raising=False)
        s = Settings(
            domino_api_host="https://example.domino.tech",
            domino_api_key=None,
            domino_user_api_key=None,
        )
        assert s.is_domino_environment is False

    def test_true_with_host_and_user_api_key(self, monkeypatch):
        """True when using the legacy domino_user_api_key."""
        monkeypatch.delenv("DOMINO_API_PROXY", raising=False)
        s = Settings(
            domino_api_host="https://example.domino.tech",
            domino_api_key=None,
            domino_user_api_key="user-key",
        )
        assert s.is_domino_environment is True

    def test_true_with_host_and_token_file(self, monkeypatch, tmp_path):
        """True when using a token file for auth."""
        monkeypatch.delenv("DOMINO_API_PROXY", raising=False)
        token_file = tmp_path / "token"
        token_file.write_text("my-token")
        monkeypatch.setenv("DOMINO_TOKEN_FILE", str(token_file))

        s = Settings(
            domino_api_host="https://example.domino.tech",
            domino_api_key=None,
            domino_user_api_key=None,
        )
        assert s.is_domino_environment is True
