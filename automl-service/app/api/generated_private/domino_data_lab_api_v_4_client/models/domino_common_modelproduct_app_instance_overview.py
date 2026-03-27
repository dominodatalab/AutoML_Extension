from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoCommonModelproductAppInstanceOverview")


@_attrs_define
class DominoCommonModelproductAppInstanceOverview:
    """
    Attributes:
        id (str):
        started (int):
        duration (int):
        publishing_user_id (str):
        publishing_username (str):
        status (str):
        goal_ids (list[str]):
    """

    id: str
    started: int
    duration: int
    publishing_user_id: str
    publishing_username: str
    status: str
    goal_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        started = self.started

        duration = self.duration

        publishing_user_id = self.publishing_user_id

        publishing_username = self.publishing_username

        status = self.status

        goal_ids = self.goal_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "started": started,
                "duration": duration,
                "publishingUserId": publishing_user_id,
                "publishingUsername": publishing_username,
                "status": status,
                "goalIds": goal_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        started = d.pop("started")

        duration = d.pop("duration")

        publishing_user_id = d.pop("publishingUserId")

        publishing_username = d.pop("publishingUsername")

        status = d.pop("status")

        goal_ids = cast(list[str], d.pop("goalIds"))

        domino_common_modelproduct_app_instance_overview = cls(
            id=id,
            started=started,
            duration=duration,
            publishing_user_id=publishing_user_id,
            publishing_username=publishing_username,
            status=status,
            goal_ids=goal_ids,
        )

        domino_common_modelproduct_app_instance_overview.additional_properties = d
        return domino_common_modelproduct_app_instance_overview

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
