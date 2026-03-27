from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_entity_link import DominoProjectsApiEntityLink
    from ..models.domino_projects_api_model_ref_project_ref_dto import DominoProjectsApiModelRefProjectRefDto
    from ..models.domino_projects_api_project_stage import DominoProjectsApiProjectStage


T = TypeVar("T", bound="DominoProjectsApiProjectGoal")


@_attrs_define
class DominoProjectsApiProjectGoal:
    """
    Attributes:
        id (str):
        title (str):
        linked_entities (list[DominoProjectsApiEntityLink]):
        current_stage (DominoProjectsApiProjectStage):
        is_complete (bool):
        is_deleted (bool):
        project_id (str):
        created_at (int):
        created_by (str):
        description (None | str | Unset):
        assignee_id (None | str | Unset):
        comment_count (int | None | Unset):
        last_title_updated_at (int | None | Unset):
        last_description_updated_at (int | None | Unset):
        last_updated_at (int | None | Unset):
        project (DominoProjectsApiModelRefProjectRefDto | Unset):
    """

    id: str
    title: str
    linked_entities: list[DominoProjectsApiEntityLink]
    current_stage: DominoProjectsApiProjectStage
    is_complete: bool
    is_deleted: bool
    project_id: str
    created_at: int
    created_by: str
    description: None | str | Unset = UNSET
    assignee_id: None | str | Unset = UNSET
    comment_count: int | None | Unset = UNSET
    last_title_updated_at: int | None | Unset = UNSET
    last_description_updated_at: int | None | Unset = UNSET
    last_updated_at: int | None | Unset = UNSET
    project: DominoProjectsApiModelRefProjectRefDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        linked_entities = []
        for linked_entities_item_data in self.linked_entities:
            linked_entities_item = linked_entities_item_data.to_dict()
            linked_entities.append(linked_entities_item)

        current_stage = self.current_stage.to_dict()

        is_complete = self.is_complete

        is_deleted = self.is_deleted

        project_id = self.project_id

        created_at = self.created_at

        created_by = self.created_by

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        else:
            assignee_id = self.assignee_id

        comment_count: int | None | Unset
        if isinstance(self.comment_count, Unset):
            comment_count = UNSET
        else:
            comment_count = self.comment_count

        last_title_updated_at: int | None | Unset
        if isinstance(self.last_title_updated_at, Unset):
            last_title_updated_at = UNSET
        else:
            last_title_updated_at = self.last_title_updated_at

        last_description_updated_at: int | None | Unset
        if isinstance(self.last_description_updated_at, Unset):
            last_description_updated_at = UNSET
        else:
            last_description_updated_at = self.last_description_updated_at

        last_updated_at: int | None | Unset
        if isinstance(self.last_updated_at, Unset):
            last_updated_at = UNSET
        else:
            last_updated_at = self.last_updated_at

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "linkedEntities": linked_entities,
                "currentStage": current_stage,
                "isComplete": is_complete,
                "isDeleted": is_deleted,
                "projectId": project_id,
                "createdAt": created_at,
                "createdBy": created_by,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if comment_count is not UNSET:
            field_dict["commentCount"] = comment_count
        if last_title_updated_at is not UNSET:
            field_dict["lastTitleUpdatedAt"] = last_title_updated_at
        if last_description_updated_at is not UNSET:
            field_dict["lastDescriptionUpdatedAt"] = last_description_updated_at
        if last_updated_at is not UNSET:
            field_dict["lastUpdatedAt"] = last_updated_at
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_entity_link import DominoProjectsApiEntityLink
        from ..models.domino_projects_api_model_ref_project_ref_dto import DominoProjectsApiModelRefProjectRefDto
        from ..models.domino_projects_api_project_stage import DominoProjectsApiProjectStage

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        linked_entities = []
        _linked_entities = d.pop("linkedEntities")
        for linked_entities_item_data in _linked_entities:
            linked_entities_item = DominoProjectsApiEntityLink.from_dict(linked_entities_item_data)

            linked_entities.append(linked_entities_item)

        current_stage = DominoProjectsApiProjectStage.from_dict(d.pop("currentStage"))

        is_complete = d.pop("isComplete")

        is_deleted = d.pop("isDeleted")

        project_id = d.pop("projectId")

        created_at = d.pop("createdAt")

        created_by = d.pop("createdBy")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_assignee_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assignee_id = _parse_assignee_id(d.pop("assigneeId", UNSET))

        def _parse_comment_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        comment_count = _parse_comment_count(d.pop("commentCount", UNSET))

        def _parse_last_title_updated_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_title_updated_at = _parse_last_title_updated_at(d.pop("lastTitleUpdatedAt", UNSET))

        def _parse_last_description_updated_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_description_updated_at = _parse_last_description_updated_at(d.pop("lastDescriptionUpdatedAt", UNSET))

        def _parse_last_updated_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_updated_at = _parse_last_updated_at(d.pop("lastUpdatedAt", UNSET))

        _project = d.pop("project", UNSET)
        project: DominoProjectsApiModelRefProjectRefDto | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = DominoProjectsApiModelRefProjectRefDto.from_dict(_project)

        domino_projects_api_project_goal = cls(
            id=id,
            title=title,
            linked_entities=linked_entities,
            current_stage=current_stage,
            is_complete=is_complete,
            is_deleted=is_deleted,
            project_id=project_id,
            created_at=created_at,
            created_by=created_by,
            description=description,
            assignee_id=assignee_id,
            comment_count=comment_count,
            last_title_updated_at=last_title_updated_at,
            last_description_updated_at=last_description_updated_at,
            last_updated_at=last_updated_at,
            project=project,
        )

        domino_projects_api_project_goal.additional_properties = d
        return domino_projects_api_project_goal

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
