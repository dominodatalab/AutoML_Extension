from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_gateway_search_search_project_tag import DominoCommonGatewaySearchSearchProjectTag


T = TypeVar("T", bound="DominoCommonGatewaySearchSearchProjectDTO")


@_attrs_define
class DominoCommonGatewaySearchSearchProjectDTO:
    """
    Attributes:
        snippet (str):
        tags (list[DominoCommonGatewaySearchSearchProjectTag]):
        goal_link (str):
        is_restricted (bool | None | Unset):
        blocker_reason (None | str | Unset):
        goal (None | str | Unset):
    """

    snippet: str
    tags: list[DominoCommonGatewaySearchSearchProjectTag]
    goal_link: str
    is_restricted: bool | None | Unset = UNSET
    blocker_reason: None | str | Unset = UNSET
    goal: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snippet = self.snippet

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        goal_link = self.goal_link

        is_restricted: bool | None | Unset
        if isinstance(self.is_restricted, Unset):
            is_restricted = UNSET
        else:
            is_restricted = self.is_restricted

        blocker_reason: None | str | Unset
        if isinstance(self.blocker_reason, Unset):
            blocker_reason = UNSET
        else:
            blocker_reason = self.blocker_reason

        goal: None | str | Unset
        if isinstance(self.goal, Unset):
            goal = UNSET
        else:
            goal = self.goal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snippet": snippet,
                "tags": tags,
                "goalLink": goal_link,
            }
        )
        if is_restricted is not UNSET:
            field_dict["isRestricted"] = is_restricted
        if blocker_reason is not UNSET:
            field_dict["blockerReason"] = blocker_reason
        if goal is not UNSET:
            field_dict["goal"] = goal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_gateway_search_search_project_tag import DominoCommonGatewaySearchSearchProjectTag

        d = dict(src_dict)
        snippet = d.pop("snippet")

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = DominoCommonGatewaySearchSearchProjectTag.from_dict(tags_item_data)

            tags.append(tags_item)

        goal_link = d.pop("goalLink")

        def _parse_is_restricted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_restricted = _parse_is_restricted(d.pop("isRestricted", UNSET))

        def _parse_blocker_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        blocker_reason = _parse_blocker_reason(d.pop("blockerReason", UNSET))

        def _parse_goal(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        goal = _parse_goal(d.pop("goal", UNSET))

        domino_common_gateway_search_search_project_dto = cls(
            snippet=snippet,
            tags=tags,
            goal_link=goal_link,
            is_restricted=is_restricted,
            blocker_reason=blocker_reason,
            goal=goal,
        )

        domino_common_gateway_search_search_project_dto.additional_properties = d
        return domino_common_gateway_search_search_project_dto

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
