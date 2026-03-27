from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_common_gateway_search_search_project_details import (
        DominoCommonGatewaySearchSearchProjectDetails,
    )


T = TypeVar("T", bound="DominoCommonGatewaySearchSearchDatasetDTO")


@_attrs_define
class DominoCommonGatewaySearchSearchDatasetDTO:
    """
    Attributes:
        description (str):
        author_name (str):
        status (str):
        created (str):
        project (DominoCommonGatewaySearchSearchProjectDetails):
        tag_names (list[str]):
    """

    description: str
    author_name: str
    status: str
    created: str
    project: DominoCommonGatewaySearchSearchProjectDetails
    tag_names: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        author_name = self.author_name

        status = self.status

        created = self.created

        project = self.project.to_dict()

        tag_names = self.tag_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "authorName": author_name,
                "status": status,
                "created": created,
                "project": project,
                "tagNames": tag_names,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_gateway_search_search_project_details import (
            DominoCommonGatewaySearchSearchProjectDetails,
        )

        d = dict(src_dict)
        description = d.pop("description")

        author_name = d.pop("authorName")

        status = d.pop("status")

        created = d.pop("created")

        project = DominoCommonGatewaySearchSearchProjectDetails.from_dict(d.pop("project"))

        tag_names = cast(list[str], d.pop("tagNames"))

        domino_common_gateway_search_search_dataset_dto = cls(
            description=description,
            author_name=author_name,
            status=status,
            created=created,
            project=project,
            tag_names=tag_names,
        )

        domino_common_gateway_search_search_dataset_dto.additional_properties = d
        return domino_common_gateway_search_search_dataset_dto

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
