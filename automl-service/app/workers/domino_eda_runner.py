"""Domino Job entrypoint for async EDA profiling."""

import argparse
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
    return parser.parse_args()


def main() -> None:
    """CLI entrypoint."""
    args = parse_args()
    _ensure_project_root_on_path()

    from app.core.data_profiler import get_data_profiler
    from app.core.eda_job_store import get_eda_job_store
    from app.core.ts_profiler import get_ts_profiler
    from app.core.utils import remap_shared_path

    file_path = remap_shared_path(args.file_path)

    store = get_eda_job_store()
    store.update_request(args.request_id, status="running")

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

        store.write_result(args.request_id, args.mode, result)
        store.update_request(args.request_id, status="completed", error=None)
    except Exception as e:
        error_message = str(e)
        store.write_error(args.request_id, error_message)
        store.update_request(args.request_id, status="failed", error=error_message)
        raise


if __name__ == "__main__":
    main()
