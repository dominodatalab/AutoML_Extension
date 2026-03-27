from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_api_repositories_access_type_dto import DominoProjectsApiRepositoriesAccessTypeDto


T = TypeVar("T", bound="DominoProjectsApiRepositoriesGitProviderDto")


@_attrs_define
class DominoProjectsApiRepositoriesGitProviderDto:
    """
    Attributes:
        value (str):
        label (str):
        requires_domain (bool):
        access_types (list[DominoProjectsApiRepositoriesAccessTypeDto]):
    """

    value: str
    label: str
    requires_domain: bool
    access_types: list[DominoProjectsApiRepositoriesAccessTypeDto]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        label = self.label

        requires_domain = self.requires_domain

        access_types = []
        for access_types_item_data in self.access_types:
            access_types_item = access_types_item_data.to_dict()
            access_types.append(access_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "label": label,
                "requiresDomain": requires_domain,
                "accessTypes": access_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_repositories_access_type_dto import DominoProjectsApiRepositoriesAccessTypeDto

        d = dict(src_dict)
        value = d.pop("value")

        label = d.pop("label")

        requires_domain = d.pop("requiresDomain")

        access_types = []
        _access_types = d.pop("accessTypes")
        for access_types_item_data in _access_types:
            access_types_item = DominoProjectsApiRepositoriesAccessTypeDto.from_dict(access_types_item_data)

            access_types.append(access_types_item)

        domino_projects_api_repositories_git_provider_dto = cls(
            value=value,
            label=label,
            requires_domain=requires_domain,
            access_types=access_types,
        )

        domino_projects_api_repositories_git_provider_dto.additional_properties = d
        return domino_projects_api_repositories_git_provider_dto

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
