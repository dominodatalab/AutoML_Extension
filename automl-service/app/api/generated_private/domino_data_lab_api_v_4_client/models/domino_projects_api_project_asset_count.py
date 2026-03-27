from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_project_asset_count_asset_type import DominoProjectsApiProjectAssetCountAssetType

T = TypeVar("T", bound="DominoProjectsApiProjectAssetCount")


@_attrs_define
class DominoProjectsApiProjectAssetCount:
    """
    Attributes:
        asset_type (DominoProjectsApiProjectAssetCountAssetType):
        asset_count (int):
    """

    asset_type: DominoProjectsApiProjectAssetCountAssetType
    asset_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_type = self.asset_type.value

        asset_count = self.asset_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetType": asset_type,
                "assetCount": asset_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_type = DominoProjectsApiProjectAssetCountAssetType(d.pop("assetType"))

        asset_count = d.pop("assetCount")

        domino_projects_api_project_asset_count = cls(
            asset_type=asset_type,
            asset_count=asset_count,
        )

        domino_projects_api_project_asset_count.additional_properties = d
        return domino_projects_api_project_asset_count

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
