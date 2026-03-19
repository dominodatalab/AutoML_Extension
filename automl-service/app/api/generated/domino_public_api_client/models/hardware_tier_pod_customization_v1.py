from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hardware_tier_pod_customization_v1_additional_annotations import (
        HardwareTierPodCustomizationV1AdditionalAnnotations,
    )
    from ..models.hardware_tier_pod_customization_v1_additional_labels import (
        HardwareTierPodCustomizationV1AdditionalLabels,
    )
    from ..models.hardware_tier_pod_customization_v1_additional_limits import (
        HardwareTierPodCustomizationV1AdditionalLimits,
    )
    from ..models.hardware_tier_pod_customization_v1_additional_requests import (
        HardwareTierPodCustomizationV1AdditionalRequests,
    )
    from ..models.hardware_tier_pod_customization_v1_hugepages import HardwareTierPodCustomizationV1Hugepages


T = TypeVar("T", bound="HardwareTierPodCustomizationV1")


@_attrs_define
class HardwareTierPodCustomizationV1:
    """Custom fields for hardwareTier

    Attributes:
        additional_annotations (HardwareTierPodCustomizationV1AdditionalAnnotations | Unset):
        additional_labels (HardwareTierPodCustomizationV1AdditionalLabels | Unset):
        additional_limits (HardwareTierPodCustomizationV1AdditionalLimits | Unset):
        additional_requests (HardwareTierPodCustomizationV1AdditionalRequests | Unset):
        capabilities (list[str] | Unset):
        hugepages (HardwareTierPodCustomizationV1Hugepages | Unset):
    """

    additional_annotations: HardwareTierPodCustomizationV1AdditionalAnnotations | Unset = UNSET
    additional_labels: HardwareTierPodCustomizationV1AdditionalLabels | Unset = UNSET
    additional_limits: HardwareTierPodCustomizationV1AdditionalLimits | Unset = UNSET
    additional_requests: HardwareTierPodCustomizationV1AdditionalRequests | Unset = UNSET
    capabilities: list[str] | Unset = UNSET
    hugepages: HardwareTierPodCustomizationV1Hugepages | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_annotations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_annotations, Unset):
            additional_annotations = self.additional_annotations.to_dict()

        additional_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_labels, Unset):
            additional_labels = self.additional_labels.to_dict()

        additional_limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_limits, Unset):
            additional_limits = self.additional_limits.to_dict()

        additional_requests: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_requests, Unset):
            additional_requests = self.additional_requests.to_dict()

        capabilities: list[str] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities

        hugepages: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hugepages, Unset):
            hugepages = self.hugepages.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_annotations is not UNSET:
            field_dict["additionalAnnotations"] = additional_annotations
        if additional_labels is not UNSET:
            field_dict["additionalLabels"] = additional_labels
        if additional_limits is not UNSET:
            field_dict["additionalLimits"] = additional_limits
        if additional_requests is not UNSET:
            field_dict["additionalRequests"] = additional_requests
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if hugepages is not UNSET:
            field_dict["hugepages"] = hugepages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hardware_tier_pod_customization_v1_additional_annotations import (
            HardwareTierPodCustomizationV1AdditionalAnnotations,
        )
        from ..models.hardware_tier_pod_customization_v1_additional_labels import (
            HardwareTierPodCustomizationV1AdditionalLabels,
        )
        from ..models.hardware_tier_pod_customization_v1_additional_limits import (
            HardwareTierPodCustomizationV1AdditionalLimits,
        )
        from ..models.hardware_tier_pod_customization_v1_additional_requests import (
            HardwareTierPodCustomizationV1AdditionalRequests,
        )
        from ..models.hardware_tier_pod_customization_v1_hugepages import HardwareTierPodCustomizationV1Hugepages

        d = dict(src_dict)
        _additional_annotations = d.pop("additionalAnnotations", UNSET)
        additional_annotations: HardwareTierPodCustomizationV1AdditionalAnnotations | Unset
        if isinstance(_additional_annotations, Unset):
            additional_annotations = UNSET
        else:
            additional_annotations = HardwareTierPodCustomizationV1AdditionalAnnotations.from_dict(
                _additional_annotations
            )

        _additional_labels = d.pop("additionalLabels", UNSET)
        additional_labels: HardwareTierPodCustomizationV1AdditionalLabels | Unset
        if isinstance(_additional_labels, Unset):
            additional_labels = UNSET
        else:
            additional_labels = HardwareTierPodCustomizationV1AdditionalLabels.from_dict(_additional_labels)

        _additional_limits = d.pop("additionalLimits", UNSET)
        additional_limits: HardwareTierPodCustomizationV1AdditionalLimits | Unset
        if isinstance(_additional_limits, Unset):
            additional_limits = UNSET
        else:
            additional_limits = HardwareTierPodCustomizationV1AdditionalLimits.from_dict(_additional_limits)

        _additional_requests = d.pop("additionalRequests", UNSET)
        additional_requests: HardwareTierPodCustomizationV1AdditionalRequests | Unset
        if isinstance(_additional_requests, Unset):
            additional_requests = UNSET
        else:
            additional_requests = HardwareTierPodCustomizationV1AdditionalRequests.from_dict(_additional_requests)

        capabilities = cast(list[str], d.pop("capabilities", UNSET))

        _hugepages = d.pop("hugepages", UNSET)
        hugepages: HardwareTierPodCustomizationV1Hugepages | Unset
        if isinstance(_hugepages, Unset):
            hugepages = UNSET
        else:
            hugepages = HardwareTierPodCustomizationV1Hugepages.from_dict(_hugepages)

        hardware_tier_pod_customization_v1 = cls(
            additional_annotations=additional_annotations,
            additional_labels=additional_labels,
            additional_limits=additional_limits,
            additional_requests=additional_requests,
            capabilities=capabilities,
            hugepages=hugepages,
        )

        hardware_tier_pod_customization_v1.additional_properties = d
        return hardware_tier_pod_customization_v1

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
