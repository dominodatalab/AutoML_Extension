from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasetrw_web_file_collision_request_file_collision_setting import (
    DominoDatasetrwWebFileCollisionRequestFileCollisionSetting,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasetrwWebFileCollisionRequest")


@_attrs_define
class DominoDatasetrwWebFileCollisionRequest:
    """
    Attributes:
        file_paths (list[str]):
        file_collision_setting (DominoDatasetrwWebFileCollisionRequestFileCollisionSetting | Unset):
        target_relative_path (None | str | Unset):
    """

    file_paths: list[str]
    file_collision_setting: DominoDatasetrwWebFileCollisionRequestFileCollisionSetting | Unset = UNSET
    target_relative_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_paths = self.file_paths

        file_collision_setting: str | Unset = UNSET
        if not isinstance(self.file_collision_setting, Unset):
            file_collision_setting = self.file_collision_setting.value

        target_relative_path: None | str | Unset
        if isinstance(self.target_relative_path, Unset):
            target_relative_path = UNSET
        else:
            target_relative_path = self.target_relative_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filePaths": file_paths,
            }
        )
        if file_collision_setting is not UNSET:
            field_dict["fileCollisionSetting"] = file_collision_setting
        if target_relative_path is not UNSET:
            field_dict["targetRelativePath"] = target_relative_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_paths = cast(list[str], d.pop("filePaths"))

        _file_collision_setting = d.pop("fileCollisionSetting", UNSET)
        file_collision_setting: DominoDatasetrwWebFileCollisionRequestFileCollisionSetting | Unset
        if isinstance(_file_collision_setting, Unset):
            file_collision_setting = UNSET
        else:
            file_collision_setting = DominoDatasetrwWebFileCollisionRequestFileCollisionSetting(_file_collision_setting)

        def _parse_target_relative_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_relative_path = _parse_target_relative_path(d.pop("targetRelativePath", UNSET))

        domino_datasetrw_web_file_collision_request = cls(
            file_paths=file_paths,
            file_collision_setting=file_collision_setting,
            target_relative_path=target_relative_path,
        )

        domino_datasetrw_web_file_collision_request.additional_properties = d
        return domino_datasetrw_web_file_collision_request

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
