from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity import Entity


T = TypeVar("T", bound="Action")


@_attrs_define
class Action:
    """
    Attributes:
        event_name (str):
        using (list[Entity]):
        trace_id (str | Unset):
    """

    event_name: str
    using: list[Entity]
    trace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_name = self.event_name

        using = []
        for componentsschemas_using_list_item_data in self.using:
            componentsschemas_using_list_item = componentsschemas_using_list_item_data.to_dict()
            using.append(componentsschemas_using_list_item)

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventName": event_name,
                "using": using,
            }
        )
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity import Entity

        d = dict(src_dict)
        event_name = d.pop("eventName")

        using = []
        _using = d.pop("using")
        for componentsschemas_using_list_item_data in _using:
            componentsschemas_using_list_item = Entity.from_dict(componentsschemas_using_list_item_data)

            using.append(componentsschemas_using_list_item)

        trace_id = d.pop("traceId", UNSET)

        action = cls(
            event_name=event_name,
            using=using,
            trace_id=trace_id,
        )

        action.additional_properties = d
        return action

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
