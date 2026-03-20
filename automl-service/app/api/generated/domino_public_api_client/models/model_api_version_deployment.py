from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelApiVersionDeployment")


@_attrs_define
class ModelApiVersionDeployment:
    """
    Attributes:
        is_pending (bool): Whether the Model API Version deployment is pending.
        status (str): The status of the Model API Version deployment.
    """

    is_pending: bool
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_pending = self.is_pending

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isPending": is_pending,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_pending = d.pop("isPending")

        status = d.pop("status")

        model_api_version_deployment = cls(
            is_pending=is_pending,
            status=status,
        )

        model_api_version_deployment.additional_properties = d
        return model_api_version_deployment

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
