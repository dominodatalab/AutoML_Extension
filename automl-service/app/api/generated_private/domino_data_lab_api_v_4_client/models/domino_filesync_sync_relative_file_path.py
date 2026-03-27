from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoFilesyncSyncRelativeFilePath")


@_attrs_define
class DominoFilesyncSyncRelativeFilePath:
    """
    Attributes:
        canonicalized_path_string (str): Path on the file system
        separator (str | Unset): Path separator Example: /.
    """

    canonicalized_path_string: str
    separator: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        canonicalized_path_string = self.canonicalized_path_string

        separator = self.separator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "canonicalizedPathString": canonicalized_path_string,
            }
        )
        if separator is not UNSET:
            field_dict["separator"] = separator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        canonicalized_path_string = d.pop("canonicalizedPathString")

        separator = d.pop("separator", UNSET)

        domino_filesync_sync_relative_file_path = cls(
            canonicalized_path_string=canonicalized_path_string,
            separator=separator,
        )

        domino_filesync_sync_relative_file_path.additional_properties = d
        return domino_filesync_sync_relative_file_path

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
