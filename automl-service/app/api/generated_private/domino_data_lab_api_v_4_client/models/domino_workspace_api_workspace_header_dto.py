from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_workspace_api_workspace_session_header_dto import DominoWorkspaceApiWorkspaceSessionHeaderDto


T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceHeaderDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceHeaderDto:
    """
    Attributes:
        id (str):
        most_recent_session (DominoWorkspaceApiWorkspaceSessionHeaderDto | Unset):
    """

    id: str
    most_recent_session: DominoWorkspaceApiWorkspaceSessionHeaderDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        most_recent_session: dict[str, Any] | Unset = UNSET
        if not isinstance(self.most_recent_session, Unset):
            most_recent_session = self.most_recent_session.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if most_recent_session is not UNSET:
            field_dict["mostRecentSession"] = most_recent_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspace_api_workspace_session_header_dto import (
            DominoWorkspaceApiWorkspaceSessionHeaderDto,
        )

        d = dict(src_dict)
        id = d.pop("id")

        _most_recent_session = d.pop("mostRecentSession", UNSET)
        most_recent_session: DominoWorkspaceApiWorkspaceSessionHeaderDto | Unset
        if isinstance(_most_recent_session, Unset):
            most_recent_session = UNSET
        else:
            most_recent_session = DominoWorkspaceApiWorkspaceSessionHeaderDto.from_dict(_most_recent_session)

        domino_workspace_api_workspace_header_dto = cls(
            id=id,
            most_recent_session=most_recent_session,
        )

        domino_workspace_api_workspace_header_dto.additional_properties = d
        return domino_workspace_api_workspace_header_dto

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
