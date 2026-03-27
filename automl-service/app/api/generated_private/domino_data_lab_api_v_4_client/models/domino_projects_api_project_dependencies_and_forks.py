from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_project_info import DominoProjectsApiProjectInfo


T = TypeVar("T", bound="DominoProjectsApiProjectDependenciesAndForks")


@_attrs_define
class DominoProjectsApiProjectDependenciesAndForks:
    """
    Attributes:
        dependencies (list[DominoProjectsApiProjectInfo]):
        related_forks (list[DominoProjectsApiProjectInfo]):
        can_create_review_request (bool):
        can_update_fork (bool):
        base_project (DominoProjectsApiProjectInfo | Unset):
    """

    dependencies: list[DominoProjectsApiProjectInfo]
    related_forks: list[DominoProjectsApiProjectInfo]
    can_create_review_request: bool
    can_update_fork: bool
    base_project: DominoProjectsApiProjectInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dependencies = []
        for dependencies_item_data in self.dependencies:
            dependencies_item = dependencies_item_data.to_dict()
            dependencies.append(dependencies_item)

        related_forks = []
        for related_forks_item_data in self.related_forks:
            related_forks_item = related_forks_item_data.to_dict()
            related_forks.append(related_forks_item)

        can_create_review_request = self.can_create_review_request

        can_update_fork = self.can_update_fork

        base_project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_project, Unset):
            base_project = self.base_project.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dependencies": dependencies,
                "relatedForks": related_forks,
                "canCreateReviewRequest": can_create_review_request,
                "canUpdateFork": can_update_fork,
            }
        )
        if base_project is not UNSET:
            field_dict["baseProject"] = base_project

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_project_info import DominoProjectsApiProjectInfo

        d = dict(src_dict)
        dependencies = []
        _dependencies = d.pop("dependencies")
        for dependencies_item_data in _dependencies:
            dependencies_item = DominoProjectsApiProjectInfo.from_dict(dependencies_item_data)

            dependencies.append(dependencies_item)

        related_forks = []
        _related_forks = d.pop("relatedForks")
        for related_forks_item_data in _related_forks:
            related_forks_item = DominoProjectsApiProjectInfo.from_dict(related_forks_item_data)

            related_forks.append(related_forks_item)

        can_create_review_request = d.pop("canCreateReviewRequest")

        can_update_fork = d.pop("canUpdateFork")

        _base_project = d.pop("baseProject", UNSET)
        base_project: DominoProjectsApiProjectInfo | Unset
        if isinstance(_base_project, Unset):
            base_project = UNSET
        else:
            base_project = DominoProjectsApiProjectInfo.from_dict(_base_project)

        domino_projects_api_project_dependencies_and_forks = cls(
            dependencies=dependencies,
            related_forks=related_forks,
            can_create_review_request=can_create_review_request,
            can_update_fork=can_update_fork,
            base_project=base_project,
        )

        domino_projects_api_project_dependencies_and_forks.additional_properties = d
        return domino_projects_api_project_dependencies_and_forks

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
