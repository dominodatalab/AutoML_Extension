"""In-process job queue with concurrency limits, recovery, and graceful shutdown."""

import asyncio
import logging
from functools import lru_cache
from typing import Dict

from app.config import get_settings
from app.db.database import async_session_maker
from app.db import crud
from app.core.utils import utc_now
from app.db.models import JobStatus

logger = logging.getLogger(__name__)

# TODO do we need this complexity?
# tracks cancellation, restarts interrupted jobs, tracks shutdown state, total jobs
# some of the functionality is not necessary for remote jobs
class JobQueueManager:
    """Manages training job execution with concurrency limits.

    Uses an asyncio.Semaphore to limit concurrent training jobs and
    asyncio.Event objects for cooperative cancellation.
    """

    def __init__(self, max_concurrent: int):
        self._max_concurrent = max_concurrent
        self._semaphore = asyncio.Semaphore(max_concurrent)
        self._tasks: Dict[str, asyncio.Task] = {}
        self._cancel_events: Dict[str, asyncio.Event] = {}
        self._lock = asyncio.Lock()
        self._shutting_down = False

    async def startup(self):
        """Recover interrupted jobs on server restart.

        Resets any RUNNING jobs to PENDING (they were interrupted by the
        previous shutdown), then re-enqueues all PENDING jobs in FIFO order.
        """
        async with async_session_maker() as db:
            # Reset RUNNING → PENDING (interrupted by restart)
            running_jobs = await crud.get_jobs_by_statuses(
                db,
                [JobStatus.RUNNING],
                execution_target="local",
            )
            for job in running_jobs:
                await crud.update_job_status(db, job.id, JobStatus.PENDING)
                await crud.update_job_progress(
                    db, job.id, progress=0, current_step="Waiting for queue slot"
                )
                logger.info(f"Recovering interrupted job: {job.id} ({job.name})")

            # Re-enqueue all PENDING jobs in FIFO order
            pending_jobs = await crud.get_jobs_by_statuses(
                db,
                [JobStatus.PENDING],
                execution_target="local",
            )
            for job in pending_jobs:
                await self.enqueue(job.id)
                logger.info(f"Re-enqueued pending job: {job.id} ({job.name})")

        logger.info(
            f"Job queue started (max concurrent: {self._max_concurrent})"
        )

    async def enqueue(self, job_id: str):
        """Enqueue a job for execution.

        Creates an asyncio.Task that waits on the semaphore before running
        the training job. While waiting, the job's current_step is set to
        "Waiting for queue slot".
        """
        async with self._lock:
            if job_id in self._tasks:
                logger.warning(f"Job {job_id} already enqueued, skipping")
                return

            cancel_event = asyncio.Event()
            self._cancel_events[job_id] = cancel_event

            task = asyncio.create_task(
                self._run_with_semaphore(job_id, cancel_event),
                name=f"training-{job_id}",
            )
            self._tasks[job_id] = task
            task.add_done_callback(
                lambda t, jid=job_id: asyncio.create_task(self._on_task_done(jid))
            )

        logger.info(f"Job {job_id} enqueued")

    async def cancel(self, job_id: str) -> bool:
        """Cancel a job, whether queued or running.

        Returns True if a task was found and cancelled.
        """
        async with self._lock:
            cancel_event = self._cancel_events.get(job_id)
            task = self._tasks.get(job_id)

        if not task:
            return False

        # Set the cancel event so checkpoints can detect it
        if cancel_event:
            cancel_event.set()

        # Cancel the asyncio task (wakes it from semaphore wait or sleep)
        task.cancel()
        logger.info(f"Cancel requested for job {job_id}")
        return True

    async def shutdown(self, timeout: float = 30.0):
        """Gracefully shut down the queue.

        Cancels all tasks and waits up to `timeout` seconds for them to finish.
        Any jobs still RUNNING after timeout are reset to PENDING for recovery
        on next startup.
        """
        self._shutting_down = True
        logger.info("Job queue shutting down...")

        async with self._lock:
            tasks = list(self._tasks.values())
            for event in self._cancel_events.values():
                event.set()
            for task in tasks:
                task.cancel()

        if tasks:
            done, pending = await asyncio.wait(tasks, timeout=timeout)
            if pending:
                logger.warning(
                    f"{len(pending)} tasks did not finish within {timeout}s"
                )

        # Mark any still-RUNNING jobs as PENDING for next-restart recovery
        async with async_session_maker() as db:
            running_jobs = await crud.get_jobs_by_statuses(
                db,
                [JobStatus.RUNNING],
                execution_target="local",
            )
            for job in running_jobs:
                await crud.update_job_status(db, job.id, JobStatus.PENDING)
                await crud.update_job_progress(
                    db, job.id, progress=0,
                    current_step="Interrupted by shutdown"
                )
                logger.info(f"Reset job {job.id} to PENDING for recovery")

        logger.info("Job queue shutdown complete")

    def get_total_tracked(self) -> int:
        """Return count of all active tasks (running + queued)."""
        return sum(1 for t in self._tasks.values() if not t.done())

    def get_queue_status(self) -> dict:
        """Return current queue status."""
        total_active = sum(1 for t in self._tasks.values() if not t.done())
        # Semaphore._value = available slots; consumed slots = running jobs
        available_slots = self._semaphore._value
        running = self._max_concurrent - available_slots
        queued = total_active - running

        return {
            "max_concurrent_jobs": self._max_concurrent,
            "running_jobs": max(running, 0),
            "queued_jobs": max(queued, 0),
            "total_tracked": total_active,
            "shutting_down": self._shutting_down,
        }

    def is_job_cancelled(self, job_id: str) -> bool:
        """Check whether a job's cancel event has been set."""
        event = self._cancel_events.get(job_id)
        return event.is_set() if event else False

    async def _run_with_semaphore(self, job_id: str, cancel_event: asyncio.Event):
        """Acquire a semaphore slot, then run the training job."""
        try:
            # Update status to show queued
            async with async_session_maker() as db:
                await crud.update_job_progress(
                    db, job_id, progress=0,
                    current_step="Waiting for queue slot"
                )

            # Wait for a semaphore slot (blocks if max concurrent reached)
            await self._semaphore.acquire()

            try:
                # Check if cancelled while waiting in queue
                if cancel_event.is_set():
                    logger.info(f"Job {job_id} cancelled while queued")
                    async with async_session_maker() as db:
                        job = await crud.get_job(db, job_id)
                        if job and job.status not in (
                            JobStatus.COMPLETED,
                            JobStatus.FAILED,
                            JobStatus.CANCELLED,
                        ):
                            await crud.update_job_status(
                                db, job_id, JobStatus.CANCELLED,
                                completed_at=utc_now(),
                            )
                    return

                # Lazy import to avoid circular imports
                from app.workers.training_worker import run_training_job

                await run_training_job(job_id)
            finally:
                self._semaphore.release()

        except asyncio.CancelledError:
            logger.info(f"Job {job_id} task cancelled")
            async with async_session_maker() as db:
                job = await crud.get_job(db, job_id)
                if job and job.status not in (
                    JobStatus.COMPLETED,
                    JobStatus.FAILED,
                    JobStatus.CANCELLED,
                ):
                    await crud.update_job_status(
                        db, job_id, JobStatus.CANCELLED,
                        completed_at=utc_now(),
                    )
            raise  # Re-raise so the Task is properly marked cancelled

    async def _on_task_done(self, job_id: str):
        """Clean up tracking dicts after a task completes."""
        async with self._lock:
            self._tasks.pop(job_id, None)
            self._cancel_events.pop(job_id, None)


@lru_cache()
def get_job_queue() -> JobQueueManager:
    """Get the global job queue manager (cached singleton)."""
    settings = get_settings()
    return JobQueueManager(max_concurrent=settings.max_concurrent_jobs)
