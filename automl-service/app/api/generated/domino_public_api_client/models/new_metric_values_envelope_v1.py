from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.new_metric_value_v1 import NewMetricValueV1


T = TypeVar("T", bound="NewMetricValuesEnvelopeV1")


@_attrs_define
class NewMetricValuesEnvelopeV1:
    """
    Attributes:
        new_metric_values (list[NewMetricValueV1]):
    """

    new_metric_values: list[NewMetricValueV1]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_metric_values = []
        for new_metric_values_item_data in self.new_metric_values:
            new_metric_values_item = new_metric_values_item_data.to_dict()
            new_metric_values.append(new_metric_values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "newMetricValues": new_metric_values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_metric_value_v1 import NewMetricValueV1

        d = dict(src_dict)
        new_metric_values = []
        _new_metric_values = d.pop("newMetricValues")
        for new_metric_values_item_data in _new_metric_values:
            new_metric_values_item = NewMetricValueV1.from_dict(new_metric_values_item_data)

            new_metric_values.append(new_metric_values_item)

        new_metric_values_envelope_v1 = cls(
            new_metric_values=new_metric_values,
        )

        new_metric_values_envelope_v1.additional_properties = d
        return new_metric_values_envelope_v1

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
