from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cost_activation_status_v1 import CostActivationStatusV1

T = TypeVar("T", bound="CostActivationStatusEnvelopeV1")


@_attrs_define
class CostActivationStatusEnvelopeV1:
    """Activation status of the Domino cost functionality

    Attributes:
        activation (CostActivationStatusV1): Determines the activation state of the Domino cost functionality
    """

    activation: CostActivationStatusV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activation = self.activation.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activation": activation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activation = CostActivationStatusV1(d.pop("activation"))

        cost_activation_status_envelope_v1 = cls(
            activation=activation,
        )

        cost_activation_status_envelope_v1.additional_properties = d
        return cost_activation_status_envelope_v1

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
