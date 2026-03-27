from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_project_management_api_domino_entity import DominoProjectManagementApiDominoEntity
    from ..models.domino_project_management_api_domino_project_to_pm_ticket_metadata import (
        DominoProjectManagementApiDominoProjectToPmTicketMetadata,
    )
    from ..models.domino_project_management_api_pm_entity import DominoProjectManagementApiPmEntity


T = TypeVar("T", bound="DominoProjectManagementApiTicketToDominoMapper")


@_attrs_define
class DominoProjectManagementApiTicketToDominoMapper:
    """
    Attributes:
        domino_entity (DominoProjectManagementApiDominoEntity):
        pm_entity (DominoProjectManagementApiPmEntity):
        metadata (DominoProjectManagementApiDominoProjectToPmTicketMetadata):
        is_deleted (bool):
    """

    domino_entity: DominoProjectManagementApiDominoEntity
    pm_entity: DominoProjectManagementApiPmEntity
    metadata: DominoProjectManagementApiDominoProjectToPmTicketMetadata
    is_deleted: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domino_entity = self.domino_entity.to_dict()

        pm_entity = self.pm_entity.to_dict()

        metadata = self.metadata.to_dict()

        is_deleted = self.is_deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dominoEntity": domino_entity,
                "pmEntity": pm_entity,
                "metadata": metadata,
                "isDeleted": is_deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_project_management_api_domino_entity import DominoProjectManagementApiDominoEntity
        from ..models.domino_project_management_api_domino_project_to_pm_ticket_metadata import (
            DominoProjectManagementApiDominoProjectToPmTicketMetadata,
        )
        from ..models.domino_project_management_api_pm_entity import DominoProjectManagementApiPmEntity

        d = dict(src_dict)
        domino_entity = DominoProjectManagementApiDominoEntity.from_dict(d.pop("dominoEntity"))

        pm_entity = DominoProjectManagementApiPmEntity.from_dict(d.pop("pmEntity"))

        metadata = DominoProjectManagementApiDominoProjectToPmTicketMetadata.from_dict(d.pop("metadata"))

        is_deleted = d.pop("isDeleted")

        domino_project_management_api_ticket_to_domino_mapper = cls(
            domino_entity=domino_entity,
            pm_entity=pm_entity,
            metadata=metadata,
            is_deleted=is_deleted,
        )

        domino_project_management_api_ticket_to_domino_mapper.additional_properties = d
        return domino_project_management_api_ticket_to_domino_mapper

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
