from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_project_status_status import DominoProjectsApiProjectStatusStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectsApiProjectStatus")


@_attrs_define
class DominoProjectsApiProjectStatus:
    """
    Attributes:
        status (DominoProjectsApiProjectStatusStatus):
        is_blocked (bool):
        blocked_reason (None | str | Unset):
        completed_message (None | str | Unset):
    """

    status: DominoProjectsApiProjectStatusStatus
    is_blocked: bool
    blocked_reason: None | str | Unset = UNSET
    completed_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        is_blocked = self.is_blocked

        blocked_reason: None | str | Unset
        if isinstance(self.blocked_reason, Unset):
            blocked_reason = UNSET
        else:
            blocked_reason = self.blocked_reason

        completed_message: None | str | Unset
        if isinstance(self.completed_message, Unset):
            completed_message = UNSET
        else:
            completed_message = self.completed_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "isBlocked": is_blocked,
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
        status = DominoProjectsApiProjectStatusStatus(d.pop("status"))

        is_blocked = d.pop("isBlocked")

        def _parse_blocked_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        blocked_reason = _parse_blocked_reason(d.pop("blockedReason", UNSET))

        def _parse_completed_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completed_message = _parse_completed_message(d.pop("completedMessage", UNSET))

        domino_projects_api_project_status = cls(
            status=status,
            is_blocked=is_blocked,
            blocked_reason=blocked_reason,
            completed_message=completed_message,
        )

        domino_projects_api_project_status.additional_properties = d
        return domino_projects_api_project_status

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
