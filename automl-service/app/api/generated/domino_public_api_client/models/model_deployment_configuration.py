from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_deployment_configuration_deployment_type import ModelDeploymentConfigurationDeploymentType
    from ..models.model_deployment_configuration_model_configs import ModelDeploymentConfigurationModelConfigs
    from ..models.model_deployment_configuration_shared_config import ModelDeploymentConfigurationSharedConfig


T = TypeVar("T", bound="ModelDeploymentConfiguration")


@_attrs_define
class ModelDeploymentConfiguration:
    """The Model Deployment configuration

    Attributes:
        deployment_type (ModelDeploymentConfigurationDeploymentType): The deployment type specific configuration
        model_configs (ModelDeploymentConfigurationModelConfigs): The model-specific configurations
        shared_config (ModelDeploymentConfigurationSharedConfig): The configurations shared by all models in the
            deployment
    """

    deployment_type: ModelDeploymentConfigurationDeploymentType
    model_configs: ModelDeploymentConfigurationModelConfigs
    shared_config: ModelDeploymentConfigurationSharedConfig
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deployment_type = self.deployment_type.to_dict()

        model_configs = self.model_configs.to_dict()

        shared_config = self.shared_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deploymentType": deployment_type,
                "modelConfigs": model_configs,
                "sharedConfig": shared_config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_deployment_configuration_deployment_type import ModelDeploymentConfigurationDeploymentType
        from ..models.model_deployment_configuration_model_configs import ModelDeploymentConfigurationModelConfigs
        from ..models.model_deployment_configuration_shared_config import ModelDeploymentConfigurationSharedConfig

        d = dict(src_dict)
        deployment_type = ModelDeploymentConfigurationDeploymentType.from_dict(d.pop("deploymentType"))

        model_configs = ModelDeploymentConfigurationModelConfigs.from_dict(d.pop("modelConfigs"))

        shared_config = ModelDeploymentConfigurationSharedConfig.from_dict(d.pop("sharedConfig"))

        model_deployment_configuration = cls(
            deployment_type=deployment_type,
            model_configs=model_configs,
            shared_config=shared_config,
        )

        model_deployment_configuration.additional_properties = d
        return model_deployment_configuration

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
