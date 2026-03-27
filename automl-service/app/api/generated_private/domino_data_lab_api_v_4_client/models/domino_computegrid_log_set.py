from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_computegrid_log_content import DominoComputegridLogContent
    from ..models.domino_computegrid_pagination_filter import DominoComputegridPaginationFilter


T = TypeVar("T", bound="DominoComputegridLogSet")


@_attrs_define
class DominoComputegridLogSet:
    """
    Attributes:
        log_content (list[DominoComputegridLogContent]):
        is_complete (bool):
        pagination (DominoComputegridPaginationFilter):
    """

    log_content: list[DominoComputegridLogContent]
    is_complete: bool
    pagination: DominoComputegridPaginationFilter
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        log_content = []
        for log_content_item_data in self.log_content:
            log_content_item = log_content_item_data.to_dict()
            log_content.append(log_content_item)

        is_complete = self.is_complete

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logContent": log_content,
                "isComplete": is_complete,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_computegrid_log_content import DominoComputegridLogContent
        from ..models.domino_computegrid_pagination_filter import DominoComputegridPaginationFilter

        d = dict(src_dict)
        log_content = []
        _log_content = d.pop("logContent")
        for log_content_item_data in _log_content:
            log_content_item = DominoComputegridLogContent.from_dict(log_content_item_data)

            log_content.append(log_content_item)

        is_complete = d.pop("isComplete")

        pagination = DominoComputegridPaginationFilter.from_dict(d.pop("pagination"))

        domino_computegrid_log_set = cls(
            log_content=log_content,
            is_complete=is_complete,
            pagination=pagination,
        )

        domino_computegrid_log_set.additional_properties = d
        return domino_computegrid_log_set

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
