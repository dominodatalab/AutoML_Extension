from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_workspaces_api_comment_context_comment_type import DominoWorkspacesApiCommentContextCommentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoWorkspacesApiCommentContext")


@_attrs_define
class DominoWorkspacesApiCommentContext:
    """
    Attributes:
        comment_type (DominoWorkspacesApiCommentContextCommentType):
        workspace_id (str):
        file_name (None | str | Unset):
        commit_id (None | str | Unset):
    """

    comment_type: DominoWorkspacesApiCommentContextCommentType
    workspace_id: str
    file_name: None | str | Unset = UNSET
    commit_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_type = self.comment_type.value

        workspace_id = self.workspace_id

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        commit_id: None | str | Unset
        if isinstance(self.commit_id, Unset):
            commit_id = UNSET
        else:
            commit_id = self.commit_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commentType": comment_type,
                "workspaceId": workspace_id,
            }
        )
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if commit_id is not UNSET:
            field_dict["commitId"] = commit_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_type = DominoWorkspacesApiCommentContextCommentType(d.pop("commentType"))

        workspace_id = d.pop("workspaceId")

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))

        def _parse_commit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_id = _parse_commit_id(d.pop("commitId", UNSET))

        domino_workspaces_api_comment_context = cls(
            comment_type=comment_type,
            workspace_id=workspace_id,
            file_name=file_name,
            commit_id=commit_id,
        )

        domino_workspaces_api_comment_context.additional_properties = d
        return domino_workspaces_api_comment_context

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
