from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.registered_model_version_details_v2_build_status import RegisteredModelVersionDetailsV2BuildStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.registered_model_project_summary_v1 import RegisteredModelProjectSummaryV1
    from ..models.registered_model_tags_v1 import RegisteredModelTagsV1
    from ..models.registered_model_version_ui_details_v2 import RegisteredModelVersionUiDetailsV2


T = TypeVar("T", bound="RegisteredModelVersionDetailsV2")


@_attrs_define
class RegisteredModelVersionDetailsV2:
    """
    Attributes:
        created_at (datetime.datetime): When the latest version of the model was created Example:
            2022-03-12T02:13:44.467Z.
        model_name (str): Name of the registered model Example: churn-prediction.
        model_version (int): The latest version of the model Example: 4.
        model_version_description (str): Description of the model version Example: Customer churn model V1.
        owner_username (str): username of the project owner Example: martin_hito.
        project (RegisteredModelProjectSummaryV1): type that tracks properties of the project associated with a model
        tags (RegisteredModelTagsV1): A map of key -> value Example: {'key': 'value', 'key2': 'anothervalue'}.
        updated_at (datetime.datetime): When the latest version of the model was updated Example:
            2022-03-12T02:13:44.467Z.
        version_ui_details (RegisteredModelVersionUiDetailsV2):
        build_status (RegisteredModelVersionDetailsV2BuildStatus | Unset): Current build status for GenAI models
            Example: Succeeded.
        experiment_run_id (None | str | Unset): The experiment run ID linked to the model version (only for MLflow
            models) Example: db79712b47084c27a463a188bf901943.
    """

    created_at: datetime.datetime
    model_name: str
    model_version: int
    model_version_description: str
    owner_username: str
    project: RegisteredModelProjectSummaryV1
    tags: RegisteredModelTagsV1
    updated_at: datetime.datetime
    version_ui_details: RegisteredModelVersionUiDetailsV2
    build_status: RegisteredModelVersionDetailsV2BuildStatus | Unset = UNSET
    experiment_run_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        model_name = self.model_name

        model_version = self.model_version

        model_version_description = self.model_version_description

        owner_username = self.owner_username

        project = self.project.to_dict()

        tags = self.tags.to_dict()

        updated_at = self.updated_at.isoformat()

        version_ui_details = self.version_ui_details.to_dict()

        build_status: str | Unset = UNSET
        if not isinstance(self.build_status, Unset):
            build_status = self.build_status.value

        experiment_run_id: None | str | Unset
        if isinstance(self.experiment_run_id, Unset):
            experiment_run_id = UNSET
        else:
            experiment_run_id = self.experiment_run_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "modelName": model_name,
                "modelVersion": model_version,
                "modelVersionDescription": model_version_description,
                "ownerUsername": owner_username,
                "project": project,
                "tags": tags,
                "updatedAt": updated_at,
                "versionUiDetails": version_ui_details,
            }
        )
        if build_status is not UNSET:
            field_dict["buildStatus"] = build_status
        if experiment_run_id is not UNSET:
            field_dict["experimentRunId"] = experiment_run_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registered_model_project_summary_v1 import RegisteredModelProjectSummaryV1
        from ..models.registered_model_tags_v1 import RegisteredModelTagsV1
        from ..models.registered_model_version_ui_details_v2 import RegisteredModelVersionUiDetailsV2

        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        model_name = d.pop("modelName")

        model_version = d.pop("modelVersion")

        model_version_description = d.pop("modelVersionDescription")

        owner_username = d.pop("ownerUsername")

        project = RegisteredModelProjectSummaryV1.from_dict(d.pop("project"))

        tags = RegisteredModelTagsV1.from_dict(d.pop("tags"))

        updated_at = isoparse(d.pop("updatedAt"))

        version_ui_details = RegisteredModelVersionUiDetailsV2.from_dict(d.pop("versionUiDetails"))

        _build_status = d.pop("buildStatus", UNSET)
        build_status: RegisteredModelVersionDetailsV2BuildStatus | Unset
        if isinstance(_build_status, Unset):
            build_status = UNSET
        else:
            build_status = RegisteredModelVersionDetailsV2BuildStatus(_build_status)

        def _parse_experiment_run_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        experiment_run_id = _parse_experiment_run_id(d.pop("experimentRunId", UNSET))

        registered_model_version_details_v2 = cls(
            created_at=created_at,
            model_name=model_name,
            model_version=model_version,
            model_version_description=model_version_description,
            owner_username=owner_username,
            project=project,
            tags=tags,
            updated_at=updated_at,
            version_ui_details=version_ui_details,
            build_status=build_status,
            experiment_run_id=experiment_run_id,
        )

        registered_model_version_details_v2.additional_properties = d
        return registered_model_version_details_v2

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
