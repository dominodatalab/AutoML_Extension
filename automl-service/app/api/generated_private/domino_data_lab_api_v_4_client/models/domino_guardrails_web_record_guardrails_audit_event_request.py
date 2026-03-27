from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_guardrails_web_record_guardrails_audit_event_request_event_type import (
    DominoGuardrailsWebRecordGuardrailsAuditEventRequestEventType,
)

if TYPE_CHECKING:
    from ..models.domino_guardrails_web_record_guardrails_audit_event_request_event_details import (
        DominoGuardrailsWebRecordGuardrailsAuditEventRequestEventDetails,
    )


T = TypeVar("T", bound="DominoGuardrailsWebRecordGuardrailsAuditEventRequest")


@_attrs_define
class DominoGuardrailsWebRecordGuardrailsAuditEventRequest:
    """
    Attributes:
        event_type (DominoGuardrailsWebRecordGuardrailsAuditEventRequestEventType): audit event type
        event_details (DominoGuardrailsWebRecordGuardrailsAuditEventRequestEventDetails):
        user_id (str):
    """

    event_type: DominoGuardrailsWebRecordGuardrailsAuditEventRequestEventType
    event_details: DominoGuardrailsWebRecordGuardrailsAuditEventRequestEventDetails
    user_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        event_details = self.event_details.to_dict()

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventType": event_type,
                "eventDetails": event_details,
                "userId": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_guardrails_web_record_guardrails_audit_event_request_event_details import (
            DominoGuardrailsWebRecordGuardrailsAuditEventRequestEventDetails,
        )

        d = dict(src_dict)
        event_type = DominoGuardrailsWebRecordGuardrailsAuditEventRequestEventType(d.pop("eventType"))

        event_details = DominoGuardrailsWebRecordGuardrailsAuditEventRequestEventDetails.from_dict(
            d.pop("eventDetails")
        )

        user_id = d.pop("userId")

        domino_guardrails_web_record_guardrails_audit_event_request = cls(
            event_type=event_type,
            event_details=event_details,
            user_id=user_id,
        )

        domino_guardrails_web_record_guardrails_audit_event_request.additional_properties = d
        return domino_guardrails_web_record_guardrails_audit_event_request

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
