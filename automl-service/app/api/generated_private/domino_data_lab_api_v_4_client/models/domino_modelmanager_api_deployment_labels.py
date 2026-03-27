from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoModelmanagerApiDeploymentLabels")


@_attrs_define
class DominoModelmanagerApiDeploymentLabels:
    """
    Attributes:
        pod_names (list[str]):
        container_names (list[str]):
    """

    pod_names: list[str]
    container_names: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pod_names = self.pod_names

        container_names = self.container_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "podNames": pod_names,
                "containerNames": container_names,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pod_names = cast(list[str], d.pop("podNames"))

        container_names = cast(list[str], d.pop("containerNames"))

        domino_modelmanager_api_deployment_labels = cls(
            pod_names=pod_names,
            container_names=container_names,
        )

        domino_modelmanager_api_deployment_labels.additional_properties = d
        return domino_modelmanager_api_deployment_labels

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
