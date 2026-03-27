from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_project_environment_dto import DominoProjectsApiProjectEnvironmentDTO
    from ..models.domino_projects_api_selected_environment_dto import DominoProjectsApiSelectedEnvironmentDTO


T = TypeVar("T", bound="DominoProjectsApiUseableProjectEnvironmentsDTO")


@_attrs_define
class DominoProjectsApiUseableProjectEnvironmentsDTO:
    """
    Attributes:
        environments (list[DominoProjectsApiProjectEnvironmentDTO]):
        currently_selected_environment (DominoProjectsApiSelectedEnvironmentDTO | Unset):
    """

    environments: list[DominoProjectsApiProjectEnvironmentDTO]
    currently_selected_environment: DominoProjectsApiSelectedEnvironmentDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environments = []
        for environments_item_data in self.environments:
            environments_item = environments_item_data.to_dict()
            environments.append(environments_item)

        currently_selected_environment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.currently_selected_environment, Unset):
            currently_selected_environment = self.currently_selected_environment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environments": environments,
            }
        )
        if currently_selected_environment is not UNSET:
            field_dict["currentlySelectedEnvironment"] = currently_selected_environment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_project_environment_dto import DominoProjectsApiProjectEnvironmentDTO
        from ..models.domino_projects_api_selected_environment_dto import DominoProjectsApiSelectedEnvironmentDTO

        d = dict(src_dict)
        environments = []
        _environments = d.pop("environments")
        for environments_item_data in _environments:
            environments_item = DominoProjectsApiProjectEnvironmentDTO.from_dict(environments_item_data)

            environments.append(environments_item)

        _currently_selected_environment = d.pop("currentlySelectedEnvironment", UNSET)
        currently_selected_environment: DominoProjectsApiSelectedEnvironmentDTO | Unset
        if isinstance(_currently_selected_environment, Unset):
            currently_selected_environment = UNSET
        else:
            currently_selected_environment = DominoProjectsApiSelectedEnvironmentDTO.from_dict(
                _currently_selected_environment
            )

        domino_projects_api_useable_project_environments_dto = cls(
            environments=environments,
            currently_selected_environment=currently_selected_environment,
        )

        domino_projects_api_useable_project_environments_dto.additional_properties = d
        return domino_projects_api_useable_project_environments_dto

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
