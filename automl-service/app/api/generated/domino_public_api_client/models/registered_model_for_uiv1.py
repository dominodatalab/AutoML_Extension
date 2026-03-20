from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.registered_model_for_uiv1_latest_version_model_type import RegisteredModelForUIV1LatestVersionModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.registered_model_metrics_v1 import RegisteredModelMetricsV1
    from ..models.registered_model_project_summary_v1 import RegisteredModelProjectSummaryV1
    from ..models.registered_model_tags_v1 import RegisteredModelTagsV1


T = TypeVar("T", bound="RegisteredModelForUIV1")


@_attrs_define
class RegisteredModelForUIV1:
    """
    Attributes:
        created_at (datetime.datetime): When the latest version of the model was created Example:
            2022-03-12T02:13:44.467Z.
        description (str): Description of the model Example: Customer churn model.
        model_api_count (int): The number of model APIs associated with the latest version of the model Example: 1.
        name (str): Name of the registered model Example: churn-prediction.
        owner_username (str): Username of the project owner Example: martin_hito.
        project (RegisteredModelProjectSummaryV1): type that tracks properties of the project associated with a model
        tags (RegisteredModelTagsV1): A map of key -> value Example: {'key': 'value', 'key2': 'anothervalue'}.
        updated_at (datetime.datetime): When the latest version of the model was updated Example:
            2022-03-12T02:13:44.467Z.
        discoverable (bool | Unset): Indicates whether this model is publicly discoverable. If true, users who are not
            project members will see this model in search results and can view basic model details.
            This field may be omitted when false.
             Default: False.
        latest_version (int | Unset): The latest version of the model Example: 1.
        latest_version_experiment_metrics (RegisteredModelMetricsV1 | Unset): A map of key -> value Example: {'key': 1,
            'key2': 100.4}.
        latest_version_model_type (RegisteredModelForUIV1LatestVersionModelType | Unset): The model type of the latest
            version (e.g., "llm", "embedding", "other-genai", "ml") Example: llm.
        prediction_count (int | Unset): The number of predictions captured for the active versions of model APIs
            associated with the latest version of the model Example: 100.
    """

    created_at: datetime.datetime
    description: str
    model_api_count: int
    name: str
    owner_username: str
    project: RegisteredModelProjectSummaryV1
    tags: RegisteredModelTagsV1
    updated_at: datetime.datetime
    discoverable: bool | Unset = False
    latest_version: int | Unset = UNSET
    latest_version_experiment_metrics: RegisteredModelMetricsV1 | Unset = UNSET
    latest_version_model_type: RegisteredModelForUIV1LatestVersionModelType | Unset = UNSET
    prediction_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description

        model_api_count = self.model_api_count

        name = self.name

        owner_username = self.owner_username

        project = self.project.to_dict()

        tags = self.tags.to_dict()

        updated_at = self.updated_at.isoformat()

        discoverable = self.discoverable

        latest_version = self.latest_version

        latest_version_experiment_metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest_version_experiment_metrics, Unset):
            latest_version_experiment_metrics = self.latest_version_experiment_metrics.to_dict()

        latest_version_model_type: str | Unset = UNSET
        if not isinstance(self.latest_version_model_type, Unset):
            latest_version_model_type = self.latest_version_model_type.value

        prediction_count = self.prediction_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "description": description,
                "modelApiCount": model_api_count,
                "name": name,
                "ownerUsername": owner_username,
                "project": project,
                "tags": tags,
                "updatedAt": updated_at,
            }
        )
        if discoverable is not UNSET:
            field_dict["discoverable"] = discoverable
        if latest_version is not UNSET:
            field_dict["latestVersion"] = latest_version
        if latest_version_experiment_metrics is not UNSET:
            field_dict["latestVersionExperimentMetrics"] = latest_version_experiment_metrics
        if latest_version_model_type is not UNSET:
            field_dict["latestVersionModelType"] = latest_version_model_type
        if prediction_count is not UNSET:
            field_dict["predictionCount"] = prediction_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registered_model_metrics_v1 import RegisteredModelMetricsV1
        from ..models.registered_model_project_summary_v1 import RegisteredModelProjectSummaryV1
        from ..models.registered_model_tags_v1 import RegisteredModelTagsV1

        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        description = d.pop("description")

        model_api_count = d.pop("modelApiCount")

        name = d.pop("name")

        owner_username = d.pop("ownerUsername")

        project = RegisteredModelProjectSummaryV1.from_dict(d.pop("project"))

        tags = RegisteredModelTagsV1.from_dict(d.pop("tags"))

        updated_at = isoparse(d.pop("updatedAt"))

        discoverable = d.pop("discoverable", UNSET)

        latest_version = d.pop("latestVersion", UNSET)

        _latest_version_experiment_metrics = d.pop("latestVersionExperimentMetrics", UNSET)
        latest_version_experiment_metrics: RegisteredModelMetricsV1 | Unset
        if isinstance(_latest_version_experiment_metrics, Unset):
            latest_version_experiment_metrics = UNSET
        else:
            latest_version_experiment_metrics = RegisteredModelMetricsV1.from_dict(_latest_version_experiment_metrics)

        _latest_version_model_type = d.pop("latestVersionModelType", UNSET)
        latest_version_model_type: RegisteredModelForUIV1LatestVersionModelType | Unset
        if isinstance(_latest_version_model_type, Unset):
            latest_version_model_type = UNSET
        else:
            latest_version_model_type = RegisteredModelForUIV1LatestVersionModelType(_latest_version_model_type)

        prediction_count = d.pop("predictionCount", UNSET)

        registered_model_for_uiv1 = cls(
            created_at=created_at,
            description=description,
            model_api_count=model_api_count,
            name=name,
            owner_username=owner_username,
            project=project,
            tags=tags,
            updated_at=updated_at,
            discoverable=discoverable,
            latest_version=latest_version,
            latest_version_experiment_metrics=latest_version_experiment_metrics,
            latest_version_model_type=latest_version_model_type,
            prediction_count=prediction_count,
        )

        registered_model_for_uiv1.additional_properties = d
        return registered_model_for_uiv1

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
