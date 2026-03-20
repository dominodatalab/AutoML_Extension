from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_rw_grant_v1 import DatasetRwGrantV1


T = TypeVar("T", bound="NewDatasetRwV1")


@_attrs_define
class NewDatasetRwV1:
    """
    Attributes:
        name (str): Name of this dataset. The name must be unique in the same project
        description (str | Unset): Description of the dataset
        grants (list[DatasetRwGrantV1] | Unset): Permission grants to be assigned for this newly created dataset. Note
            that permissions can be edited after creation. If snapshotId is passed in, this parameter won't have any effect
            and caller will be assigned dataset Ownership.
        project_id (str | Unset): ID of the project this dataset belongs to. Either projectId or snapshotId must be
            provided
        snapshot_id (str | Unset): ID of an existing snapshot to create a new dataset from. Either snapshotId or
            projectId must be provided.
    """

    name: str
    description: str | Unset = UNSET
    grants: list[DatasetRwGrantV1] | Unset = UNSET
    project_id: str | Unset = UNSET
    snapshot_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        grants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grants, Unset):
            grants = []
            for grants_item_data in self.grants:
                grants_item = grants_item_data.to_dict()
                grants.append(grants_item)

        project_id = self.project_id

        snapshot_id = self.snapshot_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if grants is not UNSET:
            field_dict["grants"] = grants
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if snapshot_id is not UNSET:
            field_dict["snapshotId"] = snapshot_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_rw_grant_v1 import DatasetRwGrantV1

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _grants = d.pop("grants", UNSET)
        grants: list[DatasetRwGrantV1] | Unset = UNSET
        if _grants is not UNSET:
            grants = []
            for grants_item_data in _grants:
                grants_item = DatasetRwGrantV1.from_dict(grants_item_data)

                grants.append(grants_item)

        project_id = d.pop("projectId", UNSET)

        snapshot_id = d.pop("snapshotId", UNSET)

        new_dataset_rw_v1 = cls(
            name=name,
            description=description,
            grants=grants,
            project_id=project_id,
            snapshot_id=snapshot_id,
        )

        new_dataset_rw_v1.additional_properties = d
        return new_dataset_rw_v1

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
