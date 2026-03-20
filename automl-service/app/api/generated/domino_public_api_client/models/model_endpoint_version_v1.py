from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.model_endpoint_model_type_v1 import ModelEndpointModelTypeV1
from ..models.model_endpoint_status_v1 import ModelEndpointStatusV1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_endpoint_configuration_v1 import ModelEndpointConfigurationV1
    from ..models.model_endpoint_environment_summary_v1 import ModelEndpointEnvironmentSummaryV1
    from ..models.model_endpoint_hardware_tier_summary_v1 import ModelEndpointHardwareTierSummaryV1
    from ..models.model_endpoint_model_source_v1 import ModelEndpointModelSourceV1
    from ..models.model_endpoint_user_v1 import ModelEndpointUserV1


T = TypeVar("T", bound="ModelEndpointVersionV1")


@_attrs_define
class ModelEndpointVersionV1:
    """
    Attributes:
        configuration (ModelEndpointConfigurationV1):
        created_at (datetime.datetime): The time the endpoint was created Example: 2022-03-12T02:13:44.467Z.
        creator (ModelEndpointUserV1):
        endpoint_id (str): The ID of the endpoint Example: 62313ce67a0af0281c01a6a5.
        environment (ModelEndpointEnvironmentSummaryV1):
        hardware_tier (ModelEndpointHardwareTierSummaryV1):
        model_source (ModelEndpointModelSourceV1):
        model_type (ModelEndpointModelTypeV1):
        number (int): The version number of the endpoint Example: 1.
        status (ModelEndpointStatusV1):
        description (str | Unset): The description of the endpoint version Example: My Endpoint Version Description.
        execution_id (str | Unset): The ID of the execution serving the endpoint, if present Example:
            62313ce67a0af0281c01a6a5.
        label (str | Unset): The label of the endpoint version Example: 1.0.
    """

    configuration: ModelEndpointConfigurationV1
    created_at: datetime.datetime
    creator: ModelEndpointUserV1
    endpoint_id: str
    environment: ModelEndpointEnvironmentSummaryV1
    hardware_tier: ModelEndpointHardwareTierSummaryV1
    model_source: ModelEndpointModelSourceV1
    model_type: ModelEndpointModelTypeV1
    number: int
    status: ModelEndpointStatusV1
    description: str | Unset = UNSET
    execution_id: str | Unset = UNSET
    label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        created_at = self.created_at.isoformat()

        creator = self.creator.to_dict()

        endpoint_id = self.endpoint_id

        environment = self.environment.to_dict()

        hardware_tier = self.hardware_tier.to_dict()

        model_source = self.model_source.to_dict()

        model_type = self.model_type.value

        number = self.number

        status = self.status.value

        description = self.description

        execution_id = self.execution_id

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "createdAt": created_at,
                "creator": creator,
                "endpointId": endpoint_id,
                "environment": environment,
                "hardwareTier": hardware_tier,
                "modelSource": model_source,
                "modelType": model_type,
                "number": number,
                "status": status,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_endpoint_configuration_v1 import ModelEndpointConfigurationV1
        from ..models.model_endpoint_environment_summary_v1 import ModelEndpointEnvironmentSummaryV1
        from ..models.model_endpoint_hardware_tier_summary_v1 import ModelEndpointHardwareTierSummaryV1
        from ..models.model_endpoint_model_source_v1 import ModelEndpointModelSourceV1
        from ..models.model_endpoint_user_v1 import ModelEndpointUserV1

        d = dict(src_dict)
        configuration = ModelEndpointConfigurationV1.from_dict(d.pop("configuration"))

        created_at = isoparse(d.pop("createdAt"))

        creator = ModelEndpointUserV1.from_dict(d.pop("creator"))

        endpoint_id = d.pop("endpointId")

        environment = ModelEndpointEnvironmentSummaryV1.from_dict(d.pop("environment"))

        hardware_tier = ModelEndpointHardwareTierSummaryV1.from_dict(d.pop("hardwareTier"))

        model_source = ModelEndpointModelSourceV1.from_dict(d.pop("modelSource"))

        model_type = ModelEndpointModelTypeV1(d.pop("modelType"))

        number = d.pop("number")

        status = ModelEndpointStatusV1(d.pop("status"))

        description = d.pop("description", UNSET)

        execution_id = d.pop("executionId", UNSET)

        label = d.pop("label", UNSET)

        model_endpoint_version_v1 = cls(
            configuration=configuration,
            created_at=created_at,
            creator=creator,
            endpoint_id=endpoint_id,
            environment=environment,
            hardware_tier=hardware_tier,
            model_source=model_source,
            model_type=model_type,
            number=number,
            status=status,
            description=description,
            execution_id=execution_id,
            label=label,
        )

        model_endpoint_version_v1.additional_properties = d
        return model_endpoint_version_v1

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
