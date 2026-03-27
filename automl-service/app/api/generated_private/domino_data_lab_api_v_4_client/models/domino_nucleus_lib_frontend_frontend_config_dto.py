from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_admin_interface_white_label_configurations import DominoAdminInterfaceWhiteLabelConfigurations
    from ..models.domino_files_interface_files_browse_settings_dto import DominoFilesInterfaceFilesBrowseSettingsDto
    from ..models.domino_nucleus_lib_auth_global_banner_settings import DominoNucleusLibAuthGlobalBannerSettings
    from ..models.domino_nucleus_lib_auth_mixpanel_settings import DominoNucleusLibAuthMixpanelSettings


T = TypeVar("T", bound="DominoNucleusLibFrontendFrontendConfigDto")


@_attrs_define
class DominoNucleusLibFrontendFrontendConfigDto:
    """
    Attributes:
        stage (str):
        version (str):
        mixpanel_settings (DominoNucleusLibAuthMixpanelSettings):
        global_banner_settings (DominoNucleusLibAuthGlobalBannerSettings):
        boolean_settings (list[str]):
        feature_flags (list[str]):
        white_label_configurations (DominoAdminInterfaceWhiteLabelConfigurations):
        file_settings (DominoFilesInterfaceFilesBrowseSettingsDto | Unset):
    """

    stage: str
    version: str
    mixpanel_settings: DominoNucleusLibAuthMixpanelSettings
    global_banner_settings: DominoNucleusLibAuthGlobalBannerSettings
    boolean_settings: list[str]
    feature_flags: list[str]
    white_label_configurations: DominoAdminInterfaceWhiteLabelConfigurations
    file_settings: DominoFilesInterfaceFilesBrowseSettingsDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage = self.stage

        version = self.version

        mixpanel_settings = self.mixpanel_settings.to_dict()

        global_banner_settings = self.global_banner_settings.to_dict()

        boolean_settings = self.boolean_settings

        feature_flags = self.feature_flags

        white_label_configurations = self.white_label_configurations.to_dict()

        file_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_settings, Unset):
            file_settings = self.file_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage": stage,
                "version": version,
                "mixpanelSettings": mixpanel_settings,
                "globalBannerSettings": global_banner_settings,
                "booleanSettings": boolean_settings,
                "featureFlags": feature_flags,
                "whiteLabelConfigurations": white_label_configurations,
            }
        )
        if file_settings is not UNSET:
            field_dict["fileSettings"] = file_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_admin_interface_white_label_configurations import (
            DominoAdminInterfaceWhiteLabelConfigurations,
        )
        from ..models.domino_files_interface_files_browse_settings_dto import DominoFilesInterfaceFilesBrowseSettingsDto
        from ..models.domino_nucleus_lib_auth_global_banner_settings import DominoNucleusLibAuthGlobalBannerSettings
        from ..models.domino_nucleus_lib_auth_mixpanel_settings import DominoNucleusLibAuthMixpanelSettings

        d = dict(src_dict)
        stage = d.pop("stage")

        version = d.pop("version")

        mixpanel_settings = DominoNucleusLibAuthMixpanelSettings.from_dict(d.pop("mixpanelSettings"))

        global_banner_settings = DominoNucleusLibAuthGlobalBannerSettings.from_dict(d.pop("globalBannerSettings"))

        boolean_settings = cast(list[str], d.pop("booleanSettings"))

        feature_flags = cast(list[str], d.pop("featureFlags"))

        white_label_configurations = DominoAdminInterfaceWhiteLabelConfigurations.from_dict(
            d.pop("whiteLabelConfigurations")
        )

        _file_settings = d.pop("fileSettings", UNSET)
        file_settings: DominoFilesInterfaceFilesBrowseSettingsDto | Unset
        if isinstance(_file_settings, Unset):
            file_settings = UNSET
        else:
            file_settings = DominoFilesInterfaceFilesBrowseSettingsDto.from_dict(_file_settings)

        domino_nucleus_lib_frontend_frontend_config_dto = cls(
            stage=stage,
            version=version,
            mixpanel_settings=mixpanel_settings,
            global_banner_settings=global_banner_settings,
            boolean_settings=boolean_settings,
            feature_flags=feature_flags,
            white_label_configurations=white_label_configurations,
            file_settings=file_settings,
        )

        domino_nucleus_lib_frontend_frontend_config_dto.additional_properties = d
        return domino_nucleus_lib_frontend_frontend_config_dto

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
