from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_resolve_review_request_resolution import (
    DominoProjectsApiResolveReviewRequestResolution,
)

if TYPE_CHECKING:
    from ..models.domino_projects_api_resolve_review_request_resolution_decisions import (
        DominoProjectsApiResolveReviewRequestResolutionDecisions,
    )


T = TypeVar("T", bound="DominoProjectsApiResolveReviewRequest")


@_attrs_define
class DominoProjectsApiResolveReviewRequest:
    """
    Attributes:
        resolution (DominoProjectsApiResolveReviewRequestResolution):
        from_commit_id (str):
        into_commit_id (str):
        resolution_decisions (DominoProjectsApiResolveReviewRequestResolutionDecisions):  Example: {'nested/file.text':
            'Keep', 'root.file': 'Accept'}.
    """

    resolution: DominoProjectsApiResolveReviewRequestResolution
    from_commit_id: str
    into_commit_id: str
    resolution_decisions: DominoProjectsApiResolveReviewRequestResolutionDecisions
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resolution = self.resolution.value

        from_commit_id = self.from_commit_id

        into_commit_id = self.into_commit_id

        resolution_decisions = self.resolution_decisions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resolution": resolution,
                "fromCommitId": from_commit_id,
                "intoCommitId": into_commit_id,
                "resolutionDecisions": resolution_decisions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_resolve_review_request_resolution_decisions import (
            DominoProjectsApiResolveReviewRequestResolutionDecisions,
        )

        d = dict(src_dict)
        resolution = DominoProjectsApiResolveReviewRequestResolution(d.pop("resolution"))

        from_commit_id = d.pop("fromCommitId")

        into_commit_id = d.pop("intoCommitId")

        resolution_decisions = DominoProjectsApiResolveReviewRequestResolutionDecisions.from_dict(
            d.pop("resolutionDecisions")
        )

        domino_projects_api_resolve_review_request = cls(
            resolution=resolution,
            from_commit_id=from_commit_id,
            into_commit_id=into_commit_id,
            resolution_decisions=resolution_decisions,
        )

        domino_projects_api_resolve_review_request.additional_properties = d
        return domino_projects_api_resolve_review_request

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
