from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_quota_web_update_quota_request_action_metadata import (
        DominoQuotaWebUpdateQuotaRequestActionMetadata,
    )


T = TypeVar("T", bound="DominoQuotaWebUpdateQuotaRequest")


@_attrs_define
class DominoQuotaWebUpdateQuotaRequest:
    """
    Attributes:
        target_id (str | Unset): Id of user for quota
        quota_limit (int | Unset): quota limit
        action_metadata (DominoQuotaWebUpdateQuotaRequestActionMetadata | Unset):
    """

    target_id: str | Unset = UNSET
    quota_limit: int | Unset = UNSET
    action_metadata: DominoQuotaWebUpdateQuotaRequestActionMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_id = self.target_id

        quota_limit = self.quota_limit

        action_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_metadata, Unset):
            action_metadata = self.action_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if quota_limit is not UNSET:
            field_dict["quotaLimit"] = quota_limit
        if action_metadata is not UNSET:
            field_dict["actionMetadata"] = action_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_quota_web_update_quota_request_action_metadata import (
            DominoQuotaWebUpdateQuotaRequestActionMetadata,
        )

        d = dict(src_dict)
        target_id = d.pop("targetId", UNSET)

        quota_limit = d.pop("quotaLimit", UNSET)

        _action_metadata = d.pop("actionMetadata", UNSET)
        action_metadata: DominoQuotaWebUpdateQuotaRequestActionMetadata | Unset
        if isinstance(_action_metadata, Unset):
            action_metadata = UNSET
        else:
            action_metadata = DominoQuotaWebUpdateQuotaRequestActionMetadata.from_dict(_action_metadata)

        domino_quota_web_update_quota_request = cls(
            target_id=target_id,
            quota_limit=quota_limit,
            action_metadata=action_metadata,
        )

        domino_quota_web_update_quota_request.additional_properties = d
        return domino_quota_web_update_quota_request

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
