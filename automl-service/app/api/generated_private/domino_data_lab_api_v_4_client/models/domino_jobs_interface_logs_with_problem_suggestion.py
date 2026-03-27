from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_jobs_interface_job_problem_suggestion import DominoJobsInterfaceJobProblemSuggestion
    from ..models.domino_jobs_interface_log_set import DominoJobsInterfaceLogSet


T = TypeVar("T", bound="DominoJobsInterfaceLogsWithProblemSuggestion")


@_attrs_define
class DominoJobsInterfaceLogsWithProblemSuggestion:
    """
    Attributes:
        logset (DominoJobsInterfaceLogSet):
        problem_suggestion (DominoJobsInterfaceJobProblemSuggestion | Unset):
    """

    logset: DominoJobsInterfaceLogSet
    problem_suggestion: DominoJobsInterfaceJobProblemSuggestion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logset = self.logset.to_dict()

        problem_suggestion: dict[str, Any] | Unset = UNSET
        if not isinstance(self.problem_suggestion, Unset):
            problem_suggestion = self.problem_suggestion.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logset": logset,
            }
        )
        if problem_suggestion is not UNSET:
            field_dict["problemSuggestion"] = problem_suggestion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_jobs_interface_job_problem_suggestion import DominoJobsInterfaceJobProblemSuggestion
        from ..models.domino_jobs_interface_log_set import DominoJobsInterfaceLogSet

        d = dict(src_dict)
        logset = DominoJobsInterfaceLogSet.from_dict(d.pop("logset"))

        _problem_suggestion = d.pop("problemSuggestion", UNSET)
        problem_suggestion: DominoJobsInterfaceJobProblemSuggestion | Unset
        if isinstance(_problem_suggestion, Unset):
            problem_suggestion = UNSET
        else:
            problem_suggestion = DominoJobsInterfaceJobProblemSuggestion.from_dict(_problem_suggestion)

        domino_jobs_interface_logs_with_problem_suggestion = cls(
            logset=logset,
            problem_suggestion=problem_suggestion,
        )

        domino_jobs_interface_logs_with_problem_suggestion.additional_properties = d
        return domino_jobs_interface_logs_with_problem_suggestion

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
