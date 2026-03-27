from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_asset_view_stats_view_type import DominoProjectsApiAssetViewStatsViewType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectsApiAssetViewStats")


@_attrs_define
class DominoProjectsApiAssetViewStats:
    """
    Attributes:
        view_type (DominoProjectsApiAssetViewStatsViewType):
        total_count (int):
        error_rate (float | None | Unset):
    """

    view_type: DominoProjectsApiAssetViewStatsViewType
    total_count: int
    error_rate: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        view_type = self.view_type.value

        total_count = self.total_count

        error_rate: float | None | Unset
        if isinstance(self.error_rate, Unset):
            error_rate = UNSET
        else:
            error_rate = self.error_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "viewType": view_type,
                "totalCount": total_count,
            }
        )
        if error_rate is not UNSET:
            field_dict["errorRate"] = error_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        view_type = DominoProjectsApiAssetViewStatsViewType(d.pop("viewType"))

        total_count = d.pop("totalCount")

        def _parse_error_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        error_rate = _parse_error_rate(d.pop("errorRate", UNSET))

        domino_projects_api_asset_view_stats = cls(
            view_type=view_type,
            total_count=total_count,
            error_rate=error_rate,
        )

        domino_projects_api_asset_view_stats.additional_properties = d
        return domino_projects_api_asset_view_stats

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
