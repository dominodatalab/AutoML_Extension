from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_nucleus_project_project_settings_update_dto_default_environment_revision_spec_type_0 import (
    DominoNucleusProjectProjectSettingsUpdateDtoDefaultEnvironmentRevisionSpecType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_nucleus_project_project_settings_update_dto_default_environment_revision_spec_type_1 import (
        DominoNucleusProjectProjectSettingsUpdateDtoDefaultEnvironmentRevisionSpecType1,
    )


T = TypeVar("T", bound="DominoNucleusProjectProjectSettingsUpdateDto")


@_attrs_define
class DominoNucleusProjectProjectSettingsUpdateDto:
    """
    Attributes:
        default_environment_id (None | str | Unset):
        default_environment_revision_spec
            (DominoNucleusProjectProjectSettingsUpdateDtoDefaultEnvironmentRevisionSpecType0 |
            DominoNucleusProjectProjectSettingsUpdateDtoDefaultEnvironmentRevisionSpecType1 | None | Unset):
        default_hardware_tier_id (None | str | Unset):
        default_volume_size_gi_b (float | None | Unset):
    """

    default_environment_id: None | str | Unset = UNSET
    default_environment_revision_spec: (
        DominoNucleusProjectProjectSettingsUpdateDtoDefaultEnvironmentRevisionSpecType0
        | DominoNucleusProjectProjectSettingsUpdateDtoDefaultEnvironmentRevisionSpecType1
        | None
        | Unset
    ) = UNSET
    default_hardware_tier_id: None | str | Unset = UNSET
    default_volume_size_gi_b: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_nucleus_project_project_settings_update_dto_default_environment_revision_spec_type_1 import (
            DominoNucleusProjectProjectSettingsUpdateDtoDefaultEnvironmentRevisionSpecType1,
        )

        default_environment_id: None | str | Unset
        if isinstance(self.default_environment_id, Unset):
            default_environment_id = UNSET
        else:
            default_environment_id = self.default_environment_id

        default_environment_revision_spec: dict[str, Any] | None | str | Unset
        if isinstance(self.default_environment_revision_spec, Unset):
            default_environment_revision_spec = UNSET
        elif isinstance(
            self.default_environment_revision_spec,
            DominoNucleusProjectProjectSettingsUpdateDtoDefaultEnvironmentRevisionSpecType0,
        ):
            default_environment_revision_spec = self.default_environment_revision_spec.value
        elif isinstance(
            self.default_environment_revision_spec,
            DominoNucleusProjectProjectSettingsUpdateDtoDefaultEnvironmentRevisionSpecType1,
        ):
            default_environment_revision_spec = self.default_environment_revision_spec.to_dict()
        else:
            default_environment_revision_spec = self.default_environment_revision_spec

        default_hardware_tier_id: None | str | Unset
        if isinstance(self.default_hardware_tier_id, Unset):
            default_hardware_tier_id = UNSET
        else:
            default_hardware_tier_id = self.default_hardware_tier_id

        default_volume_size_gi_b: float | None | Unset
        if isinstance(self.default_volume_size_gi_b, Unset):
            default_volume_size_gi_b = UNSET
        else:
            default_volume_size_gi_b = self.default_volume_size_gi_b

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_environment_id is not UNSET:
            field_dict["defaultEnvironmentId"] = default_environment_id
        if default_environment_revision_spec is not UNSET:
            field_dict["defaultEnvironmentRevisionSpec"] = default_environment_revision_spec
        if default_hardware_tier_id is not UNSET:
            field_dict["defaultHardwareTierId"] = default_hardware_tier_id
        if default_volume_size_gi_b is not UNSET:
            field_dict["defaultVolumeSizeGiB"] = default_volume_size_gi_b

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_nucleus_project_project_settings_update_dto_default_environment_revision_spec_type_1 import (
            DominoNucleusProjectProjectSettingsUpdateDtoDefaultEnvironmentRevisionSpecType1,
        )

        d = dict(src_dict)

        def _parse_default_environment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_environment_id = _parse_default_environment_id(d.pop("defaultEnvironmentId", UNSET))

        def _parse_default_environment_revision_spec(
            data: object,
        ) -> (
            DominoNucleusProjectProjectSettingsUpdateDtoDefaultEnvironmentRevisionSpecType0
            | DominoNucleusProjectProjectSettingsUpdateDtoDefaultEnvironmentRevisionSpecType1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_environment_revision_spec_type_0 = (
                    DominoNucleusProjectProjectSettingsUpdateDtoDefaultEnvironmentRevisionSpecType0(data)
                )

                return default_environment_revision_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_environment_revision_spec_type_1 = (
                    DominoNucleusProjectProjectSettingsUpdateDtoDefaultEnvironmentRevisionSpecType1.from_dict(data)
                )

                return default_environment_revision_spec_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DominoNucleusProjectProjectSettingsUpdateDtoDefaultEnvironmentRevisionSpecType0
                | DominoNucleusProjectProjectSettingsUpdateDtoDefaultEnvironmentRevisionSpecType1
                | None
                | Unset,
                data,
            )

        default_environment_revision_spec = _parse_default_environment_revision_spec(
            d.pop("defaultEnvironmentRevisionSpec", UNSET)
        )

        def _parse_default_hardware_tier_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_hardware_tier_id = _parse_default_hardware_tier_id(d.pop("defaultHardwareTierId", UNSET))

        def _parse_default_volume_size_gi_b(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        default_volume_size_gi_b = _parse_default_volume_size_gi_b(d.pop("defaultVolumeSizeGiB", UNSET))

        domino_nucleus_project_project_settings_update_dto = cls(
            default_environment_id=default_environment_id,
            default_environment_revision_spec=default_environment_revision_spec,
            default_hardware_tier_id=default_hardware_tier_id,
            default_volume_size_gi_b=default_volume_size_gi_b,
        )

        domino_nucleus_project_project_settings_update_dto.additional_properties = d
        return domino_nucleus_project_project_settings_update_dto

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
