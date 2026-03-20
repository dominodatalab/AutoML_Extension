from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FailureEnvelopeV1")


@_attrs_define
class FailureEnvelopeV1:
    """
    Attributes:
        errors (list[str]): Errors that caused a request to fail
        request_id (str): Id used to correlate a request with server actions. Example:
            bbd78579-93c4-45ee-a983-0d5c8da6d5b1.
    """

    errors: list[str]
    request_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors = self.errors

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errors": errors,
                "requestId": request_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        errors = cast(list[str], d.pop("errors"))

        request_id = d.pop("requestId")

        failure_envelope_v1 = cls(
            errors=errors,
            request_id=request_id,
        )

        failure_envelope_v1.additional_properties = d
        return failure_envelope_v1

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
