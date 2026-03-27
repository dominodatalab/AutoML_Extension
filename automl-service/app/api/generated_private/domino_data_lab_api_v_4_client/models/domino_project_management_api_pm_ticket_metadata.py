from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_project_management_api_pm_id import DominoProjectManagementApiPmId


T = TypeVar("T", bound="DominoProjectManagementApiPmTicketMetadata")


@_attrs_define
class DominoProjectManagementApiPmTicketMetadata:
    """
    Attributes:
        ticket_link (str):
        ticket_key (str):
        project_id (DominoProjectManagementApiPmId):
    """

    ticket_link: str
    ticket_key: str
    project_id: DominoProjectManagementApiPmId
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticket_link = self.ticket_link

        ticket_key = self.ticket_key

        project_id = self.project_id.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticketLink": ticket_link,
                "ticketKey": ticket_key,
                "projectId": project_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_project_management_api_pm_id import DominoProjectManagementApiPmId

        d = dict(src_dict)
        ticket_link = d.pop("ticketLink")

        ticket_key = d.pop("ticketKey")

        project_id = DominoProjectManagementApiPmId.from_dict(d.pop("projectId"))

        domino_project_management_api_pm_ticket_metadata = cls(
            ticket_link=ticket_link,
            ticket_key=ticket_key,
            project_id=project_id,
        )

        domino_project_management_api_pm_ticket_metadata.additional_properties = d
        return domino_project_management_api_pm_ticket_metadata

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
