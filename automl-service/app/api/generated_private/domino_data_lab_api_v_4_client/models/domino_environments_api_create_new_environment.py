from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_environments_api_new_environment import DominoEnvironmentsApiNewEnvironment
    from ..models.domino_environments_api_new_environment_revision import DominoEnvironmentsApiNewEnvironmentRevision


T = TypeVar("T", bound="DominoEnvironmentsApiCreateNewEnvironment")


@_attrs_define
class DominoEnvironmentsApiCreateNewEnvironment:
    """
    Attributes:
        new_environment (DominoEnvironmentsApiNewEnvironment):
        new_environment_revision (DominoEnvironmentsApiNewEnvironmentRevision):
    """

    new_environment: DominoEnvironmentsApiNewEnvironment
    new_environment_revision: DominoEnvironmentsApiNewEnvironmentRevision
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_environment = self.new_environment.to_dict()

        new_environment_revision = self.new_environment_revision.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "newEnvironment": new_environment,
                "newEnvironmentRevision": new_environment_revision,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_new_environment import DominoEnvironmentsApiNewEnvironment
        from ..models.domino_environments_api_new_environment_revision import (
            DominoEnvironmentsApiNewEnvironmentRevision,
        )

        d = dict(src_dict)
        new_environment = DominoEnvironmentsApiNewEnvironment.from_dict(d.pop("newEnvironment"))

        new_environment_revision = DominoEnvironmentsApiNewEnvironmentRevision.from_dict(
            d.pop("newEnvironmentRevision")
        )

        domino_environments_api_create_new_environment = cls(
            new_environment=new_environment,
            new_environment_revision=new_environment_revision,
        )

        domino_environments_api_create_new_environment.additional_properties = d
        return domino_environments_api_create_new_environment

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
