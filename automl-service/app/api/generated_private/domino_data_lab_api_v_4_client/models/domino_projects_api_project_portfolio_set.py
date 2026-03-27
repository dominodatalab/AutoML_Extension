from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_api_project_portfolio_element import DominoProjectsApiProjectPortfolioElement
    from ..models.domino_projects_api_project_portfolio_pagination_filter import (
        DominoProjectsApiProjectPortfolioPaginationFilter,
    )


T = TypeVar("T", bound="DominoProjectsApiProjectPortfolioSet")


@_attrs_define
class DominoProjectsApiProjectPortfolioSet:
    """
    Attributes:
        total_count (int):
        project_portfolios (list[DominoProjectsApiProjectPortfolioElement]):
        pagination_filter (DominoProjectsApiProjectPortfolioPaginationFilter):
    """

    total_count: int
    project_portfolios: list[DominoProjectsApiProjectPortfolioElement]
    pagination_filter: DominoProjectsApiProjectPortfolioPaginationFilter
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        project_portfolios = []
        for project_portfolios_item_data in self.project_portfolios:
            project_portfolios_item = project_portfolios_item_data.to_dict()
            project_portfolios.append(project_portfolios_item)

        pagination_filter = self.pagination_filter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalCount": total_count,
                "projectPortfolios": project_portfolios,
                "paginationFilter": pagination_filter,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_project_portfolio_element import DominoProjectsApiProjectPortfolioElement
        from ..models.domino_projects_api_project_portfolio_pagination_filter import (
            DominoProjectsApiProjectPortfolioPaginationFilter,
        )

        d = dict(src_dict)
        total_count = d.pop("totalCount")

        project_portfolios = []
        _project_portfolios = d.pop("projectPortfolios")
        for project_portfolios_item_data in _project_portfolios:
            project_portfolios_item = DominoProjectsApiProjectPortfolioElement.from_dict(project_portfolios_item_data)

            project_portfolios.append(project_portfolios_item)

        pagination_filter = DominoProjectsApiProjectPortfolioPaginationFilter.from_dict(d.pop("paginationFilter"))

        domino_projects_api_project_portfolio_set = cls(
            total_count=total_count,
            project_portfolios=project_portfolios,
            pagination_filter=pagination_filter,
        )

        domino_projects_api_project_portfolio_set.additional_properties = d
        return domino_projects_api_project_portfolio_set

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
