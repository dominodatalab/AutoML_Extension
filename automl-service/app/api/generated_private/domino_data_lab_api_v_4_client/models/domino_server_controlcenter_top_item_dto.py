from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoServerControlcenterTopItemDTO")


@_attrs_define
class DominoServerControlcenterTopItemDTO:
    """Represents one of the values for some object for which a specific metric has one of the top values

    Attributes:
        unit (str): What units this value is in (e.g., "$", "hours")
        name (str): Name of the object for which this metric is at the top
        id (str): Unique identifier of the ranked metric value
        value (float): What is the current value of this metric
        variation (float): Derivative of the value between the previous state and current
        username (None | str | Unset):
    """

    unit: str
    name: str
    id: str
    value: float
    variation: float
    username: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit = self.unit

        name = self.name

        id = self.id

        value = self.value

        variation = self.variation

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unit": unit,
                "name": name,
                "id": id,
                "value": value,
                "variation": variation,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unit = d.pop("unit")

        name = d.pop("name")

        id = d.pop("id")

        value = d.pop("value")

        variation = d.pop("variation")

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        domino_server_controlcenter_top_item_dto = cls(
            unit=unit,
            name=name,
            id=id,
            value=value,
            variation=variation,
            username=username,
        )

        domino_server_controlcenter_top_item_dto.additional_properties = d
        return domino_server_controlcenter_top_item_dto

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
