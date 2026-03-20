from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.registered_model_project_summary_v1 import RegisteredModelProjectSummaryV1
    from ..models.registered_model_tags_v1 import RegisteredModelTagsV1
    from ..models.registered_model_version_ui_details_v1 import RegisteredModelVersionUiDetailsV1


T = TypeVar("T", bound="RegisteredModelVersionDetailsV1")


@_attrs_define
class RegisteredModelVersionDetailsV1:
    """
    Attributes:
        created_at (datetime.datetime): When the latest version of the model was created Example:
            2022-03-12T02:13:44.467Z.
        experiment_run_id (str): The name of experiment run linked to the model version Example:
            db79712b47084c27a463a188bf901943.
        model_name (str): Name of the registered model Example: churn-prediction.
        model_version (int): The latest version of the model Example: 4.
        model_version_description (str): Description of the model version Example: Customer churn model V1.
        owner_username (str): username of the project owner Example: martin_hito.
        project (RegisteredModelProjectSummaryV1): type that tracks properties of the project associated with a model
        tags (RegisteredModelTagsV1): A map of key -> value Example: {'key': 'value', 'key2': 'anothervalue'}.
        updated_at (datetime.datetime): When the latest version of the model was updated Example:
            2022-03-12T02:13:44.467Z.
        version_ui_details (RegisteredModelVersionUiDetailsV1):
    """

    created_at: datetime.datetime
    experiment_run_id: str
    model_name: str
    model_version: int
    model_version_description: str
    owner_username: str
    project: RegisteredModelProjectSummaryV1
    tags: RegisteredModelTagsV1
    updated_at: datetime.datetime
    version_ui_details: RegisteredModelVersionUiDetailsV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        experiment_run_id = self.experiment_run_id

        model_name = self.model_name

        model_version = self.model_version

        model_version_description = self.model_version_description

        owner_username = self.owner_username

        project = self.project.to_dict()

        tags = self.tags.to_dict()

        updated_at = self.updated_at.isoformat()

        version_ui_details = self.version_ui_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "experimentRunId": experiment_run_id,
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registered_model_project_summary_v1 import RegisteredModelProjectSummaryV1
        from ..models.registered_model_tags_v1 import RegisteredModelTagsV1
        from ..models.registered_model_version_ui_details_v1 import RegisteredModelVersionUiDetailsV1

        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        experiment_run_id = d.pop("experimentRunId")

        model_name = d.pop("modelName")

        model_version = d.pop("modelVersion")

        model_version_description = d.pop("modelVersionDescription")

        owner_username = d.pop("ownerUsername")

        project = RegisteredModelProjectSummaryV1.from_dict(d.pop("project"))

        tags = RegisteredModelTagsV1.from_dict(d.pop("tags"))

        updated_at = isoparse(d.pop("updatedAt"))

        version_ui_details = RegisteredModelVersionUiDetailsV1.from_dict(d.pop("versionUiDetails"))

        registered_model_version_details_v1 = cls(
            created_at=created_at,
            experiment_run_id=experiment_run_id,
            model_name=model_name,
            model_version=model_version,
            model_version_description=model_version_description,
            owner_username=owner_username,
            project=project,
            tags=tags,
            updated_at=updated_at,
            version_ui_details=version_ui_details,
        )

        registered_model_version_details_v1.additional_properties = d
        return registered_model_version_details_v1

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
