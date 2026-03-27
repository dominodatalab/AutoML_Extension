from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_project_portfolio_pagination_filter_sort_by import (
    DominoProjectsApiProjectPortfolioPaginationFilterSortBy,
)
from ..models.domino_projects_api_project_portfolio_pagination_filter_status_item import (
    DominoProjectsApiProjectPortfolioPaginationFilterStatusItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_apiserverutils_pagination_pagination_filter import (
        DominoApiserverutilsPaginationPaginationFilter,
    )


T = TypeVar("T", bound="DominoProjectsApiProjectPortfolioPaginationFilter")


@_attrs_define
class DominoProjectsApiProjectPortfolioPaginationFilter:
    """
    Attributes:
        pagination (DominoApiserverutilsPaginationPaginationFilter):
        sort_by (DominoProjectsApiProjectPortfolioPaginationFilterSortBy):
        stage_id (list[str]):
        status (list[DominoProjectsApiProjectPortfolioPaginationFilterStatusItem]):
        search_query (None | str | Unset):
        is_blocked (bool | None | Unset):
    """

    pagination: DominoApiserverutilsPaginationPaginationFilter
    sort_by: DominoProjectsApiProjectPortfolioPaginationFilterSortBy
    stage_id: list[str]
    status: list[DominoProjectsApiProjectPortfolioPaginationFilterStatusItem]
    search_query: None | str | Unset = UNSET
    is_blocked: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        sort_by = self.sort_by.value

        stage_id = self.stage_id

        status = []
        for status_item_data in self.status:
            status_item = status_item_data.value
            status.append(status_item)

        search_query: None | str | Unset
        if isinstance(self.search_query, Unset):
            search_query = UNSET
        else:
            search_query = self.search_query

        is_blocked: bool | None | Unset
        if isinstance(self.is_blocked, Unset):
            is_blocked = UNSET
        else:
            is_blocked = self.is_blocked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "sortBy": sort_by,
                "stageId": stage_id,
                "status": status,
            }
        )
        if search_query is not UNSET:
            field_dict["searchQuery"] = search_query
        if is_blocked is not UNSET:
            field_dict["isBlocked"] = is_blocked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_apiserverutils_pagination_pagination_filter import (
            DominoApiserverutilsPaginationPaginationFilter,
        )

        d = dict(src_dict)
        pagination = DominoApiserverutilsPaginationPaginationFilter.from_dict(d.pop("pagination"))

        sort_by = DominoProjectsApiProjectPortfolioPaginationFilterSortBy(d.pop("sortBy"))

        stage_id = cast(list[str], d.pop("stageId"))

        status = []
        _status = d.pop("status")
        for status_item_data in _status:
            status_item = DominoProjectsApiProjectPortfolioPaginationFilterStatusItem(status_item_data)

            status.append(status_item)

        def _parse_search_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search_query = _parse_search_query(d.pop("searchQuery", UNSET))

        def _parse_is_blocked(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_blocked = _parse_is_blocked(d.pop("isBlocked", UNSET))

        domino_projects_api_project_portfolio_pagination_filter = cls(
            pagination=pagination,
            sort_by=sort_by,
            stage_id=stage_id,
            status=status,
            search_query=search_query,
            is_blocked=is_blocked,
        )

        domino_projects_api_project_portfolio_pagination_filter.additional_properties = d
        return domino_projects_api_project_portfolio_pagination_filter

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
