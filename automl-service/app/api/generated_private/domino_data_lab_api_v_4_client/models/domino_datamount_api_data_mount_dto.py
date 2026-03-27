from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datamount_api_data_mount_dto_volume_type import DominoDatamountApiDataMountDtoVolumeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datamount_api_data_mount_project_info_dto import DominoDatamountApiDataMountProjectInfoDto
    from ..models.domino_dataplane_data_plane_dto import DominoDataplaneDataPlaneDto


T = TypeVar("T", bound="DominoDatamountApiDataMountDto")


@_attrs_define
class DominoDatamountApiDataMountDto:
    """
    Attributes:
        id (str):
        name (str):
        volume_type (DominoDatamountApiDataMountDtoVolumeType):
        pvc_name (str):
        pv_id (str):
        mount_path (str):
        users (list[str]):
        projects (list[str]):
        read_only (bool):
        is_public (bool):
        is_registered (bool):
        data_planes (list[DominoDataplaneDataPlaneDto]):
        description (None | str | Unset):
        status (None | str | Unset):
        projects_info (list[DominoDatamountApiDataMountProjectInfoDto] | None | Unset):
    """

    id: str
    name: str
    volume_type: DominoDatamountApiDataMountDtoVolumeType
    pvc_name: str
    pv_id: str
    mount_path: str
    users: list[str]
    projects: list[str]
    read_only: bool
    is_public: bool
    is_registered: bool
    data_planes: list[DominoDataplaneDataPlaneDto]
    description: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    projects_info: list[DominoDatamountApiDataMountProjectInfoDto] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        volume_type = self.volume_type.value

        pvc_name = self.pvc_name

        pv_id = self.pv_id

        mount_path = self.mount_path

        users = self.users

        projects = self.projects

        read_only = self.read_only

        is_public = self.is_public

        is_registered = self.is_registered

        data_planes = []
        for data_planes_item_data in self.data_planes:
            data_planes_item = data_planes_item_data.to_dict()
            data_planes.append(data_planes_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        projects_info: list[dict[str, Any]] | None | Unset
        if isinstance(self.projects_info, Unset):
            projects_info = UNSET
        elif isinstance(self.projects_info, list):
            projects_info = []
            for projects_info_type_0_item_data in self.projects_info:
                projects_info_type_0_item = projects_info_type_0_item_data.to_dict()
                projects_info.append(projects_info_type_0_item)

        else:
            projects_info = self.projects_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "volumeType": volume_type,
                "pvcName": pvc_name,
                "pvId": pv_id,
                "mountPath": mount_path,
                "users": users,
                "projects": projects,
                "readOnly": read_only,
                "isPublic": is_public,
                "isRegistered": is_registered,
                "dataPlanes": data_planes,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if projects_info is not UNSET:
            field_dict["projectsInfo"] = projects_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datamount_api_data_mount_project_info_dto import DominoDatamountApiDataMountProjectInfoDto
        from ..models.domino_dataplane_data_plane_dto import DominoDataplaneDataPlaneDto

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        volume_type = DominoDatamountApiDataMountDtoVolumeType(d.pop("volumeType"))

        pvc_name = d.pop("pvcName")

        pv_id = d.pop("pvId")

        mount_path = d.pop("mountPath")

        users = cast(list[str], d.pop("users"))

        projects = cast(list[str], d.pop("projects"))

        read_only = d.pop("readOnly")

        is_public = d.pop("isPublic")

        is_registered = d.pop("isRegistered")

        data_planes = []
        _data_planes = d.pop("dataPlanes")
        for data_planes_item_data in _data_planes:
            data_planes_item = DominoDataplaneDataPlaneDto.from_dict(data_planes_item_data)

            data_planes.append(data_planes_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_projects_info(data: object) -> list[DominoDatamountApiDataMountProjectInfoDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                projects_info_type_0 = []
                _projects_info_type_0 = data
                for projects_info_type_0_item_data in _projects_info_type_0:
                    projects_info_type_0_item = DominoDatamountApiDataMountProjectInfoDto.from_dict(
                        projects_info_type_0_item_data
                    )

                    projects_info_type_0.append(projects_info_type_0_item)

                return projects_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoDatamountApiDataMountProjectInfoDto] | None | Unset, data)

        projects_info = _parse_projects_info(d.pop("projectsInfo", UNSET))

        domino_datamount_api_data_mount_dto = cls(
            id=id,
            name=name,
            volume_type=volume_type,
            pvc_name=pvc_name,
            pv_id=pv_id,
            mount_path=mount_path,
            users=users,
            projects=projects,
            read_only=read_only,
            is_public=is_public,
            is_registered=is_registered,
            data_planes=data_planes,
            description=description,
            status=status,
            projects_info=projects_info,
        )

        domino_datamount_api_data_mount_dto.additional_properties = d
        return domino_datamount_api_data_mount_dto

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
