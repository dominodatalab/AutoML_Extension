from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.ai_gateway_audit_metadata_v1 import AIGatewayAuditMetadataV1


T = TypeVar("T", bound="AIGatewayAuditDataV1")


@_attrs_define
class AIGatewayAuditDataV1:
    """
    Attributes:
        endpoint_id (str): Endpoint ID
        endpoint_type (str): Endpoint type
        event_kind (str): Event kind
        metadata (AIGatewayAuditMetadataV1): A map of string -> string Example: {'foo': 'bar'}.
        performed_by (str): ID of user who performed the event
        timestamp (datetime.datetime): timestamp of when event was performed Example: 1996-07-19T03:13:44.467Z.
    """

    endpoint_id: str
    endpoint_type: str
    event_kind: str
    metadata: AIGatewayAuditMetadataV1
    performed_by: str
    timestamp: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint_id = self.endpoint_id

        endpoint_type = self.endpoint_type

        event_kind = self.event_kind

        metadata = self.metadata.to_dict()

        performed_by = self.performed_by

        timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpointId": endpoint_id,
                "endpointType": endpoint_type,
                "eventKind": event_kind,
                "metadata": metadata,
                "performedBy": performed_by,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ai_gateway_audit_metadata_v1 import AIGatewayAuditMetadataV1

        d = dict(src_dict)
        endpoint_id = d.pop("endpointId")

        endpoint_type = d.pop("endpointType")

        event_kind = d.pop("eventKind")

        metadata = AIGatewayAuditMetadataV1.from_dict(d.pop("metadata"))

        performed_by = d.pop("performedBy")

        timestamp = isoparse(d.pop("timestamp"))

        ai_gateway_audit_data_v1 = cls(
            endpoint_id=endpoint_id,
            endpoint_type=endpoint_type,
            event_kind=event_kind,
            metadata=metadata,
            performed_by=performed_by,
            timestamp=timestamp,
        )

        ai_gateway_audit_data_v1.additional_properties = d
        return ai_gateway_audit_data_v1

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
