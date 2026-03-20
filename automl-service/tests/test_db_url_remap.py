"""Tests for _db_url_remap module."""
from unittest.mock import patch

from app.core.domino_project_type import DominoProjectType
from app.workers._db_url_remap import remap_database_url


class TestRemapDatabaseUrl:
    """remap_database_url() rewrites sqlite URLs to match local mount paths."""

    def test_existing_path_returned_as_is(self):
        url = "sqlite:////mnt/data/myproject/automl.db"
        with patch("app.workers._db_url_remap.os.path.exists", return_value=True):
            assert remap_database_url(url) == url

    def test_non_sqlite_url_returned_unchanged(self):
        url = "postgresql://localhost/mydb"
        assert remap_database_url(url) == url

    def test_remap_mnt_data_to_mnt_imported_data_git_target(self):
        """Git-based target: /mnt/data/X/automl.db -> /mnt/imported/data/X/automl.db."""
        original = "sqlite:////mnt/data/myproject/automl.db"

        def exists(p):
            return p == "/mnt/imported/data/myproject/automl.db"

        with patch("app.workers._db_url_remap.os.path.exists", side_effect=exists), \
             patch("app.workers._db_url_remap.detect_project_type", return_value=DominoProjectType.GIT):
            result = remap_database_url(original)
            assert result == "sqlite:////mnt/imported/data/myproject/automl.db"

    def test_remap_mnt_data_to_domino_datasets_local_dfs_target(self):
        """DFS target: /mnt/data/X/automl.db -> /domino/datasets/local/X/automl.db."""
        original = "sqlite:////mnt/data/myproject/automl.db"

        def exists(p):
            return p == "/domino/datasets/local/myproject/automl.db"

        with patch("app.workers._db_url_remap.os.path.exists", side_effect=exists), \
             patch("app.workers._db_url_remap.detect_project_type", return_value=DominoProjectType.DFS):
            result = remap_database_url(original)
            assert result == "sqlite:////domino/datasets/local/myproject/automl.db"

    def test_no_candidate_exists_returns_original(self):
        """When no alternative mount path has the file, return the original URL."""
        original = "sqlite:////mnt/data/myproject/automl.db"

        with patch("app.workers._db_url_remap.os.path.exists", return_value=False), \
             patch("app.workers._db_url_remap.detect_project_type", return_value=DominoProjectType.GIT):
            assert remap_database_url(original) == original

    def test_remap_domino_datasets_local_to_mnt_imported_data(self):
        """DFS source path remapped to git target."""
        original = "sqlite:////domino/datasets/local/shared/automl.db"

        def exists(p):
            return p == "/mnt/imported/data/shared/automl.db"

        with patch("app.workers._db_url_remap.os.path.exists", side_effect=exists), \
             patch("app.workers._db_url_remap.detect_project_type", return_value=DominoProjectType.GIT):
            result = remap_database_url(original)
            assert result == "sqlite:////mnt/imported/data/shared/automl.db"
