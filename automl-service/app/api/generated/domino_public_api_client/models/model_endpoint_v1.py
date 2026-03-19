from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.model_endpoint_general_access_v1 import ModelEndpointGeneralAccessV1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_endpoint_project_summary_v1 import ModelEndpointProjectSummaryV1
    from ..models.model_endpoint_user_v1 import ModelEndpointUserV1
    from ..models.model_endpoint_version_v1 import ModelEndpointVersionV1


T = TypeVar("T", bound="ModelEndpointV1")


@_attrs_define
class ModelEndpointV1:
    """
    Attributes:
        created_at (datetime.datetime): The time the endpoint was created Example: 2022-03-12T02:13:44.467Z.
        creator (ModelEndpointUserV1):
        general_access (ModelEndpointGeneralAccessV1):
        id (str): The ID of the endpoint Example: 62313ce67a0af0281c01a6a5.
        name (str): The name of the endpoint Example: My Endpoint.
        project (ModelEndpointProjectSummaryV1):
        updated_at (datetime.datetime): The last time the endpoint was modified Example: 2022-03-12T02:13:44.467Z.
        url (str): The URL of the endpoint Example: https://cloud-dogfood.domino.tech/endpoint/my-endpoint.
        vanity_url (str): The optional Vanity url for the Gen AI Endpoint. This will default to https://{domino-
            instance}/endpoints/{endpointName} Example: https://cloud-dogfood.domino.tech/endpoints/my-endpoint.
        current_version (ModelEndpointVersionV1 | Unset):
        description (str | Unset): The description of the endpoint Example: My Endpoint Description.
        instructions (str | Unset): The instructions for using the endpoint Example: Use the endpoint to generate text.
        request_count (int | Unset): The number of requests processed by the endpoint Example: 100.
    """

    created_at: datetime.datetime
    creator: ModelEndpointUserV1
    general_access: ModelEndpointGeneralAccessV1
    id: str
    name: str
    project: ModelEndpointProjectSummaryV1
    updated_at: datetime.datetime
    url: str
    vanity_url: str
    current_version: ModelEndpointVersionV1 | Unset = UNSET
    description: str | Unset = UNSET
    instructions: str | Unset = UNSET
    request_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        creator = self.creator.to_dict()

        general_access = self.general_access.value

        id = self.id

        name = self.name

        project = self.project.to_dict()

        updated_at = self.updated_at.isoformat()

        url = self.url

        vanity_url = self.vanity_url

        current_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_version, Unset):
            current_version = self.current_version.to_dict()

        description = self.description

        instructions = self.instructions

        request_count = self.request_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "creator": creator,
                "generalAccess": general_access,
                "id": id,
                "name": name,
                "project": project,
                "updatedAt": updated_at,
                "url": url,
                "vanityUrl": vanity_url,
            }
        )
        if current_version is not UNSET:
            field_dict["currentVersion"] = current_version
        if description is not UNSET:
            field_dict["description"] = description
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if request_count is not UNSET:
            field_dict["requestCount"] = request_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_endpoint_project_summary_v1 import ModelEndpointProjectSummaryV1
        from ..models.model_endpoint_user_v1 import ModelEndpointUserV1
        from ..models.model_endpoint_version_v1 import ModelEndpointVersionV1

        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        creator = ModelEndpointUserV1.from_dict(d.pop("creator"))

        general_access = ModelEndpointGeneralAccessV1(d.pop("generalAccess"))

        id = d.pop("id")

        name = d.pop("name")

        project = ModelEndpointProjectSummaryV1.from_dict(d.pop("project"))

        updated_at = isoparse(d.pop("updatedAt"))

        url = d.pop("url")

        vanity_url = d.pop("vanityUrl")

        _current_version = d.pop("currentVersion", UNSET)
        current_version: ModelEndpointVersionV1 | Unset
        if isinstance(_current_version, Unset):
            current_version = UNSET
        else:
            current_version = ModelEndpointVersionV1.from_dict(_current_version)

        description = d.pop("description", UNSET)

        instructions = d.pop("instructions", UNSET)

        request_count = d.pop("requestCount", UNSET)

        model_endpoint_v1 = cls(
            created_at=created_at,
            creator=creator,
            general_access=general_access,
            id=id,
            name=name,
            project=project,
            updated_at=updated_at,
            url=url,
            vanity_url=vanity_url,
            current_version=current_version,
            description=description,
            instructions=instructions,
            request_count=request_count,
        )

        model_endpoint_v1.additional_properties = d
        return model_endpoint_v1

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
