from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_templates_api_models_new_environment_revision_dto import (
        DominoProjectsTemplatesApiModelsNewEnvironmentRevisionDto,
    )
    from ..models.domino_projects_templates_api_models_new_hardware_tier_dto import (
        DominoProjectsTemplatesApiModelsNewHardwareTierDto,
    )


T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsNewSettingsDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsNewSettingsDto:
    """
    Attributes:
        default_environment_revision (DominoProjectsTemplatesApiModelsNewEnvironmentRevisionDto):
        default_hardware_tier (DominoProjectsTemplatesApiModelsNewHardwareTierDto):
        compute_cluster_environment_revision (DominoProjectsTemplatesApiModelsNewEnvironmentRevisionDto | Unset):
    """

    default_environment_revision: DominoProjectsTemplatesApiModelsNewEnvironmentRevisionDto
    default_hardware_tier: DominoProjectsTemplatesApiModelsNewHardwareTierDto
    compute_cluster_environment_revision: DominoProjectsTemplatesApiModelsNewEnvironmentRevisionDto | Unset = UNSET
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
        from ..models.domino_projects_templates_api_models_new_environment_revision_dto import (
            DominoProjectsTemplatesApiModelsNewEnvironmentRevisionDto,
        )
        from ..models.domino_projects_templates_api_models_new_hardware_tier_dto import (
            DominoProjectsTemplatesApiModelsNewHardwareTierDto,
        )

        d = dict(src_dict)
        default_environment_revision = DominoProjectsTemplatesApiModelsNewEnvironmentRevisionDto.from_dict(
            d.pop("defaultEnvironmentRevision")
        )

        default_hardware_tier = DominoProjectsTemplatesApiModelsNewHardwareTierDto.from_dict(
            d.pop("defaultHardwareTier")
        )

        _compute_cluster_environment_revision = d.pop("computeClusterEnvironmentRevision", UNSET)
        compute_cluster_environment_revision: DominoProjectsTemplatesApiModelsNewEnvironmentRevisionDto | Unset
        if isinstance(_compute_cluster_environment_revision, Unset):
            compute_cluster_environment_revision = UNSET
        else:
            compute_cluster_environment_revision = DominoProjectsTemplatesApiModelsNewEnvironmentRevisionDto.from_dict(
                _compute_cluster_environment_revision
            )

        domino_projects_templates_api_models_new_settings_dto = cls(
            default_environment_revision=default_environment_revision,
            default_hardware_tier=default_hardware_tier,
            compute_cluster_environment_revision=compute_cluster_environment_revision,
        )

        domino_projects_templates_api_models_new_settings_dto.additional_properties = d
        return domino_projects_templates_api_models_new_settings_dto

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
