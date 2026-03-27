from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_nucleus_gateway_users_models_project_dependency_view_project_type import (
    DominoNucleusGatewayUsersModelsProjectDependencyViewProjectType,
)

if TYPE_CHECKING:
    from ..models.domino_common_project_id import DominoCommonProjectId


T = TypeVar("T", bound="DominoNucleusGatewayUsersModelsProjectDependencyView")


@_attrs_define
class DominoNucleusGatewayUsersModelsProjectDependencyView:
    """
    Attributes:
        project_id (DominoCommonProjectId):
        project_type (DominoNucleusGatewayUsersModelsProjectDependencyViewProjectType):
        dependencies (list[DominoCommonProjectId]):
    """

    project_id: DominoCommonProjectId
    project_type: DominoNucleusGatewayUsersModelsProjectDependencyViewProjectType
    dependencies: list[DominoCommonProjectId]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id.to_dict()

        project_type = self.project_type.value

        dependencies = []
        for dependencies_item_data in self.dependencies:
            dependencies_item = dependencies_item_data.to_dict()
            dependencies.append(dependencies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "projectType": project_type,
                "dependencies": dependencies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_project_id import DominoCommonProjectId

        d = dict(src_dict)
        project_id = DominoCommonProjectId.from_dict(d.pop("projectId"))

        project_type = DominoNucleusGatewayUsersModelsProjectDependencyViewProjectType(d.pop("projectType"))

        dependencies = []
        _dependencies = d.pop("dependencies")
        for dependencies_item_data in _dependencies:
            dependencies_item = DominoCommonProjectId.from_dict(dependencies_item_data)

            dependencies.append(dependencies_item)

        domino_nucleus_gateway_users_models_project_dependency_view = cls(
            project_id=project_id,
            project_type=project_type,
            dependencies=dependencies,
        )

        domino_nucleus_gateway_users_models_project_dependency_view.additional_properties = d
        return domino_nucleus_gateway_users_models_project_dependency_view

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
