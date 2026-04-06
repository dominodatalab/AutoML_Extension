"""
This file monkey patches os.environ to enable per user mlflow authorization while
in application

DO NOT ADD MORE PATCHES TO THIS FILE
"""

from __future__ import annotations

import os
from collections.abc import Iterable, Iterator, Mapping, MutableMapping

from app.core.context import auth as auth_context

MLFLOW_TRACKING_TOKEN_KEY = "MLFLOW_TRACKING_TOKEN"

class CustomEnviron(MutableMapping[str, str]):
    """
    Read through to the real os.environ, except for MLFLOW_TRACKING_TOKEN.

    Reads of MLFLOW_TRACKING_TOKEN prefer the current request's cached auth
    token. Writes still target the real backing environment.
    """

    def __init__(self, delegate: MutableMapping[str, str]):
        self._delegate = delegate

    def _visible_snapshot(self) -> dict[str, str]:
        snapshot = dict(self._delegate)
        request_token = auth_context.get_request_auth_token()
        if request_token is not None:
            snapshot[MLFLOW_TRACKING_TOKEN_KEY] = request_token
        return snapshot

    def __getitem__(self, key: str) -> str:
        if key == MLFLOW_TRACKING_TOKEN_KEY:
            request_token = auth_context.get_request_auth_token()
            if request_token is not None:
                return request_token
        return self._delegate[key]

    def __setitem__(self, key: str, value: str) -> None:
        self._delegate[key] = value

    def __delitem__(self, key: str) -> None:
        del self._delegate[key]

    def __contains__(self, key: object) -> bool:
        if key == MLFLOW_TRACKING_TOKEN_KEY and auth_context.get_request_auth_token() is not None:
            return True
        return key in self._delegate

    def __iter__(self) -> Iterator[str]:
        return iter(self._visible_snapshot())

    def __len__(self) -> int:
        return len(self._visible_snapshot())

    def get(self, key: str, default: str | None = None) -> str | None:
        try:
            return self[key]
        except KeyError:
            return default

    def keys(self):
        return self._visible_snapshot().keys()

    def values(self):
        return self._visible_snapshot().values()

    def items(self):
        return self._visible_snapshot().items()

    def update(
        self,
        other_dict: Mapping[str, str] | Iterable[tuple[str, str]] | None = None,
        **kwargs: str,
    ) -> None:
        if other_dict is not None:
            items = other_dict.items() if isinstance(other_dict, Mapping) else other_dict
            for key, value in items:
                self[key] = value

        for key, value in kwargs.items():
            self[key] = value

    _MISSING = object()

    def pop(self, key: str, default: str | object = _MISSING) -> str:
        if key in self._delegate:
            return self._delegate.pop(key)

        if default is self._MISSING:
            raise KeyError(key)
        return default  # type: ignore[return-value]

    def copy(self) -> dict[str, str]:
        return self._visible_snapshot()


original_os_environ = getattr(os, "_automl_original_environ", os.environ)
setattr(os, "_automl_original_environ", original_os_environ)


def install_monkey_patch() -> CustomEnviron:
    """Replace os.environ with the MLflow-aware wrapper once per process."""
    if isinstance(os.environ, CustomEnviron):
        return os.environ

    patched_environ = CustomEnviron(original_os_environ)
    os.environ = patched_environ
    return patched_environ


install_monkey_patch()
