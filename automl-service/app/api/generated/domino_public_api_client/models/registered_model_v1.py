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
    from ..models.registered_model_requesting_user_access_v1 import RegisteredModelRequestingUserAccessV1
    from ..models.registered_model_tags_v1 import RegisteredModelTagsV1


T = TypeVar("T", bound="RegisteredModelV1")


@_attrs_define
class RegisteredModelV1:
    """
    Attributes:
        created_at (datetime.datetime): When the latest version of the model was created Example:
            2022-03-12T02:13:44.467Z.
        description (str): Description of the model Example: Customer churn model.
        name (str): Name of the registered model Example: churn-prediction.
        owner_username (str): Username of the model's creator Example: martin_hito.
        project (RegisteredModelProjectSummaryV1): type that tracks properties of the project associated with a model
        requesting_user_access (RegisteredModelRequestingUserAccessV1): Describes the operations that the requesting
            user has permission to do with this model.
        tags (RegisteredModelTagsV1): A map of key -> value Example: {'key': 'value', 'key2': 'anothervalue'}.
        updated_at (datetime.datetime): When the latest version of the model was updated Example:
            2022-03-12T02:13:44.467Z.
        discoverable (bool | Unset): Indicates whether this model is publicly discoverable. If true, users who are not
            project members will see this model in search results and can view basic model details.
            This field may be omitted when false.
             Default: False.
        latest_version (int | Unset): The latest version of the model Example: 1.
    """

    created_at: datetime.datetime
    description: str
    name: str
    owner_username: str
    project: RegisteredModelProjectSummaryV1
    requesting_user_access: RegisteredModelRequestingUserAccessV1
    tags: RegisteredModelTagsV1
    updated_at: datetime.datetime
    discoverable: bool | Unset = False
    latest_version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description

        name = self.name

        owner_username = self.owner_username

        project = self.project.to_dict()

        requesting_user_access = self.requesting_user_access.to_dict()

        tags = self.tags.to_dict()

        updated_at = self.updated_at.isoformat()

        discoverable = self.discoverable

        latest_version = self.latest_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "description": description,
                "name": name,
                "ownerUsername": owner_username,
                "project": project,
                "requestingUserAccess": requesting_user_access,
                "tags": tags,
                "updatedAt": updated_at,
            }
        )
        if discoverable is not UNSET:
            field_dict["discoverable"] = discoverable
        if latest_version is not UNSET:
            field_dict["latestVersion"] = latest_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registered_model_project_summary_v1 import RegisteredModelProjectSummaryV1
        from ..models.registered_model_requesting_user_access_v1 import RegisteredModelRequestingUserAccessV1
        from ..models.registered_model_tags_v1 import RegisteredModelTagsV1

        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        description = d.pop("description")

        name = d.pop("name")

        owner_username = d.pop("ownerUsername")

        project = RegisteredModelProjectSummaryV1.from_dict(d.pop("project"))

        requesting_user_access = RegisteredModelRequestingUserAccessV1.from_dict(d.pop("requestingUserAccess"))

        tags = RegisteredModelTagsV1.from_dict(d.pop("tags"))

        updated_at = isoparse(d.pop("updatedAt"))

        discoverable = d.pop("discoverable", UNSET)

        latest_version = d.pop("latestVersion", UNSET)

        registered_model_v1 = cls(
            created_at=created_at,
            description=description,
            name=name,
            owner_username=owner_username,
            project=project,
            requesting_user_access=requesting_user_access,
            tags=tags,
            updated_at=updated_at,
            discoverable=discoverable,
            latest_version=latest_version,
        )

        registered_model_v1.additional_properties = d
        return registered_model_v1

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
