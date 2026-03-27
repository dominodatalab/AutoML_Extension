from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_project_management_api_domino_project_to_pm_ticket_metadata_map_type import (
    DominoProjectManagementApiDominoProjectToPmTicketMetadataMapType,
)

if TYPE_CHECKING:
    from ..models.domino_project_management_api_pm_ticket_metadata import DominoProjectManagementApiPmTicketMetadata
    from ..models.domino_project_management_api_pm_ticket_stage import DominoProjectManagementApiPmTicketStage
    from ..models.domino_project_management_api_pm_ticket_type import DominoProjectManagementApiPmTicketType


T = TypeVar("T", bound="DominoProjectManagementApiDominoProjectToPmTicketMetadata")


@_attrs_define
class DominoProjectManagementApiDominoProjectToPmTicketMetadata:
    """
    Attributes:
        map_type (DominoProjectManagementApiDominoProjectToPmTicketMetadataMapType):
        ticket_metadata (DominoProjectManagementApiPmTicketMetadata):
        description (str):
        title (str):
        updated_at (int):
        ticket_types (list[DominoProjectManagementApiPmTicketType]):
        ticket_stages (list[DominoProjectManagementApiPmTicketStage]):
    """

    map_type: DominoProjectManagementApiDominoProjectToPmTicketMetadataMapType
    ticket_metadata: DominoProjectManagementApiPmTicketMetadata
    description: str
    title: str
    updated_at: int
    ticket_types: list[DominoProjectManagementApiPmTicketType]
    ticket_stages: list[DominoProjectManagementApiPmTicketStage]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        map_type = self.map_type.value

        ticket_metadata = self.ticket_metadata.to_dict()

        description = self.description

        title = self.title

        updated_at = self.updated_at

        ticket_types = []
        for ticket_types_item_data in self.ticket_types:
            ticket_types_item = ticket_types_item_data.to_dict()
            ticket_types.append(ticket_types_item)

        ticket_stages = []
        for ticket_stages_item_data in self.ticket_stages:
            ticket_stages_item = ticket_stages_item_data.to_dict()
            ticket_stages.append(ticket_stages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mapType": map_type,
                "ticketMetadata": ticket_metadata,
                "description": description,
                "title": title,
                "updatedAt": updated_at,
                "ticketTypes": ticket_types,
                "ticketStages": ticket_stages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_project_management_api_pm_ticket_metadata import DominoProjectManagementApiPmTicketMetadata
        from ..models.domino_project_management_api_pm_ticket_stage import DominoProjectManagementApiPmTicketStage
        from ..models.domino_project_management_api_pm_ticket_type import DominoProjectManagementApiPmTicketType

        d = dict(src_dict)
        map_type = DominoProjectManagementApiDominoProjectToPmTicketMetadataMapType(d.pop("mapType"))

        ticket_metadata = DominoProjectManagementApiPmTicketMetadata.from_dict(d.pop("ticketMetadata"))

        description = d.pop("description")

        title = d.pop("title")

        updated_at = d.pop("updatedAt")

        ticket_types = []
        _ticket_types = d.pop("ticketTypes")
        for ticket_types_item_data in _ticket_types:
            ticket_types_item = DominoProjectManagementApiPmTicketType.from_dict(ticket_types_item_data)

            ticket_types.append(ticket_types_item)

        ticket_stages = []
        _ticket_stages = d.pop("ticketStages")
        for ticket_stages_item_data in _ticket_stages:
            ticket_stages_item = DominoProjectManagementApiPmTicketStage.from_dict(ticket_stages_item_data)

            ticket_stages.append(ticket_stages_item)

        domino_project_management_api_domino_project_to_pm_ticket_metadata = cls(
            map_type=map_type,
            ticket_metadata=ticket_metadata,
            description=description,
            title=title,
            updated_at=updated_at,
            ticket_types=ticket_types,
            ticket_stages=ticket_stages,
        )

        domino_project_management_api_domino_project_to_pm_ticket_metadata.additional_properties = d
        return domino_project_management_api_domino_project_to_pm_ticket_metadata

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
