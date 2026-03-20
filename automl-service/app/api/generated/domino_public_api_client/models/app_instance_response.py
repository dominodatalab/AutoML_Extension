from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_instance_autoscaling_info import AppInstanceAutoscalingInfo
    from ..models.app_instance_resource_usage import AppInstanceResourceUsage


T = TypeVar("T", bound="AppInstanceResponse")


@_attrs_define
class AppInstanceResponse:
    """
    Attributes:
        created_at (float):
        id (str):
        resource_usage (list[AppInstanceResourceUsage]):
        status (str):
        autoscaling_info (AppInstanceAutoscalingInfo | Unset):
    """

    created_at: float
    id: str
    resource_usage: list[AppInstanceResourceUsage]
    status: str
    autoscaling_info: AppInstanceAutoscalingInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        resource_usage = []
        for componentsschemas_app_instance_resource_usage_timeseries_item_data in self.resource_usage:
            componentsschemas_app_instance_resource_usage_timeseries_item = (
                componentsschemas_app_instance_resource_usage_timeseries_item_data.to_dict()
            )
            resource_usage.append(componentsschemas_app_instance_resource_usage_timeseries_item)

        status = self.status

        autoscaling_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.autoscaling_info, Unset):
            autoscaling_info = self.autoscaling_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "id": id,
                "resourceUsage": resource_usage,
                "status": status,
            }
        )
        if autoscaling_info is not UNSET:
            field_dict["autoscalingInfo"] = autoscaling_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_instance_autoscaling_info import AppInstanceAutoscalingInfo
        from ..models.app_instance_resource_usage import AppInstanceResourceUsage

        d = dict(src_dict)
        created_at = d.pop("createdAt")

        id = d.pop("id")

        resource_usage = []
        _resource_usage = d.pop("resourceUsage")
        for componentsschemas_app_instance_resource_usage_timeseries_item_data in _resource_usage:
            componentsschemas_app_instance_resource_usage_timeseries_item = AppInstanceResourceUsage.from_dict(
                componentsschemas_app_instance_resource_usage_timeseries_item_data
            )

            resource_usage.append(componentsschemas_app_instance_resource_usage_timeseries_item)

        status = d.pop("status")

        _autoscaling_info = d.pop("autoscalingInfo", UNSET)
        autoscaling_info: AppInstanceAutoscalingInfo | Unset
        if isinstance(_autoscaling_info, Unset):
            autoscaling_info = UNSET
        else:
            autoscaling_info = AppInstanceAutoscalingInfo.from_dict(_autoscaling_info)

        app_instance_response = cls(
            created_at=created_at,
            id=id,
            resource_usage=resource_usage,
            status=status,
            autoscaling_info=autoscaling_info,
        )

        app_instance_response.additional_properties = d
        return app_instance_response

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
