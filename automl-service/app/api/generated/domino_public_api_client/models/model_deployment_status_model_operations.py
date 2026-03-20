from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_deployment_status_operation import ModelDeploymentStatusOperation


T = TypeVar("T", bound="ModelDeploymentStatusModelOperations")


@_attrs_define
class ModelDeploymentStatusModelOperations:
    """Model-specific operations supported by this model deployment. This field is required with this structure in this
    location for Domino model deployment schemas.

    """

    additional_properties: dict[str, list[ModelDeploymentStatusOperation]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item = additional_property_item_data.to_dict()
                field_dict[prop_name].append(additional_property_item)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_deployment_status_operation import ModelDeploymentStatusOperation

        d = dict(src_dict)
        model_deployment_status_model_operations = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in _additional_property:
                additional_property_item = ModelDeploymentStatusOperation.from_dict(additional_property_item_data)

                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        model_deployment_status_model_operations.additional_properties = additional_properties
        return model_deployment_status_model_operations

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[ModelDeploymentStatusOperation]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[ModelDeploymentStatusOperation]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
