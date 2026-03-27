from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasource_api_data_source_dto_auth_type import DominoDatasourceApiDataSourceDtoAuthType
from ..models.domino_datasource_api_data_source_dto_data_source_type import (
    DominoDatasourceApiDataSourceDtoDataSourceType,
)
from ..models.domino_datasource_api_data_source_dto_status import DominoDatasourceApiDataSourceDtoStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasource_api_data_source_admin_info_dto import DominoDatasourceApiDataSourceAdminInfoDto
    from ..models.domino_datasource_api_data_source_data_plane_info import DominoDatasourceApiDataSourceDataPlaneInfo
    from ..models.domino_datasource_api_data_source_dto_added_by import DominoDatasourceApiDataSourceDtoAddedBy
    from ..models.domino_datasource_api_data_source_dto_added_to_project_time_map import (
        DominoDatasourceApiDataSourceDtoAddedToProjectTimeMap,
    )
    from ..models.domino_datasource_api_data_source_dto_config import DominoDatasourceApiDataSourceDtoConfig
    from ..models.domino_datasource_api_data_source_dto_last_accessed import (
        DominoDatasourceApiDataSourceDtoLastAccessed,
    )
    from ..models.domino_datasource_api_data_source_owner_info_dto import DominoDatasourceApiDataSourceOwnerInfoDto
    from ..models.domino_datasource_api_data_source_permissions_dto import DominoDatasourceApiDataSourcePermissionsDto
    from ..models.domino_datasource_api_engine_info_dto import DominoDatasourceApiEngineInfoDto


T = TypeVar("T", bound="DominoDatasourceApiDataSourceDto")


@_attrs_define
class DominoDatasourceApiDataSourceDto:
    """
    Attributes:
        last_updated_by (str):
        added_by (DominoDatasourceApiDataSourceDtoAddedBy):
        owner_info (DominoDatasourceApiDataSourceOwnerInfoDto):
        project_ids (list[str]):
        owner_id (str):
        last_updated (int):
        admin_info (DominoDatasourceApiDataSourceAdminInfoDto):
        added_to_project_time_map (DominoDatasourceApiDataSourceDtoAddedToProjectTimeMap):
        data_source_permissions (DominoDatasourceApiDataSourcePermissionsDto):
        name (str):
        last_accessed (DominoDatasourceApiDataSourceDtoLastAccessed):
        id (str):
        config (DominoDatasourceApiDataSourceDtoConfig):
        data_source_type (DominoDatasourceApiDataSourceDtoDataSourceType):
        status (DominoDatasourceApiDataSourceDtoStatus):
        display_name (str | Unset):
        data_planes (list[DominoDatasourceApiDataSourceDataPlaneInfo] | Unset):
        description (None | str | Unset):
        auth_type (DominoDatasourceApiDataSourceDtoAuthType | Unset):
        use_all_data_planes (bool | Unset):
        engine_info (DominoDatasourceApiEngineInfoDto | Unset):
    """

    last_updated_by: str
    added_by: DominoDatasourceApiDataSourceDtoAddedBy
    owner_info: DominoDatasourceApiDataSourceOwnerInfoDto
    project_ids: list[str]
    owner_id: str
    last_updated: int
    admin_info: DominoDatasourceApiDataSourceAdminInfoDto
    added_to_project_time_map: DominoDatasourceApiDataSourceDtoAddedToProjectTimeMap
    data_source_permissions: DominoDatasourceApiDataSourcePermissionsDto
    name: str
    last_accessed: DominoDatasourceApiDataSourceDtoLastAccessed
    id: str
    config: DominoDatasourceApiDataSourceDtoConfig
    data_source_type: DominoDatasourceApiDataSourceDtoDataSourceType
    status: DominoDatasourceApiDataSourceDtoStatus
    display_name: str | Unset = UNSET
    data_planes: list[DominoDatasourceApiDataSourceDataPlaneInfo] | Unset = UNSET
    description: None | str | Unset = UNSET
    auth_type: DominoDatasourceApiDataSourceDtoAuthType | Unset = UNSET
    use_all_data_planes: bool | Unset = UNSET
    engine_info: DominoDatasourceApiEngineInfoDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_updated_by = self.last_updated_by

        added_by = self.added_by.to_dict()

        owner_info = self.owner_info.to_dict()

        project_ids = self.project_ids

        owner_id = self.owner_id

        last_updated = self.last_updated

        admin_info = self.admin_info.to_dict()

        added_to_project_time_map = self.added_to_project_time_map.to_dict()

        data_source_permissions = self.data_source_permissions.to_dict()

        name = self.name

        last_accessed = self.last_accessed.to_dict()

        id = self.id

        config = self.config.to_dict()

        data_source_type = self.data_source_type.value

        status = self.status.value

        display_name = self.display_name

        data_planes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_planes, Unset):
            data_planes = []
            for data_planes_item_data in self.data_planes:
                data_planes_item = data_planes_item_data.to_dict()
                data_planes.append(data_planes_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        auth_type: str | Unset = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.value

        use_all_data_planes = self.use_all_data_planes

        engine_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.engine_info, Unset):
            engine_info = self.engine_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastUpdatedBy": last_updated_by,
                "addedBy": added_by,
                "ownerInfo": owner_info,
                "projectIds": project_ids,
                "ownerId": owner_id,
                "lastUpdated": last_updated,
                "adminInfo": admin_info,
                "addedToProjectTimeMap": added_to_project_time_map,
                "dataSourcePermissions": data_source_permissions,
                "name": name,
                "lastAccessed": last_accessed,
                "id": id,
                "config": config,
                "dataSourceType": data_source_type,
                "status": status,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if data_planes is not UNSET:
            field_dict["dataPlanes"] = data_planes
        if description is not UNSET:
            field_dict["description"] = description
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if use_all_data_planes is not UNSET:
            field_dict["useAllDataPlanes"] = use_all_data_planes
        if engine_info is not UNSET:
            field_dict["engineInfo"] = engine_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasource_api_data_source_admin_info_dto import DominoDatasourceApiDataSourceAdminInfoDto
        from ..models.domino_datasource_api_data_source_data_plane_info import (
            DominoDatasourceApiDataSourceDataPlaneInfo,
        )
        from ..models.domino_datasource_api_data_source_dto_added_by import DominoDatasourceApiDataSourceDtoAddedBy
        from ..models.domino_datasource_api_data_source_dto_added_to_project_time_map import (
            DominoDatasourceApiDataSourceDtoAddedToProjectTimeMap,
        )
        from ..models.domino_datasource_api_data_source_dto_config import DominoDatasourceApiDataSourceDtoConfig
        from ..models.domino_datasource_api_data_source_dto_last_accessed import (
            DominoDatasourceApiDataSourceDtoLastAccessed,
        )
        from ..models.domino_datasource_api_data_source_owner_info_dto import DominoDatasourceApiDataSourceOwnerInfoDto
        from ..models.domino_datasource_api_data_source_permissions_dto import (
            DominoDatasourceApiDataSourcePermissionsDto,
        )
        from ..models.domino_datasource_api_engine_info_dto import DominoDatasourceApiEngineInfoDto

        d = dict(src_dict)
        last_updated_by = d.pop("lastUpdatedBy")

        added_by = DominoDatasourceApiDataSourceDtoAddedBy.from_dict(d.pop("addedBy"))

        owner_info = DominoDatasourceApiDataSourceOwnerInfoDto.from_dict(d.pop("ownerInfo"))

        project_ids = cast(list[str], d.pop("projectIds"))

        owner_id = d.pop("ownerId")

        last_updated = d.pop("lastUpdated")

        admin_info = DominoDatasourceApiDataSourceAdminInfoDto.from_dict(d.pop("adminInfo"))

        added_to_project_time_map = DominoDatasourceApiDataSourceDtoAddedToProjectTimeMap.from_dict(
            d.pop("addedToProjectTimeMap")
        )

        data_source_permissions = DominoDatasourceApiDataSourcePermissionsDto.from_dict(d.pop("dataSourcePermissions"))

        name = d.pop("name")

        last_accessed = DominoDatasourceApiDataSourceDtoLastAccessed.from_dict(d.pop("lastAccessed"))

        id = d.pop("id")

        config = DominoDatasourceApiDataSourceDtoConfig.from_dict(d.pop("config"))

        data_source_type = DominoDatasourceApiDataSourceDtoDataSourceType(d.pop("dataSourceType"))

        status = DominoDatasourceApiDataSourceDtoStatus(d.pop("status"))

        display_name = d.pop("displayName", UNSET)

        _data_planes = d.pop("dataPlanes", UNSET)
        data_planes: list[DominoDatasourceApiDataSourceDataPlaneInfo] | Unset = UNSET
        if _data_planes is not UNSET:
            data_planes = []
            for data_planes_item_data in _data_planes:
                data_planes_item = DominoDatasourceApiDataSourceDataPlaneInfo.from_dict(data_planes_item_data)

                data_planes.append(data_planes_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _auth_type = d.pop("authType", UNSET)
        auth_type: DominoDatasourceApiDataSourceDtoAuthType | Unset
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = DominoDatasourceApiDataSourceDtoAuthType(_auth_type)

        use_all_data_planes = d.pop("useAllDataPlanes", UNSET)

        _engine_info = d.pop("engineInfo", UNSET)
        engine_info: DominoDatasourceApiEngineInfoDto | Unset
        if isinstance(_engine_info, Unset):
            engine_info = UNSET
        else:
            engine_info = DominoDatasourceApiEngineInfoDto.from_dict(_engine_info)

        domino_datasource_api_data_source_dto = cls(
            last_updated_by=last_updated_by,
            added_by=added_by,
            owner_info=owner_info,
            project_ids=project_ids,
            owner_id=owner_id,
            last_updated=last_updated,
            admin_info=admin_info,
            added_to_project_time_map=added_to_project_time_map,
            data_source_permissions=data_source_permissions,
            name=name,
            last_accessed=last_accessed,
            id=id,
            config=config,
            data_source_type=data_source_type,
            status=status,
            display_name=display_name,
            data_planes=data_planes,
            description=description,
            auth_type=auth_type,
            use_all_data_planes=use_all_data_planes,
            engine_info=engine_info,
        )

        domino_datasource_api_data_source_dto.additional_properties = d
        return domino_datasource_api_data_source_dto

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
