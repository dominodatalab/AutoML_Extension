from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoCommonModelproductExecutorDetails")


@_attrs_define
class DominoCommonModelproductExecutorDetails:
    """
    Attributes:
        executor_instance_id (str):
        region (str):
        human_name (None | str | Unset):
        public_address (None | str | Unset):
        private_address (None | str | Unset):
    """

    executor_instance_id: str
    region: str
    human_name: None | str | Unset = UNSET
    public_address: None | str | Unset = UNSET
    private_address: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        executor_instance_id = self.executor_instance_id

        region = self.region

        human_name: None | str | Unset
        if isinstance(self.human_name, Unset):
            human_name = UNSET
        else:
            human_name = self.human_name

        public_address: None | str | Unset
        if isinstance(self.public_address, Unset):
            public_address = UNSET
        else:
            public_address = self.public_address

        private_address: None | str | Unset
        if isinstance(self.private_address, Unset):
            private_address = UNSET
        else:
            private_address = self.private_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "executorInstanceId": executor_instance_id,
                "region": region,
            }
        )
        if human_name is not UNSET:
            field_dict["humanName"] = human_name
        if public_address is not UNSET:
            field_dict["publicAddress"] = public_address
        if private_address is not UNSET:
            field_dict["privateAddress"] = private_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        executor_instance_id = d.pop("executorInstanceId")

        region = d.pop("region")

        def _parse_human_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        human_name = _parse_human_name(d.pop("humanName", UNSET))

        def _parse_public_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_address = _parse_public_address(d.pop("publicAddress", UNSET))

        def _parse_private_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        private_address = _parse_private_address(d.pop("privateAddress", UNSET))

        domino_common_modelproduct_executor_details = cls(
            executor_instance_id=executor_instance_id,
            region=region,
            human_name=human_name,
            public_address=public_address,
            private_address=private_address,
        )

        domino_common_modelproduct_executor_details.additional_properties = d
        return domino_common_modelproduct_executor_details

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
