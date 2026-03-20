from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_content_v1 import LogContentV1


T = TypeVar("T", bound="JobLogsV1")


@_attrs_define
class JobLogsV1:
    """
    Attributes:
        is_complete (bool): Whether all logs for the job have been retrieved. Example: True.
        log_content (list[LogContentV1]):
        help_link (str | Unset): Suggestion link for helpful resources. Example: Error. No such file or directory..
        problem (str | Unset): Description of issue that occurred in a job. Example: python: can't open file
            'invalid.py': [Errno 2] No such file or directory.
    """

    is_complete: bool
    log_content: list[LogContentV1]
    help_link: str | Unset = UNSET
    problem: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_complete = self.is_complete

        log_content = []
        for log_content_item_data in self.log_content:
            log_content_item = log_content_item_data.to_dict()
            log_content.append(log_content_item)

        help_link = self.help_link

        problem = self.problem

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isComplete": is_complete,
                "logContent": log_content,
            }
        )
        if help_link is not UNSET:
            field_dict["helpLink"] = help_link
        if problem is not UNSET:
            field_dict["problem"] = problem

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.log_content_v1 import LogContentV1

        d = dict(src_dict)
        is_complete = d.pop("isComplete")

        log_content = []
        _log_content = d.pop("logContent")
        for log_content_item_data in _log_content:
            log_content_item = LogContentV1.from_dict(log_content_item_data)

            log_content.append(log_content_item)

        help_link = d.pop("helpLink", UNSET)

        problem = d.pop("problem", UNSET)

        job_logs_v1 = cls(
            is_complete=is_complete,
            log_content=log_content,
            help_link=help_link,
            problem=problem,
        )

        job_logs_v1.additional_properties = d
        return job_logs_v1

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
