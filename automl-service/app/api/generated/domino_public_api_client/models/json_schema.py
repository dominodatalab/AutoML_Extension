from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.json_schema_format import JSONSchemaFormat
from ..models.json_schema_type import JSONSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_schema_properties import JSONSchemaProperties


T = TypeVar("T", bound="JSONSchema")


@_attrs_define
class JSONSchema:
    """Core schema meta-schema

    Attributes:
        additional_properties (JSONSchema | Unset): Core schema meta-schema
        default (Any | Unset):
        description (str | Unset):
        enum (list[Any] | Unset):
        example (Any | Unset):
        format_ (JSONSchemaFormat | Unset): Superset of valid JSON Schema and OpenAPI formats.
        id (str | Unset):
        items (JSONSchema | Unset): Core schema meta-schema
        max_items (int | Unset):
        max_length (int | Unset):
        max_properties (int | Unset):
        maximum (float | Unset):
        min_items (int | Unset):
        min_length (int | Unset):
        min_properties (int | Unset):
        minimum (float | Unset):
        pattern (str | Unset):
        properties (JSONSchemaProperties | Unset):
        required (list[str] | Unset):
        title (str | Unset):
        type_ (JSONSchemaType | Unset):
        unique_items (bool | Unset):  Default: False.
    """

    additional_properties: JSONSchema | Unset = UNSET
    default: Any | Unset = UNSET
    description: str | Unset = UNSET
    enum: list[Any] | Unset = UNSET
    example: Any | Unset = UNSET
    format_: JSONSchemaFormat | Unset = UNSET
    id: str | Unset = UNSET
    items: JSONSchema | Unset = UNSET
    max_items: int | Unset = UNSET
    max_length: int | Unset = UNSET
    max_properties: int | Unset = UNSET
    maximum: float | Unset = UNSET
    min_items: int | Unset = UNSET
    min_length: int | Unset = UNSET
    min_properties: int | Unset = UNSET
    minimum: float | Unset = UNSET
    pattern: str | Unset = UNSET
    properties: JSONSchemaProperties | Unset = UNSET
    required: list[str] | Unset = UNSET
    title: str | Unset = UNSET
    type_: JSONSchemaType | Unset = UNSET
    unique_items: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_properties, Unset):
            additional_properties = self.additional_properties.to_dict()

        default = self.default

        description = self.description

        enum: list[Any] | Unset = UNSET
        if not isinstance(self.enum, Unset):
            enum = self.enum

        example = self.example

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        id = self.id

        items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = self.items.to_dict()

        max_items = self.max_items

        max_length = self.max_length

        max_properties = self.max_properties

        maximum = self.maximum

        min_items = self.min_items

        min_length = self.min_length

        min_properties = self.min_properties

        minimum = self.minimum

        pattern = self.pattern

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        required: list[str] | Unset = UNSET
        if not isinstance(self.required, Unset):
            required = self.required

        title = self.title

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        unique_items = self.unique_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_properties is not UNSET:
            field_dict["additionalProperties"] = additional_properties
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if enum is not UNSET:
            field_dict["enum"] = enum
        if example is not UNSET:
            field_dict["example"] = example
        if format_ is not UNSET:
            field_dict["format"] = format_
        if id is not UNSET:
            field_dict["id"] = id
        if items is not UNSET:
            field_dict["items"] = items
        if max_items is not UNSET:
            field_dict["maxItems"] = max_items
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if max_properties is not UNSET:
            field_dict["maxProperties"] = max_properties
        if maximum is not UNSET:
            field_dict["maximum"] = maximum
        if min_items is not UNSET:
            field_dict["minItems"] = min_items
        if min_length is not UNSET:
            field_dict["minLength"] = min_length
        if min_properties is not UNSET:
            field_dict["minProperties"] = min_properties
        if minimum is not UNSET:
            field_dict["minimum"] = minimum
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if properties is not UNSET:
            field_dict["properties"] = properties
        if required is not UNSET:
            field_dict["required"] = required
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if unique_items is not UNSET:
            field_dict["uniqueItems"] = unique_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_schema_properties import JSONSchemaProperties

        d = dict(src_dict)
        _additional_properties = d.pop("additionalProperties", UNSET)
        additional_properties: JSONSchema | Unset
        if isinstance(_additional_properties, Unset):
            additional_properties = UNSET
        else:
            additional_properties = JSONSchema.from_dict(_additional_properties)

        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        enum = cast(list[Any], d.pop("enum", UNSET))

        example = d.pop("example", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: JSONSchemaFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = JSONSchemaFormat(_format_)

        id = d.pop("id", UNSET)

        _items = d.pop("items", UNSET)
        items: JSONSchema | Unset
        if isinstance(_items, Unset):
            items = UNSET
        else:
            items = JSONSchema.from_dict(_items)

        max_items = d.pop("maxItems", UNSET)

        max_length = d.pop("maxLength", UNSET)

        max_properties = d.pop("maxProperties", UNSET)

        maximum = d.pop("maximum", UNSET)

        min_items = d.pop("minItems", UNSET)

        min_length = d.pop("minLength", UNSET)

        min_properties = d.pop("minProperties", UNSET)

        minimum = d.pop("minimum", UNSET)

        pattern = d.pop("pattern", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: JSONSchemaProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = JSONSchemaProperties.from_dict(_properties)

        required = cast(list[str], d.pop("required", UNSET))

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: JSONSchemaType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = JSONSchemaType(_type_)

        unique_items = d.pop("uniqueItems", UNSET)

        json_schema = cls(
            additional_properties=additional_properties,
            default=default,
            description=description,
            enum=enum,
            example=example,
            format_=format_,
            id=id,
            items=items,
            max_items=max_items,
            max_length=max_length,
            max_properties=max_properties,
            maximum=maximum,
            min_items=min_items,
            min_length=min_length,
            min_properties=min_properties,
            minimum=minimum,
            pattern=pattern,
            properties=properties,
            required=required,
            title=title,
            type_=type_,
            unique_items=unique_items,
        )

        json_schema.additional_properties = d
        return json_schema

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
