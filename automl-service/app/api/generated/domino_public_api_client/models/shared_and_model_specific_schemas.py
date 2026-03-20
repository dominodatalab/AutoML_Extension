from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.json_schema import JSONSchema


T = TypeVar("T", bound="SharedAndModelSpecificSchemas")


@_attrs_define
class SharedAndModelSpecificSchemas:
    """Shared and Model Specific configs.

    Attributes:
        model_specific_schema (JSONSchema): Core schema meta-schema
        shared_schema (JSONSchema): Core schema meta-schema
    """

    model_specific_schema: JSONSchema
    shared_schema: JSONSchema
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_specific_schema = self.model_specific_schema.to_dict()

        shared_schema = self.shared_schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelSpecificSchema": model_specific_schema,
                "sharedSchema": shared_schema,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_schema import JSONSchema

        d = dict(src_dict)
        model_specific_schema = JSONSchema.from_dict(d.pop("modelSpecificSchema"))

        shared_schema = JSONSchema.from_dict(d.pop("sharedSchema"))

        shared_and_model_specific_schemas = cls(
            model_specific_schema=model_specific_schema,
            shared_schema=shared_schema,
        )

        shared_and_model_specific_schemas.additional_properties = d
        return shared_and_model_specific_schemas

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
