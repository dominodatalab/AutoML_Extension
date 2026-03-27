from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_single_project_permission_result import (
        DominoProjectsApiSingleProjectPermissionResult,
    )


T = TypeVar("T", bound="DominoProjectsApiProjectPermissionsResult")


@_attrs_define
class DominoProjectsApiProjectPermissionsResult:
    """
    Attributes:
        can_classify_projects (bool):
        can_create_projects (bool):
        current_project_permissions (DominoProjectsApiSingleProjectPermissionResult | Unset):
    """

    can_classify_projects: bool
    can_create_projects: bool
    current_project_permissions: DominoProjectsApiSingleProjectPermissionResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_classify_projects = self.can_classify_projects

        can_create_projects = self.can_create_projects

        current_project_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_project_permissions, Unset):
            current_project_permissions = self.current_project_permissions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "canClassifyProjects": can_classify_projects,
                "canCreateProjects": can_create_projects,
            }
        )
        if current_project_permissions is not UNSET:
            field_dict["currentProjectPermissions"] = current_project_permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_single_project_permission_result import (
            DominoProjectsApiSingleProjectPermissionResult,
        )

        d = dict(src_dict)
        can_classify_projects = d.pop("canClassifyProjects")

        can_create_projects = d.pop("canCreateProjects")

        _current_project_permissions = d.pop("currentProjectPermissions", UNSET)
        current_project_permissions: DominoProjectsApiSingleProjectPermissionResult | Unset
        if isinstance(_current_project_permissions, Unset):
            current_project_permissions = UNSET
        else:
            current_project_permissions = DominoProjectsApiSingleProjectPermissionResult.from_dict(
                _current_project_permissions
            )

        domino_projects_api_project_permissions_result = cls(
            can_classify_projects=can_classify_projects,
            can_create_projects=can_create_projects,
            current_project_permissions=current_project_permissions,
        )

        domino_projects_api_project_permissions_result.additional_properties = d
        return domino_projects_api_project_permissions_result

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
