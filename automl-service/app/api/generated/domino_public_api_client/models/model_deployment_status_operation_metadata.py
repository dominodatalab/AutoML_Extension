from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelDeploymentStatusOperationMetadata")


@_attrs_define
class ModelDeploymentStatusOperationMetadata:
    """This field provides metadata needed for an API user to invoke the operation.

    Attributes:
        operations (list[str]):
        type_ (str):
        service (str | Unset):
    """

    operations: list[str]
    type_: str
    service: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operations = self.operations

        type_ = self.type_

        service = self.service

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operations": operations,
                "type": type_,
            }
        )
        if service is not UNSET:
            field_dict["service"] = service

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operations = cast(list[str], d.pop("operations"))

        type_ = d.pop("type")

        service = d.pop("service", UNSET)

        model_deployment_status_operation_metadata = cls(
            operations=operations,
            type_=type_,
            service=service,
        )

        model_deployment_status_operation_metadata.additional_properties = d
        return model_deployment_status_operation_metadata

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
