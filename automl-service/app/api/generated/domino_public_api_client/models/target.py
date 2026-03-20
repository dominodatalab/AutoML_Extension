from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.entity import Entity
    from ..models.field_state_change import FieldStateChange


T = TypeVar("T", bound="Target")


@_attrs_define
class Target:
    """
    Attributes:
        entity (Entity):
        field_changes (list[FieldStateChange]):
    """

    entity: Entity
    field_changes: list[FieldStateChange]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.field_state_change import FieldStateChange

        entity = self.entity.to_dict()

        field_changes = []
        for field_changes_item_data in self.field_changes:
            field_changes_item: dict[str, Any]
            if isinstance(field_changes_item_data, FieldStateChange):
                field_changes_item = field_changes_item_data.to_dict()

            field_changes.append(field_changes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity": entity,
                "fieldChanges": field_changes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity import Entity
        from ..models.field_state_change import FieldStateChange

        d = dict(src_dict)
        entity = Entity.from_dict(d.pop("entity"))

        field_changes = []
        _field_changes = d.pop("fieldChanges")
        for field_changes_item_data in _field_changes:

            def _parse_field_changes_item(data: object) -> FieldStateChange:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_polymorphic_field_state_change_type_0 = FieldStateChange.from_dict(data)

                return componentsschemas_polymorphic_field_state_change_type_0

            field_changes_item = _parse_field_changes_item(field_changes_item_data)

            field_changes.append(field_changes_item)

        target = cls(
            entity=entity,
            field_changes=field_changes,
        )

        target.additional_properties = d
        return target

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
