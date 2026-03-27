from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_nucleus_lib_auth_principal_with_feature_flags_allowed_system_operations_item import (
    DominoNucleusLibAuthPrincipalWithFeatureFlagsAllowedSystemOperationsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_nucleus_lib_auth_global_banner_settings import DominoNucleusLibAuthGlobalBannerSettings
    from ..models.domino_nucleus_lib_auth_mixpanel_settings import DominoNucleusLibAuthMixpanelSettings


T = TypeVar("T", bound="DominoNucleusLibAuthPrincipalWithFeatureFlags")


@_attrs_define
class DominoNucleusLibAuthPrincipalWithFeatureFlags:
    """
    Attributes:
        is_anonymous (bool):
        is_admin (bool):
        allowed_system_operations (list[DominoNucleusLibAuthPrincipalWithFeatureFlagsAllowedSystemOperationsItem]):
        feature_flags (list[str]):
        boolean_settings (list[str]):
        mixpanel_settings (DominoNucleusLibAuthMixpanelSettings):
        global_banner_settings (DominoNucleusLibAuthGlobalBannerSettings):
        extended_identity_propagation_to_apps_remember_me_expiration_in_secs (int):
        extended_identity_propagation_to_apps_dont_remember_me_expiration_in_secs (int):
        upload_file_batch_size (int):
        idle_timeout_value_in_minutes (int):
        idle_timeout_prompt_value_in_minutes (int):
        pendo_install_key (str):
        e_signature_action_options (list[str]):
        environments_build_propagation_enabled (bool):
        apps_host (str):
        apps_subdomain (str):
        canonical_id (None | str | Unset):
        canonical_name (None | str | Unset):
        experiment_runs_page_size (int | None | Unset):
        activity_stream_max_date_range (int | None | Unset):
        require_e_signature_workflow (None | str | Unset):
    """

    is_anonymous: bool
    is_admin: bool
    allowed_system_operations: list[DominoNucleusLibAuthPrincipalWithFeatureFlagsAllowedSystemOperationsItem]
    feature_flags: list[str]
    boolean_settings: list[str]
    mixpanel_settings: DominoNucleusLibAuthMixpanelSettings
    global_banner_settings: DominoNucleusLibAuthGlobalBannerSettings
    extended_identity_propagation_to_apps_remember_me_expiration_in_secs: int
    extended_identity_propagation_to_apps_dont_remember_me_expiration_in_secs: int
    upload_file_batch_size: int
    idle_timeout_value_in_minutes: int
    idle_timeout_prompt_value_in_minutes: int
    pendo_install_key: str
    e_signature_action_options: list[str]
    environments_build_propagation_enabled: bool
    apps_host: str
    apps_subdomain: str
    canonical_id: None | str | Unset = UNSET
    canonical_name: None | str | Unset = UNSET
    experiment_runs_page_size: int | None | Unset = UNSET
    activity_stream_max_date_range: int | None | Unset = UNSET
    require_e_signature_workflow: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_anonymous = self.is_anonymous

        is_admin = self.is_admin

        allowed_system_operations = []
        for allowed_system_operations_item_data in self.allowed_system_operations:
            allowed_system_operations_item = allowed_system_operations_item_data.value
            allowed_system_operations.append(allowed_system_operations_item)

        feature_flags = self.feature_flags

        boolean_settings = self.boolean_settings

        mixpanel_settings = self.mixpanel_settings.to_dict()

        global_banner_settings = self.global_banner_settings.to_dict()

        extended_identity_propagation_to_apps_remember_me_expiration_in_secs = (
            self.extended_identity_propagation_to_apps_remember_me_expiration_in_secs
        )

        extended_identity_propagation_to_apps_dont_remember_me_expiration_in_secs = (
            self.extended_identity_propagation_to_apps_dont_remember_me_expiration_in_secs
        )

        upload_file_batch_size = self.upload_file_batch_size

        idle_timeout_value_in_minutes = self.idle_timeout_value_in_minutes

        idle_timeout_prompt_value_in_minutes = self.idle_timeout_prompt_value_in_minutes

        pendo_install_key = self.pendo_install_key

        e_signature_action_options = self.e_signature_action_options

        environments_build_propagation_enabled = self.environments_build_propagation_enabled

        apps_host = self.apps_host

        apps_subdomain = self.apps_subdomain

        canonical_id: None | str | Unset
        if isinstance(self.canonical_id, Unset):
            canonical_id = UNSET
        else:
            canonical_id = self.canonical_id

        canonical_name: None | str | Unset
        if isinstance(self.canonical_name, Unset):
            canonical_name = UNSET
        else:
            canonical_name = self.canonical_name

        experiment_runs_page_size: int | None | Unset
        if isinstance(self.experiment_runs_page_size, Unset):
            experiment_runs_page_size = UNSET
        else:
            experiment_runs_page_size = self.experiment_runs_page_size

        activity_stream_max_date_range: int | None | Unset
        if isinstance(self.activity_stream_max_date_range, Unset):
            activity_stream_max_date_range = UNSET
        else:
            activity_stream_max_date_range = self.activity_stream_max_date_range

        require_e_signature_workflow: None | str | Unset
        if isinstance(self.require_e_signature_workflow, Unset):
            require_e_signature_workflow = UNSET
        else:
            require_e_signature_workflow = self.require_e_signature_workflow

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isAnonymous": is_anonymous,
                "isAdmin": is_admin,
                "allowedSystemOperations": allowed_system_operations,
                "featureFlags": feature_flags,
                "booleanSettings": boolean_settings,
                "mixpanelSettings": mixpanel_settings,
                "globalBannerSettings": global_banner_settings,
                "extendedIdentityPropagationToAppsRememberMeExpirationInSecs": extended_identity_propagation_to_apps_remember_me_expiration_in_secs,
                "extendedIdentityPropagationToAppsDontRememberMeExpirationInSecs": extended_identity_propagation_to_apps_dont_remember_me_expiration_in_secs,
                "uploadFileBatchSize": upload_file_batch_size,
                "idleTimeoutValueInMinutes": idle_timeout_value_in_minutes,
                "idleTimeoutPromptValueInMinutes": idle_timeout_prompt_value_in_minutes,
                "pendoInstallKey": pendo_install_key,
                "eSignatureActionOptions": e_signature_action_options,
                "environmentsBuildPropagationEnabled": environments_build_propagation_enabled,
                "appsHost": apps_host,
                "appsSubdomain": apps_subdomain,
            }
        )
        if canonical_id is not UNSET:
            field_dict["canonicalId"] = canonical_id
        if canonical_name is not UNSET:
            field_dict["canonicalName"] = canonical_name
        if experiment_runs_page_size is not UNSET:
            field_dict["experimentRunsPageSize"] = experiment_runs_page_size
        if activity_stream_max_date_range is not UNSET:
            field_dict["activityStreamMaxDateRange"] = activity_stream_max_date_range
        if require_e_signature_workflow is not UNSET:
            field_dict["requireESignatureWorkflow"] = require_e_signature_workflow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_nucleus_lib_auth_global_banner_settings import DominoNucleusLibAuthGlobalBannerSettings
        from ..models.domino_nucleus_lib_auth_mixpanel_settings import DominoNucleusLibAuthMixpanelSettings

        d = dict(src_dict)
        is_anonymous = d.pop("isAnonymous")

        is_admin = d.pop("isAdmin")

        allowed_system_operations = []
        _allowed_system_operations = d.pop("allowedSystemOperations")
        for allowed_system_operations_item_data in _allowed_system_operations:
            allowed_system_operations_item = DominoNucleusLibAuthPrincipalWithFeatureFlagsAllowedSystemOperationsItem(
                allowed_system_operations_item_data
            )

            allowed_system_operations.append(allowed_system_operations_item)

        feature_flags = cast(list[str], d.pop("featureFlags"))

        boolean_settings = cast(list[str], d.pop("booleanSettings"))

        mixpanel_settings = DominoNucleusLibAuthMixpanelSettings.from_dict(d.pop("mixpanelSettings"))

        global_banner_settings = DominoNucleusLibAuthGlobalBannerSettings.from_dict(d.pop("globalBannerSettings"))

        extended_identity_propagation_to_apps_remember_me_expiration_in_secs = d.pop(
            "extendedIdentityPropagationToAppsRememberMeExpirationInSecs"
        )

        extended_identity_propagation_to_apps_dont_remember_me_expiration_in_secs = d.pop(
            "extendedIdentityPropagationToAppsDontRememberMeExpirationInSecs"
        )

        upload_file_batch_size = d.pop("uploadFileBatchSize")

        idle_timeout_value_in_minutes = d.pop("idleTimeoutValueInMinutes")

        idle_timeout_prompt_value_in_minutes = d.pop("idleTimeoutPromptValueInMinutes")

        pendo_install_key = d.pop("pendoInstallKey")

        e_signature_action_options = cast(list[str], d.pop("eSignatureActionOptions"))

        environments_build_propagation_enabled = d.pop("environmentsBuildPropagationEnabled")

        apps_host = d.pop("appsHost")

        apps_subdomain = d.pop("appsSubdomain")

        def _parse_canonical_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        canonical_id = _parse_canonical_id(d.pop("canonicalId", UNSET))

        def _parse_canonical_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        canonical_name = _parse_canonical_name(d.pop("canonicalName", UNSET))

        def _parse_experiment_runs_page_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        experiment_runs_page_size = _parse_experiment_runs_page_size(d.pop("experimentRunsPageSize", UNSET))

        def _parse_activity_stream_max_date_range(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        activity_stream_max_date_range = _parse_activity_stream_max_date_range(
            d.pop("activityStreamMaxDateRange", UNSET)
        )

        def _parse_require_e_signature_workflow(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        require_e_signature_workflow = _parse_require_e_signature_workflow(d.pop("requireESignatureWorkflow", UNSET))

        domino_nucleus_lib_auth_principal_with_feature_flags = cls(
            is_anonymous=is_anonymous,
            is_admin=is_admin,
            allowed_system_operations=allowed_system_operations,
            feature_flags=feature_flags,
            boolean_settings=boolean_settings,
            mixpanel_settings=mixpanel_settings,
            global_banner_settings=global_banner_settings,
            extended_identity_propagation_to_apps_remember_me_expiration_in_secs=extended_identity_propagation_to_apps_remember_me_expiration_in_secs,
            extended_identity_propagation_to_apps_dont_remember_me_expiration_in_secs=extended_identity_propagation_to_apps_dont_remember_me_expiration_in_secs,
            upload_file_batch_size=upload_file_batch_size,
            idle_timeout_value_in_minutes=idle_timeout_value_in_minutes,
            idle_timeout_prompt_value_in_minutes=idle_timeout_prompt_value_in_minutes,
            pendo_install_key=pendo_install_key,
            e_signature_action_options=e_signature_action_options,
            environments_build_propagation_enabled=environments_build_propagation_enabled,
            apps_host=apps_host,
            apps_subdomain=apps_subdomain,
            canonical_id=canonical_id,
            canonical_name=canonical_name,
            experiment_runs_page_size=experiment_runs_page_size,
            activity_stream_max_date_range=activity_stream_max_date_range,
            require_e_signature_workflow=require_e_signature_workflow,
        )

        domino_nucleus_lib_auth_principal_with_feature_flags.additional_properties = d
        return domino_nucleus_lib_auth_principal_with_feature_flags

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
