from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.shared_and_model_specific_schemas import SharedAndModelSpecificSchemas


T = TypeVar("T", bound="DeploymentTypeSpecificSchemas")


@_attrs_define
class DeploymentTypeSpecificSchemas:
    """The supported deployment types.  There must be one property present for each deployment type."""

    additional_properties: dict[str, SharedAndModelSpecificSchemas] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shared_and_model_specific_schemas import SharedAndModelSpecificSchemas

        d = dict(src_dict)
        deployment_type_specific_schemas = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = SharedAndModelSpecificSchemas.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        deployment_type_specific_schemas.additional_properties = additional_properties
        return deployment_type_specific_schemas

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> SharedAndModelSpecificSchemas:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: SharedAndModelSpecificSchemas) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
