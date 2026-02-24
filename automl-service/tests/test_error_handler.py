"""Tests for the handle_errors decorator (app/api/error_handler.py)."""

from pathlib import Path
import sys

import pytest
from fastapi import HTTPException

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.api.error_handler import handle_errors


# ---------------------------------------------------------------------------
# Helpers: decorated sync and async functions that raise on command
# ---------------------------------------------------------------------------


@handle_errors()
async def _async_raiser(exc: Exception = None, value: str = "ok"):
    if exc:
        raise exc
    return value


@handle_errors()
def _sync_raiser(exc: Exception = None, value: str = "ok"):
    if exc:
        raise exc
    return value


@handle_errors(detail_prefix="Prefix")
async def _async_with_prefix(exc: Exception = None):
    if exc:
        raise exc
    return "ok"


@handle_errors(detail_prefix="Prefix")
def _sync_with_prefix(exc: Exception = None):
    if exc:
        raise exc
    return "ok"


@handle_errors(error_message_prefix="custom-log-prefix")
async def _async_custom_log(exc: Exception = None):
    if exc:
        raise exc
    return "ok"


# ---------------------------------------------------------------------------
# Async function tests
# ---------------------------------------------------------------------------


class TestAsyncHandleErrors:
    """Tests for async functions wrapped with @handle_errors."""

    @pytest.mark.asyncio
    async def test_success_passthrough(self):
        result = await _async_raiser(value="hello")
        assert result == "hello"

    @pytest.mark.asyncio
    async def test_http_exception_passthrough(self):
        """HTTPException should be re-raised as-is, not wrapped."""
        original = HTTPException(status_code=418, detail="I'm a teapot")
        with pytest.raises(HTTPException) as exc_info:
            await _async_raiser(exc=original)
        assert exc_info.value.status_code == 418
        assert exc_info.value.detail == "I'm a teapot"

    @pytest.mark.asyncio
    async def test_file_not_found_becomes_404(self):
        with pytest.raises(HTTPException) as exc_info:
            await _async_raiser(exc=FileNotFoundError("missing.csv"))
        assert exc_info.value.status_code == 404
        assert "missing.csv" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_value_error_becomes_400(self):
        with pytest.raises(HTTPException) as exc_info:
            await _async_raiser(exc=ValueError("bad input"))
        assert exc_info.value.status_code == 400
        assert "bad input" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_generic_exception_becomes_500(self):
        with pytest.raises(HTTPException) as exc_info:
            await _async_raiser(exc=RuntimeError("unexpected"))
        assert exc_info.value.status_code == 500
        assert "unexpected" in exc_info.value.detail


# ---------------------------------------------------------------------------
# Sync function tests
# ---------------------------------------------------------------------------


class TestSyncHandleErrors:
    """Tests for sync functions wrapped with @handle_errors."""

    def test_success_passthrough(self):
        result = _sync_raiser(value="hello")
        assert result == "hello"

    def test_http_exception_passthrough(self):
        original = HTTPException(status_code=403, detail="forbidden")
        with pytest.raises(HTTPException) as exc_info:
            _sync_raiser(exc=original)
        assert exc_info.value.status_code == 403
        assert exc_info.value.detail == "forbidden"

    def test_file_not_found_becomes_404(self):
        with pytest.raises(HTTPException) as exc_info:
            _sync_raiser(exc=FileNotFoundError("gone.csv"))
        assert exc_info.value.status_code == 404
        assert "gone.csv" in exc_info.value.detail

    def test_value_error_becomes_400(self):
        with pytest.raises(HTTPException) as exc_info:
            _sync_raiser(exc=ValueError("invalid"))
        assert exc_info.value.status_code == 400
        assert "invalid" in exc_info.value.detail

    def test_generic_exception_becomes_500(self):
        with pytest.raises(HTTPException) as exc_info:
            _sync_raiser(exc=TypeError("boom"))
        assert exc_info.value.status_code == 500
        assert "boom" in exc_info.value.detail


# ---------------------------------------------------------------------------
# detail_prefix tests
# ---------------------------------------------------------------------------


class TestDetailPrefix:
    """Verify detail_prefix is prepended to error details for all error types."""

    @pytest.mark.asyncio
    async def test_prefix_on_file_not_found_async(self):
        with pytest.raises(HTTPException) as exc_info:
            await _async_with_prefix(exc=FileNotFoundError("no-file"))
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "Prefix: no-file"

    @pytest.mark.asyncio
    async def test_prefix_on_value_error_async(self):
        with pytest.raises(HTTPException) as exc_info:
            await _async_with_prefix(exc=ValueError("bad"))
        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == "Prefix: bad"

    @pytest.mark.asyncio
    async def test_prefix_on_generic_error_async(self):
        with pytest.raises(HTTPException) as exc_info:
            await _async_with_prefix(exc=RuntimeError("oops"))
        assert exc_info.value.status_code == 500
        assert exc_info.value.detail == "Prefix: oops"

    @pytest.mark.asyncio
    async def test_prefix_not_applied_to_http_exception(self):
        """HTTPException is re-raised verbatim; prefix has no effect."""
        original = HTTPException(status_code=409, detail="conflict")
        with pytest.raises(HTTPException) as exc_info:
            await _async_with_prefix(exc=original)
        assert exc_info.value.detail == "conflict"

    def test_prefix_on_file_not_found_sync(self):
        with pytest.raises(HTTPException) as exc_info:
            _sync_with_prefix(exc=FileNotFoundError("nope"))
        assert exc_info.value.detail == "Prefix: nope"

    def test_prefix_on_value_error_sync(self):
        with pytest.raises(HTTPException) as exc_info:
            _sync_with_prefix(exc=ValueError("wrong"))
        assert exc_info.value.detail == "Prefix: wrong"

    def test_prefix_on_generic_error_sync(self):
        with pytest.raises(HTTPException) as exc_info:
            _sync_with_prefix(exc=RuntimeError("fail"))
        assert exc_info.value.detail == "Prefix: fail"


# ---------------------------------------------------------------------------
# Log prefix / function name tests
# ---------------------------------------------------------------------------


class TestLogPrefix:
    """Verify the log prefix defaults to the function name."""

    @pytest.mark.asyncio
    async def test_default_log_prefix_uses_function_name(self, caplog):
        """When no error_message_prefix is given, the function name is used."""
        with pytest.raises(HTTPException):
            await _async_raiser(exc=RuntimeError("log-test"))
        # The logger uses the function name as prefix
        assert any("_async_raiser" in record.message for record in caplog.records)

    @pytest.mark.asyncio
    async def test_custom_log_prefix(self, caplog):
        """When error_message_prefix is given, it appears in the log."""
        with pytest.raises(HTTPException):
            await _async_custom_log(exc=RuntimeError("custom-log-test"))
        assert any(
            "custom-log-prefix" in record.message for record in caplog.records
        )


# ---------------------------------------------------------------------------
# Wrapper preserves function metadata
# ---------------------------------------------------------------------------


class TestFunctools:
    """Verify functools.wraps preserves the original function metadata."""

    def test_async_wrapper_preserves_name(self):
        assert _async_raiser.__name__ == "_async_raiser"

    def test_sync_wrapper_preserves_name(self):
        assert _sync_raiser.__name__ == "_sync_raiser"
