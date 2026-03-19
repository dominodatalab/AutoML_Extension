from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.repo_status import RepoStatus
    from ..models.snapshot_info import SnapshotInfo


T = TypeVar("T", bound="SearchResponse")


@_attrs_define
class SearchResponse:
    """
    Attributes:
        repos (list[RepoStatus]):
        snapshots (list[SnapshotInfo]):
    """

    repos: list[RepoStatus]
    snapshots: list[SnapshotInfo]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repos = []
        for repos_item_data in self.repos:
            repos_item = repos_item_data.to_dict()
            repos.append(repos_item)

        snapshots = []
        for snapshots_item_data in self.snapshots:
            snapshots_item = snapshots_item_data.to_dict()
            snapshots.append(snapshots_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repos": repos,
                "snapshots": snapshots,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repo_status import RepoStatus
        from ..models.snapshot_info import SnapshotInfo

        d = dict(src_dict)
        repos = []
        _repos = d.pop("repos")
        for repos_item_data in _repos:
            repos_item = RepoStatus.from_dict(repos_item_data)

            repos.append(repos_item)

        snapshots = []
        _snapshots = d.pop("snapshots")
        for snapshots_item_data in _snapshots:
            snapshots_item = SnapshotInfo.from_dict(snapshots_item_data)

            snapshots.append(snapshots_item)

        search_response = cls(
            repos=repos,
            snapshots=snapshots,
        )

        search_response.additional_properties = d
        return search_response

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
