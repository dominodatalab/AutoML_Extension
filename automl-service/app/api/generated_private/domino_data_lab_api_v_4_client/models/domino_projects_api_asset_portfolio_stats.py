from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_api_project_asset_count import DominoProjectsApiProjectAssetCount


T = TypeVar("T", bound="DominoProjectsApiAssetPortfolioStats")


@_attrs_define
class DominoProjectsApiAssetPortfolioStats:
    """
    Attributes:
        asset_portfolio_stats (list[DominoProjectsApiProjectAssetCount]):
    """

    asset_portfolio_stats: list[DominoProjectsApiProjectAssetCount]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_portfolio_stats = []
        for asset_portfolio_stats_item_data in self.asset_portfolio_stats:
            asset_portfolio_stats_item = asset_portfolio_stats_item_data.to_dict()
            asset_portfolio_stats.append(asset_portfolio_stats_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetPortfolioStats": asset_portfolio_stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_project_asset_count import DominoProjectsApiProjectAssetCount

        d = dict(src_dict)
        asset_portfolio_stats = []
        _asset_portfolio_stats = d.pop("assetPortfolioStats")
        for asset_portfolio_stats_item_data in _asset_portfolio_stats:
            asset_portfolio_stats_item = DominoProjectsApiProjectAssetCount.from_dict(asset_portfolio_stats_item_data)

            asset_portfolio_stats.append(asset_portfolio_stats_item)

        domino_projects_api_asset_portfolio_stats = cls(
            asset_portfolio_stats=asset_portfolio_stats,
        )

        domino_projects_api_asset_portfolio_stats.additional_properties = d
        return domino_projects_api_asset_portfolio_stats

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
