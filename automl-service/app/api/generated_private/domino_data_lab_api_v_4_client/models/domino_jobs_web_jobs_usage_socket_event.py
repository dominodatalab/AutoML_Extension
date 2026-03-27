from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoJobsWebJobsUsageSocketEvent")


@_attrs_define
class DominoJobsWebJobsUsageSocketEvent:
    """
    Attributes:
        correlation_id (str):
        job_id (str):
        room (str):
        cpu (float):
        mem (float):
        timestamp (int):
    """

    correlation_id: str
    job_id: str
    room: str
    cpu: float
    mem: float
    timestamp: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        correlation_id = self.correlation_id

        job_id = self.job_id

        room = self.room

        cpu = self.cpu

        mem = self.mem

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "correlationId": correlation_id,
                "jobId": job_id,
                "room": room,
                "cpu": cpu,
                "mem": mem,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        correlation_id = d.pop("correlationId")

        job_id = d.pop("jobId")

        room = d.pop("room")

        cpu = d.pop("cpu")

        mem = d.pop("mem")

        timestamp = d.pop("timestamp")

        domino_jobs_web_jobs_usage_socket_event = cls(
            correlation_id=correlation_id,
            job_id=job_id,
            room=room,
            cpu=cpu,
            mem=mem,
            timestamp=timestamp,
        )

        domino_jobs_web_jobs_usage_socket_event.additional_properties = d
        return domino_jobs_web_jobs_usage_socket_event

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
