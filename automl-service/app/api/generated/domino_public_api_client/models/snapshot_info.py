from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.snapshot_info_repo_type import SnapshotInfoRepoType

T = TypeVar("T", bound="SnapshotInfo")


@_attrs_define
class SnapshotInfo:
    """
    Attributes:
        packages (list[str]): List of packages with their resolved versions (e.g., ["ggplot2==3.5.0", "dplyr==1.2.0"])
        repo (str): Repository name (e.g., "validated-cran-repo")
        repo_type (SnapshotInfoRepoType): Repository type (R for CRAN, Bioconductor for Bioconductor, Python for PyPI)
        snapshot (str): Snapshot date (e.g., "20171010")
    """

    packages: list[str]
    repo: str
    repo_type: SnapshotInfoRepoType
    snapshot: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        packages = self.packages

        repo = self.repo

        repo_type = self.repo_type.value

        snapshot = self.snapshot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "packages": packages,
                "repo": repo,
                "repoType": repo_type,
                "snapshot": snapshot,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        packages = cast(list[str], d.pop("packages"))

        repo = d.pop("repo")

        repo_type = SnapshotInfoRepoType(d.pop("repoType"))

        snapshot = d.pop("snapshot")

        snapshot_info = cls(
            packages=packages,
            repo=repo,
            repo_type=repo_type,
            snapshot=snapshot,
        )

        snapshot_info.additional_properties = d
        return snapshot_info

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
