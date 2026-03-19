from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_deployment_status_operation_credentials import ModelDeploymentStatusOperationCredentials
    from ..models.model_deployment_status_operation_examples_item import ModelDeploymentStatusOperationExamplesItem
    from ..models.model_deployment_status_operation_fields import ModelDeploymentStatusOperationFields
    from ..models.model_deployment_status_operation_metadata import ModelDeploymentStatusOperationMetadata


T = TypeVar("T", bound="ModelDeploymentStatusOperation")


@_attrs_define
class ModelDeploymentStatusOperation:
    """
    Attributes:
        fields (ModelDeploymentStatusOperationFields):
        metadata (ModelDeploymentStatusOperationMetadata): This field provides metadata needed for an API user to invoke
            the operation.
        type_ (str): This field provides identifiers for the operations supported by this type of model deployment.
        credentials (ModelDeploymentStatusOperationCredentials | Unset):
        example_payload (str | Unset):
        examples (list[ModelDeploymentStatusOperationExamplesItem] | Unset):
    """

    fields: ModelDeploymentStatusOperationFields
    metadata: ModelDeploymentStatusOperationMetadata
    type_: str
    credentials: ModelDeploymentStatusOperationCredentials | Unset = UNSET
    example_payload: str | Unset = UNSET
    examples: list[ModelDeploymentStatusOperationExamplesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields = self.fields.to_dict()

        metadata = self.metadata.to_dict()

        type_ = self.type_

        credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        example_payload = self.example_payload

        examples: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.examples, Unset):
            examples = []
            for examples_item_data in self.examples:
                examples_item = examples_item_data.to_dict()
                examples.append(examples_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields": fields,
                "metadata": metadata,
                "type": type_,
            }
        )
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if example_payload is not UNSET:
            field_dict["examplePayload"] = example_payload
        if examples is not UNSET:
            field_dict["examples"] = examples

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_deployment_status_operation_credentials import ModelDeploymentStatusOperationCredentials
        from ..models.model_deployment_status_operation_examples_item import ModelDeploymentStatusOperationExamplesItem
        from ..models.model_deployment_status_operation_fields import ModelDeploymentStatusOperationFields
        from ..models.model_deployment_status_operation_metadata import ModelDeploymentStatusOperationMetadata

        d = dict(src_dict)
        fields = ModelDeploymentStatusOperationFields.from_dict(d.pop("fields"))

        metadata = ModelDeploymentStatusOperationMetadata.from_dict(d.pop("metadata"))

        type_ = d.pop("type")

        _credentials = d.pop("credentials", UNSET)
        credentials: ModelDeploymentStatusOperationCredentials | Unset
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = ModelDeploymentStatusOperationCredentials.from_dict(_credentials)

        example_payload = d.pop("examplePayload", UNSET)

        _examples = d.pop("examples", UNSET)
        examples: list[ModelDeploymentStatusOperationExamplesItem] | Unset = UNSET
        if _examples is not UNSET:
            examples = []
            for examples_item_data in _examples:
                examples_item = ModelDeploymentStatusOperationExamplesItem.from_dict(examples_item_data)

                examples.append(examples_item)

        model_deployment_status_operation = cls(
            fields=fields,
            metadata=metadata,
            type_=type_,
            credentials=credentials,
            example_payload=example_payload,
            examples=examples,
        )

        model_deployment_status_operation.additional_properties = d
        return model_deployment_status_operation

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
