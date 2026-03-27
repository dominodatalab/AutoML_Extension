from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProjectsApiAssetVersionInfo")


@_attrs_define
class DominoProjectsApiAssetVersionInfo:
    """
    Attributes:
        asset_version_id (str):
        asset_name (str):
        asset_version (str):
    """

    asset_version_id: str
    asset_name: str
    asset_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_version_id = self.asset_version_id

        asset_name = self.asset_name

        asset_version = self.asset_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetVersionId": asset_version_id,
                "assetName": asset_name,
                "assetVersion": asset_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_version_id = d.pop("assetVersionId")

        asset_name = d.pop("assetName")

        asset_version = d.pop("assetVersion")

        domino_projects_api_asset_version_info = cls(
            asset_version_id=asset_version_id,
            asset_name=asset_name,
            asset_version=asset_version,
        )

        domino_projects_api_asset_version_info.additional_properties = d
        return domino_projects_api_asset_version_info

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
