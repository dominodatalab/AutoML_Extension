from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_api_on_demand_spark_cluster_properties_spec import (
        DominoProjectsApiOnDemandSparkClusterPropertiesSpec,
    )


T = TypeVar("T", bound="DominoProjectsApiOnDemandSparkClusterDetailsView")


@_attrs_define
class DominoProjectsApiOnDemandSparkClusterDetailsView:
    """
    Attributes:
        spark_cluster_properties (DominoProjectsApiOnDemandSparkClusterPropertiesSpec):
        spark_cluster_uri (str):
    """

    spark_cluster_properties: DominoProjectsApiOnDemandSparkClusterPropertiesSpec
    spark_cluster_uri: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spark_cluster_properties = self.spark_cluster_properties.to_dict()

        spark_cluster_uri = self.spark_cluster_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sparkClusterProperties": spark_cluster_properties,
                "sparkClusterUri": spark_cluster_uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_on_demand_spark_cluster_properties_spec import (
            DominoProjectsApiOnDemandSparkClusterPropertiesSpec,
        )

        d = dict(src_dict)
        spark_cluster_properties = DominoProjectsApiOnDemandSparkClusterPropertiesSpec.from_dict(
            d.pop("sparkClusterProperties")
        )

        spark_cluster_uri = d.pop("sparkClusterUri")

        domino_projects_api_on_demand_spark_cluster_details_view = cls(
            spark_cluster_properties=spark_cluster_properties,
            spark_cluster_uri=spark_cluster_uri,
        )

        domino_projects_api_on_demand_spark_cluster_details_view.additional_properties = d
        return domino_projects_api_on_demand_spark_cluster_details_view

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
