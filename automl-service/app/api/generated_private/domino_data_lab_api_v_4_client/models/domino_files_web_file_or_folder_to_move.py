from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoFilesWebFileOrFolderToMove")


@_attrs_define
class DominoFilesWebFileOrFolderToMove:
    """
    Attributes:
        origin_path (str):
        target_path (str):
        is_directory (bool):
        owner_username (str):
        project_name (str):
    """

    origin_path: str
    target_path: str
    is_directory: bool
    owner_username: str
    project_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        origin_path = self.origin_path

        target_path = self.target_path

        is_directory = self.is_directory

        owner_username = self.owner_username

        project_name = self.project_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "originPath": origin_path,
                "targetPath": target_path,
                "isDirectory": is_directory,
                "ownerUsername": owner_username,
                "projectName": project_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        origin_path = d.pop("originPath")

        target_path = d.pop("targetPath")

        is_directory = d.pop("isDirectory")

        owner_username = d.pop("ownerUsername")

        project_name = d.pop("projectName")

        domino_files_web_file_or_folder_to_move = cls(
            origin_path=origin_path,
            target_path=target_path,
            is_directory=is_directory,
            owner_username=owner_username,
            project_name=project_name,
        )

        domino_files_web_file_or_folder_to_move.additional_properties = d
        return domino_files_web_file_or_folder_to_move

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
