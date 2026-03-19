from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_request_repo_type import SearchRequestRepoType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workspace_repo import WorkspaceRepo


T = TypeVar("T", bound="SearchRequest")


@_attrs_define
class SearchRequest:
    """
    Attributes:
        constraints (str): Comma-separated package constraints (e.g., "ggplot2==3.5.0,dplyr>=1.0.0,sf")
        bioc_version (str | Unset): Bioconductor version for Bioconductor repositories (e.g., "3.19", "3.20"). If
            omitted, auto-discovers latest version
        forward_looking_snapshot_search (bool | Unset): If true, uses currentSnapshot from workspaceRepos as starting
            point for forward search. Requires workspaceRepos to be provided Default: False.
        min_r_version (str | Unset): Minimum R version for filtering packages (e.g., "4.0", "3.5.0"). If provided, only
            packages that require this R version or greater will be returned
        repo (str | Unset): Specific repository name filter (e.g., "cran", "bioconductor", "pypi"). If omitted, query
            all enabled repos
        repo_allowlist (list[str] | Unset): Optional list of allowed repository URLs. If provided and non-empty, only
            results from repos matching these URLs will be returned
        repo_type (SearchRequestRepoType | Unset): Repository type filter. If omitted, query all repository types
        workspace_repos (list[WorkspaceRepo] | Unset): Array of workspace repositories from renv.lock. If provided,
            search is limited to matching server repositories
    """

    constraints: str
    bioc_version: str | Unset = UNSET
    forward_looking_snapshot_search: bool | Unset = False
    min_r_version: str | Unset = UNSET
    repo: str | Unset = UNSET
    repo_allowlist: list[str] | Unset = UNSET
    repo_type: SearchRequestRepoType | Unset = UNSET
    workspace_repos: list[WorkspaceRepo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constraints = self.constraints

        bioc_version = self.bioc_version

        forward_looking_snapshot_search = self.forward_looking_snapshot_search

        min_r_version = self.min_r_version

        repo = self.repo

        repo_allowlist: list[str] | Unset = UNSET
        if not isinstance(self.repo_allowlist, Unset):
            repo_allowlist = self.repo_allowlist

        repo_type: str | Unset = UNSET
        if not isinstance(self.repo_type, Unset):
            repo_type = self.repo_type.value

        workspace_repos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.workspace_repos, Unset):
            workspace_repos = []
            for workspace_repos_item_data in self.workspace_repos:
                workspace_repos_item = workspace_repos_item_data.to_dict()
                workspace_repos.append(workspace_repos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "constraints": constraints,
            }
        )
        if bioc_version is not UNSET:
            field_dict["biocVersion"] = bioc_version
        if forward_looking_snapshot_search is not UNSET:
            field_dict["forwardLookingSnapshotSearch"] = forward_looking_snapshot_search
        if min_r_version is not UNSET:
            field_dict["minRVersion"] = min_r_version
        if repo is not UNSET:
            field_dict["repo"] = repo
        if repo_allowlist is not UNSET:
            field_dict["repoAllowlist"] = repo_allowlist
        if repo_type is not UNSET:
            field_dict["repoType"] = repo_type
        if workspace_repos is not UNSET:
            field_dict["workspaceRepos"] = workspace_repos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workspace_repo import WorkspaceRepo

        d = dict(src_dict)
        constraints = d.pop("constraints")

        bioc_version = d.pop("biocVersion", UNSET)

        forward_looking_snapshot_search = d.pop("forwardLookingSnapshotSearch", UNSET)

        min_r_version = d.pop("minRVersion", UNSET)

        repo = d.pop("repo", UNSET)

        repo_allowlist = cast(list[str], d.pop("repoAllowlist", UNSET))

        _repo_type = d.pop("repoType", UNSET)
        repo_type: SearchRequestRepoType | Unset
        if isinstance(_repo_type, Unset):
            repo_type = UNSET
        else:
            repo_type = SearchRequestRepoType(_repo_type)

        _workspace_repos = d.pop("workspaceRepos", UNSET)
        workspace_repos: list[WorkspaceRepo] | Unset = UNSET
        if _workspace_repos is not UNSET:
            workspace_repos = []
            for workspace_repos_item_data in _workspace_repos:
                workspace_repos_item = WorkspaceRepo.from_dict(workspace_repos_item_data)

                workspace_repos.append(workspace_repos_item)

        search_request = cls(
            constraints=constraints,
            bioc_version=bioc_version,
            forward_looking_snapshot_search=forward_looking_snapshot_search,
            min_r_version=min_r_version,
            repo=repo,
            repo_allowlist=repo_allowlist,
            repo_type=repo_type,
            workspace_repos=workspace_repos,
        )

        search_request.additional_properties = d
        return search_request

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
