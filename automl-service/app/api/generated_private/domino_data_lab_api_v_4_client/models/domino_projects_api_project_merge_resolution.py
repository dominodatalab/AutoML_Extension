from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_filesync_sync_file_change import DominoFilesyncSyncFileChange


T = TypeVar("T", bound="DominoProjectsApiProjectMergeResolution")


@_attrs_define
class DominoProjectsApiProjectMergeResolution:
    """
    Attributes:
        conflict_resolutions (list[DominoFilesyncSyncFileChange]):
    """

    conflict_resolutions: list[DominoFilesyncSyncFileChange]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conflict_resolutions = []
        for conflict_resolutions_item_data in self.conflict_resolutions:
            conflict_resolutions_item = conflict_resolutions_item_data.to_dict()
            conflict_resolutions.append(conflict_resolutions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conflictResolutions": conflict_resolutions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_filesync_sync_file_change import DominoFilesyncSyncFileChange

        d = dict(src_dict)
        conflict_resolutions = []
        _conflict_resolutions = d.pop("conflictResolutions")
        for conflict_resolutions_item_data in _conflict_resolutions:
            conflict_resolutions_item = DominoFilesyncSyncFileChange.from_dict(conflict_resolutions_item_data)

            conflict_resolutions.append(conflict_resolutions_item)

        domino_projects_api_project_merge_resolution = cls(
            conflict_resolutions=conflict_resolutions,
        )

        domino_projects_api_project_merge_resolution.additional_properties = d
        return domino_projects_api_project_merge_resolution

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
