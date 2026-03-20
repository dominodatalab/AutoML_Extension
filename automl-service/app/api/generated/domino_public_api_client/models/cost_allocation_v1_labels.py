from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostAllocationV1Labels")


@_attrs_define
class CostAllocationV1Labels:
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
            field_dict["billing_tag"] = billing_tag
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if organization_name is not UNSET:
            field_dict["organization_name"] = organization_name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if project_owner_id is not UNSET:
            field_dict["project_owner_id"] = project_owner_id
        if project_owner_name is not UNSET:
            field_dict["project_owner_name"] = project_owner_name
        if starting_user_id is not UNSET:
            field_dict["starting_user_id"] = starting_user_id
        if starting_user_name is not UNSET:
            field_dict["starting_user_name"] = starting_user_name
        if workload_id is not UNSET:
            field_dict["workload_id"] = workload_id
        if workload_type is not UNSET:
            field_dict["workload_type"] = workload_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        billing_tag = d.pop("billing_tag", UNSET)

        organization_id = d.pop("organization_id", UNSET)

        organization_name = d.pop("organization_name", UNSET)

        project_id = d.pop("project_id", UNSET)

        project_name = d.pop("project_name", UNSET)

        project_owner_id = d.pop("project_owner_id", UNSET)

        project_owner_name = d.pop("project_owner_name", UNSET)

        starting_user_id = d.pop("starting_user_id", UNSET)

        starting_user_name = d.pop("starting_user_name", UNSET)

        workload_id = d.pop("workload_id", UNSET)

        workload_type = d.pop("workload_type", UNSET)

        cost_allocation_v1_labels = cls(
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

        cost_allocation_v1_labels.additional_properties = d
        return cost_allocation_v1_labels

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
