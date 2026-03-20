from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.registered_model_project_summary_v1 import RegisteredModelProjectSummaryV1


T = TypeVar("T", bound="RegisteredModelVersionOverviewV2")


@_attrs_define
class RegisteredModelVersionOverviewV2:
    """
    Attributes:
        created_at (datetime.datetime): When the latest version of the model was created Example:
            2022-03-12T02:13:44.467Z.
        model_name (str): Name of the registered model Example: churn-prediction.
        model_version (int): The latest version of the model Example: 4.
        owner_username (str): username of the project owner Example: martin_hito.
        project (RegisteredModelProjectSummaryV1): type that tracks properties of the project associated with a model
        updated_at (datetime.datetime): When the latest version of the model was updated Example:
            2022-03-12T02:13:44.467Z.
        experiment_run_id (None | str | Unset): Optional experiment run ID linked to the model version Example:
            db79712b47084c27a463a188bf901943.
    """

    created_at: datetime.datetime
    model_name: str
    model_version: int
    owner_username: str
    project: RegisteredModelProjectSummaryV1
    updated_at: datetime.datetime
    experiment_run_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        model_name = self.model_name

        model_version = self.model_version

        owner_username = self.owner_username

        project = self.project.to_dict()

        updated_at = self.updated_at.isoformat()

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
                "ownerUsername": owner_username,
                "project": project,
                "updatedAt": updated_at,
            }
        )
        if experiment_run_id is not UNSET:
            field_dict["experimentRunId"] = experiment_run_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registered_model_project_summary_v1 import RegisteredModelProjectSummaryV1

        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        model_name = d.pop("modelName")

        model_version = d.pop("modelVersion")

        owner_username = d.pop("ownerUsername")

        project = RegisteredModelProjectSummaryV1.from_dict(d.pop("project"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_experiment_run_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        experiment_run_id = _parse_experiment_run_id(d.pop("experimentRunId", UNSET))

        registered_model_version_overview_v2 = cls(
            created_at=created_at,
            model_name=model_name,
            model_version=model_version,
            owner_username=owner_username,
            project=project,
            updated_at=updated_at,
            experiment_run_id=experiment_run_id,
        )

        registered_model_version_overview_v2.additional_properties = d
        return registered_model_version_overview_v2

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
