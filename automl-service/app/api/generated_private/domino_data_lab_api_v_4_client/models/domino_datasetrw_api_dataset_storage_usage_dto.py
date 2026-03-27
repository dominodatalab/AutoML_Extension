from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoDatasetrwApiDatasetStorageUsageDto")


@_attrs_define
class DominoDatasetrwApiDatasetStorageUsageDto:
    """
    Attributes:
        quota_id (str):
        target_id (str):
        limit (int):
        total_storage_used (int):
        is_at_warning_threshold (bool):
        is_at_email_threshold (bool):
    """

    quota_id: str
    target_id: str
    limit: int
    total_storage_used: int
    is_at_warning_threshold: bool
    is_at_email_threshold: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quota_id = self.quota_id

        target_id = self.target_id

        limit = self.limit

        total_storage_used = self.total_storage_used

        is_at_warning_threshold = self.is_at_warning_threshold

        is_at_email_threshold = self.is_at_email_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quotaId": quota_id,
                "targetId": target_id,
                "limit": limit,
                "totalStorageUsed": total_storage_used,
                "isAtWarningThreshold": is_at_warning_threshold,
                "isAtEmailThreshold": is_at_email_threshold,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quota_id = d.pop("quotaId")

        target_id = d.pop("targetId")

        limit = d.pop("limit")

        total_storage_used = d.pop("totalStorageUsed")

        is_at_warning_threshold = d.pop("isAtWarningThreshold")

        is_at_email_threshold = d.pop("isAtEmailThreshold")

        domino_datasetrw_api_dataset_storage_usage_dto = cls(
            quota_id=quota_id,
            target_id=target_id,
            limit=limit,
            total_storage_used=total_storage_used,
            is_at_warning_threshold=is_at_warning_threshold,
            is_at_email_threshold=is_at_email_threshold,
        )

        domino_datasetrw_api_dataset_storage_usage_dto.additional_properties = d
        return domino_datasetrw_api_dataset_storage_usage_dto

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
