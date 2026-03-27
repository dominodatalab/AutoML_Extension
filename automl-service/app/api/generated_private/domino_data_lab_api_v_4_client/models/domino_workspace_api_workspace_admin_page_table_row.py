from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_workspace_api_workspace_admin_page_table_row_workspace_state import (
    DominoWorkspaceApiWorkspaceAdminPageTableRowWorkspaceState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_dataplane_data_plane_name import DominoDataplaneDataPlaneName
    from ..models.domino_workspace_api_workspace_admin_page_cluster_info import (
        DominoWorkspaceApiWorkspaceAdminPageClusterInfo,
    )
    from ..models.domino_workspace_api_workspace_admin_page_table_row_disk_usage_type_0 import (
        DominoWorkspaceApiWorkspaceAdminPageTableRowDiskUsageType0,
    )
    from ..models.information import Information


T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceAdminPageTableRow")


@_attrs_define
class DominoWorkspaceApiWorkspaceAdminPageTableRow:
    """
    Attributes:
        workspace_id (str):
        name (str):
        owner_username (str):
        workspace_created_time (datetime.datetime):
        environment_name (str):
        pv_space (Information):
        project_name (str):
        project_owner_name (str):
        workspace_state (DominoWorkspaceApiWorkspaceAdminPageTableRowWorkspaceState):
        pvc_name (str):
        data_plane_name (DominoDataplaneDataPlaneName):
        last_session_start (datetime.datetime | None | Unset):
        environment_revision_id (None | str | Unset):
        environment_revision_number (int | None | Unset):
        cluster_info (DominoWorkspaceApiWorkspaceAdminPageClusterInfo | Unset):
        disk_usage (DominoWorkspaceApiWorkspaceAdminPageTableRowDiskUsageType0 | None | Unset):
    """

    workspace_id: str
    name: str
    owner_username: str
    workspace_created_time: datetime.datetime
    environment_name: str
    pv_space: Information
    project_name: str
    project_owner_name: str
    workspace_state: DominoWorkspaceApiWorkspaceAdminPageTableRowWorkspaceState
    pvc_name: str
    data_plane_name: DominoDataplaneDataPlaneName
    last_session_start: datetime.datetime | None | Unset = UNSET
    environment_revision_id: None | str | Unset = UNSET
    environment_revision_number: int | None | Unset = UNSET
    cluster_info: DominoWorkspaceApiWorkspaceAdminPageClusterInfo | Unset = UNSET
    disk_usage: DominoWorkspaceApiWorkspaceAdminPageTableRowDiskUsageType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_workspace_api_workspace_admin_page_table_row_disk_usage_type_0 import (
            DominoWorkspaceApiWorkspaceAdminPageTableRowDiskUsageType0,
        )

        workspace_id = self.workspace_id

        name = self.name

        owner_username = self.owner_username

        workspace_created_time = self.workspace_created_time.isoformat()

        environment_name = self.environment_name

        pv_space = self.pv_space.to_dict()

        project_name = self.project_name

        project_owner_name = self.project_owner_name

        workspace_state = self.workspace_state.value

        pvc_name = self.pvc_name

        data_plane_name = self.data_plane_name.to_dict()

        last_session_start: None | str | Unset
        if isinstance(self.last_session_start, Unset):
            last_session_start = UNSET
        elif isinstance(self.last_session_start, datetime.datetime):
            last_session_start = self.last_session_start.isoformat()
        else:
            last_session_start = self.last_session_start

        environment_revision_id: None | str | Unset
        if isinstance(self.environment_revision_id, Unset):
            environment_revision_id = UNSET
        else:
            environment_revision_id = self.environment_revision_id

        environment_revision_number: int | None | Unset
        if isinstance(self.environment_revision_number, Unset):
            environment_revision_number = UNSET
        else:
            environment_revision_number = self.environment_revision_number

        cluster_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cluster_info, Unset):
            cluster_info = self.cluster_info.to_dict()

        disk_usage: dict[str, Any] | None | Unset
        if isinstance(self.disk_usage, Unset):
            disk_usage = UNSET
        elif isinstance(self.disk_usage, DominoWorkspaceApiWorkspaceAdminPageTableRowDiskUsageType0):
            disk_usage = self.disk_usage.to_dict()
        else:
            disk_usage = self.disk_usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspaceId": workspace_id,
                "name": name,
                "ownerUsername": owner_username,
                "workspaceCreatedTime": workspace_created_time,
                "environmentName": environment_name,
                "pvSpace": pv_space,
                "projectName": project_name,
                "projectOwnerName": project_owner_name,
                "workspaceState": workspace_state,
                "pvcName": pvc_name,
                "dataPlaneName": data_plane_name,
            }
        )
        if last_session_start is not UNSET:
            field_dict["lastSessionStart"] = last_session_start
        if environment_revision_id is not UNSET:
            field_dict["environmentRevisionId"] = environment_revision_id
        if environment_revision_number is not UNSET:
            field_dict["environmentRevisionNumber"] = environment_revision_number
        if cluster_info is not UNSET:
            field_dict["clusterInfo"] = cluster_info
        if disk_usage is not UNSET:
            field_dict["diskUsage"] = disk_usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_dataplane_data_plane_name import DominoDataplaneDataPlaneName
        from ..models.domino_workspace_api_workspace_admin_page_cluster_info import (
            DominoWorkspaceApiWorkspaceAdminPageClusterInfo,
        )
        from ..models.domino_workspace_api_workspace_admin_page_table_row_disk_usage_type_0 import (
            DominoWorkspaceApiWorkspaceAdminPageTableRowDiskUsageType0,
        )
        from ..models.information import Information

        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        name = d.pop("name")

        owner_username = d.pop("ownerUsername")

        workspace_created_time = isoparse(d.pop("workspaceCreatedTime"))

        environment_name = d.pop("environmentName")

        pv_space = Information.from_dict(d.pop("pvSpace"))

        project_name = d.pop("projectName")

        project_owner_name = d.pop("projectOwnerName")

        workspace_state = DominoWorkspaceApiWorkspaceAdminPageTableRowWorkspaceState(d.pop("workspaceState"))

        pvc_name = d.pop("pvcName")

        data_plane_name = DominoDataplaneDataPlaneName.from_dict(d.pop("dataPlaneName"))

        def _parse_last_session_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_session_start_type_0 = isoparse(data)

                return last_session_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_session_start = _parse_last_session_start(d.pop("lastSessionStart", UNSET))

        def _parse_environment_revision_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        environment_revision_id = _parse_environment_revision_id(d.pop("environmentRevisionId", UNSET))

        def _parse_environment_revision_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        environment_revision_number = _parse_environment_revision_number(d.pop("environmentRevisionNumber", UNSET))

        _cluster_info = d.pop("clusterInfo", UNSET)
        cluster_info: DominoWorkspaceApiWorkspaceAdminPageClusterInfo | Unset
        if isinstance(_cluster_info, Unset):
            cluster_info = UNSET
        else:
            cluster_info = DominoWorkspaceApiWorkspaceAdminPageClusterInfo.from_dict(_cluster_info)

        def _parse_disk_usage(
            data: object,
        ) -> DominoWorkspaceApiWorkspaceAdminPageTableRowDiskUsageType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                disk_usage_type_0 = DominoWorkspaceApiWorkspaceAdminPageTableRowDiskUsageType0.from_dict(data)

                return disk_usage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DominoWorkspaceApiWorkspaceAdminPageTableRowDiskUsageType0 | None | Unset, data)

        disk_usage = _parse_disk_usage(d.pop("diskUsage", UNSET))

        domino_workspace_api_workspace_admin_page_table_row = cls(
            workspace_id=workspace_id,
            name=name,
            owner_username=owner_username,
            workspace_created_time=workspace_created_time,
            environment_name=environment_name,
            pv_space=pv_space,
            project_name=project_name,
            project_owner_name=project_owner_name,
            workspace_state=workspace_state,
            pvc_name=pvc_name,
            data_plane_name=data_plane_name,
            last_session_start=last_session_start,
            environment_revision_id=environment_revision_id,
            environment_revision_number=environment_revision_number,
            cluster_info=cluster_info,
            disk_usage=disk_usage,
        )

        domino_workspace_api_workspace_admin_page_table_row.additional_properties = d
        return domino_workspace_api_workspace_admin_page_table_row

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
