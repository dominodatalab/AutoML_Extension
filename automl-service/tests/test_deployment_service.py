"""Tests for app.services.deployment_service helper functions."""

from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.services.deployment_service import (
    _is_valid_python_identifier,
    _safe_deployment_result,
)


# ---------------------------------------------------------------------------
# _is_valid_python_identifier
# ---------------------------------------------------------------------------


class TestIsValidPythonIdentifier:
    """Tests for the _is_valid_python_identifier helper."""

    # -- basic valid identifiers --

    @pytest.mark.parametrize(
        "name",
        [
            "predict",
            "predict_v2",
            "_predict",
            "__init",
            "a",
            "_",
            "myFunc",
            "CamelCase",
            "x1y2z3",
            "_leading_underscore",
            "ALLCAPS",
        ],
    )
    def test_valid_identifiers(self, name: str) -> None:
        assert _is_valid_python_identifier(name) is True

    # -- invalid identifiers: bad characters / structure --

    @pytest.mark.parametrize(
        "name",
        [
            "2predict",
            "predict-model",
            "",
            "has space",
            "has.dot",
            "has/slash",
            "123",
            "hello!",
            "a@b",
            "a b c",
        ],
    )
    def test_invalid_identifiers(self, name: str) -> None:
        assert _is_valid_python_identifier(name) is False

    # -- Python keywords must be rejected --

    @pytest.mark.parametrize(
        "name",
        [
            "class",
            "return",
            "import",
            "def",
            "if",
            "else",
            "for",
            "while",
            "try",
            "except",
            "finally",
            "with",
            "as",
            "yield",
            "lambda",
            "pass",
            "break",
            "continue",
            "raise",
            "from",
            "global",
            "nonlocal",
            "assert",
            "async",
            "await",
            "True",
            "False",
            "None",
            "and",
            "or",
            "not",
            "in",
            "is",
            "del",
        ],
    )
    def test_keywords_rejected(self, name: str) -> None:
        assert _is_valid_python_identifier(name) is False

    # -- Unicode letters are NOT accepted (regex is ASCII-only) --

    @pytest.mark.parametrize(
        "name",
        [
            "\u00e9cole",      # accented Latin
            "\u03b1\u03b2\u03b3",  # Greek letters
            "\u4f60\u597d",    # Chinese characters
            "caf\u00e9",       # trailing accent
            "\u00fcber",       # German u-umlaut
        ],
    )
    def test_unicode_rejected(self, name: str) -> None:
        assert _is_valid_python_identifier(name) is False

    # -- Python built-in names (print, len, etc.) are allowed --
    # The function only rejects keywords, not soft-keywords or built-ins.

    @pytest.mark.parametrize(
        "name",
        [
            "print",
            "len",
            "list",
            "dict",
            "int",
            "str",
            "type",
            "object",
            "Exception",
            "range",
        ],
    )
    def test_builtin_names_accepted(self, name: str) -> None:
        assert _is_valid_python_identifier(name) is True

    # -- Long names --

    def test_very_long_name_accepted(self) -> None:
        long_name = "a" * 1000
        assert _is_valid_python_identifier(long_name) is True

    def test_long_name_with_digits_accepted(self) -> None:
        name = "predict_" + "1234567890" * 10
        assert _is_valid_python_identifier(name) is True

    # -- Edge: single-character identifiers --

    @pytest.mark.parametrize("ch", list("abcdefghijklmnopqrstuvwxyz_"))
    def test_single_letter_valid(self, ch: str) -> None:
        assert _is_valid_python_identifier(ch) is True

    def test_single_digit_invalid(self) -> None:
        assert _is_valid_python_identifier("0") is False


# ---------------------------------------------------------------------------
# _safe_deployment_result
# ---------------------------------------------------------------------------


class TestSafeDeploymentResult:
    """Tests for the _safe_deployment_result normalizer."""

    # -- dict inputs --

    def test_dict_with_all_keys_preserved(self) -> None:
        result = _safe_deployment_result(
            {"success": True, "data": [{"id": "d1"}], "extra": "val"},
            "fallback msg",
        )
        assert result["success"] is True
        assert result["data"] == [{"id": "d1"}]
        assert result["extra"] == "val"

    def test_dict_missing_success_gets_default_false(self) -> None:
        result = _safe_deployment_result({"data": [1, 2]}, "fallback msg")
        assert result["success"] is False
        assert result["data"] == [1, 2]

    def test_dict_missing_data_gets_default_empty_list(self) -> None:
        result = _safe_deployment_result({"success": True}, "fallback msg")
        assert result["success"] is True
        assert result["data"] == []

    def test_empty_dict_gets_both_defaults(self) -> None:
        result = _safe_deployment_result({}, "fallback msg")
        assert result == {"success": False, "data": []}

    def test_dict_with_error_key_preserved(self) -> None:
        result = _safe_deployment_result(
            {"error": "something went wrong"},
            "fallback msg",
        )
        assert result["error"] == "something went wrong"
        assert result["success"] is False
        assert result["data"] == []

    def test_dict_does_not_mutate_original(self) -> None:
        original = {"success": True}
        result = _safe_deployment_result(original, "msg")
        # The result should have "data" added, but the original should not
        assert "data" in result
        assert "data" not in original

    # -- non-dict inputs --

    def test_none_returns_error_dict(self) -> None:
        result = _safe_deployment_result(None, "Invalid response")
        assert result == {
            "success": False,
            "data": [],
            "error": "Invalid response",
        }

    def test_string_returns_error_dict(self) -> None:
        result = _safe_deployment_result("some string", "bad response")
        assert result == {
            "success": False,
            "data": [],
            "error": "bad response",
        }

    def test_list_returns_error_dict(self) -> None:
        result = _safe_deployment_result([1, 2, 3], "not a dict")
        assert result == {
            "success": False,
            "data": [],
            "error": "not a dict",
        }

    def test_int_returns_error_dict(self) -> None:
        result = _safe_deployment_result(42, "invalid")
        assert result == {
            "success": False,
            "data": [],
            "error": "invalid",
        }

    def test_bool_returns_error_dict(self) -> None:
        # bool is not dict, should fall through
        result = _safe_deployment_result(True, "nope")
        assert result == {
            "success": False,
            "data": [],
            "error": "nope",
        }
