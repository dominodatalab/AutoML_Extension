from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_jobs_interface_job_pagination_order_by import DominoJobsInterfaceJobPaginationOrderBy
from ..models.domino_jobs_interface_job_pagination_sort_by import DominoJobsInterfaceJobPaginationSortBy
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoJobsInterfaceJobPagination")


@_attrs_define
class DominoJobsInterfaceJobPagination:
    """
    Attributes:
        offset (int):
        limit (int):
        sort_by (DominoJobsInterfaceJobPaginationSortBy):
        order_by (DominoJobsInterfaceJobPaginationOrderBy):
        domino_stats_sort_field_name (None | str | Unset):
    """

    offset: int
    limit: int
    sort_by: DominoJobsInterfaceJobPaginationSortBy
    order_by: DominoJobsInterfaceJobPaginationOrderBy
    domino_stats_sort_field_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        sort_by = self.sort_by.value

        order_by = self.order_by.value

        domino_stats_sort_field_name: None | str | Unset
        if isinstance(self.domino_stats_sort_field_name, Unset):
            domino_stats_sort_field_name = UNSET
        else:
            domino_stats_sort_field_name = self.domino_stats_sort_field_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
                "sortBy": sort_by,
                "orderBy": order_by,
            }
        )
        if domino_stats_sort_field_name is not UNSET:
            field_dict["dominoStatsSortFieldName"] = domino_stats_sort_field_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        sort_by = DominoJobsInterfaceJobPaginationSortBy(d.pop("sortBy"))

        order_by = DominoJobsInterfaceJobPaginationOrderBy(d.pop("orderBy"))

        def _parse_domino_stats_sort_field_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domino_stats_sort_field_name = _parse_domino_stats_sort_field_name(d.pop("dominoStatsSortFieldName", UNSET))

        domino_jobs_interface_job_pagination = cls(
            offset=offset,
            limit=limit,
            sort_by=sort_by,
            order_by=order_by,
            domino_stats_sort_field_name=domino_stats_sort_field_name,
        )

        domino_jobs_interface_job_pagination.additional_properties = d
        return domino_jobs_interface_job_pagination

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
