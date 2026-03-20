from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_api_source import ModelApiSource


T = TypeVar("T", bound="ModelApiVersionCreationRequest")


@_attrs_define
class ModelApiVersionCreationRequest:
    """
    Attributes:
        log_http_request_response (bool): Whether the Model API Version to create should log HTTP requests and
            responses.
        monitoring_enabled (bool): Whether the Model API Version to create should have monitoring enabled.
        project_id (str): The id of the project the Model API Version to create should belong to.
        source (ModelApiSource):
        commit_id (str | Unset): The id of the commit id of the Model API Version to create.
        description (str | Unset): The description for the Model API Version to create.
        environment_id (str | Unset): The id of the environment to deploy the Model API Version with.
        prediction_dataset_resource_id (None | str | Unset): The id of the prediction dataset to be used by the Model
            API Version to create.
        provenance_checkpoint_id (str | Unset): The id of the provenance checkpoint of the Model API Version to create.
        record_invocation (bool | Unset): Whether the Model API Version to create should record invocations.
        should_deploy (bool | Unset): Whether the Model API Version to create should be deployed.
    """

    log_http_request_response: bool
    monitoring_enabled: bool
    project_id: str
    source: ModelApiSource
    commit_id: str | Unset = UNSET
    description: str | Unset = UNSET
    environment_id: str | Unset = UNSET
    prediction_dataset_resource_id: None | str | Unset = UNSET
    provenance_checkpoint_id: str | Unset = UNSET
    record_invocation: bool | Unset = UNSET
    should_deploy: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        log_http_request_response = self.log_http_request_response

        monitoring_enabled = self.monitoring_enabled

        project_id = self.project_id

        source = self.source.to_dict()

        commit_id = self.commit_id

        description = self.description

        environment_id = self.environment_id

        prediction_dataset_resource_id: None | str | Unset
        if isinstance(self.prediction_dataset_resource_id, Unset):
            prediction_dataset_resource_id = UNSET
        else:
            prediction_dataset_resource_id = self.prediction_dataset_resource_id

        provenance_checkpoint_id = self.provenance_checkpoint_id

        record_invocation = self.record_invocation

        should_deploy = self.should_deploy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logHttpRequestResponse": log_http_request_response,
                "monitoringEnabled": monitoring_enabled,
                "projectId": project_id,
                "source": source,
            }
        )
        if commit_id is not UNSET:
            field_dict["commitId"] = commit_id
        if description is not UNSET:
            field_dict["description"] = description
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if prediction_dataset_resource_id is not UNSET:
            field_dict["predictionDatasetResourceId"] = prediction_dataset_resource_id
        if provenance_checkpoint_id is not UNSET:
            field_dict["provenanceCheckpointId"] = provenance_checkpoint_id
        if record_invocation is not UNSET:
            field_dict["recordInvocation"] = record_invocation
        if should_deploy is not UNSET:
            field_dict["shouldDeploy"] = should_deploy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_api_source import ModelApiSource

        d = dict(src_dict)
        log_http_request_response = d.pop("logHttpRequestResponse")

        monitoring_enabled = d.pop("monitoringEnabled")

        project_id = d.pop("projectId")

        source = ModelApiSource.from_dict(d.pop("source"))

        commit_id = d.pop("commitId", UNSET)

        description = d.pop("description", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        def _parse_prediction_dataset_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prediction_dataset_resource_id = _parse_prediction_dataset_resource_id(
            d.pop("predictionDatasetResourceId", UNSET)
        )

        provenance_checkpoint_id = d.pop("provenanceCheckpointId", UNSET)

        record_invocation = d.pop("recordInvocation", UNSET)

        should_deploy = d.pop("shouldDeploy", UNSET)

        model_api_version_creation_request = cls(
            log_http_request_response=log_http_request_response,
            monitoring_enabled=monitoring_enabled,
            project_id=project_id,
            source=source,
            commit_id=commit_id,
            description=description,
            environment_id=environment_id,
            prediction_dataset_resource_id=prediction_dataset_resource_id,
            provenance_checkpoint_id=provenance_checkpoint_id,
            record_invocation=record_invocation,
            should_deploy=should_deploy,
        )

        model_api_version_creation_request.additional_properties = d
        return model_api_version_creation_request

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
