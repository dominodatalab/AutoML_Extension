from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_files_interface_commented_by import DominoFilesInterfaceCommentedBy


T = TypeVar("T", bound="DominoFilesInterfaceComment")


@_attrs_define
class DominoFilesInterfaceComment:
    """
    Attributes:
        comment_id (str):
        commented_by (DominoFilesInterfaceCommentedBy):
        comment_body (str):
        created_at (int):
    """

    comment_id: str
    commented_by: DominoFilesInterfaceCommentedBy
    comment_body: str
    created_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_id = self.comment_id

        commented_by = self.commented_by.to_dict()

        comment_body = self.comment_body

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commentId": comment_id,
                "commentedBy": commented_by,
                "commentBody": comment_body,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_files_interface_commented_by import DominoFilesInterfaceCommentedBy

        d = dict(src_dict)
        comment_id = d.pop("commentId")

        commented_by = DominoFilesInterfaceCommentedBy.from_dict(d.pop("commentedBy"))

        comment_body = d.pop("commentBody")

        created_at = d.pop("createdAt")

        domino_files_interface_comment = cls(
            comment_id=comment_id,
            commented_by=commented_by,
            comment_body=comment_body,
            created_at=created_at,
        )

        domino_files_interface_comment.additional_properties = d
        return domino_files_interface_comment

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
