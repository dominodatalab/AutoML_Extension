from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoJobsInterfaceJobProblemSuggestion")


@_attrs_define
class DominoJobsInterfaceJobProblemSuggestion:
    """
    Attributes:
        problem (str):
        help_link (str):
    """

    problem: str
    help_link: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        problem = self.problem

        help_link = self.help_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "problem": problem,
                "helpLink": help_link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        problem = d.pop("problem")

        help_link = d.pop("helpLink")

        domino_jobs_interface_job_problem_suggestion = cls(
            problem=problem,
            help_link=help_link,
        )

        domino_jobs_interface_job_problem_suggestion.additional_properties = d
        return domino_jobs_interface_job_problem_suggestion

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
