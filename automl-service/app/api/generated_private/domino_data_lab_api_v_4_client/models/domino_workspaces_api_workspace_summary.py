from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_workspaces_api_domino_stats import DominoWorkspacesApiDominoStats
    from ..models.domino_workspaces_api_stage_time import DominoWorkspacesApiStageTime
    from ..models.domino_workspaces_api_workspace_resource_usage import DominoWorkspacesApiWorkspaceResourceUsage
    from ..models.domino_workspaces_api_workspace_started_by import DominoWorkspacesApiWorkspaceStartedBy
    from ..models.domino_workspaces_api_workspace_tag import DominoWorkspacesApiWorkspaceTag


T = TypeVar("T", bound="DominoWorkspacesApiWorkspaceSummary")


@_attrs_define
class DominoWorkspacesApiWorkspaceSummary:
    """
    Attributes:
        id (str):
        project_id (str):
        title (str):
        stage_time (DominoWorkspacesApiStageTime):
        number (int):
        is_completed (bool):
        is_archived (bool):
        comments_count (int):
        status (str):
        tags (list[DominoWorkspacesApiWorkspaceTag]):
        domino_stats (list[DominoWorkspacesApiDominoStats]):
        goal_ids (list[str]):
        is_restartable (bool):
        started_by (DominoWorkspacesApiWorkspaceStartedBy | Unset):
        usage (DominoWorkspacesApiWorkspaceResourceUsage | Unset):
    """

    id: str
    project_id: str
    title: str
    stage_time: DominoWorkspacesApiStageTime
    number: int
    is_completed: bool
    is_archived: bool
    comments_count: int
    status: str
    tags: list[DominoWorkspacesApiWorkspaceTag]
    domino_stats: list[DominoWorkspacesApiDominoStats]
    goal_ids: list[str]
    is_restartable: bool
    started_by: DominoWorkspacesApiWorkspaceStartedBy | Unset = UNSET
    usage: DominoWorkspacesApiWorkspaceResourceUsage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        project_id = self.project_id

        title = self.title

        stage_time = self.stage_time.to_dict()

        number = self.number

        is_completed = self.is_completed

        is_archived = self.is_archived

        comments_count = self.comments_count

        status = self.status

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        domino_stats = []
        for domino_stats_item_data in self.domino_stats:
            domino_stats_item = domino_stats_item_data.to_dict()
            domino_stats.append(domino_stats_item)

        goal_ids = self.goal_ids

        is_restartable = self.is_restartable

        started_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.started_by, Unset):
            started_by = self.started_by.to_dict()

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "projectId": project_id,
                "title": title,
                "stageTime": stage_time,
                "number": number,
                "isCompleted": is_completed,
                "isArchived": is_archived,
                "commentsCount": comments_count,
                "status": status,
                "tags": tags,
                "dominoStats": domino_stats,
                "goalIds": goal_ids,
                "isRestartable": is_restartable,
            }
        )
        if started_by is not UNSET:
            field_dict["startedBy"] = started_by
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspaces_api_domino_stats import DominoWorkspacesApiDominoStats
        from ..models.domino_workspaces_api_stage_time import DominoWorkspacesApiStageTime
        from ..models.domino_workspaces_api_workspace_resource_usage import DominoWorkspacesApiWorkspaceResourceUsage
        from ..models.domino_workspaces_api_workspace_started_by import DominoWorkspacesApiWorkspaceStartedBy
        from ..models.domino_workspaces_api_workspace_tag import DominoWorkspacesApiWorkspaceTag

        d = dict(src_dict)
        id = d.pop("id")

        project_id = d.pop("projectId")

        title = d.pop("title")

        stage_time = DominoWorkspacesApiStageTime.from_dict(d.pop("stageTime"))

        number = d.pop("number")

        is_completed = d.pop("isCompleted")

        is_archived = d.pop("isArchived")

        comments_count = d.pop("commentsCount")

        status = d.pop("status")

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = DominoWorkspacesApiWorkspaceTag.from_dict(tags_item_data)

            tags.append(tags_item)

        domino_stats = []
        _domino_stats = d.pop("dominoStats")
        for domino_stats_item_data in _domino_stats:
            domino_stats_item = DominoWorkspacesApiDominoStats.from_dict(domino_stats_item_data)

            domino_stats.append(domino_stats_item)

        goal_ids = cast(list[str], d.pop("goalIds"))

        is_restartable = d.pop("isRestartable")

        _started_by = d.pop("startedBy", UNSET)
        started_by: DominoWorkspacesApiWorkspaceStartedBy | Unset
        if isinstance(_started_by, Unset):
            started_by = UNSET
        else:
            started_by = DominoWorkspacesApiWorkspaceStartedBy.from_dict(_started_by)

        _usage = d.pop("usage", UNSET)
        usage: DominoWorkspacesApiWorkspaceResourceUsage | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = DominoWorkspacesApiWorkspaceResourceUsage.from_dict(_usage)

        domino_workspaces_api_workspace_summary = cls(
            id=id,
            project_id=project_id,
            title=title,
            stage_time=stage_time,
            number=number,
            is_completed=is_completed,
            is_archived=is_archived,
            comments_count=comments_count,
            status=status,
            tags=tags,
            domino_stats=domino_stats,
            goal_ids=goal_ids,
            is_restartable=is_restartable,
            started_by=started_by,
            usage=usage,
        )

        domino_workspaces_api_workspace_summary.additional_properties = d
        return domino_workspaces_api_workspace_summary

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
