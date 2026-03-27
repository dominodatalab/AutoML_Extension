from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_project_management_api_pm_id import DominoProjectManagementApiPmId


T = TypeVar("T", bound="DominoProjectManagementApiPmTicketStage")


@_attrs_define
class DominoProjectManagementApiPmTicketStage:
    """
    Attributes:
        id (DominoProjectManagementApiPmId):
        name (str):
    """

    id: DominoProjectManagementApiPmId
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_project_management_api_pm_id import DominoProjectManagementApiPmId

        d = dict(src_dict)
        id = DominoProjectManagementApiPmId.from_dict(d.pop("id"))

        name = d.pop("name")

        domino_project_management_api_pm_ticket_stage = cls(
            id=id,
            name=name,
        )

        domino_project_management_api_pm_ticket_stage.additional_properties = d
        return domino_project_management_api_pm_ticket_stage

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
