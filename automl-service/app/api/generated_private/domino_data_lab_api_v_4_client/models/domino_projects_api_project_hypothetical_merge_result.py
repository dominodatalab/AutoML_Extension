from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_filesync_sync_relative_file_path import DominoFilesyncSyncRelativeFilePath


T = TypeVar("T", bound="DominoProjectsApiProjectHypotheticalMergeResult")


@_attrs_define
class DominoProjectsApiProjectHypotheticalMergeResult:
    """
    Attributes:
        merge_base_commit_id (str):
        can_be_merged_with_no_conflict (bool):
        has_conflicts (bool):
        total_conflicts (int):
        get_conflicting_paths_set (list[DominoFilesyncSyncRelativeFilePath] | None | Unset):
    """

    merge_base_commit_id: str
    can_be_merged_with_no_conflict: bool
    has_conflicts: bool
    total_conflicts: int
    get_conflicting_paths_set: list[DominoFilesyncSyncRelativeFilePath] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merge_base_commit_id = self.merge_base_commit_id

        can_be_merged_with_no_conflict = self.can_be_merged_with_no_conflict

        has_conflicts = self.has_conflicts

        total_conflicts = self.total_conflicts

        get_conflicting_paths_set: list[dict[str, Any]] | None | Unset
        if isinstance(self.get_conflicting_paths_set, Unset):
            get_conflicting_paths_set = UNSET
        elif isinstance(self.get_conflicting_paths_set, list):
            get_conflicting_paths_set = []
            for get_conflicting_paths_set_type_0_item_data in self.get_conflicting_paths_set:
                get_conflicting_paths_set_type_0_item = get_conflicting_paths_set_type_0_item_data.to_dict()
                get_conflicting_paths_set.append(get_conflicting_paths_set_type_0_item)

        else:
            get_conflicting_paths_set = self.get_conflicting_paths_set

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mergeBaseCommitId": merge_base_commit_id,
                "canBeMergedWithNoConflict": can_be_merged_with_no_conflict,
                "hasConflicts": has_conflicts,
                "totalConflicts": total_conflicts,
            }
        )
        if get_conflicting_paths_set is not UNSET:
            field_dict["getConflictingPathsSet"] = get_conflicting_paths_set

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_filesync_sync_relative_file_path import DominoFilesyncSyncRelativeFilePath

        d = dict(src_dict)
        merge_base_commit_id = d.pop("mergeBaseCommitId")

        can_be_merged_with_no_conflict = d.pop("canBeMergedWithNoConflict")

        has_conflicts = d.pop("hasConflicts")

        total_conflicts = d.pop("totalConflicts")

        def _parse_get_conflicting_paths_set(data: object) -> list[DominoFilesyncSyncRelativeFilePath] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                get_conflicting_paths_set_type_0 = []
                _get_conflicting_paths_set_type_0 = data
                for get_conflicting_paths_set_type_0_item_data in _get_conflicting_paths_set_type_0:
                    get_conflicting_paths_set_type_0_item = DominoFilesyncSyncRelativeFilePath.from_dict(
                        get_conflicting_paths_set_type_0_item_data
                    )

                    get_conflicting_paths_set_type_0.append(get_conflicting_paths_set_type_0_item)

                return get_conflicting_paths_set_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoFilesyncSyncRelativeFilePath] | None | Unset, data)

        get_conflicting_paths_set = _parse_get_conflicting_paths_set(d.pop("getConflictingPathsSet", UNSET))

        domino_projects_api_project_hypothetical_merge_result = cls(
            merge_base_commit_id=merge_base_commit_id,
            can_be_merged_with_no_conflict=can_be_merged_with_no_conflict,
            has_conflicts=has_conflicts,
            total_conflicts=total_conflicts,
            get_conflicting_paths_set=get_conflicting_paths_set,
        )

        domino_projects_api_project_hypothetical_merge_result.additional_properties = d
        return domino_projects_api_project_hypothetical_merge_result

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
