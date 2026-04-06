import importlib
import os

import pytest

from app.core.context.auth import set_request_auth_header


@pytest.fixture()
def patched_environ(monkeypatch):
    import app.run_monkey_patching as run_monkey_patching

    original = run_monkey_patching.original_os_environ
    monkeypatch.setattr(os, "environ", original, raising=True)
    monkeypatch.setattr(os, "_automl_original_environ", original, raising=False)

    module = importlib.reload(run_monkey_patching)
    try:
        yield module
    finally:
        set_request_auth_header(None)


def test_import_installs_custom_environ_wrapper(patched_environ):
    assert isinstance(os.environ, patched_environ.CustomEnviron)
    assert patched_environ.install_monkey_patch() is os.environ


def test_mlflow_tracking_token_uses_request_bearer_token(monkeypatch, patched_environ):
    """
    Tests square brackets, get()
    """
    monkeypatch.delenv(patched_environ.MLFLOW_TRACKING_TOKEN_KEY, raising=False)

    set_request_auth_header("Bearer request-token")

    assert os.environ[patched_environ.MLFLOW_TRACKING_TOKEN_KEY] == "request-token"
    assert os.environ.get(patched_environ.MLFLOW_TRACKING_TOKEN_KEY) == "request-token"


def test_mlflow_tracking_token_falls_back_to_real_environment(monkeypatch, patched_environ):
    """
    If the MLFLOW_TRACKING_TOKEN virtual key doesn't have a value, we fallback to the origin value. This
    should allow mlflow actions in executions to still work
    """
    set_request_auth_header(None)
    monkeypatch.setenv(patched_environ.MLFLOW_TRACKING_TOKEN_KEY, "env-token")

    assert os.environ[patched_environ.MLFLOW_TRACKING_TOKEN_KEY] == "env-token"
    assert os.environ.get(patched_environ.MLFLOW_TRACKING_TOKEN_KEY, "missing") == "env-token"


def test_visible_mapping_includes_request_token_overlay(monkeypatch, patched_environ):
    """
    Tests items(), keys()
    """
    monkeypatch.delenv(patched_environ.MLFLOW_TRACKING_TOKEN_KEY, raising=False)
    set_request_auth_header("Bearer overlay-token")

    visible = dict(os.environ.items())

    assert patched_environ.MLFLOW_TRACKING_TOKEN_KEY in os.environ
    assert visible[patched_environ.MLFLOW_TRACKING_TOKEN_KEY] == "overlay-token"
    assert patched_environ.MLFLOW_TRACKING_TOKEN_KEY in os.environ.keys()


def test_len_counts_request_token_overlay(monkeypatch, patched_environ):
    """
    Tests len()
    """
    monkeypatch.delenv(patched_environ.MLFLOW_TRACKING_TOKEN_KEY, raising=False)
    set_request_auth_header("Bearer overlay-token")

    assert len(os.environ) == len(patched_environ.original_os_environ) + 1


def test_iterating_over_environ_includes_request_token_overlay(monkeypatch, patched_environ):
    """
    Tests iterating over dictionary
    """
    monkeypatch.delenv(patched_environ.MLFLOW_TRACKING_TOKEN_KEY, raising=False)
    set_request_auth_header("Bearer overlay-token")

    iterated_keys = set(os.environ)

    assert patched_environ.MLFLOW_TRACKING_TOKEN_KEY in iterated_keys


def test_update_and_pop_delegate_to_backing_environment(monkeypatch, patched_environ):
    """
    Tests update(), pop(), membership testing
    """
    key = "AUTOML_TEST_ENV_KEY"
    monkeypatch.delenv(key, raising=False)

    os.environ.update({key: "value"})

    assert patched_environ.original_os_environ[key] == "value"
    assert os.environ.pop(key) == "value"
    assert key not in patched_environ.original_os_environ


def test_delitem_deletes_backing_environment_entry(monkeypatch, patched_environ):
    """
    Tests delete
    """
    key = "AUTOML_TEST_DELETE_KEY"
    monkeypatch.setenv(key, "value")

    del os.environ[key]

    assert key not in patched_environ.original_os_environ


def test_delitem_on_mlflow_tracking_token_deletes_real_env_only(monkeypatch, patched_environ):
    """
    Verifies that you can't delete the MLFLOW_TRACKING_TOKEN virtual key
    """
    monkeypatch.setenv(patched_environ.MLFLOW_TRACKING_TOKEN_KEY, "env-token")
    set_request_auth_header("Bearer request-token")

    del os.environ[patched_environ.MLFLOW_TRACKING_TOKEN_KEY]

    assert patched_environ.MLFLOW_TRACKING_TOKEN_KEY not in patched_environ.original_os_environ
    assert os.environ[patched_environ.MLFLOW_TRACKING_TOKEN_KEY] == "request-token"
