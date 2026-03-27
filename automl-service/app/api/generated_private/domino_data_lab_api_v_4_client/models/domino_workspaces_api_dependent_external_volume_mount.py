from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_workspaces_api_volume_mount import DominoWorkspacesApiVolumeMount


T = TypeVar("T", bound="DominoWorkspacesApiDependentExternalVolumeMount")


@_attrs_define
class DominoWorkspacesApiDependentExternalVolumeMount:
    """
    Attributes:
        name (str):
        mount (DominoWorkspacesApiVolumeMount):
    """

    name: str
    mount: DominoWorkspacesApiVolumeMount
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mount = self.mount.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "mount": mount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspaces_api_volume_mount import DominoWorkspacesApiVolumeMount

        d = dict(src_dict)
        name = d.pop("name")

        mount = DominoWorkspacesApiVolumeMount.from_dict(d.pop("mount"))

        domino_workspaces_api_dependent_external_volume_mount = cls(
            name=name,
            mount=mount,
        )

        domino_workspaces_api_dependent_external_volume_mount.additional_properties = d
        return domino_workspaces_api_dependent_external_volume_mount

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
