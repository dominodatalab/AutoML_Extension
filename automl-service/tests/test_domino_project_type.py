"""Tests for domino_project_type detection module."""
from unittest.mock import patch

from app.core.domino_project_type import detect_project_type, DominoProjectType


class TestDetectProjectType:
    """detect_project_type() probes filesystem to determine DFS vs git-based."""

    def test_dfs_when_domino_datasets_local_exists(self):
        with patch("os.path.isdir", side_effect=lambda p: p == "/domino/datasets/local"):
            assert detect_project_type() == DominoProjectType.DFS

    def test_git_when_mnt_imported_data_exists(self):
        def isdir(p):
            return p == "/mnt/imported/data"

        with patch("os.path.isdir", side_effect=isdir):
            assert detect_project_type() == DominoProjectType.GIT

    def test_git_when_mnt_data_exists(self):
        def isdir(p):
            return p == "/mnt/data"

        with patch("os.path.isdir", side_effect=isdir):
            assert detect_project_type() == DominoProjectType.GIT

    def test_unknown_when_nothing_exists(self):
        with patch("os.path.isdir", return_value=False):
            assert detect_project_type() == DominoProjectType.UNKNOWN

    def test_dfs_takes_priority_over_git(self):
        """If both DFS and git paths exist, DFS wins."""
        with patch("os.path.isdir", return_value=True):
            assert detect_project_type() == DominoProjectType.DFS
