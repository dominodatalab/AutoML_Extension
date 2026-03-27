from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_environments_api_environment_permissions import DominoEnvironmentsApiEnvironmentPermissions


T = TypeVar("T", bound="DominoEnvironmentsApiEnvironmentPermissionsResult")


@_attrs_define
class DominoEnvironmentsApiEnvironmentPermissionsResult:
    """
    Attributes:
        can_classify_environments (bool):
        can_create_environments (bool):
        can_set_environments_as_default (bool):
        can_transfer_ownership (bool):
        can_create_global_environment (bool):
        can_edit_privileged_fields (bool):
        environment (DominoEnvironmentsApiEnvironmentPermissions | Unset):
    """

    can_classify_environments: bool
    can_create_environments: bool
    can_set_environments_as_default: bool
    can_transfer_ownership: bool
    can_create_global_environment: bool
    can_edit_privileged_fields: bool
    environment: DominoEnvironmentsApiEnvironmentPermissions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_classify_environments = self.can_classify_environments

        can_create_environments = self.can_create_environments

        can_set_environments_as_default = self.can_set_environments_as_default

        can_transfer_ownership = self.can_transfer_ownership

        can_create_global_environment = self.can_create_global_environment

        can_edit_privileged_fields = self.can_edit_privileged_fields

        environment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "canClassifyEnvironments": can_classify_environments,
                "canCreateEnvironments": can_create_environments,
                "canSetEnvironmentsAsDefault": can_set_environments_as_default,
                "canTransferOwnership": can_transfer_ownership,
                "canCreateGlobalEnvironment": can_create_global_environment,
                "canEditPrivilegedFields": can_edit_privileged_fields,
            }
        )
        if environment is not UNSET:
            field_dict["environment"] = environment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_environment_permissions import DominoEnvironmentsApiEnvironmentPermissions

        d = dict(src_dict)
        can_classify_environments = d.pop("canClassifyEnvironments")

        can_create_environments = d.pop("canCreateEnvironments")

        can_set_environments_as_default = d.pop("canSetEnvironmentsAsDefault")

        can_transfer_ownership = d.pop("canTransferOwnership")

        can_create_global_environment = d.pop("canCreateGlobalEnvironment")

        can_edit_privileged_fields = d.pop("canEditPrivilegedFields")

        _environment = d.pop("environment", UNSET)
        environment: DominoEnvironmentsApiEnvironmentPermissions | Unset
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = DominoEnvironmentsApiEnvironmentPermissions.from_dict(_environment)

        domino_environments_api_environment_permissions_result = cls(
            can_classify_environments=can_classify_environments,
            can_create_environments=can_create_environments,
            can_set_environments_as_default=can_set_environments_as_default,
            can_transfer_ownership=can_transfer_ownership,
            can_create_global_environment=can_create_global_environment,
            can_edit_privileged_fields=can_edit_privileged_fields,
            environment=environment,
        )

        domino_environments_api_environment_permissions_result.additional_properties = d
        return domino_environments_api_environment_permissions_result

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
