from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO
    from ..models.domino_workspace_api_ssh_config_dto import DominoWorkspaceApiSshConfigDto
    from ..models.domino_workspace_api_workspace_persistence_config_dto import (
        DominoWorkspaceApiWorkspacePersistenceConfigDto,
    )
    from ..models.domino_workspace_api_workspace_reproduction_details_dto import (
        DominoWorkspaceApiWorkspaceReproductionDetailsDto,
    )
    from ..models.information import Information


T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceInitConfigDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceInitConfigDto:
    """
    Attributes:
        volume_size (Information):
        workspace_reproduction_details (DominoWorkspaceApiWorkspaceReproductionDetailsDto | Unset):
        main_git_repo_ref (DominoProjectsApiRepositoriesReferenceDTO | Unset):
        ssh (DominoWorkspaceApiSshConfigDto | Unset):
        persistence (DominoWorkspaceApiWorkspacePersistenceConfigDto | Unset):
    """

    volume_size: Information
    workspace_reproduction_details: DominoWorkspaceApiWorkspaceReproductionDetailsDto | Unset = UNSET
    main_git_repo_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset = UNSET
    ssh: DominoWorkspaceApiSshConfigDto | Unset = UNSET
    persistence: DominoWorkspaceApiWorkspacePersistenceConfigDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volume_size = self.volume_size.to_dict()

        workspace_reproduction_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workspace_reproduction_details, Unset):
            workspace_reproduction_details = self.workspace_reproduction_details.to_dict()

        main_git_repo_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_git_repo_ref, Unset):
            main_git_repo_ref = self.main_git_repo_ref.to_dict()

        ssh: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssh, Unset):
            ssh = self.ssh.to_dict()

        persistence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.persistence, Unset):
            persistence = self.persistence.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "volumeSize": volume_size,
            }
        )
        if workspace_reproduction_details is not UNSET:
            field_dict["workspaceReproductionDetails"] = workspace_reproduction_details
        if main_git_repo_ref is not UNSET:
            field_dict["mainGitRepoRef"] = main_git_repo_ref
        if ssh is not UNSET:
            field_dict["ssh"] = ssh
        if persistence is not UNSET:
            field_dict["persistence"] = persistence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO
        from ..models.domino_workspace_api_ssh_config_dto import DominoWorkspaceApiSshConfigDto
        from ..models.domino_workspace_api_workspace_persistence_config_dto import (
            DominoWorkspaceApiWorkspacePersistenceConfigDto,
        )
        from ..models.domino_workspace_api_workspace_reproduction_details_dto import (
            DominoWorkspaceApiWorkspaceReproductionDetailsDto,
        )
        from ..models.information import Information

        d = dict(src_dict)
        volume_size = Information.from_dict(d.pop("volumeSize"))

        _workspace_reproduction_details = d.pop("workspaceReproductionDetails", UNSET)
        workspace_reproduction_details: DominoWorkspaceApiWorkspaceReproductionDetailsDto | Unset
        if isinstance(_workspace_reproduction_details, Unset):
            workspace_reproduction_details = UNSET
        else:
            workspace_reproduction_details = DominoWorkspaceApiWorkspaceReproductionDetailsDto.from_dict(
                _workspace_reproduction_details
            )

        _main_git_repo_ref = d.pop("mainGitRepoRef", UNSET)
        main_git_repo_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset
        if isinstance(_main_git_repo_ref, Unset):
            main_git_repo_ref = UNSET
        else:
            main_git_repo_ref = DominoProjectsApiRepositoriesReferenceDTO.from_dict(_main_git_repo_ref)

        _ssh = d.pop("ssh", UNSET)
        ssh: DominoWorkspaceApiSshConfigDto | Unset
        if isinstance(_ssh, Unset):
            ssh = UNSET
        else:
            ssh = DominoWorkspaceApiSshConfigDto.from_dict(_ssh)

        _persistence = d.pop("persistence", UNSET)
        persistence: DominoWorkspaceApiWorkspacePersistenceConfigDto | Unset
        if isinstance(_persistence, Unset):
            persistence = UNSET
        else:
            persistence = DominoWorkspaceApiWorkspacePersistenceConfigDto.from_dict(_persistence)

        domino_workspace_api_workspace_init_config_dto = cls(
            volume_size=volume_size,
            workspace_reproduction_details=workspace_reproduction_details,
            main_git_repo_ref=main_git_repo_ref,
            ssh=ssh,
            persistence=persistence,
        )

        domino_workspace_api_workspace_init_config_dto.additional_properties = d
        return domino_workspace_api_workspace_init_config_dto

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
