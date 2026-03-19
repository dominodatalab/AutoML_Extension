"""Database connection and session management."""

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from app.config import get_settings


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""
    pass


settings = get_settings()

# Convert sqlite:/// to sqlite+aiosqlite:///
database_url = settings.database_url
if database_url.startswith("sqlite:///"):
    database_url = database_url.replace("sqlite:///", "sqlite+aiosqlite:///")

engine = create_async_engine(
    database_url,
    echo=settings.debug,
    future=True,
)

async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def create_tables():
    """Create all database tables."""
    try:
        async with engine.begin() as conn:
            # checkfirst=True is default but be explicit for multi-worker safety
            await conn.run_sync(lambda sync_conn: Base.metadata.create_all(sync_conn, checkfirst=True))
    except Exception as e:
        # Ignore "table already exists" errors from race conditions with multiple workers
        if "already exists" in str(e):
            pass
        else:
            raise

    # Run migrations to add new columns to existing tables
    await run_migrations()


async def run_migrations():
    """Add new columns to existing tables (safe for SQLite)."""
    import logging
    logger = logging.getLogger(__name__)

    migrations = [
        ("jobs", "models_trained", "INTEGER DEFAULT 0"),
        ("jobs", "current_model", "VARCHAR(255)"),
        ("jobs", "eta_seconds", "INTEGER"),
        ("jobs", "execution_target", "VARCHAR(20) DEFAULT 'local'"),
        ("jobs", "domino_job_id", "VARCHAR(255)"),
        ("jobs", "domino_job_status", "VARCHAR(100)"),
        ("jobs", "project_owner", "VARCHAR(255)"),
        ("jobs", "enable_mlflow", "BOOLEAN DEFAULT 0"),
        ("jobs", "auto_register", "BOOLEAN DEFAULT 0"),
        ("jobs", "register_name", "VARCHAR(255)"),
        ("jobs", "diagnostics_data", "JSON"),
        # EDA owner/project scoping for RBAC
        ("eda_results", "owner", "VARCHAR(255)"),
        ("eda_results", "project_id", "VARCHAR(255)"),
    ]

    async with engine.begin() as conn:
        for table, column, col_type in migrations:
            try:
                await conn.execute(
                    text(f"ALTER TABLE {table} ADD COLUMN {column} {col_type}")
                )
                logger.info(f"Added column {column} to {table}")
            except Exception as e:
                # Column already exists - that's fine
                if "duplicate column name" in str(e).lower():
                    pass
                else:
                    logger.debug(f"Migration skipped: {column} on {table} - {e}")

        # Backfill execution_target for rows created before the column existed.
        try:
            await conn.execute(
                text("UPDATE jobs SET execution_target = 'local' WHERE execution_target IS NULL")
            )
        except Exception as e:
            logger.debug(f"Migration skipped: execution_target backfill - {e}")

        try:
            await conn.execute(
                text(
                    "CREATE UNIQUE INDEX IF NOT EXISTS uq_jobs_owner_project_name_ci "
                    "ON jobs ("
                    "COALESCE(owner, ''), "
                    "COALESCE(project_id, project_name, ''), "
                    "lower(trim(name))"
                    ")"
                )
            )
        except Exception as e:
            logger.warning(
                "Migration skipped: scoped unique job-name index - %s. "
                "Existing duplicate names may need cleanup before this index can be created.",
                e,
            )


async def drop_tables():
    """Drop all database tables."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
