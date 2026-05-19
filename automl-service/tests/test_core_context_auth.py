import asyncio
import ast
from pathlib import Path

import pytest


def test_set_get_and_clear_auth_header():
    from app.core.context.auth import set_request_auth_header, get_request_auth_header, get_request_auth_token

    # assert initial state is empty
    assert get_request_auth_header() is None
    assert get_request_auth_token() is None

    # set a value and read it back
    set_request_auth_header("Bearer root-token")
    assert get_request_auth_header() == "Bearer root-token"
    assert get_request_auth_token() == "root-token"

    # clear back to None
    set_request_auth_header(None)
    assert get_request_auth_header() is None
    assert get_request_auth_token() is None


@pytest.mark.asyncio
async def test_contextvar_is_per_task_isolated():
    from app.core.context.auth import set_request_auth_header, get_request_auth_header

    # Ensure the base context is clear
    set_request_auth_header(None)
    assert get_request_auth_header() is None

    async def worker(val: str):
        # each task sets its own value and should see only that value
        set_request_auth_header(val)
        await asyncio.sleep(0)
        return get_request_auth_header()

    v1, v2 = await asyncio.gather(worker("Bearer token-A"), worker("Bearer token-B"))
    assert v1 == "Bearer token-A"
    assert v2 == "Bearer token-B"

    # main context remains unchanged
    assert get_request_auth_header() is None


def test_contextvar_propagates_to_forked_processes():
    import threading
    import contextvars
    from app.core.context.auth import set_request_auth_header, get_request_auth_header

    # Set a value in the parent context
    set_request_auth_header("Bearer parent-token")

    seen: list[str | None] = []

    def worker():
        # Should see the same value as the parent when run under copied context
        seen.append(get_request_auth_header())

    # Copy the current context and run the worker inside it on a new thread
    ctx = contextvars.copy_context()
    t = threading.Thread(target=lambda: ctx.run(worker))
    t.start()
    t.join()

    assert seen == ["Bearer parent-token"]
    # Parent context remains unchanged
    assert get_request_auth_header() == "Bearer parent-token"

    # Note: thread test below covers propagation via copy_context


@pytest.mark.asyncio
async def test_run_in_executor_with_context_propagates_auth_header():
    from app.core.context.auth import set_request_auth_header, get_request_auth_header
    from app.core.context.executor import run_in_executor_with_context

    set_request_auth_header("Bearer executor-token")
    try:
        result = await run_in_executor_with_context(None, get_request_auth_header)
    finally:
        set_request_auth_header(None)

    assert result == "Bearer executor-token"


def test_direct_run_in_executor_calls_are_limited_to_context_helper():
    service_root = Path(__file__).resolve().parents[1]
    app_root = service_root / "app"
    helper_path = app_root / "core" / "context" / "executor.py"

    violations: list[str] = []
    for path in app_root.rglob("*.py"):
        if path == helper_path:
            continue

        tree = ast.parse(path.read_text(), filename=str(path))
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "run_in_executor"
            ):
                relative_path = path.relative_to(service_root)
                violations.append(f"{relative_path}:{node.lineno}")

    assert violations == [], (
        "Direct run_in_executor calls do not preserve request ContextVars. "
        "Use the context-preserving helper instead:\n"
        "from app.core.context.executor import run_in_executor_with_context\n"
        "result = await run_in_executor_with_context(None, blocking_func, *args)\n"
        f"Found direct calls at: {', '.join(violations)}"
    )
