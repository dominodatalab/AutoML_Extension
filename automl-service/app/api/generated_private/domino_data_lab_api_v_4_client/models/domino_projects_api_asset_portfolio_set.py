from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_api_asset_portfolio_element import DominoProjectsApiAssetPortfolioElement
    from ..models.domino_projects_api_asset_portfolio_pagination_filter import (
        DominoProjectsApiAssetPortfolioPaginationFilter,
    )


T = TypeVar("T", bound="DominoProjectsApiAssetPortfolioSet")


@_attrs_define
class DominoProjectsApiAssetPortfolioSet:
    """
    Attributes:
        total_count (int):
        asset_portfolios (list[DominoProjectsApiAssetPortfolioElement]):
        filter_ (DominoProjectsApiAssetPortfolioPaginationFilter):
    """

    total_count: int
    asset_portfolios: list[DominoProjectsApiAssetPortfolioElement]
    filter_: DominoProjectsApiAssetPortfolioPaginationFilter
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        asset_portfolios = []
        for asset_portfolios_item_data in self.asset_portfolios:
            asset_portfolios_item = asset_portfolios_item_data.to_dict()
            asset_portfolios.append(asset_portfolios_item)

        filter_ = self.filter_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalCount": total_count,
                "assetPortfolios": asset_portfolios,
                "filter": filter_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_asset_portfolio_element import DominoProjectsApiAssetPortfolioElement
        from ..models.domino_projects_api_asset_portfolio_pagination_filter import (
            DominoProjectsApiAssetPortfolioPaginationFilter,
        )

        d = dict(src_dict)
        total_count = d.pop("totalCount")

        asset_portfolios = []
        _asset_portfolios = d.pop("assetPortfolios")
        for asset_portfolios_item_data in _asset_portfolios:
            asset_portfolios_item = DominoProjectsApiAssetPortfolioElement.from_dict(asset_portfolios_item_data)

            asset_portfolios.append(asset_portfolios_item)

        filter_ = DominoProjectsApiAssetPortfolioPaginationFilter.from_dict(d.pop("filter"))

        domino_projects_api_asset_portfolio_set = cls(
            total_count=total_count,
            asset_portfolios=asset_portfolios,
            filter_=filter_,
        )

        domino_projects_api_asset_portfolio_set.additional_properties = d
        return domino_projects_api_asset_portfolio_set

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
