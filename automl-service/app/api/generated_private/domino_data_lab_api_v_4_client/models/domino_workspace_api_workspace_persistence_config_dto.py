from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoWorkspaceApiWorkspacePersistenceConfigDto")


@_attrs_define
class DominoWorkspaceApiWorkspacePersistenceConfigDto:
    """
    Attributes:
        persist_packages (bool):
        persist_home_directory (bool):
    """

    persist_packages: bool
    persist_home_directory: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        persist_packages = self.persist_packages

        persist_home_directory = self.persist_home_directory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "persistPackages": persist_packages,
                "persistHomeDirectory": persist_home_directory,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        persist_packages = d.pop("persistPackages")

        persist_home_directory = d.pop("persistHomeDirectory")

        domino_workspace_api_workspace_persistence_config_dto = cls(
            persist_packages=persist_packages,
            persist_home_directory=persist_home_directory,
        )

        domino_workspace_api_workspace_persistence_config_dto.additional_properties = d
        return domino_workspace_api_workspace_persistence_config_dto

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
