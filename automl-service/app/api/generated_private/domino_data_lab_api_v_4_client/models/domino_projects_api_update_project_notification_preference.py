from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProjectsApiUpdateProjectNotificationPreference")


@_attrs_define
class DominoProjectsApiUpdateProjectNotificationPreference:
    """
    Attributes:
        collaborator_id (str):
        notification_preference (str):
    """

    collaborator_id: str
    notification_preference: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collaborator_id = self.collaborator_id

        notification_preference = self.notification_preference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collaboratorId": collaborator_id,
                "notificationPreference": notification_preference,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collaborator_id = d.pop("collaboratorId")

        notification_preference = d.pop("notificationPreference")

        domino_projects_api_update_project_notification_preference = cls(
            collaborator_id=collaborator_id,
            notification_preference=notification_preference,
        )

        domino_projects_api_update_project_notification_preference.additional_properties = d
        return domino_projects_api_update_project_notification_preference

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
