from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoJobsInterfaceAbnormalStatus")


@_attrs_define
class DominoJobsInterfaceAbnormalStatus:
    """
    Attributes:
        run_failure_reason (str):
        run_failure_message (str):
    """

    run_failure_reason: str
    run_failure_message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_failure_reason = self.run_failure_reason

        run_failure_message = self.run_failure_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runFailureReason": run_failure_reason,
                "runFailureMessage": run_failure_message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_failure_reason = d.pop("runFailureReason")

        run_failure_message = d.pop("runFailureMessage")

        domino_jobs_interface_abnormal_status = cls(
            run_failure_reason=run_failure_reason,
            run_failure_message=run_failure_message,
        )

        domino_jobs_interface_abnormal_status.additional_properties = d
        return domino_jobs_interface_abnormal_status

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
