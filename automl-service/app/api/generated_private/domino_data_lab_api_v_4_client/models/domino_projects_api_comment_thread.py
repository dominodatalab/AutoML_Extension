from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_api_comment import DominoProjectsApiComment


T = TypeVar("T", bound="DominoProjectsApiCommentThread")


@_attrs_define
class DominoProjectsApiCommentThread:
    """
    Attributes:
        id (str):
        comments (list[DominoProjectsApiComment]):
    """

    id: str
    comments: list[DominoProjectsApiComment]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()
            comments.append(comments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "comments": comments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_comment import DominoProjectsApiComment

        d = dict(src_dict)
        id = d.pop("id")

        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = DominoProjectsApiComment.from_dict(comments_item_data)

            comments.append(comments_item)

        domino_projects_api_comment_thread = cls(
            id=id,
            comments=comments,
        )

        domino_projects_api_comment_thread.additional_properties = d
        return domino_projects_api_comment_thread

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
