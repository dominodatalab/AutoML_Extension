from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProjectsApiCreateReviewRequest")


@_attrs_define
class DominoProjectsApiCreateReviewRequest:
    """
    Attributes:
        author_id (str):
        title (str):
        summary (str):
        into_project_id (str):
        from_project_id (str):
    """

    author_id: str
    title: str
    summary: str
    into_project_id: str
    from_project_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_id = self.author_id

        title = self.title

        summary = self.summary

        into_project_id = self.into_project_id

        from_project_id = self.from_project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authorId": author_id,
                "title": title,
                "summary": summary,
                "intoProjectId": into_project_id,
                "fromProjectId": from_project_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author_id = d.pop("authorId")

        title = d.pop("title")

        summary = d.pop("summary")

        into_project_id = d.pop("intoProjectId")

        from_project_id = d.pop("fromProjectId")

        domino_projects_api_create_review_request = cls(
            author_id=author_id,
            title=title,
            summary=summary,
            into_project_id=into_project_id,
            from_project_id=from_project_id,
        )

        domino_projects_api_create_review_request.additional_properties = d
        return domino_projects_api_create_review_request

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
