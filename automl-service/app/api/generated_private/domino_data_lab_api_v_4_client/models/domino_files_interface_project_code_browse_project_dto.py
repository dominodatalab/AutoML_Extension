from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_files_interface_git_repo import DominoFilesInterfaceGitRepo


T = TypeVar("T", bound="DominoFilesInterfaceProjectCodeBrowseProjectDto")


@_attrs_define
class DominoFilesInterfaceProjectCodeBrowseProjectDto:
    """
    Attributes:
        project_id (str):
        project_visibility (str):
        project_type (str):
        is_git_based_project (bool):
        are_data_projects_enabled (bool):
        is_analytic_project (bool):
        no_repos (bool):
        repositories (list[DominoFilesInterfaceGitRepo]):
    """

    project_id: str
    project_visibility: str
    project_type: str
    is_git_based_project: bool
    are_data_projects_enabled: bool
    is_analytic_project: bool
    no_repos: bool
    repositories: list[DominoFilesInterfaceGitRepo]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        project_visibility = self.project_visibility

        project_type = self.project_type

        is_git_based_project = self.is_git_based_project

        are_data_projects_enabled = self.are_data_projects_enabled

        is_analytic_project = self.is_analytic_project

        no_repos = self.no_repos

        repositories = []
        for repositories_item_data in self.repositories:
            repositories_item = repositories_item_data.to_dict()
            repositories.append(repositories_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "projectVisibility": project_visibility,
                "projectType": project_type,
                "isGitBasedProject": is_git_based_project,
                "areDataProjectsEnabled": are_data_projects_enabled,
                "isAnalyticProject": is_analytic_project,
                "noRepos": no_repos,
                "repositories": repositories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_files_interface_git_repo import DominoFilesInterfaceGitRepo

        d = dict(src_dict)
        project_id = d.pop("projectId")

        project_visibility = d.pop("projectVisibility")

        project_type = d.pop("projectType")

        is_git_based_project = d.pop("isGitBasedProject")

        are_data_projects_enabled = d.pop("areDataProjectsEnabled")

        is_analytic_project = d.pop("isAnalyticProject")

        no_repos = d.pop("noRepos")

        repositories = []
        _repositories = d.pop("repositories")
        for repositories_item_data in _repositories:
            repositories_item = DominoFilesInterfaceGitRepo.from_dict(repositories_item_data)

            repositories.append(repositories_item)

        domino_files_interface_project_code_browse_project_dto = cls(
            project_id=project_id,
            project_visibility=project_visibility,
            project_type=project_type,
            is_git_based_project=is_git_based_project,
            are_data_projects_enabled=are_data_projects_enabled,
            is_analytic_project=is_analytic_project,
            no_repos=no_repos,
            repositories=repositories,
        )

        domino_files_interface_project_code_browse_project_dto.additional_properties = d
        return domino_files_interface_project_code_browse_project_dto

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
