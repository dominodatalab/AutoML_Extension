from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProjectsWebAddBlockedAtComment")


@_attrs_define
class DominoProjectsWebAddBlockedAtComment:
    """
    Attributes:
        comment (str):
        blocked_at (int):
    """

    comment: str
    blocked_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        blocked_at = self.blocked_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment": comment,
                "blockedAt": blocked_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment")

        blocked_at = d.pop("blockedAt")

        domino_projects_web_add_blocked_at_comment = cls(
            comment=comment,
            blocked_at=blocked_at,
        )

        domino_projects_web_add_blocked_at_comment.additional_properties = d
        return domino_projects_web_add_blocked_at_comment

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
