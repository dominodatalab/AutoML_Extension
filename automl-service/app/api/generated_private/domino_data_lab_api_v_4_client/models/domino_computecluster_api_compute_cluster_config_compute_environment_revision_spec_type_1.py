from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoComputeclusterApiComputeClusterConfigComputeEnvironmentRevisionSpecType1")


@_attrs_define
class DominoComputeclusterApiComputeClusterConfigComputeEnvironmentRevisionSpecType1:
    """
    Attributes:
        revision_id (str):
    """

    revision_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revision_id = self.revision_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revisionId": revision_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        revision_id = d.pop("revisionId")

        domino_computecluster_api_compute_cluster_config_compute_environment_revision_spec_type_1 = cls(
            revision_id=revision_id,
        )

        domino_computecluster_api_compute_cluster_config_compute_environment_revision_spec_type_1.additional_properties = d
        return domino_computecluster_api_compute_cluster_config_compute_environment_revision_spec_type_1

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
