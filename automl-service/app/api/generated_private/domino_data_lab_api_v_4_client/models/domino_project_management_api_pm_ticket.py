from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_project_management_api_pm_comment import DominoProjectManagementApiPmComment
    from ..models.domino_project_management_api_pm_id import DominoProjectManagementApiPmId
    from ..models.domino_project_management_api_pm_ticket_metadata import DominoProjectManagementApiPmTicketMetadata
    from ..models.domino_project_management_api_pm_ticket_stage import DominoProjectManagementApiPmTicketStage
    from ..models.domino_project_management_api_pm_ticket_type import DominoProjectManagementApiPmTicketType
    from ..models.domino_project_management_api_pm_user import DominoProjectManagementApiPmUser


T = TypeVar("T", bound="DominoProjectManagementApiPmTicket")


@_attrs_define
class DominoProjectManagementApiPmTicket:
    """
    Attributes:
        id (DominoProjectManagementApiPmId):
        ticket_type (DominoProjectManagementApiPmTicketType):
        stage (DominoProjectManagementApiPmTicketStage):
        title (str):
        comments (list[DominoProjectManagementApiPmComment]):
        ticket_metadata (DominoProjectManagementApiPmTicketMetadata):
        updated_at (int):
        sub_tickets (list[DominoProjectManagementApiPmTicket]):
        description (None | str | Unset):
        assignee (DominoProjectManagementApiPmUser | Unset):
    """

    id: DominoProjectManagementApiPmId
    ticket_type: DominoProjectManagementApiPmTicketType
    stage: DominoProjectManagementApiPmTicketStage
    title: str
    comments: list[DominoProjectManagementApiPmComment]
    ticket_metadata: DominoProjectManagementApiPmTicketMetadata
    updated_at: int
    sub_tickets: list[DominoProjectManagementApiPmTicket]
    description: None | str | Unset = UNSET
    assignee: DominoProjectManagementApiPmUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id.to_dict()

        ticket_type = self.ticket_type.to_dict()

        stage = self.stage.to_dict()

        title = self.title

        comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()
            comments.append(comments_item)

        ticket_metadata = self.ticket_metadata.to_dict()

        updated_at = self.updated_at

        sub_tickets = []
        for sub_tickets_item_data in self.sub_tickets:
            sub_tickets_item = sub_tickets_item_data.to_dict()
            sub_tickets.append(sub_tickets_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ticketType": ticket_type,
                "stage": stage,
                "title": title,
                "comments": comments,
                "ticketMetadata": ticket_metadata,
                "updatedAt": updated_at,
                "subTickets": sub_tickets,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if assignee is not UNSET:
            field_dict["assignee"] = assignee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_project_management_api_pm_comment import DominoProjectManagementApiPmComment
        from ..models.domino_project_management_api_pm_id import DominoProjectManagementApiPmId
        from ..models.domino_project_management_api_pm_ticket_metadata import DominoProjectManagementApiPmTicketMetadata
        from ..models.domino_project_management_api_pm_ticket_stage import DominoProjectManagementApiPmTicketStage
        from ..models.domino_project_management_api_pm_ticket_type import DominoProjectManagementApiPmTicketType
        from ..models.domino_project_management_api_pm_user import DominoProjectManagementApiPmUser

        d = dict(src_dict)
        id = DominoProjectManagementApiPmId.from_dict(d.pop("id"))

        ticket_type = DominoProjectManagementApiPmTicketType.from_dict(d.pop("ticketType"))

        stage = DominoProjectManagementApiPmTicketStage.from_dict(d.pop("stage"))

        title = d.pop("title")

        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = DominoProjectManagementApiPmComment.from_dict(comments_item_data)

            comments.append(comments_item)

        ticket_metadata = DominoProjectManagementApiPmTicketMetadata.from_dict(d.pop("ticketMetadata"))

        updated_at = d.pop("updatedAt")

        sub_tickets = []
        _sub_tickets = d.pop("subTickets")
        for sub_tickets_item_data in _sub_tickets:
            sub_tickets_item = DominoProjectManagementApiPmTicket.from_dict(sub_tickets_item_data)

            sub_tickets.append(sub_tickets_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _assignee = d.pop("assignee", UNSET)
        assignee: DominoProjectManagementApiPmUser | Unset
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = DominoProjectManagementApiPmUser.from_dict(_assignee)

        domino_project_management_api_pm_ticket = cls(
            id=id,
            ticket_type=ticket_type,
            stage=stage,
            title=title,
            comments=comments,
            ticket_metadata=ticket_metadata,
            updated_at=updated_at,
            sub_tickets=sub_tickets,
            description=description,
            assignee=assignee,
        )

        domino_project_management_api_pm_ticket.additional_properties = d
        return domino_project_management_api_pm_ticket

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
