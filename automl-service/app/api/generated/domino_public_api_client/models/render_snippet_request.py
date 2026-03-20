from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.render_snippet_request_mode import RenderSnippetRequestMode
from ..models.render_snippet_request_repo_type import RenderSnippetRequestRepoType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workspace_repo import WorkspaceRepo


T = TypeVar("T", bound="RenderSnippetRequest")


@_attrs_define
class RenderSnippetRequest:
    """
    Attributes:
        bioc_version (str | Unset): Bioconductor version for Bioconductor repositories (e.g., "3.19", "3.20"). If
            omitted, auto-discovers latest version
        constraints (str | Unset): Comma-separated package constraints (e.g., "ggplot2==3.5.0,dplyr>=1.0.0,sf"). If
            omitted, generates snippet without specific packages
        mode (RenderSnippetRequestMode | Unset): Output mode for the snippet. "r" generates pure R code for direct
            execution in R console. "bash" wraps the R code in a Rscript command for bash execution. Defaults to "r" if
            omitted
        repo (str | Unset): Specific repository name filter (e.g., "cran", "bioconductor", "pypi"). If omitted, uses all
            enabled repos
        repo_type (RenderSnippetRequestRepoType | Unset): Repository type filter. If omitted, uses all repository types
        target_snapshot (str | Unset): Target snapshot date for the snippet generation. If omitted, uses latest
        workspace_repos (list[WorkspaceRepo] | Unset): Array of workspace repositories from renv.lock. If provided,
            snippet generation is based on matching server repositories
    """

    bioc_version: str | Unset = UNSET
    constraints: str | Unset = UNSET
    mode: RenderSnippetRequestMode | Unset = UNSET
    repo: str | Unset = UNSET
    repo_type: RenderSnippetRequestRepoType | Unset = UNSET
    target_snapshot: str | Unset = UNSET
    workspace_repos: list[WorkspaceRepo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bioc_version = self.bioc_version

        constraints = self.constraints

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        repo = self.repo

        repo_type: str | Unset = UNSET
        if not isinstance(self.repo_type, Unset):
            repo_type = self.repo_type.value

        target_snapshot = self.target_snapshot

        workspace_repos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.workspace_repos, Unset):
            workspace_repos = []
            for workspace_repos_item_data in self.workspace_repos:
                workspace_repos_item = workspace_repos_item_data.to_dict()
                workspace_repos.append(workspace_repos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bioc_version is not UNSET:
            field_dict["biocVersion"] = bioc_version
        if constraints is not UNSET:
            field_dict["constraints"] = constraints
        if mode is not UNSET:
            field_dict["mode"] = mode
        if repo is not UNSET:
            field_dict["repo"] = repo
        if repo_type is not UNSET:
            field_dict["repoType"] = repo_type
        if target_snapshot is not UNSET:
            field_dict["targetSnapshot"] = target_snapshot
        if workspace_repos is not UNSET:
            field_dict["workspaceRepos"] = workspace_repos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workspace_repo import WorkspaceRepo

        d = dict(src_dict)
        bioc_version = d.pop("biocVersion", UNSET)

        constraints = d.pop("constraints", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: RenderSnippetRequestMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = RenderSnippetRequestMode(_mode)

        repo = d.pop("repo", UNSET)

        _repo_type = d.pop("repoType", UNSET)
        repo_type: RenderSnippetRequestRepoType | Unset
        if isinstance(_repo_type, Unset):
            repo_type = UNSET
        else:
            repo_type = RenderSnippetRequestRepoType(_repo_type)

        target_snapshot = d.pop("targetSnapshot", UNSET)

        _workspace_repos = d.pop("workspaceRepos", UNSET)
        workspace_repos: list[WorkspaceRepo] | Unset = UNSET
        if _workspace_repos is not UNSET:
            workspace_repos = []
            for workspace_repos_item_data in _workspace_repos:
                workspace_repos_item = WorkspaceRepo.from_dict(workspace_repos_item_data)

                workspace_repos.append(workspace_repos_item)

        render_snippet_request = cls(
            bioc_version=bioc_version,
            constraints=constraints,
            mode=mode,
            repo=repo,
            repo_type=repo_type,
            target_snapshot=target_snapshot,
            workspace_repos=workspace_repos,
        )

        render_snippet_request.additional_properties = d
        return render_snippet_request

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
