from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_workspace_api_ref_project_ref_dto import DominoWorkspaceApiRefProjectRefDto
    from ..models.domino_workspace_api_workspace_config_dto import DominoWorkspaceApiWorkspaceConfigDto
    from ..models.domino_workspace_api_workspace_imported_git_repo import DominoWorkspaceApiWorkspaceImportedGitRepo
    from ..models.domino_workspace_api_workspace_imported_project import DominoWorkspaceApiWorkspaceImportedProject
    from ..models.domino_workspace_api_workspace_init_config_dto import DominoWorkspaceApiWorkspaceInitConfigDto
    from ..models.domino_workspace_api_workspace_session_dto import DominoWorkspaceApiWorkspaceSessionDto
    from ..models.domino_workspace_api_workspace_session_stats_dto import DominoWorkspaceApiWorkspaceSessionStatsDto


T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceDto:
    """
    Attributes:
        id (str):
        deleted (bool):
        project_id (str):
        owner_id (str):
        owner_name (str):
        name (str):
        state (str):
        state_updated_at (datetime.datetime):
        init_config (DominoWorkspaceApiWorkspaceInitConfigDto):
        config_template (DominoWorkspaceApiWorkspaceConfigDto):
        created_at (datetime.datetime):
        imported_projects (list[DominoWorkspaceApiWorkspaceImportedProject]):
        imported_git_repos (list[DominoWorkspaceApiWorkspaceImportedGitRepo]):
        data_plane_id (str):
        session_stats (DominoWorkspaceApiWorkspaceSessionStatsDto):
        is_legacy (bool):
        is_reproduced (bool):
        most_recent_session (DominoWorkspaceApiWorkspaceSessionDto | Unset):
        last_commit_time (datetime.datetime | None | Unset):
        dfs_branch_name (None | str | Unset):
        code_branch_name (None | str | Unset):
        marked_for_delete_time (datetime.datetime | None | Unset):
        project (DominoWorkspaceApiRefProjectRefDto | Unset):
    """

    id: str
    deleted: bool
    project_id: str
    owner_id: str
    owner_name: str
    name: str
    state: str
    state_updated_at: datetime.datetime
    init_config: DominoWorkspaceApiWorkspaceInitConfigDto
    config_template: DominoWorkspaceApiWorkspaceConfigDto
    created_at: datetime.datetime
    imported_projects: list[DominoWorkspaceApiWorkspaceImportedProject]
    imported_git_repos: list[DominoWorkspaceApiWorkspaceImportedGitRepo]
    data_plane_id: str
    session_stats: DominoWorkspaceApiWorkspaceSessionStatsDto
    is_legacy: bool
    is_reproduced: bool
    most_recent_session: DominoWorkspaceApiWorkspaceSessionDto | Unset = UNSET
    last_commit_time: datetime.datetime | None | Unset = UNSET
    dfs_branch_name: None | str | Unset = UNSET
    code_branch_name: None | str | Unset = UNSET
    marked_for_delete_time: datetime.datetime | None | Unset = UNSET
    project: DominoWorkspaceApiRefProjectRefDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        deleted = self.deleted

        project_id = self.project_id

        owner_id = self.owner_id

        owner_name = self.owner_name

        name = self.name

        state = self.state

        state_updated_at = self.state_updated_at.isoformat()

        init_config = self.init_config.to_dict()

        config_template = self.config_template.to_dict()

        created_at = self.created_at.isoformat()

        imported_projects = []
        for imported_projects_item_data in self.imported_projects:
            imported_projects_item = imported_projects_item_data.to_dict()
            imported_projects.append(imported_projects_item)

        imported_git_repos = []
        for imported_git_repos_item_data in self.imported_git_repos:
            imported_git_repos_item = imported_git_repos_item_data.to_dict()
            imported_git_repos.append(imported_git_repos_item)

        data_plane_id = self.data_plane_id

        session_stats = self.session_stats.to_dict()

        is_legacy = self.is_legacy

        is_reproduced = self.is_reproduced

        most_recent_session: dict[str, Any] | Unset = UNSET
        if not isinstance(self.most_recent_session, Unset):
            most_recent_session = self.most_recent_session.to_dict()

        last_commit_time: None | str | Unset
        if isinstance(self.last_commit_time, Unset):
            last_commit_time = UNSET
        elif isinstance(self.last_commit_time, datetime.datetime):
            last_commit_time = self.last_commit_time.isoformat()
        else:
            last_commit_time = self.last_commit_time

        dfs_branch_name: None | str | Unset
        if isinstance(self.dfs_branch_name, Unset):
            dfs_branch_name = UNSET
        else:
            dfs_branch_name = self.dfs_branch_name

        code_branch_name: None | str | Unset
        if isinstance(self.code_branch_name, Unset):
            code_branch_name = UNSET
        else:
            code_branch_name = self.code_branch_name

        marked_for_delete_time: None | str | Unset
        if isinstance(self.marked_for_delete_time, Unset):
            marked_for_delete_time = UNSET
        elif isinstance(self.marked_for_delete_time, datetime.datetime):
            marked_for_delete_time = self.marked_for_delete_time.isoformat()
        else:
            marked_for_delete_time = self.marked_for_delete_time

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "deleted": deleted,
                "projectId": project_id,
                "ownerId": owner_id,
                "ownerName": owner_name,
                "name": name,
                "state": state,
                "stateUpdatedAt": state_updated_at,
                "initConfig": init_config,
                "configTemplate": config_template,
                "createdAt": created_at,
                "importedProjects": imported_projects,
                "importedGitRepos": imported_git_repos,
                "dataPlaneId": data_plane_id,
                "sessionStats": session_stats,
                "isLegacy": is_legacy,
                "isReproduced": is_reproduced,
            }
        )
        if most_recent_session is not UNSET:
            field_dict["mostRecentSession"] = most_recent_session
        if last_commit_time is not UNSET:
            field_dict["lastCommitTime"] = last_commit_time
        if dfs_branch_name is not UNSET:
            field_dict["dfsBranchName"] = dfs_branch_name
        if code_branch_name is not UNSET:
            field_dict["codeBranchName"] = code_branch_name
        if marked_for_delete_time is not UNSET:
            field_dict["markedForDeleteTime"] = marked_for_delete_time
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspace_api_ref_project_ref_dto import DominoWorkspaceApiRefProjectRefDto
        from ..models.domino_workspace_api_workspace_config_dto import DominoWorkspaceApiWorkspaceConfigDto
        from ..models.domino_workspace_api_workspace_imported_git_repo import DominoWorkspaceApiWorkspaceImportedGitRepo
        from ..models.domino_workspace_api_workspace_imported_project import DominoWorkspaceApiWorkspaceImportedProject
        from ..models.domino_workspace_api_workspace_init_config_dto import DominoWorkspaceApiWorkspaceInitConfigDto
        from ..models.domino_workspace_api_workspace_session_dto import DominoWorkspaceApiWorkspaceSessionDto
        from ..models.domino_workspace_api_workspace_session_stats_dto import DominoWorkspaceApiWorkspaceSessionStatsDto

        d = dict(src_dict)
        id = d.pop("id")

        deleted = d.pop("deleted")

        project_id = d.pop("projectId")

        owner_id = d.pop("ownerId")

        owner_name = d.pop("ownerName")

        name = d.pop("name")

        state = d.pop("state")

        state_updated_at = isoparse(d.pop("stateUpdatedAt"))

        init_config = DominoWorkspaceApiWorkspaceInitConfigDto.from_dict(d.pop("initConfig"))

        config_template = DominoWorkspaceApiWorkspaceConfigDto.from_dict(d.pop("configTemplate"))

        created_at = isoparse(d.pop("createdAt"))

        imported_projects = []
        _imported_projects = d.pop("importedProjects")
        for imported_projects_item_data in _imported_projects:
            imported_projects_item = DominoWorkspaceApiWorkspaceImportedProject.from_dict(imported_projects_item_data)

            imported_projects.append(imported_projects_item)

        imported_git_repos = []
        _imported_git_repos = d.pop("importedGitRepos")
        for imported_git_repos_item_data in _imported_git_repos:
            imported_git_repos_item = DominoWorkspaceApiWorkspaceImportedGitRepo.from_dict(imported_git_repos_item_data)

            imported_git_repos.append(imported_git_repos_item)

        data_plane_id = d.pop("dataPlaneId")

        session_stats = DominoWorkspaceApiWorkspaceSessionStatsDto.from_dict(d.pop("sessionStats"))

        is_legacy = d.pop("isLegacy")

        is_reproduced = d.pop("isReproduced")

        _most_recent_session = d.pop("mostRecentSession", UNSET)
        most_recent_session: DominoWorkspaceApiWorkspaceSessionDto | Unset
        if isinstance(_most_recent_session, Unset):
            most_recent_session = UNSET
        else:
            most_recent_session = DominoWorkspaceApiWorkspaceSessionDto.from_dict(_most_recent_session)

        def _parse_last_commit_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_commit_time_type_0 = isoparse(data)

                return last_commit_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_commit_time = _parse_last_commit_time(d.pop("lastCommitTime", UNSET))

        def _parse_dfs_branch_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dfs_branch_name = _parse_dfs_branch_name(d.pop("dfsBranchName", UNSET))

        def _parse_code_branch_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code_branch_name = _parse_code_branch_name(d.pop("codeBranchName", UNSET))

        def _parse_marked_for_delete_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                marked_for_delete_time_type_0 = isoparse(data)

                return marked_for_delete_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        marked_for_delete_time = _parse_marked_for_delete_time(d.pop("markedForDeleteTime", UNSET))

        _project = d.pop("project", UNSET)
        project: DominoWorkspaceApiRefProjectRefDto | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = DominoWorkspaceApiRefProjectRefDto.from_dict(_project)

        domino_workspace_api_workspace_dto = cls(
            id=id,
            deleted=deleted,
            project_id=project_id,
            owner_id=owner_id,
            owner_name=owner_name,
            name=name,
            state=state,
            state_updated_at=state_updated_at,
            init_config=init_config,
            config_template=config_template,
            created_at=created_at,
            imported_projects=imported_projects,
            imported_git_repos=imported_git_repos,
            data_plane_id=data_plane_id,
            session_stats=session_stats,
            is_legacy=is_legacy,
            is_reproduced=is_reproduced,
            most_recent_session=most_recent_session,
            last_commit_time=last_commit_time,
            dfs_branch_name=dfs_branch_name,
            code_branch_name=code_branch_name,
            marked_for_delete_time=marked_for_delete_time,
            project=project,
        )

        domino_workspace_api_workspace_dto.additional_properties = d
        return domino_workspace_api_workspace_dto

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
