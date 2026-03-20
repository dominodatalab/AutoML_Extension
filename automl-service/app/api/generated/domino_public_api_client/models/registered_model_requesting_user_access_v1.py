from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RegisteredModelRequestingUserAccessV1")


@_attrs_define
class RegisteredModelRequestingUserAccessV1:
    """Describes the operations that the requesting user has permission to do with this model.

    Attributes:
        can_edit_model (bool): True if the requesting user can update this model
        can_edit_project_assets (bool): True if the requesting user has permissions to edit other assets of the project
            that this model belongs to.
        can_view_experiment_runs (bool): True if the requesting user can view experiment runs of the project that this
            model belongs to.
        can_view_model_apis (bool): True if the requesting user can view model apis of the project that this model
            belongs to.
        can_view_project (bool): True if the requesting user can view the project overview of the project that this
            model belongs to.
        can_view_project_files (bool): True if the requesting user can view the files of the project that this model
            belongs to.
    """

    can_edit_model: bool
    can_edit_project_assets: bool
    can_view_experiment_runs: bool
    can_view_model_apis: bool
    can_view_project: bool
    can_view_project_files: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_edit_model = self.can_edit_model

        can_edit_project_assets = self.can_edit_project_assets

        can_view_experiment_runs = self.can_view_experiment_runs

        can_view_model_apis = self.can_view_model_apis

        can_view_project = self.can_view_project

        can_view_project_files = self.can_view_project_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "canEditModel": can_edit_model,
                "canEditProjectAssets": can_edit_project_assets,
                "canViewExperimentRuns": can_view_experiment_runs,
                "canViewModelApis": can_view_model_apis,
                "canViewProject": can_view_project,
                "canViewProjectFiles": can_view_project_files,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_edit_model = d.pop("canEditModel")

        can_edit_project_assets = d.pop("canEditProjectAssets")

        can_view_experiment_runs = d.pop("canViewExperimentRuns")

        can_view_model_apis = d.pop("canViewModelApis")

        can_view_project = d.pop("canViewProject")

        can_view_project_files = d.pop("canViewProjectFiles")

        registered_model_requesting_user_access_v1 = cls(
            can_edit_model=can_edit_model,
            can_edit_project_assets=can_edit_project_assets,
            can_view_experiment_runs=can_view_experiment_runs,
            can_view_model_apis=can_view_model_apis,
            can_view_project=can_view_project,
            can_view_project_files=can_view_project_files,
        )

        registered_model_requesting_user_access_v1.additional_properties = d
        return registered_model_requesting_user_access_v1

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
