from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_activity_api_project_link_change_activity_metadata_project_link_action import (
    DominoActivityApiProjectLinkChangeActivityMetadataProjectLinkAction,
)

T = TypeVar("T", bound="DominoActivityApiProjectLinkChangeActivityMetadata")


@_attrs_define
class DominoActivityApiProjectLinkChangeActivityMetadata:
    """
    Attributes:
        ticket_key (str):
        ticket_url (str):
        project_link_action (DominoActivityApiProjectLinkChangeActivityMetadataProjectLinkAction):
        keep_existing_goals (bool):
    """

    ticket_key: str
    ticket_url: str
    project_link_action: DominoActivityApiProjectLinkChangeActivityMetadataProjectLinkAction
    keep_existing_goals: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticket_key = self.ticket_key

        ticket_url = self.ticket_url

        project_link_action = self.project_link_action.value

        keep_existing_goals = self.keep_existing_goals

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticketKey": ticket_key,
                "ticketUrl": ticket_url,
                "projectLinkAction": project_link_action,
                "keepExistingGoals": keep_existing_goals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticket_key = d.pop("ticketKey")

        ticket_url = d.pop("ticketUrl")

        project_link_action = DominoActivityApiProjectLinkChangeActivityMetadataProjectLinkAction(
            d.pop("projectLinkAction")
        )

        keep_existing_goals = d.pop("keepExistingGoals")

        domino_activity_api_project_link_change_activity_metadata = cls(
            ticket_key=ticket_key,
            ticket_url=ticket_url,
            project_link_action=project_link_action,
            keep_existing_goals=keep_existing_goals,
        )

        domino_activity_api_project_link_change_activity_metadata.additional_properties = d
        return domino_activity_api_project_link_change_activity_metadata

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
