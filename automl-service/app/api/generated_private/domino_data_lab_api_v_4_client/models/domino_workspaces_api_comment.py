from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_workspaces_api_comment_content import DominoWorkspacesApiCommentContent
    from ..models.domino_workspaces_api_commenter import DominoWorkspacesApiCommenter


T = TypeVar("T", bound="DominoWorkspacesApiComment")


@_attrs_define
class DominoWorkspacesApiComment:
    """
    Attributes:
        comment_id (str):
        commenter (DominoWorkspacesApiCommenter):
        comment_body (DominoWorkspacesApiCommentContent):
        created (int):
    """

    comment_id: str
    commenter: DominoWorkspacesApiCommenter
    comment_body: DominoWorkspacesApiCommentContent
    created: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_id = self.comment_id

        commenter = self.commenter.to_dict()

        comment_body = self.comment_body.to_dict()

        created = self.created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commentId": comment_id,
                "commenter": commenter,
                "commentBody": comment_body,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspaces_api_comment_content import DominoWorkspacesApiCommentContent
        from ..models.domino_workspaces_api_commenter import DominoWorkspacesApiCommenter

        d = dict(src_dict)
        comment_id = d.pop("commentId")

        commenter = DominoWorkspacesApiCommenter.from_dict(d.pop("commenter"))

        comment_body = DominoWorkspacesApiCommentContent.from_dict(d.pop("commentBody"))

        created = d.pop("created")

        domino_workspaces_api_comment = cls(
            comment_id=comment_id,
            commenter=commenter,
            comment_body=comment_body,
            created=created,
        )

        domino_workspaces_api_comment.additional_properties = d
        return domino_workspaces_api_comment

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
