from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_status_v1_status import ProjectStatusV1Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectStatusV1")


@_attrs_define
class ProjectStatusV1:
    """
    Attributes:
        is_blocked (bool): Whether or not the project is blocked. If true, it has precedence over the status
        status (ProjectStatusV1Status): The project status
        blocked_reason (str | Unset): The reason the project is blocked
        completed_message (str | Unset): The completed project message
    """

    is_blocked: bool
    status: ProjectStatusV1Status
    blocked_reason: str | Unset = UNSET
    completed_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_blocked = self.is_blocked

        status = self.status.value

        blocked_reason = self.blocked_reason

        completed_message = self.completed_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isBlocked": is_blocked,
                "status": status,
            }
        )
        if blocked_reason is not UNSET:
            field_dict["blockedReason"] = blocked_reason
        if completed_message is not UNSET:
            field_dict["completedMessage"] = completed_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_blocked = d.pop("isBlocked")

        status = ProjectStatusV1Status(d.pop("status"))

        blocked_reason = d.pop("blockedReason", UNSET)

        completed_message = d.pop("completedMessage", UNSET)

        project_status_v1 = cls(
            is_blocked=is_blocked,
            status=status,
            blocked_reason=blocked_reason,
            completed_message=completed_message,
        )

        project_status_v1.additional_properties = d
        return project_status_v1

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
