from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="DominoAdminInterfaceComputeNodeStatus")


@_attrs_define
class DominoAdminInterfaceComputeNodeStatus:
    """
    Attributes:
        condition_type (str):
        condition_status (str):
        reason (str):
        message (str):
        last_heartbeat_time (datetime.datetime):
        last_transition_time (datetime.datetime):
    """

    condition_type: str
    condition_status: str
    reason: str
    message: str
    last_heartbeat_time: datetime.datetime
    last_transition_time: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition_type = self.condition_type

        condition_status = self.condition_status

        reason = self.reason

        message = self.message

        last_heartbeat_time = self.last_heartbeat_time.isoformat()

        last_transition_time = self.last_transition_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conditionType": condition_type,
                "conditionStatus": condition_status,
                "reason": reason,
                "message": message,
                "lastHeartbeatTime": last_heartbeat_time,
                "lastTransitionTime": last_transition_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        condition_type = d.pop("conditionType")

        condition_status = d.pop("conditionStatus")

        reason = d.pop("reason")

        message = d.pop("message")

        last_heartbeat_time = isoparse(d.pop("lastHeartbeatTime"))

        last_transition_time = isoparse(d.pop("lastTransitionTime"))

        domino_admin_interface_compute_node_status = cls(
            condition_type=condition_type,
            condition_status=condition_status,
            reason=reason,
            message=message,
            last_heartbeat_time=last_heartbeat_time,
            last_transition_time=last_transition_time,
        )

        domino_admin_interface_compute_node_status.additional_properties = d
        return domino_admin_interface_compute_node_status

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
