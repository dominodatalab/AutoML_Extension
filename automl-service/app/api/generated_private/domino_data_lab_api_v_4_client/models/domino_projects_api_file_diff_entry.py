from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_filesync_sync_domino_file import DominoFilesyncSyncDominoFile
    from ..models.domino_filesync_sync_relative_file_path import DominoFilesyncSyncRelativeFilePath


T = TypeVar("T", bound="DominoProjectsApiFileDiffEntry")


@_attrs_define
class DominoProjectsApiFileDiffEntry:
    """
    Attributes:
        path (DominoFilesyncSyncRelativeFilePath):
        content_matches (bool):
        into_file_is_full_deleted (bool):
        from_file_is_full_deleted (bool):
        base_file (DominoFilesyncSyncDominoFile | Unset):
        target_file (DominoFilesyncSyncDominoFile | Unset):
    """

    path: DominoFilesyncSyncRelativeFilePath
    content_matches: bool
    into_file_is_full_deleted: bool
    from_file_is_full_deleted: bool
    base_file: DominoFilesyncSyncDominoFile | Unset = UNSET
    target_file: DominoFilesyncSyncDominoFile | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path.to_dict()

        content_matches = self.content_matches

        into_file_is_full_deleted = self.into_file_is_full_deleted

        from_file_is_full_deleted = self.from_file_is_full_deleted

        base_file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_file, Unset):
            base_file = self.base_file.to_dict()

        target_file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_file, Unset):
            target_file = self.target_file.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "contentMatches": content_matches,
                "intoFileIsFullDeleted": into_file_is_full_deleted,
                "fromFileIsFullDeleted": from_file_is_full_deleted,
            }
        )
        if base_file is not UNSET:
            field_dict["baseFile"] = base_file
        if target_file is not UNSET:
            field_dict["targetFile"] = target_file

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_filesync_sync_domino_file import DominoFilesyncSyncDominoFile
        from ..models.domino_filesync_sync_relative_file_path import DominoFilesyncSyncRelativeFilePath

        d = dict(src_dict)
        path = DominoFilesyncSyncRelativeFilePath.from_dict(d.pop("path"))

        content_matches = d.pop("contentMatches")

        into_file_is_full_deleted = d.pop("intoFileIsFullDeleted")

        from_file_is_full_deleted = d.pop("fromFileIsFullDeleted")

        _base_file = d.pop("baseFile", UNSET)
        base_file: DominoFilesyncSyncDominoFile | Unset
        if isinstance(_base_file, Unset):
            base_file = UNSET
        else:
            base_file = DominoFilesyncSyncDominoFile.from_dict(_base_file)

        _target_file = d.pop("targetFile", UNSET)
        target_file: DominoFilesyncSyncDominoFile | Unset
        if isinstance(_target_file, Unset):
            target_file = UNSET
        else:
            target_file = DominoFilesyncSyncDominoFile.from_dict(_target_file)

        domino_projects_api_file_diff_entry = cls(
            path=path,
            content_matches=content_matches,
            into_file_is_full_deleted=into_file_is_full_deleted,
            from_file_is_full_deleted=from_file_is_full_deleted,
            base_file=base_file,
            target_file=target_file,
        )

        domino_projects_api_file_diff_entry.additional_properties = d
        return domino_projects_api_file_diff_entry

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
