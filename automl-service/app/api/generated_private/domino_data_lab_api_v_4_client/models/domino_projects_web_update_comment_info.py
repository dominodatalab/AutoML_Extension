from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProjectsWebUpdateCommentInfo")


@_attrs_define
class DominoProjectsWebUpdateCommentInfo:
    """
    Attributes:
        comment_thread_id (str):
        comment_id (str):
        comment_body (str):
    """

    comment_thread_id: str
    comment_id: str
    comment_body: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_thread_id = self.comment_thread_id

        comment_id = self.comment_id

        comment_body = self.comment_body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commentThreadId": comment_thread_id,
                "commentId": comment_id,
                "commentBody": comment_body,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_thread_id = d.pop("commentThreadId")

        comment_id = d.pop("commentId")

        comment_body = d.pop("commentBody")

        domino_projects_web_update_comment_info = cls(
            comment_thread_id=comment_thread_id,
            comment_id=comment_id,
            comment_body=comment_body,
        )

        domino_projects_web_update_comment_info.additional_properties = d
        return domino_projects_web_update_comment_info

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
