from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.commenter import Commenter


T = TypeVar("T", bound="Comment")


@_attrs_define
class Comment:
    """
    Attributes:
        comment_id (str):
        commenter (Commenter):
        comment_body (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    comment_id: str
    commenter: Commenter
    comment_body: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_id = self.comment_id

        commenter = self.commenter.to_dict()

        comment_body = self.comment_body

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commentId": comment_id,
                "commenter": commenter,
                "commentBody": comment_body,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commenter import Commenter

        d = dict(src_dict)
        comment_id = d.pop("commentId")

        commenter = Commenter.from_dict(d.pop("commenter"))

        comment_body = d.pop("commentBody")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        comment = cls(
            comment_id=comment_id,
            commenter=commenter,
            comment_body=comment_body,
            created_at=created_at,
            updated_at=updated_at,
        )

        comment.additional_properties = d
        return comment

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
