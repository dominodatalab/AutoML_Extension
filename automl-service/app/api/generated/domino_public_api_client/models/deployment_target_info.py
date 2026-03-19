from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeploymentTargetInfo")


@_attrs_define
class DeploymentTargetInfo:
    """Information about a Deployment Target and its corresponding Deployment Target Type

    Attributes:
        id (str): Id of the Deployment Target Example: ABC-123.
        name (str): Name of the Deployment Target Example: Production.
        type_name (str): Name of the Deployment Target Type Example: AWS SageMaker.
    """

    id: str
    name: str
    type_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_name = self.type_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "typeName": type_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_name = d.pop("typeName")

        deployment_target_info = cls(
            id=id,
            name=name,
            type_name=type_name,
        )

        deployment_target_info.additional_properties = d
        return deployment_target_info

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
