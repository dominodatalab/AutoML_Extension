from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwStorageUsageDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwStorageUsageDto:
    """
    Attributes:
        quota_id (str):
        limit (int):
        total_storage_used (int):
        is_at_warning_threshold (bool):
        is_at_email_threshold (bool):
        target_id (str | Unset):
    """

    quota_id: str
    limit: int
    total_storage_used: int
    is_at_warning_threshold: bool
    is_at_email_threshold: bool
    target_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quota_id = self.quota_id

        limit = self.limit

        total_storage_used = self.total_storage_used

        is_at_warning_threshold = self.is_at_warning_threshold

        is_at_email_threshold = self.is_at_email_threshold

        target_id = self.target_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quotaId": quota_id,
                "limit": limit,
                "totalStorageUsed": total_storage_used,
                "isAtWarningThreshold": is_at_warning_threshold,
                "isAtEmailThreshold": is_at_email_threshold,
            }
        )
        if target_id is not UNSET:
            field_dict["targetId"] = target_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quota_id = d.pop("quotaId")

        limit = d.pop("limit")

        total_storage_used = d.pop("totalStorageUsed")

        is_at_warning_threshold = d.pop("isAtWarningThreshold")

        is_at_email_threshold = d.pop("isAtEmailThreshold")

        target_id = d.pop("targetId", UNSET)

        domino_datasetrw_api_dataset_rw_storage_usage_dto = cls(
            quota_id=quota_id,
            limit=limit,
            total_storage_used=total_storage_used,
            is_at_warning_threshold=is_at_warning_threshold,
            is_at_email_threshold=is_at_email_threshold,
            target_id=target_id,
        )

        domino_datasetrw_api_dataset_rw_storage_usage_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_storage_usage_dto

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
