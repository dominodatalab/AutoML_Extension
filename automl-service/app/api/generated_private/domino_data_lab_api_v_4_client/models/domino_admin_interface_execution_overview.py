from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_admin_interface_execution_overview_compute_grid_type import (
    DominoAdminInterfaceExecutionOverviewComputeGridType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_admin_interface_compute_cluster_overview import DominoAdminInterfaceComputeClusterOverview
    from ..models.domino_admin_interface_hardware_tier_overview import DominoAdminInterfaceHardwareTierOverview
    from ..models.domino_admin_interface_on_demand_spark_cluster_overview import (
        DominoAdminInterfaceOnDemandSparkClusterOverview,
    )
    from ..models.domino_admin_interface_on_demand_spark_execution_unit_overview import (
        DominoAdminInterfaceOnDemandSparkExecutionUnitOverview,
    )
    from ..models.domino_common_project_id import DominoCommonProjectId
    from ..models.domino_computegrid_execution_unit_overview import DominoComputegridExecutionUnitOverview


T = TypeVar("T", bound="DominoAdminInterfaceExecutionOverview")


@_attrs_define
class DominoAdminInterfaceExecutionOverview:
    """
    Attributes:
        id (str):
        compute_grid_type (DominoAdminInterfaceExecutionOverviewComputeGridType):
        project_id (str):
        project_identifier (DominoCommonProjectId):
        hardware_tier (DominoAdminInterfaceHardwareTierOverview):
        status (str):
        execution_units (list[DominoComputegridExecutionUnitOverview]):
        created (datetime.datetime):
        workload_type (str):
        compute_cluster_overviews (list[DominoAdminInterfaceComputeClusterOverview]):
        on_demand_spark_execution_units (list[DominoAdminInterfaceOnDemandSparkExecutionUnitOverview]):
        starting_user_id (None | str | Unset):
        starting_username (None | str | Unset):
        title (None | str | Unset):
        on_demand_spark_cluster_properties (DominoAdminInterfaceOnDemandSparkClusterOverview | Unset):
    """

    id: str
    compute_grid_type: DominoAdminInterfaceExecutionOverviewComputeGridType
    project_id: str
    project_identifier: DominoCommonProjectId
    hardware_tier: DominoAdminInterfaceHardwareTierOverview
    status: str
    execution_units: list[DominoComputegridExecutionUnitOverview]
    created: datetime.datetime
    workload_type: str
    compute_cluster_overviews: list[DominoAdminInterfaceComputeClusterOverview]
    on_demand_spark_execution_units: list[DominoAdminInterfaceOnDemandSparkExecutionUnitOverview]
    starting_user_id: None | str | Unset = UNSET
    starting_username: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    on_demand_spark_cluster_properties: DominoAdminInterfaceOnDemandSparkClusterOverview | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        compute_grid_type = self.compute_grid_type.value

        project_id = self.project_id

        project_identifier = self.project_identifier.to_dict()

        hardware_tier = self.hardware_tier.to_dict()

        status = self.status

        execution_units = []
        for execution_units_item_data in self.execution_units:
            execution_units_item = execution_units_item_data.to_dict()
            execution_units.append(execution_units_item)

        created = self.created.isoformat()

        workload_type = self.workload_type

        compute_cluster_overviews = []
        for compute_cluster_overviews_item_data in self.compute_cluster_overviews:
            compute_cluster_overviews_item = compute_cluster_overviews_item_data.to_dict()
            compute_cluster_overviews.append(compute_cluster_overviews_item)

        on_demand_spark_execution_units = []
        for on_demand_spark_execution_units_item_data in self.on_demand_spark_execution_units:
            on_demand_spark_execution_units_item = on_demand_spark_execution_units_item_data.to_dict()
            on_demand_spark_execution_units.append(on_demand_spark_execution_units_item)

        starting_user_id: None | str | Unset
        if isinstance(self.starting_user_id, Unset):
            starting_user_id = UNSET
        else:
            starting_user_id = self.starting_user_id

        starting_username: None | str | Unset
        if isinstance(self.starting_username, Unset):
            starting_username = UNSET
        else:
            starting_username = self.starting_username

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        on_demand_spark_cluster_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.on_demand_spark_cluster_properties, Unset):
            on_demand_spark_cluster_properties = self.on_demand_spark_cluster_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "computeGridType": compute_grid_type,
                "projectId": project_id,
                "projectIdentifier": project_identifier,
                "hardwareTier": hardware_tier,
                "status": status,
                "executionUnits": execution_units,
                "created": created,
                "workloadType": workload_type,
                "computeClusterOverviews": compute_cluster_overviews,
                "onDemandSparkExecutionUnits": on_demand_spark_execution_units,
            }
        )
        if starting_user_id is not UNSET:
            field_dict["startingUserId"] = starting_user_id
        if starting_username is not UNSET:
            field_dict["startingUsername"] = starting_username
        if title is not UNSET:
            field_dict["title"] = title
        if on_demand_spark_cluster_properties is not UNSET:
            field_dict["onDemandSparkClusterProperties"] = on_demand_spark_cluster_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_admin_interface_compute_cluster_overview import DominoAdminInterfaceComputeClusterOverview
        from ..models.domino_admin_interface_hardware_tier_overview import DominoAdminInterfaceHardwareTierOverview
        from ..models.domino_admin_interface_on_demand_spark_cluster_overview import (
            DominoAdminInterfaceOnDemandSparkClusterOverview,
        )
        from ..models.domino_admin_interface_on_demand_spark_execution_unit_overview import (
            DominoAdminInterfaceOnDemandSparkExecutionUnitOverview,
        )
        from ..models.domino_common_project_id import DominoCommonProjectId
        from ..models.domino_computegrid_execution_unit_overview import DominoComputegridExecutionUnitOverview

        d = dict(src_dict)
        id = d.pop("id")

        compute_grid_type = DominoAdminInterfaceExecutionOverviewComputeGridType(d.pop("computeGridType"))

        project_id = d.pop("projectId")

        project_identifier = DominoCommonProjectId.from_dict(d.pop("projectIdentifier"))

        hardware_tier = DominoAdminInterfaceHardwareTierOverview.from_dict(d.pop("hardwareTier"))

        status = d.pop("status")

        execution_units = []
        _execution_units = d.pop("executionUnits")
        for execution_units_item_data in _execution_units:
            execution_units_item = DominoComputegridExecutionUnitOverview.from_dict(execution_units_item_data)

            execution_units.append(execution_units_item)

        created = isoparse(d.pop("created"))

        workload_type = d.pop("workloadType")

        compute_cluster_overviews = []
        _compute_cluster_overviews = d.pop("computeClusterOverviews")
        for compute_cluster_overviews_item_data in _compute_cluster_overviews:
            compute_cluster_overviews_item = DominoAdminInterfaceComputeClusterOverview.from_dict(
                compute_cluster_overviews_item_data
            )

            compute_cluster_overviews.append(compute_cluster_overviews_item)

        on_demand_spark_execution_units = []
        _on_demand_spark_execution_units = d.pop("onDemandSparkExecutionUnits")
        for on_demand_spark_execution_units_item_data in _on_demand_spark_execution_units:
            on_demand_spark_execution_units_item = DominoAdminInterfaceOnDemandSparkExecutionUnitOverview.from_dict(
                on_demand_spark_execution_units_item_data
            )

            on_demand_spark_execution_units.append(on_demand_spark_execution_units_item)

        def _parse_starting_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        starting_user_id = _parse_starting_user_id(d.pop("startingUserId", UNSET))

        def _parse_starting_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        starting_username = _parse_starting_username(d.pop("startingUsername", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        _on_demand_spark_cluster_properties = d.pop("onDemandSparkClusterProperties", UNSET)
        on_demand_spark_cluster_properties: DominoAdminInterfaceOnDemandSparkClusterOverview | Unset
        if isinstance(_on_demand_spark_cluster_properties, Unset):
            on_demand_spark_cluster_properties = UNSET
        else:
            on_demand_spark_cluster_properties = DominoAdminInterfaceOnDemandSparkClusterOverview.from_dict(
                _on_demand_spark_cluster_properties
            )

        domino_admin_interface_execution_overview = cls(
            id=id,
            compute_grid_type=compute_grid_type,
            project_id=project_id,
            project_identifier=project_identifier,
            hardware_tier=hardware_tier,
            status=status,
            execution_units=execution_units,
            created=created,
            workload_type=workload_type,
            compute_cluster_overviews=compute_cluster_overviews,
            on_demand_spark_execution_units=on_demand_spark_execution_units,
            starting_user_id=starting_user_id,
            starting_username=starting_username,
            title=title,
            on_demand_spark_cluster_properties=on_demand_spark_cluster_properties,
        )

        domino_admin_interface_execution_overview.additional_properties = d
        return domino_admin_interface_execution_overview

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
