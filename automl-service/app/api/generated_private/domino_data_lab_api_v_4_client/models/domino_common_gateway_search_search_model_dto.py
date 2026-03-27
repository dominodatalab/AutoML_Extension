from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_common_gateway_search_collaborator_details import DominoCommonGatewaySearchCollaboratorDetails
    from ..models.domino_common_gateway_search_search_project_details import (
        DominoCommonGatewaySearchSearchProjectDetails,
    )


T = TypeVar("T", bound="DominoCommonGatewaySearchSearchModelDTO")


@_attrs_define
class DominoCommonGatewaySearchSearchModelDTO:
    """
    Attributes:
        environment_name (str):
        environment_link (str):
        projects (list[DominoCommonGatewaySearchSearchProjectDetails]):
        collaborators (list[DominoCommonGatewaySearchCollaboratorDetails]):
    """

    environment_name: str
    environment_link: str
    projects: list[DominoCommonGatewaySearchSearchProjectDetails]
    collaborators: list[DominoCommonGatewaySearchCollaboratorDetails]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment_name = self.environment_name

        environment_link = self.environment_link

        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()
            projects.append(projects_item)

        collaborators = []
        for collaborators_item_data in self.collaborators:
            collaborators_item = collaborators_item_data.to_dict()
            collaborators.append(collaborators_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environmentName": environment_name,
                "environmentLink": environment_link,
                "projects": projects,
                "collaborators": collaborators,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_gateway_search_collaborator_details import (
            DominoCommonGatewaySearchCollaboratorDetails,
        )
        from ..models.domino_common_gateway_search_search_project_details import (
            DominoCommonGatewaySearchSearchProjectDetails,
        )

        d = dict(src_dict)
        environment_name = d.pop("environmentName")

        environment_link = d.pop("environmentLink")

        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = DominoCommonGatewaySearchSearchProjectDetails.from_dict(projects_item_data)

            projects.append(projects_item)

        collaborators = []
        _collaborators = d.pop("collaborators")
        for collaborators_item_data in _collaborators:
            collaborators_item = DominoCommonGatewaySearchCollaboratorDetails.from_dict(collaborators_item_data)

            collaborators.append(collaborators_item)

        domino_common_gateway_search_search_model_dto = cls(
            environment_name=environment_name,
            environment_link=environment_link,
            projects=projects,
            collaborators=collaborators,
        )

        domino_common_gateway_search_search_model_dto.additional_properties = d
        return domino_common_gateway_search_search_model_dto

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
