from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostLabelsV2")


@_attrs_define
class CostLabelsV2:
    """
    Attributes:
        billing_tag (str | Unset):
        organization_id (str | Unset):
        organization_name (str | Unset):
        project_id (str | Unset):
        project_name (str | Unset):
        project_owner_id (str | Unset):
        project_owner_name (str | Unset):
        starting_user_id (str | Unset):
        starting_user_name (str | Unset):
        workload_id (str | Unset):
        workload_type (str | Unset):
    """

    billing_tag: str | Unset = UNSET
    organization_id: str | Unset = UNSET
    organization_name: str | Unset = UNSET
    project_id: str | Unset = UNSET
    project_name: str | Unset = UNSET
    project_owner_id: str | Unset = UNSET
    project_owner_name: str | Unset = UNSET
    starting_user_id: str | Unset = UNSET
    starting_user_name: str | Unset = UNSET
    workload_id: str | Unset = UNSET
    workload_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_tag = self.billing_tag

        organization_id = self.organization_id

        organization_name = self.organization_name

        project_id = self.project_id

        project_name = self.project_name

        project_owner_id = self.project_owner_id

        project_owner_name = self.project_owner_name

        starting_user_id = self.starting_user_id

        starting_user_name = self.starting_user_name

        workload_id = self.workload_id

        workload_type = self.workload_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_tag is not UNSET:
            field_dict["billingTag"] = billing_tag
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if project_name is not UNSET:
            field_dict["projectName"] = project_name
        if project_owner_id is not UNSET:
            field_dict["projectOwnerId"] = project_owner_id
        if project_owner_name is not UNSET:
            field_dict["projectOwnerName"] = project_owner_name
        if starting_user_id is not UNSET:
            field_dict["startingUserId"] = starting_user_id
        if starting_user_name is not UNSET:
            field_dict["startingUserName"] = starting_user_name
        if workload_id is not UNSET:
            field_dict["workloadId"] = workload_id
        if workload_type is not UNSET:
            field_dict["workloadType"] = workload_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        billing_tag = d.pop("billingTag", UNSET)

        organization_id = d.pop("organizationId", UNSET)

        organization_name = d.pop("organizationName", UNSET)

        project_id = d.pop("projectId", UNSET)

        project_name = d.pop("projectName", UNSET)

        project_owner_id = d.pop("projectOwnerId", UNSET)

        project_owner_name = d.pop("projectOwnerName", UNSET)

        starting_user_id = d.pop("startingUserId", UNSET)

        starting_user_name = d.pop("startingUserName", UNSET)

        workload_id = d.pop("workloadId", UNSET)

        workload_type = d.pop("workloadType", UNSET)

        cost_labels_v2 = cls(
            billing_tag=billing_tag,
            organization_id=organization_id,
            organization_name=organization_name,
            project_id=project_id,
            project_name=project_name,
            project_owner_id=project_owner_id,
            project_owner_name=project_owner_name,
            starting_user_id=starting_user_id,
            starting_user_name=starting_user_name,
            workload_id=workload_id,
            workload_type=workload_type,
        )

        cost_labels_v2.additional_properties = d
        return cost_labels_v2

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
