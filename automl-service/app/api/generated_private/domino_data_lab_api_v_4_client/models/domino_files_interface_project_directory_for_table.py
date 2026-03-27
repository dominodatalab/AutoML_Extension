from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoFilesInterfaceProjectDirectoryForTable")


@_attrs_define
class DominoFilesInterfaceProjectDirectoryForTable:
    """
    Attributes:
        path (str):
        size_in_bytes (int):
        name (str):
    """

    path: str
    size_in_bytes: int
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        size_in_bytes = self.size_in_bytes

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "sizeInBytes": size_in_bytes,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        size_in_bytes = d.pop("sizeInBytes")

        name = d.pop("name")

        domino_files_interface_project_directory_for_table = cls(
            path=path,
            size_in_bytes=size_in_bytes,
            name=name,
        )

        domino_files_interface_project_directory_for_table.additional_properties = d
        return domino_files_interface_project_directory_for_table

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
