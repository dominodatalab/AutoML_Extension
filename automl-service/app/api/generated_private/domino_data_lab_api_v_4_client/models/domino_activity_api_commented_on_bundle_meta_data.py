from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_activity_api_commented_on_bundle_meta_data_thread_status import (
    DominoActivityApiCommentedOnBundleMetaDataThreadStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoActivityApiCommentedOnBundleMetaData")


@_attrs_define
class DominoActivityApiCommentedOnBundleMetaData:
    """
    Attributes:
        bundle_id (str):
        thread_status (DominoActivityApiCommentedOnBundleMetaDataThreadStatus):
        artifact_id (None | str | Unset):
        approval_id (None | str | Unset):
    """

    bundle_id: str
    thread_status: DominoActivityApiCommentedOnBundleMetaDataThreadStatus
    artifact_id: None | str | Unset = UNSET
    approval_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bundle_id = self.bundle_id

        thread_status = self.thread_status.value

        artifact_id: None | str | Unset
        if isinstance(self.artifact_id, Unset):
            artifact_id = UNSET
        else:
            artifact_id = self.artifact_id

        approval_id: None | str | Unset
        if isinstance(self.approval_id, Unset):
            approval_id = UNSET
        else:
            approval_id = self.approval_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bundleId": bundle_id,
                "threadStatus": thread_status,
            }
        )
        if artifact_id is not UNSET:
            field_dict["artifactId"] = artifact_id
        if approval_id is not UNSET:
            field_dict["approvalId"] = approval_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bundle_id = d.pop("bundleId")

        thread_status = DominoActivityApiCommentedOnBundleMetaDataThreadStatus(d.pop("threadStatus"))

        def _parse_artifact_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        artifact_id = _parse_artifact_id(d.pop("artifactId", UNSET))

        def _parse_approval_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approval_id = _parse_approval_id(d.pop("approvalId", UNSET))

        domino_activity_api_commented_on_bundle_meta_data = cls(
            bundle_id=bundle_id,
            thread_status=thread_status,
            artifact_id=artifact_id,
            approval_id=approval_id,
        )

        domino_activity_api_commented_on_bundle_meta_data.additional_properties = d
        return domino_activity_api_commented_on_bundle_meta_data

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
