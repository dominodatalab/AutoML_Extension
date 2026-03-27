from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_project_management_api_domino_goal_to_pm_sub_ticket_metadata_map_type import (
    DominoProjectManagementApiDominoGoalToPmSubTicketMetadataMapType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_project_management_api_pm_ticket_metadata import DominoProjectManagementApiPmTicketMetadata
    from ..models.domino_project_management_api_pm_ticket_stage import DominoProjectManagementApiPmTicketStage
    from ..models.domino_project_management_api_pm_user import DominoProjectManagementApiPmUser


T = TypeVar("T", bound="DominoProjectManagementApiDominoGoalToPmSubTicketMetadata")


@_attrs_define
class DominoProjectManagementApiDominoGoalToPmSubTicketMetadata:
    """
    Attributes:
        map_type (DominoProjectManagementApiDominoGoalToPmSubTicketMetadataMapType):
        domino_project_id (str):
        updated_at (int):
        ticket_metadata (DominoProjectManagementApiPmTicketMetadata):
        ticket_stages (list[DominoProjectManagementApiPmTicketStage]):
        ticket_assignee (DominoProjectManagementApiPmUser | Unset):
    """

    map_type: DominoProjectManagementApiDominoGoalToPmSubTicketMetadataMapType
    domino_project_id: str
    updated_at: int
    ticket_metadata: DominoProjectManagementApiPmTicketMetadata
    ticket_stages: list[DominoProjectManagementApiPmTicketStage]
    ticket_assignee: DominoProjectManagementApiPmUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        map_type = self.map_type.value

        domino_project_id = self.domino_project_id

        updated_at = self.updated_at

        ticket_metadata = self.ticket_metadata.to_dict()

        ticket_stages = []
        for ticket_stages_item_data in self.ticket_stages:
            ticket_stages_item = ticket_stages_item_data.to_dict()
            ticket_stages.append(ticket_stages_item)

        ticket_assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ticket_assignee, Unset):
            ticket_assignee = self.ticket_assignee.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mapType": map_type,
                "dominoProjectId": domino_project_id,
                "updatedAt": updated_at,
                "ticketMetadata": ticket_metadata,
                "ticketStages": ticket_stages,
            }
        )
        if ticket_assignee is not UNSET:
            field_dict["ticketAssignee"] = ticket_assignee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_project_management_api_pm_ticket_metadata import DominoProjectManagementApiPmTicketMetadata
        from ..models.domino_project_management_api_pm_ticket_stage import DominoProjectManagementApiPmTicketStage
        from ..models.domino_project_management_api_pm_user import DominoProjectManagementApiPmUser

        d = dict(src_dict)
        map_type = DominoProjectManagementApiDominoGoalToPmSubTicketMetadataMapType(d.pop("mapType"))

        domino_project_id = d.pop("dominoProjectId")

        updated_at = d.pop("updatedAt")

        ticket_metadata = DominoProjectManagementApiPmTicketMetadata.from_dict(d.pop("ticketMetadata"))

        ticket_stages = []
        _ticket_stages = d.pop("ticketStages")
        for ticket_stages_item_data in _ticket_stages:
            ticket_stages_item = DominoProjectManagementApiPmTicketStage.from_dict(ticket_stages_item_data)

            ticket_stages.append(ticket_stages_item)

        _ticket_assignee = d.pop("ticketAssignee", UNSET)
        ticket_assignee: DominoProjectManagementApiPmUser | Unset
        if isinstance(_ticket_assignee, Unset):
            ticket_assignee = UNSET
        else:
            ticket_assignee = DominoProjectManagementApiPmUser.from_dict(_ticket_assignee)

        domino_project_management_api_domino_goal_to_pm_sub_ticket_metadata = cls(
            map_type=map_type,
            domino_project_id=domino_project_id,
            updated_at=updated_at,
            ticket_metadata=ticket_metadata,
            ticket_stages=ticket_stages,
            ticket_assignee=ticket_assignee,
        )

        domino_project_management_api_domino_goal_to_pm_sub_ticket_metadata.additional_properties = d
        return domino_project_management_api_domino_goal_to_pm_sub_ticket_metadata

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
