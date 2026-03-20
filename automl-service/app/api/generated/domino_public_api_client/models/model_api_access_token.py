from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelApiAccessToken")


@_attrs_define
class ModelApiAccessToken:
    """
    Attributes:
        created (float): The creation date for the access token.
        created_by (str): The id of the user that created the access token.
        id (str): The id of the access token.
        last_generated (float): The date the access token was last generated.
        last_generated_by (str): The id of the user that last generated the access token.
        name (str | Unset): The name of the access token.
    """

    created: float
    created_by: str
    id: str
    last_generated: float
    last_generated_by: str
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        created_by = self.created_by

        id = self.id

        last_generated = self.last_generated

        last_generated_by = self.last_generated_by

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "createdBy": created_by,
                "id": id,
                "lastGenerated": last_generated,
                "lastGeneratedBy": last_generated_by,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created")

        created_by = d.pop("createdBy")

        id = d.pop("id")

        last_generated = d.pop("lastGenerated")

        last_generated_by = d.pop("lastGeneratedBy")

        name = d.pop("name", UNSET)

        model_api_access_token = cls(
            created=created,
            created_by=created_by,
            id=id,
            last_generated=last_generated,
            last_generated_by=last_generated_by,
            name=name,
        )

        model_api_access_token.additional_properties = d
        return model_api_access_token

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
