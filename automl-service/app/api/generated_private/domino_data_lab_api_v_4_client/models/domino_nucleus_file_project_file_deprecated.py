from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_filesync_sync_relative_file_path import DominoFilesyncSyncRelativeFilePath


T = TypeVar("T", bound="DominoNucleusFileProjectFileDeprecated")


@_attrs_define
class DominoNucleusFileProjectFileDeprecated:
    """
    Attributes:
        path (DominoFilesyncSyncRelativeFilePath):
        last_modified (int):
        size (int):
        key (str):
    """

    path: DominoFilesyncSyncRelativeFilePath
    last_modified: int
    size: int
    key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path.to_dict()

        last_modified = self.last_modified

        size = self.size

        key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "lastModified": last_modified,
                "size": size,
                "key": key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_filesync_sync_relative_file_path import DominoFilesyncSyncRelativeFilePath

        d = dict(src_dict)
        path = DominoFilesyncSyncRelativeFilePath.from_dict(d.pop("path"))

        last_modified = d.pop("lastModified")

        size = d.pop("size")

        key = d.pop("key")

        domino_nucleus_file_project_file_deprecated = cls(
            path=path,
            last_modified=last_modified,
            size=size,
            key=key,
        )

        domino_nucleus_file_project_file_deprecated.additional_properties = d
        return domino_nucleus_file_project_file_deprecated

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
