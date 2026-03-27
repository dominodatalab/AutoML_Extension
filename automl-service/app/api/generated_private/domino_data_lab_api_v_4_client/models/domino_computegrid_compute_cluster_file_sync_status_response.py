from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_computegrid_compute_cluster_file_sync_status_response_reason import (
    DominoComputegridComputeClusterFileSyncStatusResponseReason,
)
from ..models.domino_computegrid_compute_cluster_file_sync_status_response_status import (
    DominoComputegridComputeClusterFileSyncStatusResponseStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoComputegridComputeClusterFileSyncStatusResponse")


@_attrs_define
class DominoComputegridComputeClusterFileSyncStatusResponse:
    """
    Attributes:
        status (DominoComputegridComputeClusterFileSyncStatusResponseStatus):
        reason (DominoComputegridComputeClusterFileSyncStatusResponseReason):
        message (str):
        last_synced_started_at (datetime.datetime | None | Unset):
    """

    status: DominoComputegridComputeClusterFileSyncStatusResponseStatus
    reason: DominoComputegridComputeClusterFileSyncStatusResponseReason
    message: str
    last_synced_started_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        reason = self.reason.value

        message = self.message

        last_synced_started_at: None | str | Unset
        if isinstance(self.last_synced_started_at, Unset):
            last_synced_started_at = UNSET
        elif isinstance(self.last_synced_started_at, datetime.datetime):
            last_synced_started_at = self.last_synced_started_at.isoformat()
        else:
            last_synced_started_at = self.last_synced_started_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "reason": reason,
                "message": message,
            }
        )
        if last_synced_started_at is not UNSET:
            field_dict["lastSyncedStartedAt"] = last_synced_started_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = DominoComputegridComputeClusterFileSyncStatusResponseStatus(d.pop("status"))

        reason = DominoComputegridComputeClusterFileSyncStatusResponseReason(d.pop("reason"))

        message = d.pop("message")

        def _parse_last_synced_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_started_at_type_0 = isoparse(data)

                return last_synced_started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_synced_started_at = _parse_last_synced_started_at(d.pop("lastSyncedStartedAt", UNSET))

        domino_computegrid_compute_cluster_file_sync_status_response = cls(
            status=status,
            reason=reason,
            message=message,
            last_synced_started_at=last_synced_started_at,
        )

        domino_computegrid_compute_cluster_file_sync_status_response.additional_properties = d
        return domino_computegrid_compute_cluster_file_sync_status_response

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
