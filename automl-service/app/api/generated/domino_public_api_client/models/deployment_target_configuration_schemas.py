from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.deployment_target_configuration_schemas_default_resource_configs import (
        DeploymentTargetConfigurationSchemasDefaultResourceConfigs,
    )
    from ..models.json_schema import JSONSchema


T = TypeVar("T", bound="DeploymentTargetConfigurationSchemas")


@_attrs_define
class DeploymentTargetConfigurationSchemas:
    """The Deployment Target configuration schemas.  Each configuration can have properties that are direct children or one
    layer deep.  Two or more layers of nesting is not supported.

        Attributes:
            default_resource_configs (DeploymentTargetConfigurationSchemasDefaultResourceConfigs):
            resource_config_schema (JSONSchema): Core schema meta-schema
            target_config_schema (JSONSchema): Core schema meta-schema
    """

    default_resource_configs: DeploymentTargetConfigurationSchemasDefaultResourceConfigs
    resource_config_schema: JSONSchema
    target_config_schema: JSONSchema
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_resource_configs = self.default_resource_configs.to_dict()

        resource_config_schema = self.resource_config_schema.to_dict()

        target_config_schema = self.target_config_schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "defaultResourceConfigs": default_resource_configs,
                "resourceConfigSchema": resource_config_schema,
                "targetConfigSchema": target_config_schema,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment_target_configuration_schemas_default_resource_configs import (
            DeploymentTargetConfigurationSchemasDefaultResourceConfigs,
        )
        from ..models.json_schema import JSONSchema

        d = dict(src_dict)
        default_resource_configs = DeploymentTargetConfigurationSchemasDefaultResourceConfigs.from_dict(
            d.pop("defaultResourceConfigs")
        )

        resource_config_schema = JSONSchema.from_dict(d.pop("resourceConfigSchema"))

        target_config_schema = JSONSchema.from_dict(d.pop("targetConfigSchema"))

        deployment_target_configuration_schemas = cls(
            default_resource_configs=default_resource_configs,
            resource_config_schema=resource_config_schema,
            target_config_schema=target_config_schema,
        )

        deployment_target_configuration_schemas.additional_properties = d
        return deployment_target_configuration_schemas

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
