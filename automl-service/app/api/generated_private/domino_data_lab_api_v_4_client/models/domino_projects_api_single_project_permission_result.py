from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProjectsApiSingleProjectPermissionResult")


@_attrs_define
class DominoProjectsApiSingleProjectPermissionResult:
    """
    Attributes:
        can_fork (bool):
        can_copy (bool):
    """

    can_fork: bool
    can_copy: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_fork = self.can_fork

        can_copy = self.can_copy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "canFork": can_fork,
                "canCopy": can_copy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_fork = d.pop("canFork")

        can_copy = d.pop("canCopy")

        domino_projects_api_single_project_permission_result = cls(
            can_fork=can_fork,
            can_copy=can_copy,
        )

        domino_projects_api_single_project_permission_result.additional_properties = d
        return domino_projects_api_single_project_permission_result

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
