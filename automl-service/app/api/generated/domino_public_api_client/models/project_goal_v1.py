from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectGoalV1")


@_attrs_define
class ProjectGoalV1:
    """
    Attributes:
        created_at (datetime.datetime): Timestamp at which goal was created Example: 2022-03-12T02:13:44.467Z.
        creator_id (str): User id that created the goal
        id (str): The unique project goal id
        is_complete (bool): Flag indicating if the goal is complete
        project_id (str): Id of project to which the goal belongs
        title (str): The title of project goal
        description (str | Unset): Optional description of project goal
    """

    created_at: datetime.datetime
    creator_id: str
    id: str
    is_complete: bool
    project_id: str
    title: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        creator_id = self.creator_id

        id = self.id

        is_complete = self.is_complete

        project_id = self.project_id

        title = self.title

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "creatorId": creator_id,
                "id": id,
                "isComplete": is_complete,
                "projectId": project_id,
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        creator_id = d.pop("creatorId")

        id = d.pop("id")

        is_complete = d.pop("isComplete")

        project_id = d.pop("projectId")

        title = d.pop("title")

        description = d.pop("description", UNSET)

        project_goal_v1 = cls(
            created_at=created_at,
            creator_id=creator_id,
            id=id,
            is_complete=is_complete,
            project_id=project_id,
            title=title,
            description=description,
        )

        project_goal_v1.additional_properties = d
        return project_goal_v1

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
