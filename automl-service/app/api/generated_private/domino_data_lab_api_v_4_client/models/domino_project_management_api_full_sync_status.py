from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_project_management_api_full_sync_status_sync_status import (
    DominoProjectManagementApiFullSyncStatusSyncStatus,
)

T = TypeVar("T", bound="DominoProjectManagementApiFullSyncStatus")


@_attrs_define
class DominoProjectManagementApiFullSyncStatus:
    """
    Attributes:
        sync_status (DominoProjectManagementApiFullSyncStatusSyncStatus):
        last_sync_initiated_at (int):
    """

    sync_status: DominoProjectManagementApiFullSyncStatusSyncStatus
    last_sync_initiated_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sync_status = self.sync_status.value

        last_sync_initiated_at = self.last_sync_initiated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "syncStatus": sync_status,
                "lastSyncInitiatedAt": last_sync_initiated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sync_status = DominoProjectManagementApiFullSyncStatusSyncStatus(d.pop("syncStatus"))

        last_sync_initiated_at = d.pop("lastSyncInitiatedAt")

        domino_project_management_api_full_sync_status = cls(
            sync_status=sync_status,
            last_sync_initiated_at=last_sync_initiated_at,
        )

        domino_project_management_api_full_sync_status.additional_properties = d
        return domino_project_management_api_full_sync_status

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
