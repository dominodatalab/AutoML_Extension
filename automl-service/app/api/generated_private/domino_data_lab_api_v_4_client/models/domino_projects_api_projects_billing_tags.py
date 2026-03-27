from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_api_project_billing_tag import DominoProjectsApiProjectBillingTag


T = TypeVar("T", bound="DominoProjectsApiProjectsBillingTags")


@_attrs_define
class DominoProjectsApiProjectsBillingTags:
    """
    Attributes:
        projects_billing_tags (list[DominoProjectsApiProjectBillingTag]):
    """

    projects_billing_tags: list[DominoProjectsApiProjectBillingTag]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        projects_billing_tags = []
        for projects_billing_tags_item_data in self.projects_billing_tags:
            projects_billing_tags_item = projects_billing_tags_item_data.to_dict()
            projects_billing_tags.append(projects_billing_tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectsBillingTags": projects_billing_tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_project_billing_tag import DominoProjectsApiProjectBillingTag

        d = dict(src_dict)
        projects_billing_tags = []
        _projects_billing_tags = d.pop("projectsBillingTags")
        for projects_billing_tags_item_data in _projects_billing_tags:
            projects_billing_tags_item = DominoProjectsApiProjectBillingTag.from_dict(projects_billing_tags_item_data)

            projects_billing_tags.append(projects_billing_tags_item)

        domino_projects_api_projects_billing_tags = cls(
            projects_billing_tags=projects_billing_tags,
        )

        domino_projects_api_projects_billing_tags.additional_properties = d
        return domino_projects_api_projects_billing_tags

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
