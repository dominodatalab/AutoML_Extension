from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_project_management_api_pm_id import DominoProjectManagementApiPmId


T = TypeVar("T", bound="DominoProjectManagementApiLinkedProjectDetails")


@_attrs_define
class DominoProjectManagementApiLinkedProjectDetails:
    """
    Attributes:
        project_id (str):
        project_name (str):
        ticket_id (DominoProjectManagementApiPmId):
        ticket_key (str):
        ticket_link (str):
    """

    project_id: str
    project_name: str
    ticket_id: DominoProjectManagementApiPmId
    ticket_key: str
    ticket_link: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        project_name = self.project_name

        ticket_id = self.ticket_id.to_dict()

        ticket_key = self.ticket_key

        ticket_link = self.ticket_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "projectName": project_name,
                "ticketId": ticket_id,
                "ticketKey": ticket_key,
                "ticketLink": ticket_link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_project_management_api_pm_id import DominoProjectManagementApiPmId

        d = dict(src_dict)
        project_id = d.pop("projectId")

        project_name = d.pop("projectName")

        ticket_id = DominoProjectManagementApiPmId.from_dict(d.pop("ticketId"))

        ticket_key = d.pop("ticketKey")

        ticket_link = d.pop("ticketLink")

        domino_project_management_api_linked_project_details = cls(
            project_id=project_id,
            project_name=project_name,
            ticket_id=ticket_id,
            ticket_key=ticket_key,
            ticket_link=ticket_link,
        )

        domino_project_management_api_linked_project_details.additional_properties = d
        return domino_project_management_api_linked_project_details

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
