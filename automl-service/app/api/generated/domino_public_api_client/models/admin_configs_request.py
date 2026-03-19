from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.admin_config_request import AdminConfigRequest


T = TypeVar("T", bound="AdminConfigsRequest")


@_attrs_define
class AdminConfigsRequest:
    """
    Attributes:
        configs (list[AdminConfigRequest]): Array of PPM configurations (currently only first is used)
    """

    configs: list[AdminConfigRequest]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configs = []
        for configs_item_data in self.configs:
            configs_item = configs_item_data.to_dict()
            configs.append(configs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configs": configs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_config_request import AdminConfigRequest

        d = dict(src_dict)
        configs = []
        _configs = d.pop("configs")
        for configs_item_data in _configs:
            configs_item = AdminConfigRequest.from_dict(configs_item_data)

            configs.append(configs_item)

        admin_configs_request = cls(
            configs=configs,
        )

        admin_configs_request.additional_properties = d
        return admin_configs_request

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
