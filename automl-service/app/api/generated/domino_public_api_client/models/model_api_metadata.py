from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelApiMetadata")


@_attrs_define
class ModelApiMetadata:
    """
    Attributes:
        created (float): The date when the Model API was created.
        created_by (str): The id of the user that created the Model API.
        last_modified (float): The date when the Model API was last modified.
    """

    created: float
    created_by: str
    last_modified: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        created_by = self.created_by

        last_modified = self.last_modified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "createdBy": created_by,
                "lastModified": last_modified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created")

        created_by = d.pop("createdBy")

        last_modified = d.pop("lastModified")

        model_api_metadata = cls(
            created=created,
            created_by=created_by,
            last_modified=last_modified,
        )

        model_api_metadata.additional_properties = d
        return model_api_metadata

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
