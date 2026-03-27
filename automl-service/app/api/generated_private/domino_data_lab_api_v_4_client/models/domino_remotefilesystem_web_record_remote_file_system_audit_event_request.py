from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_remotefilesystem_web_record_remote_file_system_audit_event_request_event_type import (
    DominoRemotefilesystemWebRecordRemoteFileSystemAuditEventRequestEventType,
)

if TYPE_CHECKING:
    from ..models.domino_remotefilesystem_web_record_remote_file_system_audit_event_request_event_details import (
        DominoRemotefilesystemWebRecordRemoteFileSystemAuditEventRequestEventDetails,
    )


T = TypeVar("T", bound="DominoRemotefilesystemWebRecordRemoteFileSystemAuditEventRequest")


@_attrs_define
class DominoRemotefilesystemWebRecordRemoteFileSystemAuditEventRequest:
    """
    Attributes:
        event_type (DominoRemotefilesystemWebRecordRemoteFileSystemAuditEventRequestEventType): audit event type
        event_details (DominoRemotefilesystemWebRecordRemoteFileSystemAuditEventRequestEventDetails):
    """

    event_type: DominoRemotefilesystemWebRecordRemoteFileSystemAuditEventRequestEventType
    event_details: DominoRemotefilesystemWebRecordRemoteFileSystemAuditEventRequestEventDetails
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        event_details = self.event_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventType": event_type,
                "eventDetails": event_details,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_remotefilesystem_web_record_remote_file_system_audit_event_request_event_details import (
            DominoRemotefilesystemWebRecordRemoteFileSystemAuditEventRequestEventDetails,
        )

        d = dict(src_dict)
        event_type = DominoRemotefilesystemWebRecordRemoteFileSystemAuditEventRequestEventType(d.pop("eventType"))

        event_details = DominoRemotefilesystemWebRecordRemoteFileSystemAuditEventRequestEventDetails.from_dict(
            d.pop("eventDetails")
        )

        domino_remotefilesystem_web_record_remote_file_system_audit_event_request = cls(
            event_type=event_type,
            event_details=event_details,
        )

        domino_remotefilesystem_web_record_remote_file_system_audit_event_request.additional_properties = d
        return domino_remotefilesystem_web_record_remote_file_system_audit_event_request

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
