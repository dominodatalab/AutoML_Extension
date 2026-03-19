from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.information_v1 import InformationV1


T = TypeVar("T", bound="HardwareTierResourcesV1")


@_attrs_define
class HardwareTierResourcesV1:
    """Compute resources for a hardware tier

    Attributes:
        allow_shared_memory_to_exceed_default (bool):
        cores (float):  Example: 1.
        memory (InformationV1):
        cores_limit (float | Unset):
        memory_limit (InformationV1 | Unset):
        memory_swap_limit (InformationV1 | Unset):
        shared_memory_limit (InformationV1 | Unset):
    """

    allow_shared_memory_to_exceed_default: bool
    cores: float
    memory: InformationV1
    cores_limit: float | Unset = UNSET
    memory_limit: InformationV1 | Unset = UNSET
    memory_swap_limit: InformationV1 | Unset = UNSET
    shared_memory_limit: InformationV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_shared_memory_to_exceed_default = self.allow_shared_memory_to_exceed_default

        cores = self.cores

        memory = self.memory.to_dict()

        cores_limit = self.cores_limit

        memory_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.memory_limit, Unset):
            memory_limit = self.memory_limit.to_dict()

        memory_swap_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.memory_swap_limit, Unset):
            memory_swap_limit = self.memory_swap_limit.to_dict()

        shared_memory_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shared_memory_limit, Unset):
            shared_memory_limit = self.shared_memory_limit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowSharedMemoryToExceedDefault": allow_shared_memory_to_exceed_default,
                "cores": cores,
                "memory": memory,
            }
        )
        if cores_limit is not UNSET:
            field_dict["coresLimit"] = cores_limit
        if memory_limit is not UNSET:
            field_dict["memoryLimit"] = memory_limit
        if memory_swap_limit is not UNSET:
            field_dict["memorySwapLimit"] = memory_swap_limit
        if shared_memory_limit is not UNSET:
            field_dict["sharedMemoryLimit"] = shared_memory_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.information_v1 import InformationV1

        d = dict(src_dict)
        allow_shared_memory_to_exceed_default = d.pop("allowSharedMemoryToExceedDefault")

        cores = d.pop("cores")

        memory = InformationV1.from_dict(d.pop("memory"))

        cores_limit = d.pop("coresLimit", UNSET)

        _memory_limit = d.pop("memoryLimit", UNSET)
        memory_limit: InformationV1 | Unset
        if isinstance(_memory_limit, Unset):
            memory_limit = UNSET
        else:
            memory_limit = InformationV1.from_dict(_memory_limit)

        _memory_swap_limit = d.pop("memorySwapLimit", UNSET)
        memory_swap_limit: InformationV1 | Unset
        if isinstance(_memory_swap_limit, Unset):
            memory_swap_limit = UNSET
        else:
            memory_swap_limit = InformationV1.from_dict(_memory_swap_limit)

        _shared_memory_limit = d.pop("sharedMemoryLimit", UNSET)
        shared_memory_limit: InformationV1 | Unset
        if isinstance(_shared_memory_limit, Unset):
            shared_memory_limit = UNSET
        else:
            shared_memory_limit = InformationV1.from_dict(_shared_memory_limit)

        hardware_tier_resources_v1 = cls(
            allow_shared_memory_to_exceed_default=allow_shared_memory_to_exceed_default,
            cores=cores,
            memory=memory,
            cores_limit=cores_limit,
            memory_limit=memory_limit,
            memory_swap_limit=memory_swap_limit,
            shared_memory_limit=shared_memory_limit,
        )

        hardware_tier_resources_v1.additional_properties = d
        return hardware_tier_resources_v1

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
