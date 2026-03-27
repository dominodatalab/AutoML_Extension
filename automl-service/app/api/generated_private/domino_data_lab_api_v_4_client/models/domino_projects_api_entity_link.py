from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_entity_link_entity_link_type import DominoProjectsApiEntityLinkEntityLinkType

T = TypeVar("T", bound="DominoProjectsApiEntityLink")


@_attrs_define
class DominoProjectsApiEntityLink:
    """
    Attributes:
        entity_link_type (DominoProjectsApiEntityLinkEntityLinkType):
        metadata (Any):
        timestamp (int):
        created_by (str):
    """

    entity_link_type: DominoProjectsApiEntityLinkEntityLinkType
    metadata: Any
    timestamp: int
    created_by: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_link_type = self.entity_link_type.value

        metadata = self.metadata

        timestamp = self.timestamp

        created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entityLinkType": entity_link_type,
                "metadata": metadata,
                "timestamp": timestamp,
                "createdBy": created_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_link_type = DominoProjectsApiEntityLinkEntityLinkType(d.pop("entityLinkType"))

        metadata = d.pop("metadata")

        timestamp = d.pop("timestamp")

        created_by = d.pop("createdBy")

        domino_projects_api_entity_link = cls(
            entity_link_type=entity_link_type,
            metadata=metadata,
            timestamp=timestamp,
            created_by=created_by,
        )

        domino_projects_api_entity_link.additional_properties = d
        return domino_projects_api_entity_link

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
