from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoFilesInterfaceProjectFile")


@_attrs_define
class DominoFilesInterfaceProjectFile:
    """
    Attributes:
        path (str):
        last_modified (int):
        size (int):
        key (str):
        goal_ids (list[str]):
    """

    path: str
    last_modified: int
    size: int
    key: str
    goal_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        last_modified = self.last_modified

        size = self.size

        key = self.key

        goal_ids = self.goal_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "lastModified": last_modified,
                "size": size,
                "key": key,
                "goalIds": goal_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        last_modified = d.pop("lastModified")

        size = d.pop("size")

        key = d.pop("key")

        goal_ids = cast(list[str], d.pop("goalIds"))

        domino_files_interface_project_file = cls(
            path=path,
            last_modified=last_modified,
            size=size,
            key=key,
            goal_ids=goal_ids,
        )

        domino_files_interface_project_file.additional_properties = d
        return domino_files_interface_project_file

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
