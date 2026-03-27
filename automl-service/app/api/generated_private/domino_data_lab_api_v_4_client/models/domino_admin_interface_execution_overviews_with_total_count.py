from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_admin_interface_execution_overview import DominoAdminInterfaceExecutionOverview


T = TypeVar("T", bound="DominoAdminInterfaceExecutionOverviewsWithTotalCount")


@_attrs_define
class DominoAdminInterfaceExecutionOverviewsWithTotalCount:
    """
    Attributes:
        overviews (list[DominoAdminInterfaceExecutionOverview]):
        total_count (int):
    """

    overviews: list[DominoAdminInterfaceExecutionOverview]
    total_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        overviews = []
        for overviews_item_data in self.overviews:
            overviews_item = overviews_item_data.to_dict()
            overviews.append(overviews_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "overviews": overviews,
                "totalCount": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_admin_interface_execution_overview import DominoAdminInterfaceExecutionOverview

        d = dict(src_dict)
        overviews = []
        _overviews = d.pop("overviews")
        for overviews_item_data in _overviews:
            overviews_item = DominoAdminInterfaceExecutionOverview.from_dict(overviews_item_data)

            overviews.append(overviews_item)

        total_count = d.pop("totalCount")

        domino_admin_interface_execution_overviews_with_total_count = cls(
            overviews=overviews,
            total_count=total_count,
        )

        domino_admin_interface_execution_overviews_with_total_count.additional_properties = d
        return domino_admin_interface_execution_overviews_with_total_count

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
