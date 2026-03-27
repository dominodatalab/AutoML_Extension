from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_filesync_sync_file_signature_last_modified import DominoFilesyncSyncFileSignatureLastModified


T = TypeVar("T", bound="DominoFilesyncSyncFileSignature")


@_attrs_define
class DominoFilesyncSyncFileSignature:
    """
    Attributes:
        last_modified (DominoFilesyncSyncFileSignatureLastModified | Unset):
        size (int | Unset):
        content_hash (str | Unset):
    """

    last_modified: DominoFilesyncSyncFileSignatureLastModified | Unset = UNSET
    size: int | Unset = UNSET
    content_hash: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_modified: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.to_dict()

        size = self.size

        content_hash = self.content_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if size is not UNSET:
            field_dict["size"] = size
        if content_hash is not UNSET:
            field_dict["contentHash"] = content_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_filesync_sync_file_signature_last_modified import (
            DominoFilesyncSyncFileSignatureLastModified,
        )

        d = dict(src_dict)
        _last_modified = d.pop("lastModified", UNSET)
        last_modified: DominoFilesyncSyncFileSignatureLastModified | Unset
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = DominoFilesyncSyncFileSignatureLastModified.from_dict(_last_modified)

        size = d.pop("size", UNSET)

        content_hash = d.pop("contentHash", UNSET)

        domino_filesync_sync_file_signature = cls(
            last_modified=last_modified,
            size=size,
            content_hash=content_hash,
        )

        domino_filesync_sync_file_signature.additional_properties = d
        return domino_filesync_sync_file_signature

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
