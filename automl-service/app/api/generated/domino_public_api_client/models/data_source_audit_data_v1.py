from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.data_source_audit_event_kind_v1 import DataSourceAuditEventKindV1

if TYPE_CHECKING:
    from ..models.data_source_audit_metadata_v1 import DataSourceAuditMetadataV1


T = TypeVar("T", bound="DataSourceAuditDataV1")


@_attrs_define
class DataSourceAuditDataV1:
    """
    Attributes:
        data_source_id (str): ID of the Data Source
        data_source_name (str): name of the Data Source
        data_source_type (str): The configuration type of the Data Source Example: ADLSConfig.
        event_kind (DataSourceAuditEventKindV1): Kinds of Data Source audit events
        metadata (DataSourceAuditMetadataV1): A map of string -> string Example: {'foo': 'bar'}.
        performed_by (str): ID of user who performed the event
        timestamp (datetime.datetime): timestamp of when event was performed Example: 1996-07-19T03:13:44.467Z.
    """

    data_source_id: str
    data_source_name: str
    data_source_type: str
    event_kind: DataSourceAuditEventKindV1
    metadata: DataSourceAuditMetadataV1
    performed_by: str
    timestamp: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_source_id = self.data_source_id

        data_source_name = self.data_source_name

        data_source_type = self.data_source_type

        event_kind = self.event_kind.value

        metadata = self.metadata.to_dict()

        performed_by = self.performed_by

        timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataSourceId": data_source_id,
                "dataSourceName": data_source_name,
                "dataSourceType": data_source_type,
                "eventKind": event_kind,
                "metadata": metadata,
                "performedBy": performed_by,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_audit_metadata_v1 import DataSourceAuditMetadataV1

        d = dict(src_dict)
        data_source_id = d.pop("dataSourceId")

        data_source_name = d.pop("dataSourceName")

        data_source_type = d.pop("dataSourceType")

        event_kind = DataSourceAuditEventKindV1(d.pop("eventKind"))

        metadata = DataSourceAuditMetadataV1.from_dict(d.pop("metadata"))

        performed_by = d.pop("performedBy")

        timestamp = isoparse(d.pop("timestamp"))

        data_source_audit_data_v1 = cls(
            data_source_id=data_source_id,
            data_source_name=data_source_name,
            data_source_type=data_source_type,
            event_kind=event_kind,
            metadata=metadata,
            performed_by=performed_by,
            timestamp=timestamp,
        )

        data_source_audit_data_v1.additional_properties = d
        return data_source_audit_data_v1

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
