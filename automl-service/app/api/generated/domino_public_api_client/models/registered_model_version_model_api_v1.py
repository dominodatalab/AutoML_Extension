from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.registered_model_project_summary_v1 import RegisteredModelProjectSummaryV1


T = TypeVar("T", bound="RegisteredModelVersionModelApiV1")


@_attrs_define
class RegisteredModelVersionModelApiV1:
    """
    Attributes:
        description (str): Description of the model Example: Customer churn model.
        id (str): ID of the Model API Example: 6452f88ac21bd0c60eca085.
        name (str): Name of the Model API Example: Test Model API.
        project (RegisteredModelProjectSummaryV1): type that tracks properties of the project associated with a model
        updated_at (datetime.datetime): When the latest version of the model was updated Example:
            2022-03-12T02:13:44.467Z.
        active_model_version_id (str | Unset): The id of the Model API Example: 6452f88ac21bd0c60eca087.
        active_version_number (int | Unset): The active version number of the Model API Example: 2.
        active_version_status (str | Unset): The status of the Model API Example: Running.
    """

    description: str
    id: str
    name: str
    project: RegisteredModelProjectSummaryV1
    updated_at: datetime.datetime
    active_model_version_id: str | Unset = UNSET
    active_version_number: int | Unset = UNSET
    active_version_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        name = self.name

        project = self.project.to_dict()

        updated_at = self.updated_at.isoformat()

        active_model_version_id = self.active_model_version_id

        active_version_number = self.active_version_number

        active_version_status = self.active_version_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "id": id,
                "name": name,
                "project": project,
                "updatedAt": updated_at,
            }
        )
        if active_model_version_id is not UNSET:
            field_dict["activeModelVersionId"] = active_model_version_id
        if active_version_number is not UNSET:
            field_dict["activeVersionNumber"] = active_version_number
        if active_version_status is not UNSET:
            field_dict["activeVersionStatus"] = active_version_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registered_model_project_summary_v1 import RegisteredModelProjectSummaryV1

        d = dict(src_dict)
        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        project = RegisteredModelProjectSummaryV1.from_dict(d.pop("project"))

        updated_at = isoparse(d.pop("updatedAt"))

        active_model_version_id = d.pop("activeModelVersionId", UNSET)

        active_version_number = d.pop("activeVersionNumber", UNSET)

        active_version_status = d.pop("activeVersionStatus", UNSET)

        registered_model_version_model_api_v1 = cls(
            description=description,
            id=id,
            name=name,
            project=project,
            updated_at=updated_at,
            active_model_version_id=active_model_version_id,
            active_version_number=active_version_number,
            active_version_status=active_version_status,
        )

        registered_model_version_model_api_v1.additional_properties = d
        return registered_model_version_model_api_v1

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
