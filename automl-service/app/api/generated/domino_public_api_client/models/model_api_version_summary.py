from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_api_version_deployment import ModelApiVersionDeployment


T = TypeVar("T", bound="ModelApiVersionSummary")


@_attrs_define
class ModelApiVersionSummary:
    """
    Attributes:
        data_plane_id (str): The id of the data plane the Model API Version is deployed to.
        id (str): The id of the Model API Version.
        deployment (ModelApiVersionDeployment | Unset):
        number (int | Unset): The version number of the Model API Version.
    """

    data_plane_id: str
    id: str
    deployment: ModelApiVersionDeployment | Unset = UNSET
    number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_plane_id = self.data_plane_id

        id = self.id

        deployment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deployment, Unset):
            deployment = self.deployment.to_dict()

        number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataPlaneId": data_plane_id,
                "id": id,
            }
        )
        if deployment is not UNSET:
            field_dict["deployment"] = deployment
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_api_version_deployment import ModelApiVersionDeployment

        d = dict(src_dict)
        data_plane_id = d.pop("dataPlaneId")

        id = d.pop("id")

        _deployment = d.pop("deployment", UNSET)
        deployment: ModelApiVersionDeployment | Unset
        if isinstance(_deployment, Unset):
            deployment = UNSET
        else:
            deployment = ModelApiVersionDeployment.from_dict(_deployment)

        number = d.pop("number", UNSET)

        model_api_version_summary = cls(
            data_plane_id=data_plane_id,
            id=id,
            deployment=deployment,
            number=number,
        )

        model_api_version_summary.additional_properties = d
        return model_api_version_summary

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
