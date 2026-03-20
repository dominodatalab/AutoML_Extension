from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.job_logs_v1 import JobLogsV1
    from ..models.logs_envelope_v1_metadata import LogsEnvelopeV1Metadata


T = TypeVar("T", bound="LogsEnvelopeV1")


@_attrs_define
class LogsEnvelopeV1:
    """
    Attributes:
        logs (JobLogsV1):
        metadata (LogsEnvelopeV1Metadata):
    """

    logs: JobLogsV1
    metadata: LogsEnvelopeV1Metadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logs = self.logs.to_dict()

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logs": logs,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_logs_v1 import JobLogsV1
        from ..models.logs_envelope_v1_metadata import LogsEnvelopeV1Metadata

        d = dict(src_dict)
        logs = JobLogsV1.from_dict(d.pop("logs"))

        metadata = LogsEnvelopeV1Metadata.from_dict(d.pop("metadata"))

        logs_envelope_v1 = cls(
            logs=logs,
            metadata=metadata,
        )

        logs_envelope_v1.additional_properties = d
        return logs_envelope_v1

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
