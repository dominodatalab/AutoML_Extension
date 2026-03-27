import asyncio
import pytest
from httpx import ASGITransport, AsyncClient


@pytest.mark.asyncio
async def test_parallel_requests_use_distinct_auth_values(monkeypatch, tmp_path):
    """Two parallel requests with different Authorization headers should not leak.

    The route handler calls a helper that reads the per-request Authorization
    from the ContextVar. We capture the values the helper sees and assert they
    match the two different headers sent in parallel.
    """
    # Point DB and service paths at tmp_path to avoid side effects
    db_file = tmp_path / "auth_concurrency.sqlite"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{db_file}")
    monkeypatch.setenv("MODELS_PATH", str(tmp_path / "models"))
    monkeypatch.setenv("UPLOADS_PATH", str(tmp_path / "uploads"))
    monkeypatch.setenv("DATASETS_PATH", str(tmp_path / "datasets"))
    monkeypatch.setenv("TEMP_PATH", str(tmp_path / "temp"))
    monkeypatch.setenv("EDA_RESULTS_PATH", str(tmp_path / "eda_results"))

    # Reset settings so env vars apply
    import app.config as config_module
    config_module._settings_instance = None

    import fastapi.dependencies.utils as fastapi_utils
    monkeypatch.setattr(fastapi_utils, "ensure_multipart_is_installed", lambda: None, raising=True)

    from app.main import create_app
    from app.core.context.auth import get_request_auth_header

    app = create_app()

    hits: list[str | None] = []

    def consumer() -> str | None:
        val = get_request_auth_header()
        hits.append(val)
        return val

    @app.get("/svc/v1/test/consume-auth")
    async def consume_auth():
        return {"auth": consumer()}

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        auth1 = "Bearer alpha"
        auth2 = "Bearer beta"

        async def do_req(auth_value: str):
            resp = await client.get(
                "/svc/v1/test/consume-auth",
                headers={"Authorization": auth_value},
            )
            assert resp.status_code == 200
            return resp.json()["auth"]

        # Send requests in parallel
        r1, r2 = await asyncio.gather(do_req(auth1), do_req(auth2))

    # Verify the helper saw the two distinct values and responses match
    assert r1 == auth1
    assert r2 == auth2
    assert len(hits) == 2
    assert set(hits) == {auth1, auth2}
