from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination_filter_v1 import PaginationFilterV1
    from ..models.project_template import ProjectTemplate


T = TypeVar("T", bound="PaginatedBaseTemplatesCollectionV1")


@_attrs_define
class PaginatedBaseTemplatesCollectionV1:
    """
    Attributes:
        items (list[ProjectTemplate]):
        pagination_details (PaginationFilterV1):
        total_count (int):
    """

    items: list[ProjectTemplate]
    pagination_details: PaginationFilterV1
    total_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        pagination_details = self.pagination_details.to_dict()

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "paginationDetails": pagination_details,
                "totalCount": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination_filter_v1 import PaginationFilterV1
        from ..models.project_template import ProjectTemplate

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ProjectTemplate.from_dict(items_item_data)

            items.append(items_item)

        pagination_details = PaginationFilterV1.from_dict(d.pop("paginationDetails"))

        total_count = d.pop("totalCount")

        paginated_base_templates_collection_v1 = cls(
            items=items,
            pagination_details=pagination_details,
            total_count=total_count,
        )

        paginated_base_templates_collection_v1.additional_properties = d
        return paginated_base_templates_collection_v1

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
