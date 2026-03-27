from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoDatasetrwWebRenameFileOrDirectoryRequest")


@_attrs_define
class DominoDatasetrwWebRenameFileOrDirectoryRequest:
    """
    Attributes:
        relative_path (str):
        new_name_with_extension (str):
    """

    relative_path: str
    new_name_with_extension: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relative_path = self.relative_path

        new_name_with_extension = self.new_name_with_extension

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relativePath": relative_path,
                "newNameWithExtension": new_name_with_extension,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        relative_path = d.pop("relativePath")

        new_name_with_extension = d.pop("newNameWithExtension")

        domino_datasetrw_web_rename_file_or_directory_request = cls(
            relative_path=relative_path,
            new_name_with_extension=new_name_with_extension,
        )

        domino_datasetrw_web_rename_file_or_directory_request.additional_properties = d
        return domino_datasetrw_web_rename_file_or_directory_request

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
