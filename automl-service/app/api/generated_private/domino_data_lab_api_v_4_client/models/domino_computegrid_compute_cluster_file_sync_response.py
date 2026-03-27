from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_computegrid_compute_cluster_file_sync_response_reason import (
    DominoComputegridComputeClusterFileSyncResponseReason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoComputegridComputeClusterFileSyncResponse")


@_attrs_define
class DominoComputegridComputeClusterFileSyncResponse:
    """
    Attributes:
        started (bool):
        reason (DominoComputegridComputeClusterFileSyncResponseReason):
        message (str):
        start_timestamp (datetime.datetime | None | Unset):
    """

    started: bool
    reason: DominoComputegridComputeClusterFileSyncResponseReason
    message: str
    start_timestamp: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        started = self.started

        reason = self.reason.value

        message = self.message

        start_timestamp: None | str | Unset
        if isinstance(self.start_timestamp, Unset):
            start_timestamp = UNSET
        elif isinstance(self.start_timestamp, datetime.datetime):
            start_timestamp = self.start_timestamp.isoformat()
        else:
            start_timestamp = self.start_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "started": started,
                "reason": reason,
                "message": message,
            }
        )
        if start_timestamp is not UNSET:
            field_dict["startTimestamp"] = start_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        started = d.pop("started")

        reason = DominoComputegridComputeClusterFileSyncResponseReason(d.pop("reason"))

        message = d.pop("message")

        def _parse_start_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_timestamp_type_0 = isoparse(data)

                return start_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_timestamp = _parse_start_timestamp(d.pop("startTimestamp", UNSET))

        domino_computegrid_compute_cluster_file_sync_response = cls(
            started=started,
            reason=reason,
            message=message,
            start_timestamp=start_timestamp,
        )

        domino_computegrid_compute_cluster_file_sync_response.additional_properties = d
        return domino_computegrid_compute_cluster_file_sync_response

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
