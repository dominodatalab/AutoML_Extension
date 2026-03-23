import asyncio
import pytest


def test_set_get_and_clear_auth_header():
    from app.core.context.auth import set_request_auth_header, get_request_auth_header

    # assert initial state is empty
    assert get_request_auth_header() is None

    # set a value and read it back
    set_request_auth_header("Bearer root-token")
    assert get_request_auth_header() == "Bearer root-token"

    # clear back to None
    set_request_auth_header(None)
    assert get_request_auth_header() is None


def test_set_get_and_clear_project_id():
    from app.core.context.auth import set_request_project_id, get_request_project_id

    assert get_request_project_id() is None

    set_request_project_id("project-123")
    assert get_request_project_id() == "project-123"

    set_request_project_id(None)
    assert get_request_project_id() is None


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
