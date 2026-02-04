"""Domino Model API entry point.

This module provides the entry point for running the AutoML service
as a Domino Model API or standalone FastAPI server.
"""

import uvicorn

from app.main import app


def predict(data: dict) -> dict:
    """
    Domino Model API prediction function.

    This function is called by Domino when the model API receives a request.
    For the AutoML service, this acts as a pass-through to the FastAPI app.

    Args:
        data: Request data containing the API endpoint and payload.

    Returns:
        API response.
    """
    # This is a placeholder for Domino Model API integration
    # In practice, the FastAPI app handles all routing
    return {
        "message": "Use the FastAPI endpoints directly",
        "docs": "/docs",
        "health": "/api/v1/health",
    }


if __name__ == "__main__":
    # Run the FastAPI server directly for local development
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
