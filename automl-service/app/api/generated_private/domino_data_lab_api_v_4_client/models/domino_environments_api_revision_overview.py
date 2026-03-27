from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_environments_api_revision_overview_status import DominoEnvironmentsApiRevisionOverviewStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_environments_api_environment_workspace_tool_definition import (
        DominoEnvironmentsApiEnvironmentWorkspaceToolDefinition,
    )


T = TypeVar("T", bound="DominoEnvironmentsApiRevisionOverview")


@_attrs_define
class DominoEnvironmentsApiRevisionOverview:
    """
    Attributes:
        id (str):
        number (int):
        url (str):
        available_tools (list[DominoEnvironmentsApiEnvironmentWorkspaceToolDefinition]):
        is_restricted (bool):
        status (DominoEnvironmentsApiRevisionOverviewStatus | Unset):
        tags (list[str] | None | Unset):
    """

    id: str
    number: int
    url: str
    available_tools: list[DominoEnvironmentsApiEnvironmentWorkspaceToolDefinition]
    is_restricted: bool
    status: DominoEnvironmentsApiRevisionOverviewStatus | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        number = self.number

        url = self.url

        available_tools = []
        for available_tools_item_data in self.available_tools:
            available_tools_item = available_tools_item_data.to_dict()
            available_tools.append(available_tools_item)

        is_restricted = self.is_restricted

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "number": number,
                "url": url,
                "availableTools": available_tools,
                "isRestricted": is_restricted,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_environment_workspace_tool_definition import (
            DominoEnvironmentsApiEnvironmentWorkspaceToolDefinition,
        )

        d = dict(src_dict)
        id = d.pop("id")

        number = d.pop("number")

        url = d.pop("url")

        available_tools = []
        _available_tools = d.pop("availableTools")
        for available_tools_item_data in _available_tools:
            available_tools_item = DominoEnvironmentsApiEnvironmentWorkspaceToolDefinition.from_dict(
                available_tools_item_data
            )

            available_tools.append(available_tools_item)

        is_restricted = d.pop("isRestricted")

        _status = d.pop("status", UNSET)
        status: DominoEnvironmentsApiRevisionOverviewStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DominoEnvironmentsApiRevisionOverviewStatus(_status)

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        domino_environments_api_revision_overview = cls(
            id=id,
            number=number,
            url=url,
            available_tools=available_tools,
            is_restricted=is_restricted,
            status=status,
            tags=tags,
        )

        domino_environments_api_revision_overview.additional_properties = d
        return domino_environments_api_revision_overview

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
