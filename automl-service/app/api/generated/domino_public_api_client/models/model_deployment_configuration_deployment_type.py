from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_deployment_configuration_deployment_type_type import ModelDeploymentConfigurationDeploymentTypeType

if TYPE_CHECKING:
    from ..models.model_deployment_configuration_deployment_type_model_configs import (
        ModelDeploymentConfigurationDeploymentTypeModelConfigs,
    )
    from ..models.model_deployment_configuration_deployment_type_shared_config import (
        ModelDeploymentConfigurationDeploymentTypeSharedConfig,
    )


T = TypeVar("T", bound="ModelDeploymentConfigurationDeploymentType")


@_attrs_define
class ModelDeploymentConfigurationDeploymentType:
    """The deployment type specific configuration

    Attributes:
        model_configs (ModelDeploymentConfigurationDeploymentTypeModelConfigs): The model-specific configurations
        shared_config (ModelDeploymentConfigurationDeploymentTypeSharedConfig): The configurations shared by all models
            in the deployment
        type_ (ModelDeploymentConfigurationDeploymentTypeType): The type of the deployment Example: SYNC_ENDPOINT.
    """

    model_configs: ModelDeploymentConfigurationDeploymentTypeModelConfigs
    shared_config: ModelDeploymentConfigurationDeploymentTypeSharedConfig
    type_: ModelDeploymentConfigurationDeploymentTypeType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_configs = self.model_configs.to_dict()

        shared_config = self.shared_config.to_dict()

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelConfigs": model_configs,
                "sharedConfig": shared_config,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_deployment_configuration_deployment_type_model_configs import (
            ModelDeploymentConfigurationDeploymentTypeModelConfigs,
        )
        from ..models.model_deployment_configuration_deployment_type_shared_config import (
            ModelDeploymentConfigurationDeploymentTypeSharedConfig,
        )

        d = dict(src_dict)
        model_configs = ModelDeploymentConfigurationDeploymentTypeModelConfigs.from_dict(d.pop("modelConfigs"))

        shared_config = ModelDeploymentConfigurationDeploymentTypeSharedConfig.from_dict(d.pop("sharedConfig"))

        type_ = ModelDeploymentConfigurationDeploymentTypeType(d.pop("type"))

        model_deployment_configuration_deployment_type = cls(
            model_configs=model_configs,
            shared_config=shared_config,
            type_=type_,
        )

        model_deployment_configuration_deployment_type.additional_properties = d
        return model_deployment_configuration_deployment_type

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
