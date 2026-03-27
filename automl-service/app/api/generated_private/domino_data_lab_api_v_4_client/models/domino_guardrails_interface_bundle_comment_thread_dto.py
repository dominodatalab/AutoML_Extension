from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_guardrails_interface_bundle_comment_thread_dto_thread_status import (
    DominoGuardrailsInterfaceBundleCommentThreadDtoThreadStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment import Comment


T = TypeVar("T", bound="DominoGuardrailsInterfaceBundleCommentThreadDto")


@_attrs_define
class DominoGuardrailsInterfaceBundleCommentThreadDto:
    """
    Attributes:
        id (str):
        bundle_id (str):
        project_id (str):
        thread_status (DominoGuardrailsInterfaceBundleCommentThreadDtoThreadStatus):
        comments (list[Comment]):
        artifact_id (str | Unset):
        approval_id (str | Unset):
    """

    id: str
    bundle_id: str
    project_id: str
    thread_status: DominoGuardrailsInterfaceBundleCommentThreadDtoThreadStatus
    comments: list[Comment]
    artifact_id: str | Unset = UNSET
    approval_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        bundle_id = self.bundle_id

        project_id = self.project_id

        thread_status = self.thread_status.value

        comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()
            comments.append(comments_item)

        artifact_id = self.artifact_id

        approval_id = self.approval_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "bundleId": bundle_id,
                "projectId": project_id,
                "threadStatus": thread_status,
                "comments": comments,
            }
        )
        if artifact_id is not UNSET:
            field_dict["artifactId"] = artifact_id
        if approval_id is not UNSET:
            field_dict["approvalId"] = approval_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment import Comment

        d = dict(src_dict)
        id = d.pop("id")

        bundle_id = d.pop("bundleId")

        project_id = d.pop("projectId")

        thread_status = DominoGuardrailsInterfaceBundleCommentThreadDtoThreadStatus(d.pop("threadStatus"))

        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = Comment.from_dict(comments_item_data)

            comments.append(comments_item)

        artifact_id = d.pop("artifactId", UNSET)

        approval_id = d.pop("approvalId", UNSET)

        domino_guardrails_interface_bundle_comment_thread_dto = cls(
            id=id,
            bundle_id=bundle_id,
            project_id=project_id,
            thread_status=thread_status,
            comments=comments,
            artifact_id=artifact_id,
            approval_id=approval_id,
        )

        domino_guardrails_interface_bundle_comment_thread_dto.additional_properties = d
        return domino_guardrails_interface_bundle_comment_thread_dto

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
