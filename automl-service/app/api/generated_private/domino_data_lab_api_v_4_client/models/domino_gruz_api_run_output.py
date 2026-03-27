from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_models_diagnostic_statistics import DominoCommonModelsDiagnosticStatistics


T = TypeVar("T", bound="DominoGruzApiRunOutput")


@_attrs_define
class DominoGruzApiRunOutput:
    """
    Attributes:
        output_commit_id (None | str | Unset):
        commit_message (None | str | Unset):
        diagnostic_statistics (DominoCommonModelsDiagnosticStatistics | Unset):
    """

    output_commit_id: None | str | Unset = UNSET
    commit_message: None | str | Unset = UNSET
    diagnostic_statistics: DominoCommonModelsDiagnosticStatistics | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        output_commit_id: None | str | Unset
        if isinstance(self.output_commit_id, Unset):
            output_commit_id = UNSET
        else:
            output_commit_id = self.output_commit_id

        commit_message: None | str | Unset
        if isinstance(self.commit_message, Unset):
            commit_message = UNSET
        else:
            commit_message = self.commit_message

        diagnostic_statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.diagnostic_statistics, Unset):
            diagnostic_statistics = self.diagnostic_statistics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if output_commit_id is not UNSET:
            field_dict["outputCommitId"] = output_commit_id
        if commit_message is not UNSET:
            field_dict["commitMessage"] = commit_message
        if diagnostic_statistics is not UNSET:
            field_dict["diagnosticStatistics"] = diagnostic_statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_models_diagnostic_statistics import DominoCommonModelsDiagnosticStatistics

        d = dict(src_dict)

        def _parse_output_commit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output_commit_id = _parse_output_commit_id(d.pop("outputCommitId", UNSET))

        def _parse_commit_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_message = _parse_commit_message(d.pop("commitMessage", UNSET))

        _diagnostic_statistics = d.pop("diagnosticStatistics", UNSET)
        diagnostic_statistics: DominoCommonModelsDiagnosticStatistics | Unset
        if isinstance(_diagnostic_statistics, Unset):
            diagnostic_statistics = UNSET
        else:
            diagnostic_statistics = DominoCommonModelsDiagnosticStatistics.from_dict(_diagnostic_statistics)

        domino_gruz_api_run_output = cls(
            output_commit_id=output_commit_id,
            commit_message=commit_message,
            diagnostic_statistics=diagnostic_statistics,
        )

        domino_gruz_api_run_output.additional_properties = d
        return domino_gruz_api_run_output

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
