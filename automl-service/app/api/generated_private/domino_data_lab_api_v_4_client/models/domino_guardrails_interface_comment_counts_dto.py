from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_guardrails_interface_comment_counts_dto_comment_counts_map import (
        DominoGuardrailsInterfaceCommentCountsDtoCommentCountsMap,
    )


T = TypeVar("T", bound="DominoGuardrailsInterfaceCommentCountsDto")


@_attrs_define
class DominoGuardrailsInterfaceCommentCountsDto:
    """
    Attributes:
        comment_counts_map (DominoGuardrailsInterfaceCommentCountsDtoCommentCountsMap):
    """

    comment_counts_map: DominoGuardrailsInterfaceCommentCountsDtoCommentCountsMap
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_counts_map = self.comment_counts_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commentCountsMap": comment_counts_map,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_guardrails_interface_comment_counts_dto_comment_counts_map import (
            DominoGuardrailsInterfaceCommentCountsDtoCommentCountsMap,
        )

        d = dict(src_dict)
        comment_counts_map = DominoGuardrailsInterfaceCommentCountsDtoCommentCountsMap.from_dict(
            d.pop("commentCountsMap")
        )

        domino_guardrails_interface_comment_counts_dto = cls(
            comment_counts_map=comment_counts_map,
        )

        domino_guardrails_interface_comment_counts_dto.additional_properties = d
        return domino_guardrails_interface_comment_counts_dto

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
