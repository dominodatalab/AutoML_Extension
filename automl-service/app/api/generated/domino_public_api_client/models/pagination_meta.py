from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pagination_meta_order import PaginationMetaOrder
from ..models.pagination_meta_sort_by import PaginationMetaSortBy

if TYPE_CHECKING:
    from ..models.pagination_meta_filters import PaginationMetaFilters
    from ..models.pagination_meta_pagination import PaginationMetaPagination


T = TypeVar("T", bound="PaginationMeta")


@_attrs_define
class PaginationMeta:
    """
    Attributes:
        filters (list[PaginationMetaFilters]):
        order (PaginationMetaOrder): The order that the list of Extensions is sorted in.
        pagination (PaginationMetaPagination): The pagination information for the list of Extensions.
        sort_by (PaginationMetaSortBy): The field that the list of Extensions is sorted by.
    """

    filters: list[PaginationMetaFilters]
    order: PaginationMetaOrder
    pagination: PaginationMetaPagination
    sort_by: PaginationMetaSortBy
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        order = self.order.value

        pagination = self.pagination.to_dict()

        sort_by = self.sort_by.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
                "order": order,
                "pagination": pagination,
                "sortBy": sort_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination_meta_filters import PaginationMetaFilters
        from ..models.pagination_meta_pagination import PaginationMetaPagination

        d = dict(src_dict)
        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = PaginationMetaFilters.from_dict(filters_item_data)

            filters.append(filters_item)

        order = PaginationMetaOrder(d.pop("order"))

        pagination = PaginationMetaPagination.from_dict(d.pop("pagination"))

        sort_by = PaginationMetaSortBy(d.pop("sortBy"))

        pagination_meta = cls(
            filters=filters,
            order=order,
            pagination=pagination,
            sort_by=sort_by,
        )

        pagination_meta.additional_properties = d
        return pagination_meta

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
