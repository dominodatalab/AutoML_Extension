from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_nucleus_project_project_settings_dto_default_environment_revision_spec_type_0 import (
    DominoNucleusProjectProjectSettingsDtoDefaultEnvironmentRevisionSpecType0,
)
from ..models.domino_nucleus_project_project_settings_dto_spark_cluster_mode import (
    DominoNucleusProjectProjectSettingsDtoSparkClusterMode,
)

if TYPE_CHECKING:
    from ..models.domino_nucleus_project_project_settings_dto_default_environment_revision_spec_type_1 import (
        DominoNucleusProjectProjectSettingsDtoDefaultEnvironmentRevisionSpecType1,
    )


T = TypeVar("T", bound="DominoNucleusProjectProjectSettingsDto")


@_attrs_define
class DominoNucleusProjectProjectSettingsDto:
    """
    Attributes:
        default_environment_id (str):
        default_environment_revision_spec (DominoNucleusProjectProjectSettingsDtoDefaultEnvironmentRevisionSpecType0 |
            DominoNucleusProjectProjectSettingsDtoDefaultEnvironmentRevisionSpecType1):
        default_hardware_tier_id (str):
        spark_cluster_mode (DominoNucleusProjectProjectSettingsDtoSparkClusterMode):
        default_volume_size_gi_b (float):
        max_volume_size_gi_b (float):
        min_volume_size_gi_b (float):
        recommended_volume_size_gi_b (float):
    """

    default_environment_id: str
    default_environment_revision_spec: (
        DominoNucleusProjectProjectSettingsDtoDefaultEnvironmentRevisionSpecType0
        | DominoNucleusProjectProjectSettingsDtoDefaultEnvironmentRevisionSpecType1
    )
    default_hardware_tier_id: str
    spark_cluster_mode: DominoNucleusProjectProjectSettingsDtoSparkClusterMode
    default_volume_size_gi_b: float
    max_volume_size_gi_b: float
    min_volume_size_gi_b: float
    recommended_volume_size_gi_b: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_environment_id = self.default_environment_id

        default_environment_revision_spec: dict[str, Any] | str
        if isinstance(
            self.default_environment_revision_spec,
            DominoNucleusProjectProjectSettingsDtoDefaultEnvironmentRevisionSpecType0,
        ):
            default_environment_revision_spec = self.default_environment_revision_spec.value
        else:
            default_environment_revision_spec = self.default_environment_revision_spec.to_dict()

        default_hardware_tier_id = self.default_hardware_tier_id

        spark_cluster_mode = self.spark_cluster_mode.value

        default_volume_size_gi_b = self.default_volume_size_gi_b

        max_volume_size_gi_b = self.max_volume_size_gi_b

        min_volume_size_gi_b = self.min_volume_size_gi_b

        recommended_volume_size_gi_b = self.recommended_volume_size_gi_b

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "defaultEnvironmentId": default_environment_id,
                "defaultEnvironmentRevisionSpec": default_environment_revision_spec,
                "defaultHardwareTierId": default_hardware_tier_id,
                "sparkClusterMode": spark_cluster_mode,
                "defaultVolumeSizeGiB": default_volume_size_gi_b,
                "maxVolumeSizeGiB": max_volume_size_gi_b,
                "minVolumeSizeGiB": min_volume_size_gi_b,
                "recommendedVolumeSizeGiB": recommended_volume_size_gi_b,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_nucleus_project_project_settings_dto_default_environment_revision_spec_type_1 import (
            DominoNucleusProjectProjectSettingsDtoDefaultEnvironmentRevisionSpecType1,
        )

        d = dict(src_dict)
        default_environment_id = d.pop("defaultEnvironmentId")

        def _parse_default_environment_revision_spec(
            data: object,
        ) -> (
            DominoNucleusProjectProjectSettingsDtoDefaultEnvironmentRevisionSpecType0
            | DominoNucleusProjectProjectSettingsDtoDefaultEnvironmentRevisionSpecType1
        ):
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_environment_revision_spec_type_0 = (
                    DominoNucleusProjectProjectSettingsDtoDefaultEnvironmentRevisionSpecType0(data)
                )

                return default_environment_revision_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            default_environment_revision_spec_type_1 = (
                DominoNucleusProjectProjectSettingsDtoDefaultEnvironmentRevisionSpecType1.from_dict(data)
            )

            return default_environment_revision_spec_type_1

        default_environment_revision_spec = _parse_default_environment_revision_spec(
            d.pop("defaultEnvironmentRevisionSpec")
        )

        default_hardware_tier_id = d.pop("defaultHardwareTierId")

        spark_cluster_mode = DominoNucleusProjectProjectSettingsDtoSparkClusterMode(d.pop("sparkClusterMode"))

        default_volume_size_gi_b = d.pop("defaultVolumeSizeGiB")

        max_volume_size_gi_b = d.pop("maxVolumeSizeGiB")

        min_volume_size_gi_b = d.pop("minVolumeSizeGiB")

        recommended_volume_size_gi_b = d.pop("recommendedVolumeSizeGiB")

        domino_nucleus_project_project_settings_dto = cls(
            default_environment_id=default_environment_id,
            default_environment_revision_spec=default_environment_revision_spec,
            default_hardware_tier_id=default_hardware_tier_id,
            spark_cluster_mode=spark_cluster_mode,
            default_volume_size_gi_b=default_volume_size_gi_b,
            max_volume_size_gi_b=max_volume_size_gi_b,
            min_volume_size_gi_b=min_volume_size_gi_b,
            recommended_volume_size_gi_b=recommended_volume_size_gi_b,
        )

        domino_nucleus_project_project_settings_dto.additional_properties = d
        return domino_nucleus_project_project_settings_dto

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
