"""Executor helpers that preserve request context."""
from __future__ import annotations

import asyncio
from collections.abc import Callable
from concurrent.futures import Executor
from contextvars import Context, copy_context
from functools import partial
from typing import Any, TypeVar

R = TypeVar("R")


def copy_current_context() -> Context:
    return copy_context()


async def run_in_executor_with_context(
    executor: Executor | None,
    func: Callable[..., R],
    *args: Any,
    **kwargs: Any,
) -> R:
    context = copy_current_context()
    loop = asyncio.get_running_loop()

    if kwargs:
        bound_func = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, context.run, bound_func)

    return await loop.run_in_executor(executor, context.run, func, *args)
