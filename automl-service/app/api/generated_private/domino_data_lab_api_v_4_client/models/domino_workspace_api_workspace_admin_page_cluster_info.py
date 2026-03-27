from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compute_cluster_type import ComputeClusterType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceAdminPageClusterInfo")


@_attrs_define
class DominoWorkspaceApiWorkspaceAdminPageClusterInfo:
    """
    Attributes:
        cluster_type (ComputeClusterType): Type of compute cluster
        min_workers (int):
        max_workers (int | None | Unset):
    """

    cluster_type: ComputeClusterType
    min_workers: int
    max_workers: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_type = self.cluster_type.value

        min_workers = self.min_workers

        max_workers: int | None | Unset
        if isinstance(self.max_workers, Unset):
            max_workers = UNSET
        else:
            max_workers = self.max_workers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clusterType": cluster_type,
                "minWorkers": min_workers,
            }
        )
        if max_workers is not UNSET:
            field_dict["maxWorkers"] = max_workers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cluster_type = ComputeClusterType(d.pop("clusterType"))

        min_workers = d.pop("minWorkers")

        def _parse_max_workers(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_workers = _parse_max_workers(d.pop("maxWorkers", UNSET))

        domino_workspace_api_workspace_admin_page_cluster_info = cls(
            cluster_type=cluster_type,
            min_workers=min_workers,
            max_workers=max_workers,
        )

        domino_workspace_api_workspace_admin_page_cluster_info.additional_properties = d
        return domino_workspace_api_workspace_admin_page_cluster_info

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
