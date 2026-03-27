from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_hardwaretier_api_hardware_tier_pod_customization_dto_additional_annotations import (
        DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalAnnotations,
    )
    from ..models.domino_hardwaretier_api_hardware_tier_pod_customization_dto_additional_labels import (
        DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalLabels,
    )
    from ..models.domino_hardwaretier_api_hardware_tier_pod_customization_dto_additional_limits import (
        DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalLimits,
    )
    from ..models.domino_hardwaretier_api_hardware_tier_pod_customization_dto_additional_requests import (
        DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalRequests,
    )
    from ..models.domino_hardwaretier_api_hardware_tier_pod_customization_dto_hugepages import (
        DominoHardwaretierApiHardwareTierPodCustomizationDtoHugepages,
    )


T = TypeVar("T", bound="DominoHardwaretierApiHardwareTierPodCustomizationDto")


@_attrs_define
class DominoHardwaretierApiHardwareTierPodCustomizationDto:
    """
    Attributes:
        additional_requests (DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalRequests):
        additional_limits (DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalLimits):
        additional_annotations (DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalAnnotations):
        additional_labels (DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalLabels):
        hugepages (DominoHardwaretierApiHardwareTierPodCustomizationDtoHugepages):
        capabilities (list[str]):
    """

    additional_requests: DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalRequests
    additional_limits: DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalLimits
    additional_annotations: DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalAnnotations
    additional_labels: DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalLabels
    hugepages: DominoHardwaretierApiHardwareTierPodCustomizationDtoHugepages
    capabilities: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_requests = self.additional_requests.to_dict()

        additional_limits = self.additional_limits.to_dict()

        additional_annotations = self.additional_annotations.to_dict()

        additional_labels = self.additional_labels.to_dict()

        hugepages = self.hugepages.to_dict()

        capabilities = self.capabilities

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "additionalRequests": additional_requests,
                "additionalLimits": additional_limits,
                "additionalAnnotations": additional_annotations,
                "additionalLabels": additional_labels,
                "hugepages": hugepages,
                "capabilities": capabilities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_hardwaretier_api_hardware_tier_pod_customization_dto_additional_annotations import (
            DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalAnnotations,
        )
        from ..models.domino_hardwaretier_api_hardware_tier_pod_customization_dto_additional_labels import (
            DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalLabels,
        )
        from ..models.domino_hardwaretier_api_hardware_tier_pod_customization_dto_additional_limits import (
            DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalLimits,
        )
        from ..models.domino_hardwaretier_api_hardware_tier_pod_customization_dto_additional_requests import (
            DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalRequests,
        )
        from ..models.domino_hardwaretier_api_hardware_tier_pod_customization_dto_hugepages import (
            DominoHardwaretierApiHardwareTierPodCustomizationDtoHugepages,
        )

        d = dict(src_dict)
        additional_requests = DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalRequests.from_dict(
            d.pop("additionalRequests")
        )

        additional_limits = DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalLimits.from_dict(
            d.pop("additionalLimits")
        )

        additional_annotations = DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalAnnotations.from_dict(
            d.pop("additionalAnnotations")
        )

        additional_labels = DominoHardwaretierApiHardwareTierPodCustomizationDtoAdditionalLabels.from_dict(
            d.pop("additionalLabels")
        )

        hugepages = DominoHardwaretierApiHardwareTierPodCustomizationDtoHugepages.from_dict(d.pop("hugepages"))

        capabilities = cast(list[str], d.pop("capabilities"))

        domino_hardwaretier_api_hardware_tier_pod_customization_dto = cls(
            additional_requests=additional_requests,
            additional_limits=additional_limits,
            additional_annotations=additional_annotations,
            additional_labels=additional_labels,
            hugepages=hugepages,
            capabilities=capabilities,
        )

        domino_hardwaretier_api_hardware_tier_pod_customization_dto.additional_properties = d
        return domino_hardwaretier_api_hardware_tier_pod_customization_dto

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
