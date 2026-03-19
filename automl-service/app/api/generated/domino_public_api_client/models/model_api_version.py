from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_api_source import ModelApiSource
    from ..models.model_api_version_deployment import ModelApiVersionDeployment
    from ..models.model_api_version_metadata import ModelApiVersionMetadata


T = TypeVar("T", bound="ModelApiVersion")


@_attrs_define
class ModelApiVersion:
    """
    Attributes:
        commit_id (str): The id of the commit of the Model API Version.
        data_plane_id (str): The id of the data plane the Model API Version is deployed to.
        environment_revision_id (str): The id of the environment revision the Model API Version is deployed on.
        id (str): The id of the Model API Version.
        labels (list[str]): The labels of the Model API Version.
        log_http_request_response (bool): Whether the Model API Version should log the HTTP requests and responses.
        metadata (ModelApiVersionMetadata):
        model_api_id (str): The id of the Model API the version belongs to.
        monitoring_enabled (bool): Whether monitoring is enabled for the Mode API Version.
        project_id (str): The id of the project the Model API Version belongs to.
        record_invocation (bool): Whether the Model API Version should record invocations.
        source (ModelApiSource):
        bundle_id (None | str | Unset): The ID of the bundle governing the model API to create.
        deployment (ModelApiVersionDeployment | Unset):
        description (str | Unset): The description of the Model API Version.
        number (int | Unset): The version number of the Model API Version.
        prediction_dataset_resource_id (None | str | Unset): The id of the prediction dataset used by the Model API
            Version.
        provenance_checkpoint_id (None | str | Unset): The id of the provenance checkpoint of the Model API Version.
    """

    commit_id: str
    data_plane_id: str
    environment_revision_id: str
    id: str
    labels: list[str]
    log_http_request_response: bool
    metadata: ModelApiVersionMetadata
    model_api_id: str
    monitoring_enabled: bool
    project_id: str
    record_invocation: bool
    source: ModelApiSource
    bundle_id: None | str | Unset = UNSET
    deployment: ModelApiVersionDeployment | Unset = UNSET
    description: str | Unset = UNSET
    number: int | Unset = UNSET
    prediction_dataset_resource_id: None | str | Unset = UNSET
    provenance_checkpoint_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit_id = self.commit_id

        data_plane_id = self.data_plane_id

        environment_revision_id = self.environment_revision_id

        id = self.id

        labels = self.labels

        log_http_request_response = self.log_http_request_response

        metadata = self.metadata.to_dict()

        model_api_id = self.model_api_id

        monitoring_enabled = self.monitoring_enabled

        project_id = self.project_id

        record_invocation = self.record_invocation

        source = self.source.to_dict()

        bundle_id: None | str | Unset
        if isinstance(self.bundle_id, Unset):
            bundle_id = UNSET
        else:
            bundle_id = self.bundle_id

        deployment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deployment, Unset):
            deployment = self.deployment.to_dict()

        description = self.description

        number = self.number

        prediction_dataset_resource_id: None | str | Unset
        if isinstance(self.prediction_dataset_resource_id, Unset):
            prediction_dataset_resource_id = UNSET
        else:
            prediction_dataset_resource_id = self.prediction_dataset_resource_id

        provenance_checkpoint_id: None | str | Unset
        if isinstance(self.provenance_checkpoint_id, Unset):
            provenance_checkpoint_id = UNSET
        else:
            provenance_checkpoint_id = self.provenance_checkpoint_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commitId": commit_id,
                "dataPlaneId": data_plane_id,
                "environmentRevisionId": environment_revision_id,
                "id": id,
                "labels": labels,
                "logHttpRequestResponse": log_http_request_response,
                "metadata": metadata,
                "modelApiId": model_api_id,
                "monitoringEnabled": monitoring_enabled,
                "projectId": project_id,
                "recordInvocation": record_invocation,
                "source": source,
            }
        )
        if bundle_id is not UNSET:
            field_dict["bundleId"] = bundle_id
        if deployment is not UNSET:
            field_dict["deployment"] = deployment
        if description is not UNSET:
            field_dict["description"] = description
        if number is not UNSET:
            field_dict["number"] = number
        if prediction_dataset_resource_id is not UNSET:
            field_dict["predictionDatasetResourceId"] = prediction_dataset_resource_id
        if provenance_checkpoint_id is not UNSET:
            field_dict["provenanceCheckpointId"] = provenance_checkpoint_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_api_source import ModelApiSource
        from ..models.model_api_version_deployment import ModelApiVersionDeployment
        from ..models.model_api_version_metadata import ModelApiVersionMetadata

        d = dict(src_dict)
        commit_id = d.pop("commitId")

        data_plane_id = d.pop("dataPlaneId")

        environment_revision_id = d.pop("environmentRevisionId")

        id = d.pop("id")

        labels = cast(list[str], d.pop("labels"))

        log_http_request_response = d.pop("logHttpRequestResponse")

        metadata = ModelApiVersionMetadata.from_dict(d.pop("metadata"))

        model_api_id = d.pop("modelApiId")

        monitoring_enabled = d.pop("monitoringEnabled")

        project_id = d.pop("projectId")

        record_invocation = d.pop("recordInvocation")

        source = ModelApiSource.from_dict(d.pop("source"))

        def _parse_bundle_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bundle_id = _parse_bundle_id(d.pop("bundleId", UNSET))

        _deployment = d.pop("deployment", UNSET)
        deployment: ModelApiVersionDeployment | Unset
        if isinstance(_deployment, Unset):
            deployment = UNSET
        else:
            deployment = ModelApiVersionDeployment.from_dict(_deployment)

        description = d.pop("description", UNSET)

        number = d.pop("number", UNSET)

        def _parse_prediction_dataset_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prediction_dataset_resource_id = _parse_prediction_dataset_resource_id(
            d.pop("predictionDatasetResourceId", UNSET)
        )

        def _parse_provenance_checkpoint_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provenance_checkpoint_id = _parse_provenance_checkpoint_id(d.pop("provenanceCheckpointId", UNSET))

        model_api_version = cls(
            commit_id=commit_id,
            data_plane_id=data_plane_id,
            environment_revision_id=environment_revision_id,
            id=id,
            labels=labels,
            log_http_request_response=log_http_request_response,
            metadata=metadata,
            model_api_id=model_api_id,
            monitoring_enabled=monitoring_enabled,
            project_id=project_id,
            record_invocation=record_invocation,
            source=source,
            bundle_id=bundle_id,
            deployment=deployment,
            description=description,
            number=number,
            prediction_dataset_resource_id=prediction_dataset_resource_id,
            provenance_checkpoint_id=provenance_checkpoint_id,
        )

        model_api_version.additional_properties = d
        return model_api_version

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
