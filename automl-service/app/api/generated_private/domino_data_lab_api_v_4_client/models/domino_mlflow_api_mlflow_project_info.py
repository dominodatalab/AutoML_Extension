from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_api_collaborator_dto import DominoProjectsApiCollaboratorDTO


T = TypeVar("T", bound="DominoMlflowApiMlflowProjectInfo")


@_attrs_define
class DominoMlflowApiMlflowProjectInfo:
    """
    Attributes:
        id (str):
        name (str):
        owner_id (str):
        owner_name (str):
        collaborators (list[DominoProjectsApiCollaboratorDTO]):
    """

    id: str
    name: str
    owner_id: str
    owner_name: str
    collaborators: list[DominoProjectsApiCollaboratorDTO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        owner_id = self.owner_id

        owner_name = self.owner_name

        collaborators = []
        for collaborators_item_data in self.collaborators:
            collaborators_item = collaborators_item_data.to_dict()
            collaborators.append(collaborators_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "ownerId": owner_id,
                "ownerName": owner_name,
                "collaborators": collaborators,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_collaborator_dto import DominoProjectsApiCollaboratorDTO

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        owner_id = d.pop("ownerId")

        owner_name = d.pop("ownerName")

        collaborators = []
        _collaborators = d.pop("collaborators")
        for collaborators_item_data in _collaborators:
            collaborators_item = DominoProjectsApiCollaboratorDTO.from_dict(collaborators_item_data)

            collaborators.append(collaborators_item)

        domino_mlflow_api_mlflow_project_info = cls(
            id=id,
            name=name,
            owner_id=owner_id,
            owner_name=owner_name,
            collaborators=collaborators,
        )

        domino_mlflow_api_mlflow_project_info.additional_properties = d
        return domino_mlflow_api_mlflow_project_info

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
