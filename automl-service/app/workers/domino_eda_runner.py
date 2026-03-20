"""Domino Job entrypoint for async EDA profiling."""

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
    parser = argparse.ArgumentParser(description="Run AutoML EDA profile from Domino")
    parser.add_argument("--request-id", required=True)
    parser.add_argument("--mode", choices=["tabular", "timeseries"], default="tabular")
    parser.add_argument("--file-path", required=True)
    parser.add_argument("--sample-size", type=int, default=50000)
    parser.add_argument("--sampling-strategy", default="random")
    parser.add_argument("--stratify-column", default=None)
    parser.add_argument("--time-column", default=None)
    parser.add_argument("--target-column", default=None)
    parser.add_argument("--id-column", default=None)
    parser.add_argument("--rolling-window", type=int, default=None)
    parser.add_argument("--database-url", default=None, help="Override DATABASE_URL for cross-project jobs")
    parser.add_argument("--project-id", default=None, help="Target project ID for dataset file resolution")
    return parser.parse_args()


async def _run(args) -> None:
    """Async entrypoint for EDA profiling."""
    from app.dependencies import get_db_session
    from app.core.eda_job_store import get_eda_job_store
    from app.core.data_profiler import get_data_profiler
    from app.core.ts_profiler import get_ts_profiler
    from app.core.utils import remap_shared_path, ensure_local_file
    from app.db.database import create_tables

    # Ensure tables exist (the job may be first to use this DB path)
    await create_tables()

    store = get_eda_job_store()
    file_path = remap_shared_path(args.file_path)
    # Download on demand if the file isn't on the local mount (e.g. stale
    # read-only snapshot or cross-project dataset).
    file_path = await ensure_local_file(file_path, args.project_id)

    async with get_db_session() as db:
        await store.update_request(db, args.request_id, status="running")

    try:
        if args.mode == "tabular":
            result = get_data_profiler().profile_file(
                file_path=file_path,
                sample_size=args.sample_size,
                sampling_strategy=args.sampling_strategy,
                stratify_column=args.stratify_column,
            )
        else:
            if not args.time_column or not args.target_column:
                raise ValueError("time_column and target_column are required for timeseries profiling")
            result = get_ts_profiler().profile_timeseries_file(
                file_path=file_path,
                time_column=args.time_column,
                target_column=args.target_column,
                id_column=args.id_column,
                sample_size=args.sample_size,
                sampling_strategy=args.sampling_strategy,
                rolling_window=args.rolling_window,
            )

        async with get_db_session() as db:
            await store.write_result(db, args.request_id, args.mode, result)
            await store.update_request(db, args.request_id, status="completed", error=None)
    except Exception as e:
        async with get_db_session() as db:
            await store.write_error(db, args.request_id, str(e))
            await store.update_request(db, args.request_id, status="failed", error=str(e))
        raise


def main() -> None:
    """CLI entrypoint."""
    args = parse_args()
    _ensure_project_root_on_path()

    if args.database_url:
        from app.workers._db_url_remap import remap_database_url

        os.environ["DATABASE_URL"] = remap_database_url(args.database_url)

    asyncio.run(_run(args))


if __name__ == "__main__":
    main()
