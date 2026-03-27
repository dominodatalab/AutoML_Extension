from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_files_interface_credential_mappings import DominoFilesInterfaceCredentialMappings
    from ..models.domino_files_interface_files_permissions_dto import DominoFilesInterfaceFilesPermissionsDto
    from ..models.domino_files_interface_git_credentials import DominoFilesInterfaceGitCredentials
    from ..models.domino_files_interface_repository_view_model_dto import DominoFilesInterfaceRepositoryViewModelDto
    from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO


T = TypeVar("T", bound="DominoFilesInterfaceProjectGitBrowseDto")


@_attrs_define
class DominoFilesInterfaceProjectGitBrowseDto:
    """
    Attributes:
        are_references_customizable (bool):
        repositories (list[DominoFilesInterfaceRepositoryViewModelDto]):
        project_id (str):
        no_repos (bool):
        project_type (str):
        git_credentials (list[DominoFilesInterfaceGitCredentials]):
        all_credential_mappings (list[DominoFilesInterfaceCredentialMappings]):
        permissions (DominoFilesInterfaceFilesPermissionsDto):
        project_main_repository_id (None | str | Unset):
        project_main_repository_uri (None | str | Unset):
        project_main_repository_default_ref_type (None | str | Unset):
        project_main_repository_default_ref_value (None | str | Unset):
        project_main_repository_service_provider (None | str | Unset):
        project_default_branch (DominoProjectsApiRepositoriesReferenceDTO | Unset):
        csrf_token (None | str | Unset):
    """

    are_references_customizable: bool
    repositories: list[DominoFilesInterfaceRepositoryViewModelDto]
    project_id: str
    no_repos: bool
    project_type: str
    git_credentials: list[DominoFilesInterfaceGitCredentials]
    all_credential_mappings: list[DominoFilesInterfaceCredentialMappings]
    permissions: DominoFilesInterfaceFilesPermissionsDto
    project_main_repository_id: None | str | Unset = UNSET
    project_main_repository_uri: None | str | Unset = UNSET
    project_main_repository_default_ref_type: None | str | Unset = UNSET
    project_main_repository_default_ref_value: None | str | Unset = UNSET
    project_main_repository_service_provider: None | str | Unset = UNSET
    project_default_branch: DominoProjectsApiRepositoriesReferenceDTO | Unset = UNSET
    csrf_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        are_references_customizable = self.are_references_customizable

        repositories = []
        for repositories_item_data in self.repositories:
            repositories_item = repositories_item_data.to_dict()
            repositories.append(repositories_item)

        project_id = self.project_id

        no_repos = self.no_repos

        project_type = self.project_type

        git_credentials = []
        for git_credentials_item_data in self.git_credentials:
            git_credentials_item = git_credentials_item_data.to_dict()
            git_credentials.append(git_credentials_item)

        all_credential_mappings = []
        for all_credential_mappings_item_data in self.all_credential_mappings:
            all_credential_mappings_item = all_credential_mappings_item_data.to_dict()
            all_credential_mappings.append(all_credential_mappings_item)

        permissions = self.permissions.to_dict()

        project_main_repository_id: None | str | Unset
        if isinstance(self.project_main_repository_id, Unset):
            project_main_repository_id = UNSET
        else:
            project_main_repository_id = self.project_main_repository_id

        project_main_repository_uri: None | str | Unset
        if isinstance(self.project_main_repository_uri, Unset):
            project_main_repository_uri = UNSET
        else:
            project_main_repository_uri = self.project_main_repository_uri

        project_main_repository_default_ref_type: None | str | Unset
        if isinstance(self.project_main_repository_default_ref_type, Unset):
            project_main_repository_default_ref_type = UNSET
        else:
            project_main_repository_default_ref_type = self.project_main_repository_default_ref_type

        project_main_repository_default_ref_value: None | str | Unset
        if isinstance(self.project_main_repository_default_ref_value, Unset):
            project_main_repository_default_ref_value = UNSET
        else:
            project_main_repository_default_ref_value = self.project_main_repository_default_ref_value

        project_main_repository_service_provider: None | str | Unset
        if isinstance(self.project_main_repository_service_provider, Unset):
            project_main_repository_service_provider = UNSET
        else:
            project_main_repository_service_provider = self.project_main_repository_service_provider

        project_default_branch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_default_branch, Unset):
            project_default_branch = self.project_default_branch.to_dict()

        csrf_token: None | str | Unset
        if isinstance(self.csrf_token, Unset):
            csrf_token = UNSET
        else:
            csrf_token = self.csrf_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "areReferencesCustomizable": are_references_customizable,
                "repositories": repositories,
                "projectId": project_id,
                "noRepos": no_repos,
                "projectType": project_type,
                "gitCredentials": git_credentials,
                "allCredentialMappings": all_credential_mappings,
                "permissions": permissions,
            }
        )
        if project_main_repository_id is not UNSET:
            field_dict["projectMainRepositoryId"] = project_main_repository_id
        if project_main_repository_uri is not UNSET:
            field_dict["projectMainRepositoryUri"] = project_main_repository_uri
        if project_main_repository_default_ref_type is not UNSET:
            field_dict["projectMainRepositoryDefaultRefType"] = project_main_repository_default_ref_type
        if project_main_repository_default_ref_value is not UNSET:
            field_dict["projectMainRepositoryDefaultRefValue"] = project_main_repository_default_ref_value
        if project_main_repository_service_provider is not UNSET:
            field_dict["projectMainRepositoryServiceProvider"] = project_main_repository_service_provider
        if project_default_branch is not UNSET:
            field_dict["projectDefaultBranch"] = project_default_branch
        if csrf_token is not UNSET:
            field_dict["csrfToken"] = csrf_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_files_interface_credential_mappings import DominoFilesInterfaceCredentialMappings
        from ..models.domino_files_interface_files_permissions_dto import DominoFilesInterfaceFilesPermissionsDto
        from ..models.domino_files_interface_git_credentials import DominoFilesInterfaceGitCredentials
        from ..models.domino_files_interface_repository_view_model_dto import DominoFilesInterfaceRepositoryViewModelDto
        from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO

        d = dict(src_dict)
        are_references_customizable = d.pop("areReferencesCustomizable")

        repositories = []
        _repositories = d.pop("repositories")
        for repositories_item_data in _repositories:
            repositories_item = DominoFilesInterfaceRepositoryViewModelDto.from_dict(repositories_item_data)

            repositories.append(repositories_item)

        project_id = d.pop("projectId")

        no_repos = d.pop("noRepos")

        project_type = d.pop("projectType")

        git_credentials = []
        _git_credentials = d.pop("gitCredentials")
        for git_credentials_item_data in _git_credentials:
            git_credentials_item = DominoFilesInterfaceGitCredentials.from_dict(git_credentials_item_data)

            git_credentials.append(git_credentials_item)

        all_credential_mappings = []
        _all_credential_mappings = d.pop("allCredentialMappings")
        for all_credential_mappings_item_data in _all_credential_mappings:
            all_credential_mappings_item = DominoFilesInterfaceCredentialMappings.from_dict(
                all_credential_mappings_item_data
            )

            all_credential_mappings.append(all_credential_mappings_item)

        permissions = DominoFilesInterfaceFilesPermissionsDto.from_dict(d.pop("permissions"))

        def _parse_project_main_repository_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_main_repository_id = _parse_project_main_repository_id(d.pop("projectMainRepositoryId", UNSET))

        def _parse_project_main_repository_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_main_repository_uri = _parse_project_main_repository_uri(d.pop("projectMainRepositoryUri", UNSET))

        def _parse_project_main_repository_default_ref_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_main_repository_default_ref_type = _parse_project_main_repository_default_ref_type(
            d.pop("projectMainRepositoryDefaultRefType", UNSET)
        )

        def _parse_project_main_repository_default_ref_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_main_repository_default_ref_value = _parse_project_main_repository_default_ref_value(
            d.pop("projectMainRepositoryDefaultRefValue", UNSET)
        )

        def _parse_project_main_repository_service_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_main_repository_service_provider = _parse_project_main_repository_service_provider(
            d.pop("projectMainRepositoryServiceProvider", UNSET)
        )

        _project_default_branch = d.pop("projectDefaultBranch", UNSET)
        project_default_branch: DominoProjectsApiRepositoriesReferenceDTO | Unset
        if isinstance(_project_default_branch, Unset):
            project_default_branch = UNSET
        else:
            project_default_branch = DominoProjectsApiRepositoriesReferenceDTO.from_dict(_project_default_branch)

        def _parse_csrf_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        csrf_token = _parse_csrf_token(d.pop("csrfToken", UNSET))

        domino_files_interface_project_git_browse_dto = cls(
            are_references_customizable=are_references_customizable,
            repositories=repositories,
            project_id=project_id,
            no_repos=no_repos,
            project_type=project_type,
            git_credentials=git_credentials,
            all_credential_mappings=all_credential_mappings,
            permissions=permissions,
            project_main_repository_id=project_main_repository_id,
            project_main_repository_uri=project_main_repository_uri,
            project_main_repository_default_ref_type=project_main_repository_default_ref_type,
            project_main_repository_default_ref_value=project_main_repository_default_ref_value,
            project_main_repository_service_provider=project_main_repository_service_provider,
            project_default_branch=project_default_branch,
            csrf_token=csrf_token,
        )

        domino_files_interface_project_git_browse_dto.additional_properties = d
        return domino_files_interface_project_git_browse_dto

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
