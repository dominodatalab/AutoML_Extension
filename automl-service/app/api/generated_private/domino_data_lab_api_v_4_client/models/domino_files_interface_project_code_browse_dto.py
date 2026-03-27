from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_files_interface_credential_mappings import DominoFilesInterfaceCredentialMappings
    from ..models.domino_files_interface_files_browse_settings_dto import DominoFilesInterfaceFilesBrowseSettingsDto
    from ..models.domino_files_interface_files_permissions_dto import DominoFilesInterfaceFilesPermissionsDto
    from ..models.domino_files_interface_git_credentials import DominoFilesInterfaceGitCredentials
    from ..models.domino_files_interface_project_code_browse_commit_dto import (
        DominoFilesInterfaceProjectCodeBrowseCommitDto,
    )
    from ..models.domino_files_interface_project_code_browse_dto_relative_breadcrumb_data_item import (
        DominoFilesInterfaceProjectCodeBrowseDtoRelativeBreadcrumbDataItem,
    )
    from ..models.domino_files_interface_project_code_browse_project_dto import (
        DominoFilesInterfaceProjectCodeBrowseProjectDto,
    )
    from ..models.domino_files_interface_project_imports_dto import DominoFilesInterfaceProjectImportsDto


T = TypeVar("T", bound="DominoFilesInterfaceProjectCodeBrowseDto")


@_attrs_define
class DominoFilesInterfaceProjectCodeBrowseDto:
    """
    Attributes:
        project_imports_is_empty (bool):
        imported_projects (list[DominoFilesInterfaceProjectImportsDto]):
        run_tagging_enabled (bool):
        show_upload_component_on_start (bool):
        suggest_datasets (bool):
        relative_breadcrumb_data (list[DominoFilesInterfaceProjectCodeBrowseDtoRelativeBreadcrumbDataItem]):
        download_cli_page_endpoint (str):
        are_references_customizable (bool):
        all_credential_mappings (list[DominoFilesInterfaceCredentialMappings]):
        git_credentials (list[DominoFilesInterfaceGitCredentials]):
        enable_read_write_datasets (bool):
        permissions (DominoFilesInterfaceFilesPermissionsDto):
        commit_settings (DominoFilesInterfaceProjectCodeBrowseCommitDto):
        project_settings (DominoFilesInterfaceProjectCodeBrowseProjectDto):
        file_settings (DominoFilesInterfaceFilesBrowseSettingsDto):
        previous_directory_url (str):
        csrf_token (None | str | Unset):
    """

    project_imports_is_empty: bool
    imported_projects: list[DominoFilesInterfaceProjectImportsDto]
    run_tagging_enabled: bool
    show_upload_component_on_start: bool
    suggest_datasets: bool
    relative_breadcrumb_data: list[DominoFilesInterfaceProjectCodeBrowseDtoRelativeBreadcrumbDataItem]
    download_cli_page_endpoint: str
    are_references_customizable: bool
    all_credential_mappings: list[DominoFilesInterfaceCredentialMappings]
    git_credentials: list[DominoFilesInterfaceGitCredentials]
    enable_read_write_datasets: bool
    permissions: DominoFilesInterfaceFilesPermissionsDto
    commit_settings: DominoFilesInterfaceProjectCodeBrowseCommitDto
    project_settings: DominoFilesInterfaceProjectCodeBrowseProjectDto
    file_settings: DominoFilesInterfaceFilesBrowseSettingsDto
    previous_directory_url: str
    csrf_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_imports_is_empty = self.project_imports_is_empty

        imported_projects = []
        for imported_projects_item_data in self.imported_projects:
            imported_projects_item = imported_projects_item_data.to_dict()
            imported_projects.append(imported_projects_item)

        run_tagging_enabled = self.run_tagging_enabled

        show_upload_component_on_start = self.show_upload_component_on_start

        suggest_datasets = self.suggest_datasets

        relative_breadcrumb_data = []
        for relative_breadcrumb_data_item_data in self.relative_breadcrumb_data:
            relative_breadcrumb_data_item = relative_breadcrumb_data_item_data.to_dict()
            relative_breadcrumb_data.append(relative_breadcrumb_data_item)

        download_cli_page_endpoint = self.download_cli_page_endpoint

        are_references_customizable = self.are_references_customizable

        all_credential_mappings = []
        for all_credential_mappings_item_data in self.all_credential_mappings:
            all_credential_mappings_item = all_credential_mappings_item_data.to_dict()
            all_credential_mappings.append(all_credential_mappings_item)

        git_credentials = []
        for git_credentials_item_data in self.git_credentials:
            git_credentials_item = git_credentials_item_data.to_dict()
            git_credentials.append(git_credentials_item)

        enable_read_write_datasets = self.enable_read_write_datasets

        permissions = self.permissions.to_dict()

        commit_settings = self.commit_settings.to_dict()

        project_settings = self.project_settings.to_dict()

        file_settings = self.file_settings.to_dict()

        previous_directory_url = self.previous_directory_url

        csrf_token: None | str | Unset
        if isinstance(self.csrf_token, Unset):
            csrf_token = UNSET
        else:
            csrf_token = self.csrf_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectImportsIsEmpty": project_imports_is_empty,
                "importedProjects": imported_projects,
                "runTaggingEnabled": run_tagging_enabled,
                "showUploadComponentOnStart": show_upload_component_on_start,
                "suggestDatasets": suggest_datasets,
                "relativeBreadcrumbData": relative_breadcrumb_data,
                "downloadCLIPageEndpoint": download_cli_page_endpoint,
                "areReferencesCustomizable": are_references_customizable,
                "allCredentialMappings": all_credential_mappings,
                "gitCredentials": git_credentials,
                "enableReadWriteDatasets": enable_read_write_datasets,
                "permissions": permissions,
                "commitSettings": commit_settings,
                "projectSettings": project_settings,
                "fileSettings": file_settings,
                "previousDirectoryUrl": previous_directory_url,
            }
        )
        if csrf_token is not UNSET:
            field_dict["csrfToken"] = csrf_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_files_interface_credential_mappings import DominoFilesInterfaceCredentialMappings
        from ..models.domino_files_interface_files_browse_settings_dto import DominoFilesInterfaceFilesBrowseSettingsDto
        from ..models.domino_files_interface_files_permissions_dto import DominoFilesInterfaceFilesPermissionsDto
        from ..models.domino_files_interface_git_credentials import DominoFilesInterfaceGitCredentials
        from ..models.domino_files_interface_project_code_browse_commit_dto import (
            DominoFilesInterfaceProjectCodeBrowseCommitDto,
        )
        from ..models.domino_files_interface_project_code_browse_dto_relative_breadcrumb_data_item import (
            DominoFilesInterfaceProjectCodeBrowseDtoRelativeBreadcrumbDataItem,
        )
        from ..models.domino_files_interface_project_code_browse_project_dto import (
            DominoFilesInterfaceProjectCodeBrowseProjectDto,
        )
        from ..models.domino_files_interface_project_imports_dto import DominoFilesInterfaceProjectImportsDto

        d = dict(src_dict)
        project_imports_is_empty = d.pop("projectImportsIsEmpty")

        imported_projects = []
        _imported_projects = d.pop("importedProjects")
        for imported_projects_item_data in _imported_projects:
            imported_projects_item = DominoFilesInterfaceProjectImportsDto.from_dict(imported_projects_item_data)

            imported_projects.append(imported_projects_item)

        run_tagging_enabled = d.pop("runTaggingEnabled")

        show_upload_component_on_start = d.pop("showUploadComponentOnStart")

        suggest_datasets = d.pop("suggestDatasets")

        relative_breadcrumb_data = []
        _relative_breadcrumb_data = d.pop("relativeBreadcrumbData")
        for relative_breadcrumb_data_item_data in _relative_breadcrumb_data:
            relative_breadcrumb_data_item = (
                DominoFilesInterfaceProjectCodeBrowseDtoRelativeBreadcrumbDataItem.from_dict(
                    relative_breadcrumb_data_item_data
                )
            )

            relative_breadcrumb_data.append(relative_breadcrumb_data_item)

        download_cli_page_endpoint = d.pop("downloadCLIPageEndpoint")

        are_references_customizable = d.pop("areReferencesCustomizable")

        all_credential_mappings = []
        _all_credential_mappings = d.pop("allCredentialMappings")
        for all_credential_mappings_item_data in _all_credential_mappings:
            all_credential_mappings_item = DominoFilesInterfaceCredentialMappings.from_dict(
                all_credential_mappings_item_data
            )

            all_credential_mappings.append(all_credential_mappings_item)

        git_credentials = []
        _git_credentials = d.pop("gitCredentials")
        for git_credentials_item_data in _git_credentials:
            git_credentials_item = DominoFilesInterfaceGitCredentials.from_dict(git_credentials_item_data)

            git_credentials.append(git_credentials_item)

        enable_read_write_datasets = d.pop("enableReadWriteDatasets")

        permissions = DominoFilesInterfaceFilesPermissionsDto.from_dict(d.pop("permissions"))

        commit_settings = DominoFilesInterfaceProjectCodeBrowseCommitDto.from_dict(d.pop("commitSettings"))

        project_settings = DominoFilesInterfaceProjectCodeBrowseProjectDto.from_dict(d.pop("projectSettings"))

        file_settings = DominoFilesInterfaceFilesBrowseSettingsDto.from_dict(d.pop("fileSettings"))

        previous_directory_url = d.pop("previousDirectoryUrl")

        def _parse_csrf_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        csrf_token = _parse_csrf_token(d.pop("csrfToken", UNSET))

        domino_files_interface_project_code_browse_dto = cls(
            project_imports_is_empty=project_imports_is_empty,
            imported_projects=imported_projects,
            run_tagging_enabled=run_tagging_enabled,
            show_upload_component_on_start=show_upload_component_on_start,
            suggest_datasets=suggest_datasets,
            relative_breadcrumb_data=relative_breadcrumb_data,
            download_cli_page_endpoint=download_cli_page_endpoint,
            are_references_customizable=are_references_customizable,
            all_credential_mappings=all_credential_mappings,
            git_credentials=git_credentials,
            enable_read_write_datasets=enable_read_write_datasets,
            permissions=permissions,
            commit_settings=commit_settings,
            project_settings=project_settings,
            file_settings=file_settings,
            previous_directory_url=previous_directory_url,
            csrf_token=csrf_token,
        )

        domino_files_interface_project_code_browse_dto.additional_properties = d
        return domino_files_interface_project_code_browse_dto

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
