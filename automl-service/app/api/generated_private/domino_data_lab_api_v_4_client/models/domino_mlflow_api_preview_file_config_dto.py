from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoMlflowApiPreviewFileConfigDTO")


@_attrs_define
class DominoMlflowApiPreviewFileConfigDTO:
    """
    Attributes:
        max_preview_file_size_mb (int):
    """

    max_preview_file_size_mb: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_preview_file_size_mb = self.max_preview_file_size_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maxPreviewFileSizeMB": max_preview_file_size_mb,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_preview_file_size_mb = d.pop("maxPreviewFileSizeMB")

        domino_mlflow_api_preview_file_config_dto = cls(
            max_preview_file_size_mb=max_preview_file_size_mb,
        )

        domino_mlflow_api_preview_file_config_dto.additional_properties = d
        return domino_mlflow_api_preview_file_config_dto

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
