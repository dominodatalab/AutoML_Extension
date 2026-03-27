from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_filesync_sync_file_signature import DominoFilesyncSyncFileSignature
    from ..models.domino_filesync_sync_relative_file_path import DominoFilesyncSyncRelativeFilePath


T = TypeVar("T", bound="DominoFilesyncSyncDominoFile")


@_attrs_define
class DominoFilesyncSyncDominoFile:
    """
    Attributes:
        path (DominoFilesyncSyncRelativeFilePath):
        signature (DominoFilesyncSyncFileSignature):
    """

    path: DominoFilesyncSyncRelativeFilePath
    signature: DominoFilesyncSyncFileSignature
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path.to_dict()

        signature = self.signature.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_filesync_sync_file_signature import DominoFilesyncSyncFileSignature
        from ..models.domino_filesync_sync_relative_file_path import DominoFilesyncSyncRelativeFilePath

        d = dict(src_dict)
        path = DominoFilesyncSyncRelativeFilePath.from_dict(d.pop("path"))

        signature = DominoFilesyncSyncFileSignature.from_dict(d.pop("signature"))

        domino_filesync_sync_domino_file = cls(
            path=path,
            signature=signature,
        )

        domino_filesync_sync_domino_file.additional_properties = d
        return domino_filesync_sync_domino_file

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
