from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoGuardrailsWebCreateCommentRequest")


@_attrs_define
class DominoGuardrailsWebCreateCommentRequest:
    """
    Attributes:
        bundle_id (str):
        project_id (str):
        comment (str):
        bundle_name (str | Unset):
        policy_id (str | Unset):
        artifact_id (str | Unset):
        approval_id (str | Unset):
    """

    bundle_id: str
    project_id: str
    comment: str
    bundle_name: str | Unset = UNSET
    policy_id: str | Unset = UNSET
    artifact_id: str | Unset = UNSET
    approval_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bundle_id = self.bundle_id

        project_id = self.project_id

        comment = self.comment

        bundle_name = self.bundle_name

        policy_id = self.policy_id

        artifact_id = self.artifact_id

        approval_id = self.approval_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bundleId": bundle_id,
                "projectId": project_id,
                "comment": comment,
            }
        )
        if bundle_name is not UNSET:
            field_dict["bundleName"] = bundle_name
        if policy_id is not UNSET:
            field_dict["policyId"] = policy_id
        if artifact_id is not UNSET:
            field_dict["artifactId"] = artifact_id
        if approval_id is not UNSET:
            field_dict["approvalId"] = approval_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bundle_id = d.pop("bundleId")

        project_id = d.pop("projectId")

        comment = d.pop("comment")

        bundle_name = d.pop("bundleName", UNSET)

        policy_id = d.pop("policyId", UNSET)

        artifact_id = d.pop("artifactId", UNSET)

        approval_id = d.pop("approvalId", UNSET)

        domino_guardrails_web_create_comment_request = cls(
            bundle_id=bundle_id,
            project_id=project_id,
            comment=comment,
            bundle_name=bundle_name,
            policy_id=policy_id,
            artifact_id=artifact_id,
            approval_id=approval_id,
        )

        domino_guardrails_web_create_comment_request.additional_properties = d
        return domino_guardrails_web_create_comment_request

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
