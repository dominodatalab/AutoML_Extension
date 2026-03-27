from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_guardrails_interface_bundle_comments_summary_artifact_comments_count_map import (
        DominoGuardrailsInterfaceBundleCommentsSummaryArtifactCommentsCountMap,
    )


T = TypeVar("T", bound="DominoGuardrailsInterfaceBundleCommentsSummary")


@_attrs_define
class DominoGuardrailsInterfaceBundleCommentsSummary:
    """
    Attributes:
        bundle_comments_count (int):
        artifact_comments_count_map (DominoGuardrailsInterfaceBundleCommentsSummaryArtifactCommentsCountMap):
    """

    bundle_comments_count: int
    artifact_comments_count_map: DominoGuardrailsInterfaceBundleCommentsSummaryArtifactCommentsCountMap
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bundle_comments_count = self.bundle_comments_count

        artifact_comments_count_map = self.artifact_comments_count_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bundleCommentsCount": bundle_comments_count,
                "artifactCommentsCountMap": artifact_comments_count_map,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_guardrails_interface_bundle_comments_summary_artifact_comments_count_map import (
            DominoGuardrailsInterfaceBundleCommentsSummaryArtifactCommentsCountMap,
        )

        d = dict(src_dict)
        bundle_comments_count = d.pop("bundleCommentsCount")

        artifact_comments_count_map = DominoGuardrailsInterfaceBundleCommentsSummaryArtifactCommentsCountMap.from_dict(
            d.pop("artifactCommentsCountMap")
        )

        domino_guardrails_interface_bundle_comments_summary = cls(
            bundle_comments_count=bundle_comments_count,
            artifact_comments_count_map=artifact_comments_count_map,
        )

        domino_guardrails_interface_bundle_comments_summary.additional_properties = d
        return domino_guardrails_interface_bundle_comments_summary

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
