from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_revision import EnvironmentRevision
    from ..models.hardware_tier import HardwareTier


T = TypeVar("T", bound="ProjectSettings")


@_attrs_define
class ProjectSettings:
    """
    Attributes:
        default_environment_revision (EnvironmentRevision):
        default_hardware_tier (HardwareTier):
        compute_cluster_environment_revision (EnvironmentRevision | Unset):
    """

    default_environment_revision: EnvironmentRevision
    default_hardware_tier: HardwareTier
    compute_cluster_environment_revision: EnvironmentRevision | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_environment_revision = self.default_environment_revision.to_dict()

        default_hardware_tier = self.default_hardware_tier.to_dict()

        compute_cluster_environment_revision: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster_environment_revision, Unset):
            compute_cluster_environment_revision = self.compute_cluster_environment_revision.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "defaultEnvironmentRevision": default_environment_revision,
                "defaultHardwareTier": default_hardware_tier,
            }
        )
        if compute_cluster_environment_revision is not UNSET:
            field_dict["computeClusterEnvironmentRevision"] = compute_cluster_environment_revision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_revision import EnvironmentRevision
        from ..models.hardware_tier import HardwareTier

        d = dict(src_dict)
        default_environment_revision = EnvironmentRevision.from_dict(d.pop("defaultEnvironmentRevision"))

        default_hardware_tier = HardwareTier.from_dict(d.pop("defaultHardwareTier"))

        _compute_cluster_environment_revision = d.pop("computeClusterEnvironmentRevision", UNSET)
        compute_cluster_environment_revision: EnvironmentRevision | Unset
        if isinstance(_compute_cluster_environment_revision, Unset):
            compute_cluster_environment_revision = UNSET
        else:
            compute_cluster_environment_revision = EnvironmentRevision.from_dict(_compute_cluster_environment_revision)

        project_settings = cls(
            default_environment_revision=default_environment_revision,
            default_hardware_tier=default_hardware_tier,
            compute_cluster_environment_revision=compute_cluster_environment_revision,
        )

        project_settings.additional_properties = d
        return project_settings

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
