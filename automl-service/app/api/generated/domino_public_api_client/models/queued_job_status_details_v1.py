from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QueuedJobStatusDetailsV1")


@_attrs_define
class QueuedJobStatusDetailsV1:
    """
    Attributes:
        expected_wait (str): Message describing estimated wait time between state changes. Example: Now.
        explanation (str): Message explaining the wait time Example: Your run has been assigned to a machine.
        help_text (str): Message informing the caller what should be done next Example: It will start being prepared for
            execution momentarily.
    """

    expected_wait: str
    explanation: str
    help_text: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expected_wait = self.expected_wait

        explanation = self.explanation

        help_text = self.help_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expectedWait": expected_wait,
                "explanation": explanation,
                "helpText": help_text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expected_wait = d.pop("expectedWait")

        explanation = d.pop("explanation")

        help_text = d.pop("helpText")

        queued_job_status_details_v1 = cls(
            expected_wait=expected_wait,
            explanation=explanation,
            help_text=help_text,
        )

        queued_job_status_details_v1.additional_properties = d
        return queued_job_status_details_v1

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
