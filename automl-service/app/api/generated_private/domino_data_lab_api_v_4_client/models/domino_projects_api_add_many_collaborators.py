from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectsApiAddManyCollaborators")


@_attrs_define
class DominoProjectsApiAddManyCollaborators:
    """
    Attributes:
        collaborator_username_or_emails (list[str]):
        welcome_message (None | str | Unset):
    """

    collaborator_username_or_emails: list[str]
    welcome_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collaborator_username_or_emails = self.collaborator_username_or_emails

        welcome_message: None | str | Unset
        if isinstance(self.welcome_message, Unset):
            welcome_message = UNSET
        else:
            welcome_message = self.welcome_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collaboratorUsernameOrEmails": collaborator_username_or_emails,
            }
        )
        if welcome_message is not UNSET:
            field_dict["welcomeMessage"] = welcome_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collaborator_username_or_emails = cast(list[str], d.pop("collaboratorUsernameOrEmails"))

        def _parse_welcome_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        welcome_message = _parse_welcome_message(d.pop("welcomeMessage", UNSET))

        domino_projects_api_add_many_collaborators = cls(
            collaborator_username_or_emails=collaborator_username_or_emails,
            welcome_message=welcome_message,
        )

        domino_projects_api_add_many_collaborators.additional_properties = d
        return domino_projects_api_add_many_collaborators

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
