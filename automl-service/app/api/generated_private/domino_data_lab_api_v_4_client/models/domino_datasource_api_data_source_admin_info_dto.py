from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_datasource_api_data_source_admin_info_dto_project_id_owner_username_map import (
        DominoDatasourceApiDataSourceAdminInfoDtoProjectIdOwnerUsernameMap,
    )
    from ..models.domino_datasource_api_data_source_admin_info_dto_project_last_active_map import (
        DominoDatasourceApiDataSourceAdminInfoDtoProjectLastActiveMap,
    )
    from ..models.domino_datasource_api_data_source_admin_info_dto_project_names import (
        DominoDatasourceApiDataSourceAdminInfoDtoProjectNames,
    )


T = TypeVar("T", bound="DominoDatasourceApiDataSourceAdminInfoDto")


@_attrs_define
class DominoDatasourceApiDataSourceAdminInfoDto:
    """
    Attributes:
        project_last_active_map (DominoDatasourceApiDataSourceAdminInfoDtoProjectLastActiveMap):
        project_names (DominoDatasourceApiDataSourceAdminInfoDtoProjectNames):
        project_id_owner_username_map (DominoDatasourceApiDataSourceAdminInfoDtoProjectIdOwnerUsernameMap):
    """

    project_last_active_map: DominoDatasourceApiDataSourceAdminInfoDtoProjectLastActiveMap
    project_names: DominoDatasourceApiDataSourceAdminInfoDtoProjectNames
    project_id_owner_username_map: DominoDatasourceApiDataSourceAdminInfoDtoProjectIdOwnerUsernameMap
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_last_active_map = self.project_last_active_map.to_dict()

        project_names = self.project_names.to_dict()

        project_id_owner_username_map = self.project_id_owner_username_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectLastActiveMap": project_last_active_map,
                "projectNames": project_names,
                "projectIdOwnerUsernameMap": project_id_owner_username_map,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasource_api_data_source_admin_info_dto_project_id_owner_username_map import (
            DominoDatasourceApiDataSourceAdminInfoDtoProjectIdOwnerUsernameMap,
        )
        from ..models.domino_datasource_api_data_source_admin_info_dto_project_last_active_map import (
            DominoDatasourceApiDataSourceAdminInfoDtoProjectLastActiveMap,
        )
        from ..models.domino_datasource_api_data_source_admin_info_dto_project_names import (
            DominoDatasourceApiDataSourceAdminInfoDtoProjectNames,
        )

        d = dict(src_dict)
        project_last_active_map = DominoDatasourceApiDataSourceAdminInfoDtoProjectLastActiveMap.from_dict(
            d.pop("projectLastActiveMap")
        )

        project_names = DominoDatasourceApiDataSourceAdminInfoDtoProjectNames.from_dict(d.pop("projectNames"))

        project_id_owner_username_map = DominoDatasourceApiDataSourceAdminInfoDtoProjectIdOwnerUsernameMap.from_dict(
            d.pop("projectIdOwnerUsernameMap")
        )

        domino_datasource_api_data_source_admin_info_dto = cls(
            project_last_active_map=project_last_active_map,
            project_names=project_names,
            project_id_owner_username_map=project_id_owner_username_map,
        )

        domino_datasource_api_data_source_admin_info_dto.additional_properties = d
        return domino_datasource_api_data_source_admin_info_dto

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
