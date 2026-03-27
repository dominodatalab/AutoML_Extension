from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_on_demand_spark_cluster_status_cluster_state import (
    DominoProjectsApiOnDemandSparkClusterStatusClusterState,
)

T = TypeVar("T", bound="DominoProjectsApiOnDemandSparkClusterStatus")


@_attrs_define
class DominoProjectsApiOnDemandSparkClusterStatus:
    """
    Attributes:
        cluster_name (str):
        cluster_state (DominoProjectsApiOnDemandSparkClusterStatusClusterState):
        exists (bool):
        is_ready (bool):
        worker_count (int):
    """

    cluster_name: str
    cluster_state: DominoProjectsApiOnDemandSparkClusterStatusClusterState
    exists: bool
    is_ready: bool
    worker_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_name = self.cluster_name

        cluster_state = self.cluster_state.value

        exists = self.exists

        is_ready = self.is_ready

        worker_count = self.worker_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clusterName": cluster_name,
                "clusterState": cluster_state,
                "exists": exists,
                "isReady": is_ready,
                "workerCount": worker_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cluster_name = d.pop("clusterName")

        cluster_state = DominoProjectsApiOnDemandSparkClusterStatusClusterState(d.pop("clusterState"))

        exists = d.pop("exists")

        is_ready = d.pop("isReady")

        worker_count = d.pop("workerCount")

        domino_projects_api_on_demand_spark_cluster_status = cls(
            cluster_name=cluster_name,
            cluster_state=cluster_state,
            exists=exists,
            is_ready=is_ready,
            worker_count=worker_count,
        )

        domino_projects_api_on_demand_spark_cluster_status.additional_properties = d
        return domino_projects_api_on_demand_spark_cluster_status

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
