from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_deployment_credentials import ModelDeploymentCredentials


T = TypeVar("T", bound="ModelDeploymentCredentialsList")


@_attrs_define
class ModelDeploymentCredentialsList:
    """
    Attributes:
        items (list[ModelDeploymentCredentials]): The Model Deployments Credentials in the list
    """

    items: list[ModelDeploymentCredentials]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_deployment_credentials import ModelDeploymentCredentials

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ModelDeploymentCredentials.from_dict(items_item_data)

            items.append(items_item)

        model_deployment_credentials_list = cls(
            items=items,
        )

        model_deployment_credentials_list.additional_properties = d
        return model_deployment_credentials_list

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
