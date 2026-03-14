"""Domino Job entrypoint for external AutoML training execution."""

import argparse
import asyncio
import os
import sys
from pathlib import Path


def _ensure_project_root_on_path() -> None:
    """Ensure the repository root is importable when run as a Domino Job."""
    current_file = Path(__file__).resolve()
    project_root = current_file.parents[2]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    os.chdir(project_root)


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="Run AutoML training job from Domino")
    parser.add_argument("--job-id", required=True, help="AutoML job id")
    parser.add_argument("--database-url", default=None, help="Override DATABASE_URL for cross-project jobs")
    return parser.parse_args()


def main() -> None:
    """CLI entrypoint."""
    args = parse_args()
    _ensure_project_root_on_path()

    if args.database_url:
        os.environ["DATABASE_URL"] = args.database_url

    from app.workers.training_worker import run_training_job

    asyncio.run(run_training_job(args.job_id))


if __name__ == "__main__":
    main()
