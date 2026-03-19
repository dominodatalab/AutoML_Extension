from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action import Action
    from ..models.actor import Actor
    from ..models.entity import Entity
    from ..models.string_string_map import StringStringMap
    from ..models.target import Target


T = TypeVar("T", bound="AuditEvent")


@_attrs_define
class AuditEvent:
    """
    Attributes:
        action (Action):
        actor (Actor):
        affecting (list[Entity]):
        metadata (StringStringMap):
        targets (list[Target]):
        timestamp (int):
        from_ (Entity | Unset):
        in_ (Entity | Unset):
        to (Entity | Unset):
    """

    action: Action
    actor: Actor
    affecting: list[Entity]
    metadata: StringStringMap
    targets: list[Target]
    timestamp: int
    from_: Entity | Unset = UNSET
    in_: Entity | Unset = UNSET
    to: Entity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.to_dict()

        actor = self.actor.to_dict()

        affecting = []
        for componentsschemas_affecting_item_data in self.affecting:
            componentsschemas_affecting_item = componentsschemas_affecting_item_data.to_dict()
            affecting.append(componentsschemas_affecting_item)

        metadata = self.metadata.to_dict()

        targets = []
        for componentsschemas_target_list_item_data in self.targets:
            componentsschemas_target_list_item = componentsschemas_target_list_item_data.to_dict()
            targets.append(componentsschemas_target_list_item)

        timestamp = self.timestamp

        from_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        in_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.in_, Unset):
            in_ = self.in_.to_dict()

        to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "actor": actor,
                "affecting": affecting,
                "metadata": metadata,
                "targets": targets,
                "timestamp": timestamp,
            }
        )
        if from_ is not UNSET:
            field_dict["from"] = from_
        if in_ is not UNSET:
            field_dict["in"] = in_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action import Action
        from ..models.actor import Actor
        from ..models.entity import Entity
        from ..models.string_string_map import StringStringMap
        from ..models.target import Target

        d = dict(src_dict)
        action = Action.from_dict(d.pop("action"))

        actor = Actor.from_dict(d.pop("actor"))

        affecting = []
        _affecting = d.pop("affecting")
        for componentsschemas_affecting_item_data in _affecting:
            componentsschemas_affecting_item = Entity.from_dict(componentsschemas_affecting_item_data)

            affecting.append(componentsschemas_affecting_item)

        metadata = StringStringMap.from_dict(d.pop("metadata"))

        targets = []
        _targets = d.pop("targets")
        for componentsschemas_target_list_item_data in _targets:
            componentsschemas_target_list_item = Target.from_dict(componentsschemas_target_list_item_data)

            targets.append(componentsschemas_target_list_item)

        timestamp = d.pop("timestamp")

        _from_ = d.pop("from", UNSET)
        from_: Entity | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = Entity.from_dict(_from_)

        _in_ = d.pop("in", UNSET)
        in_: Entity | Unset
        if isinstance(_in_, Unset):
            in_ = UNSET
        else:
            in_ = Entity.from_dict(_in_)

        _to = d.pop("to", UNSET)
        to: Entity | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = Entity.from_dict(_to)

        audit_event = cls(
            action=action,
            actor=actor,
            affecting=affecting,
            metadata=metadata,
            targets=targets,
            timestamp=timestamp,
            from_=from_,
            in_=in_,
            to=to,
        )

        audit_event.additional_properties = d
        return audit_event

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
