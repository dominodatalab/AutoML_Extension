from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_project_management_api_pm_entity_entity_type import DominoProjectManagementApiPmEntityEntityType

if TYPE_CHECKING:
    from ..models.domino_project_management_api_pm_id import DominoProjectManagementApiPmId


T = TypeVar("T", bound="DominoProjectManagementApiPmEntity")


@_attrs_define
class DominoProjectManagementApiPmEntity:
    """
    Attributes:
        entity_id (DominoProjectManagementApiPmId):
        entity_type (DominoProjectManagementApiPmEntityEntityType):
    """

    entity_id: DominoProjectManagementApiPmId
    entity_type: DominoProjectManagementApiPmEntityEntityType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_id = self.entity_id.to_dict()

        entity_type = self.entity_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entityId": entity_id,
                "entityType": entity_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_project_management_api_pm_id import DominoProjectManagementApiPmId

        d = dict(src_dict)
        entity_id = DominoProjectManagementApiPmId.from_dict(d.pop("entityId"))

        entity_type = DominoProjectManagementApiPmEntityEntityType(d.pop("entityType"))

        domino_project_management_api_pm_entity = cls(
            entity_id=entity_id,
            entity_type=entity_type,
        )

        domino_project_management_api_pm_entity.additional_properties = d
        return domino_project_management_api_pm_entity

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
