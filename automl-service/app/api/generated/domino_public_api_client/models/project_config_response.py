from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_repo import ServerRepo
    from ..models.workspace_repo import WorkspaceRepo


T = TypeVar("T", bound="ProjectConfigResponse")


@_attrs_define
class ProjectConfigResponse:
    """
    Attributes:
        server_repos (list[ServerRepo]): Repositories available on PPM servers
        workspace_repos (list[WorkspaceRepo]): Repositories detected from workspace renv.lock
        bioc_version (None | str | Unset): Bioconductor version from renv.lock (if available)
        r_version (None | str | Unset): R version from renv.lock (if available)
        repo_allowlist (list[str] | Unset): List of allowed repository URLs from .domino/repo-allowlist file
    """

    server_repos: list[ServerRepo]
    workspace_repos: list[WorkspaceRepo]
    bioc_version: None | str | Unset = UNSET
    r_version: None | str | Unset = UNSET
    repo_allowlist: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_repos = []
        for server_repos_item_data in self.server_repos:
            server_repos_item = server_repos_item_data.to_dict()
            server_repos.append(server_repos_item)

        workspace_repos = []
        for workspace_repos_item_data in self.workspace_repos:
            workspace_repos_item = workspace_repos_item_data.to_dict()
            workspace_repos.append(workspace_repos_item)

        bioc_version: None | str | Unset
        if isinstance(self.bioc_version, Unset):
            bioc_version = UNSET
        else:
            bioc_version = self.bioc_version

        r_version: None | str | Unset
        if isinstance(self.r_version, Unset):
            r_version = UNSET
        else:
            r_version = self.r_version

        repo_allowlist: list[str] | Unset = UNSET
        if not isinstance(self.repo_allowlist, Unset):
            repo_allowlist = self.repo_allowlist

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serverRepos": server_repos,
                "workspaceRepos": workspace_repos,
            }
        )
        if bioc_version is not UNSET:
            field_dict["biocVersion"] = bioc_version
        if r_version is not UNSET:
            field_dict["rVersion"] = r_version
        if repo_allowlist is not UNSET:
            field_dict["repoAllowlist"] = repo_allowlist

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_repo import ServerRepo
        from ..models.workspace_repo import WorkspaceRepo

        d = dict(src_dict)
        server_repos = []
        _server_repos = d.pop("serverRepos")
        for server_repos_item_data in _server_repos:
            server_repos_item = ServerRepo.from_dict(server_repos_item_data)

            server_repos.append(server_repos_item)

        workspace_repos = []
        _workspace_repos = d.pop("workspaceRepos")
        for workspace_repos_item_data in _workspace_repos:
            workspace_repos_item = WorkspaceRepo.from_dict(workspace_repos_item_data)

            workspace_repos.append(workspace_repos_item)

        def _parse_bioc_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bioc_version = _parse_bioc_version(d.pop("biocVersion", UNSET))

        def _parse_r_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        r_version = _parse_r_version(d.pop("rVersion", UNSET))

        repo_allowlist = cast(list[str], d.pop("repoAllowlist", UNSET))

        project_config_response = cls(
            server_repos=server_repos,
            workspace_repos=workspace_repos,
            bioc_version=bioc_version,
            r_version=r_version,
            repo_allowlist=repo_allowlist,
        )

        project_config_response.additional_properties = d
        return project_config_response

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
