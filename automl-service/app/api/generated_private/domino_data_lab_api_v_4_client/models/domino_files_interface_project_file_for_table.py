from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoFilesInterfaceProjectFileForTable")


@_attrs_define
class DominoFilesInterfaceProjectFileForTable:
    """
    Attributes:
        path (str):
        last_modified (int):
        size (int):
        key (str):
        goal_ids (list[str]):
        name (str):
        quoted_file_path (str):
        size_label (str):
        is_file_launchable_as_notebook (bool):
        is_file_runnable_from_view (bool):
        is_file_runnable_as_app (bool):
    """

    path: str
    last_modified: int
    size: int
    key: str
    goal_ids: list[str]
    name: str
    quoted_file_path: str
    size_label: str
    is_file_launchable_as_notebook: bool
    is_file_runnable_from_view: bool
    is_file_runnable_as_app: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        last_modified = self.last_modified

        size = self.size

        key = self.key

        goal_ids = self.goal_ids

        name = self.name

        quoted_file_path = self.quoted_file_path

        size_label = self.size_label

        is_file_launchable_as_notebook = self.is_file_launchable_as_notebook

        is_file_runnable_from_view = self.is_file_runnable_from_view

        is_file_runnable_as_app = self.is_file_runnable_as_app

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "lastModified": last_modified,
                "size": size,
                "key": key,
                "goalIds": goal_ids,
                "name": name,
                "quotedFilePath": quoted_file_path,
                "sizeLabel": size_label,
                "isFileLaunchableAsNotebook": is_file_launchable_as_notebook,
                "isFileRunnableFromView": is_file_runnable_from_view,
                "isFileRunnableAsApp": is_file_runnable_as_app,
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

        name = d.pop("name")

        quoted_file_path = d.pop("quotedFilePath")

        size_label = d.pop("sizeLabel")

        is_file_launchable_as_notebook = d.pop("isFileLaunchableAsNotebook")

        is_file_runnable_from_view = d.pop("isFileRunnableFromView")

        is_file_runnable_as_app = d.pop("isFileRunnableAsApp")

        domino_files_interface_project_file_for_table = cls(
            path=path,
            last_modified=last_modified,
            size=size,
            key=key,
            goal_ids=goal_ids,
            name=name,
            quoted_file_path=quoted_file_path,
            size_label=size_label,
            is_file_launchable_as_notebook=is_file_launchable_as_notebook,
            is_file_runnable_from_view=is_file_runnable_from_view,
            is_file_runnable_as_app=is_file_runnable_as_app,
        )

        domino_files_interface_project_file_for_table.additional_properties = d
        return domino_files_interface_project_file_for_table

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
