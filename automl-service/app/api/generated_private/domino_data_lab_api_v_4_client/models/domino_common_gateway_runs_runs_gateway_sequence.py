from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_gateway_runs_runs_gateway_summary import DominoCommonGatewayRunsRunsGatewaySummary


T = TypeVar("T", bound="DominoCommonGatewayRunsRunsGatewaySequence")


@_attrs_define
class DominoCommonGatewayRunsRunsGatewaySequence:
    """
    Attributes:
        runs (list[DominoCommonGatewayRunsRunsGatewaySummary]):
        next_batch_id (None | str | Unset):
    """

    runs: list[DominoCommonGatewayRunsRunsGatewaySummary]
    next_batch_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runs = []
        for runs_item_data in self.runs:
            runs_item = runs_item_data.to_dict()
            runs.append(runs_item)

        next_batch_id: None | str | Unset
        if isinstance(self.next_batch_id, Unset):
            next_batch_id = UNSET
        else:
            next_batch_id = self.next_batch_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runs": runs,
            }
        )
        if next_batch_id is not UNSET:
            field_dict["nextBatchId"] = next_batch_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_gateway_runs_runs_gateway_summary import DominoCommonGatewayRunsRunsGatewaySummary

        d = dict(src_dict)
        runs = []
        _runs = d.pop("runs")
        for runs_item_data in _runs:
            runs_item = DominoCommonGatewayRunsRunsGatewaySummary.from_dict(runs_item_data)

            runs.append(runs_item)

        def _parse_next_batch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_batch_id = _parse_next_batch_id(d.pop("nextBatchId", UNSET))

        domino_common_gateway_runs_runs_gateway_sequence = cls(
            runs=runs,
            next_batch_id=next_batch_id,
        )

        domino_common_gateway_runs_runs_gateway_sequence.additional_properties = d
        return domino_common_gateway_runs_runs_gateway_sequence

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
