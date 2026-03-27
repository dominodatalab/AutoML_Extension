from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoFilesWebSaveFile")


@_attrs_define
class DominoFilesWebSaveFile:
    """
    Attributes:
        path (str):
        content (str):
        must_run (bool | None | Unset):
        creating_new_file (bool | None | Unset):
    """

    path: str
    content: str
    must_run: bool | None | Unset = UNSET
    creating_new_file: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        content = self.content

        must_run: bool | None | Unset
        if isinstance(self.must_run, Unset):
            must_run = UNSET
        else:
            must_run = self.must_run

        creating_new_file: bool | None | Unset
        if isinstance(self.creating_new_file, Unset):
            creating_new_file = UNSET
        else:
            creating_new_file = self.creating_new_file

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "content": content,
            }
        )
        if must_run is not UNSET:
            field_dict["mustRun"] = must_run
        if creating_new_file is not UNSET:
            field_dict["creatingNewFile"] = creating_new_file

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        content = d.pop("content")

        def _parse_must_run(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        must_run = _parse_must_run(d.pop("mustRun", UNSET))

        def _parse_creating_new_file(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        creating_new_file = _parse_creating_new_file(d.pop("creatingNewFile", UNSET))

        domino_files_web_save_file = cls(
            path=path,
            content=content,
            must_run=must_run,
            creating_new_file=creating_new_file,
        )

        domino_files_web_save_file.additional_properties = d
        return domino_files_web_save_file

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
