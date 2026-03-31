"""Tests for compatibility dataset routes."""

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

pytestmark = pytest.mark.domino


def _build_compat_dataset_app(monkeypatch) -> FastAPI:
    import fastapi.dependencies.utils as fastapi_utils
    from app.api.compat.custom_datasets import register_custom_dataset_routes

    monkeypatch.setattr(fastapi_utils, "ensure_multipart_is_installed", lambda: None, raising=True)

    app = FastAPI()
    register_custom_dataset_routes(app)
    return app


@pytest.mark.asyncio
async def test_svcdatasetpreview_openapi_uses_typed_request_model(monkeypatch):
    app = _build_compat_dataset_app(monkeypatch)

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/openapi.json")

    assert response.status_code == 200
    schema = response.json()["paths"]["/svcdatasetpreview"]["post"]["requestBody"]["content"]["application/json"]["schema"]
    assert schema["$ref"] == "#/components/schemas/CompatDatasetPreviewRequest"


@pytest.mark.asyncio
async def test_svcdatasetpreview_rejects_empty_body_with_typed_model(monkeypatch):
    from app.api.compat import custom_datasets as custom_datasets_module

    app = _build_compat_dataset_app(monkeypatch)
    captured = {}

    async def fake_build_compat_dataset_preview_payload(dataset_manager, body):
        captured["dataset_manager"] = dataset_manager
        captured["body"] = body
        return {"ok": True}

    monkeypatch.setattr(
        custom_datasets_module,
        "build_compat_dataset_preview_payload",
        fake_build_compat_dataset_preview_payload,
        raising=True,
    )

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post("/svcdatasetpreview")

    assert response.status_code == 422
    assert "Field required" in response.text
    assert captured == {}
