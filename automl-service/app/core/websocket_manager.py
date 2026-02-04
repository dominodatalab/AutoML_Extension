"""WebSocket connection manager for real-time training progress."""

import asyncio
import json
import logging
from typing import Dict, Set
from fastapi import WebSocket

logger = logging.getLogger(__name__)


class ConnectionManager:
    """Manages WebSocket connections for real-time job progress updates."""

    def __init__(self):
        # Map job_id -> set of connected WebSocket clients
        self.active_connections: Dict[str, Set[WebSocket]] = {}
        # Lock for thread-safe operations
        self._lock = asyncio.Lock()

    async def connect(self, websocket: WebSocket, job_id: str):
        """Accept a WebSocket connection and register it for a job."""
        await websocket.accept()
        async with self._lock:
            if job_id not in self.active_connections:
                self.active_connections[job_id] = set()
            self.active_connections[job_id].add(websocket)
            logger.info(f"WebSocket connected for job {job_id}. Total connections: {len(self.active_connections[job_id])}")

    async def disconnect(self, websocket: WebSocket, job_id: str):
        """Remove a WebSocket connection."""
        async with self._lock:
            if job_id in self.active_connections:
                self.active_connections[job_id].discard(websocket)
                if not self.active_connections[job_id]:
                    del self.active_connections[job_id]
                logger.info(f"WebSocket disconnected for job {job_id}")

    async def send_progress(self, job_id: str, data: dict):
        """Send progress update to all clients watching a job."""
        async with self._lock:
            connections = self.active_connections.get(job_id, set()).copy()

        if not connections:
            return

        message = json.dumps(data)
        disconnected = set()

        for websocket in connections:
            try:
                await websocket.send_text(message)
            except Exception as e:
                logger.warning(f"Failed to send to WebSocket: {e}")
                disconnected.add(websocket)

        # Clean up disconnected sockets
        if disconnected:
            async with self._lock:
                if job_id in self.active_connections:
                    self.active_connections[job_id] -= disconnected

    async def broadcast_job_update(
        self,
        job_id: str,
        status: str,
        progress: int,
        current_step: str = None,
        models_trained: int = 0,
        current_model: str = None,
        eta_seconds: int = None,
        metrics: dict = None,
        leaderboard: list = None,
        error_message: str = None,
    ):
        """Broadcast a job progress update to all connected clients."""
        data = {
            "type": "progress",
            "job_id": job_id,
            "status": status,
            "progress": progress,
            "current_step": current_step,
            "models_trained": models_trained,
            "current_model": current_model,
            "eta_seconds": eta_seconds,
        }

        if metrics:
            data["metrics"] = metrics
        if leaderboard:
            data["leaderboard"] = leaderboard
        if error_message:
            data["error_message"] = error_message

        await self.send_progress(job_id, data)

    async def broadcast_log(self, job_id: str, level: str, message: str):
        """Broadcast a log message to all connected clients."""
        data = {
            "type": "log",
            "job_id": job_id,
            "level": level,
            "message": message,
        }
        await self.send_progress(job_id, data)

    async def broadcast_model_trained(
        self,
        job_id: str,
        model_name: str,
        score: float,
        fit_time: float,
        rank: int,
    ):
        """Broadcast when a new model is trained."""
        data = {
            "type": "model_trained",
            "job_id": job_id,
            "model_name": model_name,
            "score": score,
            "fit_time": fit_time,
            "rank": rank,
        }
        await self.send_progress(job_id, data)

    async def broadcast_completion(
        self,
        job_id: str,
        success: bool,
        metrics: dict = None,
        leaderboard: list = None,
        error_message: str = None,
    ):
        """Broadcast job completion."""
        data = {
            "type": "completed",
            "job_id": job_id,
            "success": success,
        }

        if metrics:
            data["metrics"] = metrics
        if leaderboard:
            data["leaderboard"] = leaderboard
        if error_message:
            data["error_message"] = error_message

        await self.send_progress(job_id, data)

    def get_connection_count(self, job_id: str = None) -> int:
        """Get the number of active connections."""
        if job_id:
            return len(self.active_connections.get(job_id, set()))
        return sum(len(conns) for conns in self.active_connections.values())


# Global singleton instance
_manager = None


def get_websocket_manager() -> ConnectionManager:
    """Get the global WebSocket connection manager."""
    global _manager
    if _manager is None:
        _manager = ConnectionManager()
    return _manager
