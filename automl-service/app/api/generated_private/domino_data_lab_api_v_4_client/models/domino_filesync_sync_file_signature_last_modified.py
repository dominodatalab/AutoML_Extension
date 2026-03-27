from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoFilesyncSyncFileSignatureLastModified")


@_attrs_define
class DominoFilesyncSyncFileSignatureLastModified:
    """
    Attributes:
        rounded_value (int):
    """

    rounded_value: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rounded_value = self.rounded_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "roundedValue": rounded_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rounded_value = d.pop("roundedValue")

        domino_filesync_sync_file_signature_last_modified = cls(
            rounded_value=rounded_value,
        )

        domino_filesync_sync_file_signature_last_modified.additional_properties = d
        return domino_filesync_sync_file_signature_last_modified

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
